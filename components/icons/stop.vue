<template>
    <div>
        <svg :width="width ? width + 'em' : '1em'" :height="height ? height + 'em' : '1em'" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 384 512">
            <!--!Font Awesome Free 6.5.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2024 Fonticons, Inc. -->
            <path :stroke="color ? color : '#000'" :fill="color ? color : '#000'" d="M0 128C0 92.7 28.7 64 64 64H320c35.3 0 64 28.7 64 64V384c0 35.3-28.7 64-64 64H64c-35.3 0-64-28.7-64-64V128z"/>
        </svg>
    </div>
</template>
<script setup lang="ts">
defineProps <{
    width?: string,
    height?: string,
    color?: string
}>()
</script>