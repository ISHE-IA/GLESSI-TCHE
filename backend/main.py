from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
import os
import ffmpeg
from pydub import AudioSegment
from pydub.silence import detect_nonsilent
from transformers import pipeline, WhisperForConditionalGeneration
import whisper

app = FastAPI()

# Fonction pour supprimer le silence dans l'audio
def remove_silence_from_end(input_file_path, silence_threshold=-50.0, chunk_size=10, is_start=True):
    format = input_file_path.split('.')[-1].lower()
    audio = AudioSegment.from_file(input_file_path, format=format if format in ['wav','mp3'] else 'mp4')

    nonsilent_chunks = detect_nonsilent(
        audio,
        min_silence_len=chunk_size,
        silence_thresh=silence_threshold
    )

    if nonsilent_chunks:
        start_index, end_index = nonsilent_chunks[-1]
    else:
        return input_file_path

    trimmed_audio = audio[:end_index]
    if is_start and nonsilent_chunks[0] and nonsilent_chunks[0][0] > 0:
        trimmed_audio = audio[nonsilent_chunks[0][0]:end_index]

    output_file_path = input_file_path.split('.')[0].lower() + "_trimmed.wav"
    trimmed_audio.export(output_file_path, format='wav')
    return output_file_path

# Endpoint pour supprimer le silence et transcrire
@app.post("/process-audio/")
async def process_audio_endpoint(file: UploadFile = File(...), lang: str = 'en'):
    input_path = f"temp_{file.filename}"
    output_path = f"processed_{file.filename}"

    with open(input_path, "wb") as f:
        f.write(file.file.read())

    processed_path = remove_silence_from_end(input_path)

    transcription_result, transcription_text = transcription_yoruba(processed_path, lang)

    os.remove(input_path)
    return {"transcription": transcription_text}

# Fonction pour transcrire l'audio en Yoruba
def transcription_yoruba(input_file_path, lang):
    model = whisper.load_model("small")
    if lang == 'yo':
        finetune_model = WhisperForConditionalGeneration.from_pretrained("steja/whisper-small-yoruba")
        state_dict = finetune_model.model.state_dict()
        rename_keys(state_dict)
        missing, unexpected = model.load_state_dict(state_dict, strict=False)
        if missing:
            raise ValueError("Missing weights for the model.")
        result = model.transcribe(input_file_path, verbose=False)
    else:
        result = model.transcribe(input_file_path, language=lang, verbose=False)
    complet_chain = "\n".join(s['text'] for s in result["segments"])
    return result, complet_chain

# Fonction de mapping de dictionnaire
def rename_keys(s_dict):
    WHISPER_MAPPING = {
        "encoder.ln_post.weight": "encoder.layer_norm.weight",
        "encoder.ln_post.bias": "encoder.layer_norm.bias",
        "blocks": "layers",
        "mlp.0": "fc1",
        "mlp.2": "fc2",
        "mlp_ln": "final_layer_norm",
        ".attn.query": ".self_attn.q_proj",
        ".attn.key": ".self_attn.k_proj",
        ".attn.value": ".self_attn.v_proj",
        ".attn_ln": ".self_attn_layer_norm",
        ".attn.out": ".self_attn.out_proj",
        ".cross_attn.query": ".encoder_attn.q_proj",
        ".cross_attn.key": ".encoder_attn.k_proj",
        ".cross_attn.value": ".encoder_attn.v_proj",
        ".cross_attn_ln": ".encoder_attn_layer_norm",
        ".cross_attn.out": ".encoder_attn.out_proj",
        "decoder.ln.": "decoder.layer_norm.",
        "encoder.ln.": "encoder.layer_norm.",
        "token_embedding": "embed_tokens",
        "encoder.positional_embedding": "encoder.embed_positions.weight",
        "decoder.positional_embedding": "decoder.embed_positions.weight",
    }
    keys = list(s_dict.keys())
    for key in keys:
        new_key = key
        for v, k in WHISPER_MAPPING.items():
            if k in key:
                new_key = new_key.replace(k, v)
        s_dict[new_key] = s_dict.pop(key)
    return s_dict

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
