<script>

$: to_be_fetched = {
        grid: [
            ["c", "c", "c", "c", "c"],
            ["a-d", "a-d", "a-d", "c", "c"],
            ["c", "c", "c", "c", "c"],
            ["c", "c", "c", "g", "c"],
            ["c", "c", "c", "c", "c"]
        ],
        stats: {
            size: 5,
            longestPath: 7,
            shortestPath: 5,
        },
        agents: [
            {
                position: {
                    x: 0,
                    y: 1,
                },
                status: "a-d",
                sequence: ['l', 'r  ', 'm', 'm', 'l', 'm', 'm'],
                stats: {
                    id: 1,
                    time: 5,
                    path: 5,
                }
            },
        ], 
        searchTypes: [
            "Breadth First Search",
            "Depth First Search",
            "Depth Limit Search",
            "Uniform Cost Search",
            "Iterative Depth Limited Search"
        ]
    }

</script>

<div class="flex justify-center">
    <div class="p-3 w-[40em] bg-white grid">
        <h1 class="text-3xl bold p-5 text-center">Stats</h1>
        <div class="grid gap-5">
            <div class="stats shadow">
                <div class="stat">
                    <div class="stat-title">Longest Path</div>
                    <div class="stat-value text-primary">25.6K</div>
                </div>
    
                <div class="stat">
                    <div class="stat-title">Shortest Path</div>
                    <div class="stat-value text-primary">25.6K</div>
                </div>
    
                <div class="stat">
                    <div class="stat-title">Longest Time</div>
                    <div class="stat-value text-primary">25.6K</div>
                </div>
            </div>
        </div>
    
        <h1 class="text-center p-5 text-3xl">Individual Trucks</h1>
        <div class="grid gap-5">
            {#each to_be_fetched.agents as agent}
    
            <div class="stats shadow">
                <div class="stat">
                    <div class="stat-title">Truck ID</div>
                    <div class="stat-value text-primary">Truck {agent.stats.id}</div>
                </div>
                
                <div class="stat">
                    <div class="stat-title">Path Length</div>
                    <div class="stat-value text-primary">{agent.stats.path}</div>
                </div>
    
                <div class="stat">
                    <div class="stat-title">Time to solve</div>
                    <div class="stat-value text-primary">{agent.stats.time}s</div>
                </div>
            </div>
            {/each}
        </div>  
    </div>
</div>