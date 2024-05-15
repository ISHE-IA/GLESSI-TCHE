<template>
    <div  class="w-screen h-screen bg-cover bg-fixed bg-no-repeat bg-center" style="background-image: url('tomato.jpeg')">
        <div class="h-screen py-16 flex flex-col justify-around items-center bg-black bg-opacity-65">
            <div class="max-w-md flex flex-col justify-center items-center">
                <img src="~/assets/images/bot.webp" alt="" class="rounded-full w-24 h-24 mb-5">
                <h1 class="text-4xl text-white uppercase font-bold">Glessi-tche</h1>
            </div>
            <div class="max-w-md w-full flex justify-around">
                <div class="w-32 h-32 rounded-3xl flex justify-center items-center bg-white">
                    <NuxtLink to="/chat/audio">
                        <IconsMicrophone :height="'3'" :width="'3'" :color="'#0B873A'"/>
                    </NuxtLink>
                    
                </div>
                <div class="w-32 h-32 rounded-3xl flex justify-center items-center bg-white">
                    <NuxtLink to="/chat/camera">
                        <IconsCamera :height="'3'" :width="'3'" :color="'#0B873A'"/>
                    </NuxtLink>
                </div>
            </div>
            <div class="max-w-md w-full flex justify-center px-5 md:px-10">
                <div id="end_chat">
                    <NuxtLink to="/"><IconsArrowLeft :height="'3'" :width="'3'" :color="'#fff'"/></NuxtLink>
                </div>
            </div>
        </div>
    </div>
</template>