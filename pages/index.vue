<template>
    <div class="w-screen h-screen bg-cover bg-fixed bg-no-repeat bg-center" style="background-image: url('famer.jpeg')">
        <div class="h-screen flex flex-col justify-between items-center bg-green-600 bg-opacity-65">
            <div id="head" class="h-full flex items-center">
                <div class="flex flex-col justify-center items-center">
                    <img src="~/assets/images/bot.webp" alt="" class="rounded-full w-24 h-24 mb-5">
                    <h1 class="text-4xl text-white uppercase font-bold">Glessi-tche</h1>
                </div>
            </div>
            <div class="bg-white w-full py-10 rounded-t-3xl flex justify-center">
                <div class="grid grid-cols-2 gap-8">
                    <div @click="goToChat" class=" cursor-pointer rounded-3xl text-white w-32 h-32 flex flex-col justify-around items-center bg-green-glessi">
                        <div class="text-2xl">FON</div>
                        <div>
                            <IconsVolumeHight :height="'3'" :width="'3'" :color="'#fff'"/>
                        </div>
                    </div>
                    <div @click="goToChat" class=" cursor-pointer rounded-3xl text-white w-32 h-32 flex flex-col justify-around items-center bg-yellow-glessi">
                        <div class="text-2xl text-black">YORUBA</div>
                        <div>
                            <IconsVolumeHight :height="'3'" :width="'3'"/>
                        </div>
                    </div>
                    <div @click="goToChat" class=" cursor-pointer rounded-3xl text-white w-32 h-32 flex flex-col justify-around items-center bg-red-glessi">
                        <div class="text-2xl">DENDI</div>
                        <div>
                            <IconsVolumeHight :height="'3'" :width="'3'" :color="'#fff'"/>
                        </div>
                    </div>
                    <div @click="goToChat" class=" cursor-pointer rounded-3xl text-white w-32 h-32 flex flex-col justify-around items-center bg-blue-glessi">
                        <div class="text-2xl">BARIBA</div>
                        <div>
                            <IconsVolumeHight :height="'3'" :width="'3'" :color="'#fff'"/>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
function goToChat () {
    return navigateTo('/chat')
}
</script>