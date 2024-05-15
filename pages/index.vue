<template>
    <div class="w-screen h-screen bg-cover bg-fixed bg-no-repeat bg-center" style="background-image: url('famer.jpeg')">
        <div class="h-screen flex flex-col justify-end items-center bg-green-600 bg-opacity-65">
            

            <div class="bg-white w-full py-10 rounded-t-3xl flex justify-center">
                <div class="grid grid-cols-2 gap-8">
                    <div class="rounded-3xl text-white w-32 h-32 flex flex-col justify-around items-center bg-green-glessi">
                        <div class="text-2xl">FON</div>
                        <div>
                            <IconsVolumeHight :height="'3'" :width="'3'" :color="'#fff'"/>
                        </div>
                    </div>
                    <div class="rounded-3xl text-white w-32 h-32 flex flex-col justify-around items-center bg-yellow-glessi">
                        <div class="text-2xl text-black">YORUBA</div>
                        <div>
                            <IconsVolumeHight :height="'3'" :width="'3'"/>
                        </div>
                    </div>
                    <div class="rounded-3xl text-white w-32 h-32 flex flex-col justify-around items-center bg-red-glessi">
                        <div class="text-2xl">DENDI</div>
                        <div>
                            <IconsVolumeHight :height="'3'" :width="'3'" :color="'#fff'"/>
                        </div>
                    </div>
                    <div class="rounded-3xl text-white w-32 h-32 flex flex-col justify-around items-center bg-blue-glessi">
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