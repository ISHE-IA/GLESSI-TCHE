<template>
    <div class="h-screen flex flex-col justify-between items-center bg-gradient-to-t from-black">
        <h1 class="text-2xl sm:text-3xl md:text-4xl text-white font-semibold mt-2 sm:mt-4 md:mt-6">GLESSI-TCHE</h1>

        <div class="py-5">
            <ul id="lang" class="flex flex-col justify-between items-center">
                <li class="my-2 sm:my-3 md:my-4 w-24 sm:w-32 md:w-40 h-6 rounded text-center py-auto text-white bg-green-glessi"><NuxtLink to="/chat">FON</NuxtLink></li>
                <li class="my-2 sm:my-3 md:my-4 w-24 sm:w-32 md:w-40 h-6 rounded text-center py-auto text-white bg-yellow-glessi"><NuxtLink to="/chat">YORUBA</NuxtLink></li>
                <li class="my-2 sm:my-3 md:my-4 w-24 sm:w-32 md:w-40 h-6 rounded text-center py-auto text-white bg-red-glessi"><NuxtLink to="/chat">HAOUSSA</NuxtLink></li>
                <li class="my-4 sm:my-6 md:my-8 w-12 h-12 flex justify-center items-center rounded-full bg-orange-glessi"><NuxtLink to="/chat"><IconsMicrophone :height="'1.5'" :color="'#fff'"/></NuxtLink></li>
            </ul>
        </div>
    </div>
</template>