<script>
    import Game from "$lib/main/Game.svelte";
    import Tabs from "$lib/main/Tabs.svelte";
    import Stats from "$lib/main/Stats.svelte";

    const tabs = [
        { name: "Game", content: "Tab 1 content", id: 1 },
        { name: "Experiments", content: "Tab 2 content", id: 2 },
    ];

    let activeTab = 1;
    
    function setActiveTab(id) {
        activeTab = id;
    }
   
</script>


<div>
    <h1 class="text-center text-6xl my-10">TRUCK AGENT WORLD</h1>
    
    <div>
        <div class="flex justify-center tabs tabs-boxed">
            {#each tabs as tab}
                <div on:click={() => setActiveTab(tab.id)} class={activeTab === tab.id ? "tab-active tab" : "tab"} >{tab.name}</div>
            {/each}
        </div>
        <div class="tab-content p-5">
            {#if activeTab === 1}
                <Game />
            {/if}
            {#if activeTab === 2}
                <Stats/>
            {/if}
        </div>
    </div>
</div>