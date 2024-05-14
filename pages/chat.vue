<template>
    <div class="h-screen flex flex-col justify-between items-center py-5 bg-gradient-to-t from-black">
        <h1 class="text-xl sm:text-2xl md:text-3xl text-white font-semibold text-center uppercase">KWABO</h1>
        <div><img class="rounded-full w-40 h-40 border-2 border-famer-color" :src="'robot.jpg'" alt=""></div>
        <div class="flex">
            <div class="mx-4">
                <div class="relative w-28">
                    <div class="absolute inset-0 flex items-center justify-center">
                        <div class="w-28 h-28 flex justify-center items-center rounded-full bg-white"><IconsCamera :height="'3'" :width="'3'" :color="'#FF8B04'"/></div>
                    </div>
                </div>
                <!--<input type="file" class="w-28 h-28 flex justify-center items-center"/>-->
            </div>
            <div class="mx-4">
                <div class="relative w-28">
                    <div @click="startOrStopRecording" class="absolute inset-0 flex items-center justify-center z-10">
                        <div class="w-28 h-28 flex justify-center items-center rounded-full bg-orange-glessi">
                            <IconsStop v-if="isRecording" :height="'3'" :width="'3'" :color="'#fff'"/>
                            <IconsMicrophone v-else :height="'3'" :width="'3'" :color="'#fff'"/>
                        </div>
                    </div>
                    <div v-if="isRecording" class="recording-indicator w-28 h-28"></div>
                </div>
            </div>
        </div>
        <div class="w-32 h-10 rounded flex justify-center items-center bg-red-600"><NuxtLink to="/"><IconsPhoneEnd :height="'3'" :width="'3'"  :color="'#fff'"/></NuxtLink> </div>
    </div>
</template>
<script setup lang="ts">

const isRecording = ref(false);
const audioChunks = ref<Blob[]>([]);
const audioPlayback = ref<HTMLAudioElement | null>(null);
let mediaRecorder: MediaRecorder | null = null;
let mediaStream: MediaStream | null = null;

function startOrStopRecording() {
    if (isRecording.value) {
        stopRecording();
    } else {
        startRecording();
    }
}

const startRecording = async () => {
    mediaStream = await navigator.mediaDevices.getUserMedia({ audio: true });

    mediaRecorder = new MediaRecorder(mediaStream);
    audioChunks.value = [];

    mediaRecorder.ondataavailable = (event: BlobEvent) => {
        audioChunks.value.push(event.data);
    };

    mediaRecorder.onstop = () => {
            const audioBlob = new Blob(audioChunks.value, { type: 'audio/wav' });
            const audioUrl = URL.createObjectURL(audioBlob);
            if (audioPlayback.value) {
            audioPlayback.value.src = audioUrl;
        }

        // Sauvegarder l'audio dans un fichier
        const a = document.createElement('a');
        a.href = audioUrl;
        a.download = 'enregistrement.wav';
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);

        if (mediaStream) {
            mediaStream.getTracks().forEach(track => track.stop());
        }
    };

    mediaRecorder.start();
    isRecording.value = true;
};

const stopRecording = () => {
    if (mediaRecorder) {
        mediaRecorder.stop();
        isRecording.value = false;
    }
};

// Cleanup media stream when the component is unmounted
onUnmounted(() => {
    if (mediaRecorder && mediaRecorder.state !== 'inactive') {
        mediaRecorder.stop();
    }
    if (mediaStream) {
        mediaStream.getTracks().forEach(track => track.stop());
    }
});
</script>

<style scoped>
.recording-indicator {
  border-radius: 50%;
  background-color: red;
  animation: pulse 1s infinite;
}

@keyframes pulse {
  0% {
    transform: scale(1);
  }
  50% {
    transform: scale(1.2);
  }
  100% {
    transform: scale(1);
  }
}
</style>