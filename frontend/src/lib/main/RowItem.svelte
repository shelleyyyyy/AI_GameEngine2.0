<script>
    import {
        Walk,
        ArrowUpOutline,
        ArrowDownOutline,
        ArrowForwardOutline,
        ArrowBackOutline,
        WalkOutline,
        ChevronUpOutline,
        ChevronDownOutline,
        ChevronForwardOutline,
        ChevronBackOutline,
        HeartCircleOutline,

    } from "svelte-ionicons";


    // get grid diminseions
    export let diminsions;
    export let item;

    let calc = 30/diminsions;
    let size = String(calc) + "rem"
</script>

{#if "o" == item}
    <div style:height={size} style:width={size} class="border-black border-2 shadow-xl w-full">
        <!-- {item} -->
    </div>
{/if}

{#if "c" == item}
        <div style:height={size} style:width={size} class=" bg-black text-white shadow-xl w-full">
            <!-- {item} -->
        </div>
{/if}

{#if "a-u" == item}
    <div style:height={size} style:width={size} class="p-1 flex justify-center bg-red-700 text-white shadow-xl w-full">
        <!-- <ArrowUpOutline size="fit" rotate={2}/> -->
        <img  class="h-20 rotate-90" src=""/>
    </div>
    <!-- <img  class="h-20 rotate-90" src="https://www.vmi.edu/media/content-assets/images/people/faculty/LRamoni.jpg"/> -->
{/if}

{#if "a-r" == item}
    <div style:height={size} style:width={size} class="p-1 flex justify-center bg-red-700 text-white shadow-xl w-full">
        <!-- <ArrowForwardOutline size="fit" rotate={2}/> -->
        <img  class=" rotate-90" src=""/>
    </div>
{/if}

{#if "a-d" == item}
    <div style:height={size} style:width={size} class="p-1 flex justify-center bg-red-700 text-white shadow-xl w-full">
        <!-- <ArrowDownOutline size="fit" rotate={2}/> -->
        <img  class="h-20 rotate-180" src=""/>
    </div>
{/if}

{#if "a-l" == item}
    <div style:height={size} style:width={size} class="p-1 flex justify-center bg-red-700 text-white shadow-xl w-full">
        <!-- <ArrowBackOutline size="fit" rotate={2}/> -->
        <img  class="h-20 rotate-270" src=""/>
    </div>
{/if}


{#if "p-u" == item}
    <div style:height={size} style:width={size} class="flex justify-center bg-gray-400 text-white shadow-xl w-full">
        <ChevronUpOutline size="fit" />
    </div>
{/if}  

{#if "p-r" == item}
    <div style:height={size} style:width={size} class="flex justify-center bg-gray-400 text-white shadow-xl w-full">
        <ChevronForwardOutline size="fit" />
    </div>
{/if}  

{#if "p-d" == item}
    <div style:height={size} style:width={size} class="flex justify-center bg-gray-400 text-white shadow-xl w-full">
        <ChevronDownOutline size="fit" />
    </div>
{/if}  

{#if "p-l" == item}
    <div style:height={size} style:width={size} class="flex justify-center bg-gray-400 text-white shadow-xl w-full">
        <ChevronBackOutline size="fit" />
    </div>
{/if}  

{#if "g" == item}
    <div style:height={size} style:width={size} class="flex justify-center bg-pink-400 text-white shadow-xl w-full">
        <HeartCircleOutline size="fit" />
    </div>
{/if}  