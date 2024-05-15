<template>
    <div  class="w-screen h-screen bg-cover bg-fixed bg-no-repeat bg-center">
        <div class="h-screen py-16 flex flex-col justify-around items-center bg-black bg-opacity-65">
            <div class="max-w-md flex flex-col justify-center items-center">
                <img src="~/assets/images/bot.webp" alt="" class="rounded-full w-24 h-24 mb-5">
                <h1 class="text-4xl text-white uppercase font-bold">Glessi-tche</h1>
            </div>
            <div id="timer" class="max-w-md text-white">
                <span class="text-4xl mx-4">{{ hours < 10 ? '0' + hours : hours }}</span>
                <span class="text-4xl mx-4">:</span>
                <span class="text-4xl mx-4">{{ minutes < 10 ? '0' + minutes : minutes }}</span>
                <span class="text-4xl mx-4">:</span>
                <span class="text-4xl mx-4">{{ seconds < 10 ? '0' + seconds : seconds }}</span>
            </div>
            <div class="max-w-md w-full flex justify-center">
                <div @click="startOrStopRecording" class="w-32 h-32 rounded-3xl flex justify-center items-center bg-white">
                    <IconsStop v-if="isRecording" :height="'4'" :width="'4'" :color="'#0B873A'"/>
                    <IconsMicrophone v-else :height="'3'" :width="'3'" :color="'#0B873A'"/>
                </div>
            </div>
            <div class="max-w-md w-full flex justify-center px-5 md:px-10">
                <div id="end_chat" class="w-full h-16 rounded-md bg-red-600 flex justify-center items-center">
                    <NuxtLink to="/chat"><IconsPhoneEnd :height="'3'" :width="'3'" :color="'#fff'"/></NuxtLink>
                </div>
            </div>
        </div>
    </div>
</template>
<script setup lang="ts">
const hours = ref<number>(0)
const minutes = ref<number>(0)
const seconds = ref<number>(0)
const time = ref<number>(0)

let timer: ReturnType<typeof setInterval> | null = null

function setTime() {
    hours.value = Math.floor(time.value / 3600)
    minutes.value = Math.floor((time.value % 3600) / 60)
    seconds.value = Math.floor(time.value % 60)
}

function startTimer() {
    if (timer !== null) {
        clearInterval(timer)
    }
    time.value = 0
    timer = setInterval(() => {
        time.value++
        setTime()
    }, 1000)
}

function stopTimer() {
    if (timer !== null) {
        clearInterval(timer)
        timer = null
    }
}

const isRecording = ref(false);
const audioChunks = ref<Blob[]>([]);
const audioPlayback = ref<HTMLAudioElement | null>(null);
let mediaRecorder: MediaRecorder | null = null;
let mediaStream: MediaStream | null = null;

function startOrStopRecording() {
    if (isRecording.value) {
        stopRecording();
        stopTimer();
    } else {
        startRecording();
        startTimer();
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