<template>
    <div class="h-screen flex flex-col justify-between items-center bg-gradient-to-t from-black">
        <h1 class="text-2xl sm:text-3xl md:text-4xl text-white">Acceuil</h1>

        <div class="py-5">
            <ul id="lang" class="flex flex-col justify-between items-center">
                <li><div class="my-2 sm:my-4 md:my-6 w-24 h-6 rounded text-center py-auto text-white bg-green-glessi">FON</div></li>
                <li><div class="my-2 sm:my-4 md:my-6 w-24 h-6 rounded text-center py-auto text-white bg-yellow-glessi">YORUBA</div></li>
                <li><div class="my-2 sm:my-4 md:my-6 w-24 h-6 rounded text-center py-auto text-white bg-red-glessi">HAOUSSA</div></li>
                <li>
                    <div class="my-4 sm:my-6 md:my-8 w-12 h-12 flex justify-center items-center rounded-full bg-orange-glessi">
                        <IconsMicrophone :height="'1.5'" :color="'#fff'"/>
                    </div>
                </li>
            </ul>
        </div>
    </div>
</template>