<template>
    <div class="h-screen flex flex-col justify-center items-center bg-gradient-to-t from-black py-5 md:py-7">
        <h1 class="text-4xl text-white font-semibold mt-60">GLESSI-TCHE</h1>

        <ul id="lang" class="flex flex-col justify-center items-center w-full h-full">
            <li class="w-1/2 h-16 rounded flex justify-center items-center text-2xl text-white bg-green-glessi"><NuxtLink to="/chat">FON</NuxtLink></li>
            <li class="my-4 w-1/2 h-16 rounded flex justify-center items-center text-2xl text-black bg-yellow-glessi"><NuxtLink to="/chat">YORUBA</NuxtLink></li>
            <li class="w-1/2 h-16 rounded flex justify-center items-center text-2xl text-white bg-red-glessi"><NuxtLink to="/chat">HAOUSSA</NuxtLink></li>
            <li class="my-4 sm:my-6 md:my-8 w-24 h-24 flex justify-center items-center rounded-full bg-orange-glessi"><NuxtLink to="/chat"><IconsMicrophone :height="'1.5'" :color="'#fff'"/></NuxtLink></li>
        </ul>
    </div>
</template>