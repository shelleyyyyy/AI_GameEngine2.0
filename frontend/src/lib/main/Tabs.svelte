<script>

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
    <div class="flex justify-center tabs tabs-boxed">
        {#each tabs as tab}
            <div on:click={() => setActiveTab(tab.id)} class={activeTab === tab.id ? "tab-active tab" : "tab"} >{tab.name}</div>
        {/each}
    </div>
    <div class="tab-content">
        {#if activeTab === 1}
            <div class="tab-pane">content1</div>
        {/if}
        {#if activeTab === 2}
            <div class="tab-pane">content1</div>
        {/if}
    </div>
</div>