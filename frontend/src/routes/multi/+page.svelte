
<script>
	import Grid from "$lib/main/Grid.svelte";
	
    let loading = false;

    const to_be_fetched = {
        grid: [
            ["c", "c", "c", "c", "c"],
            ["a-d", "a-d", "a-d", "c", "c"],
            ["c", "c", "c", "c", "c"],
            ["c", "c", "c", "c", "c"],
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
                sequince: ['l', 'r  ', 'm', 'm', 'l', 'm', 'm'],
                stats: {
                    id: 1,
                    time: 5,
                    path: 5,
                }
            },
            // {
            //     position: {
            //         x: 1,
            //         y: 1,
            //     },
            //     status: "a-d",
            //     sequince: ['l', 'r  ', 'm'],
            //     stats: {
            //         id: 2,
            //         time: 5,
            //         path: 5,
            //     }
            // },
            // {
            //     position: {
            //         x: 2,
            //         y: 1,
            //     },
            //     status: "a-d",
            //     sequince: ['l', 'r  ', 'm'],
            //     stats: {
            //         id: 3,
            //         time: 5,
            //         path: 5,
            //     }
            // },
            
        ], 
        searchTypes: [
            "Breadth First Search",
            "Depth First Search",
            "Depth Limit Search",
            "Uniform Cost Search",
            "Iterative Depth Limited Search"
        ]
    }

    $: local_grid = to_be_fetched.grid;

    $: size = to_be_fetched.stats.size;
    let longestPath = to_be_fetched.stats.longestPath;
    $: agents = to_be_fetched.agents

    function moveAgent(position, status, iter){
        let x = position.x;
        let y = position.y;
        console.log(status)
        switch(status){
            case "a-u":
                console.log("agent up")
                local_grid[y][x] = "p-u";
                agents[iter].position.y -= 1;
                y -= 1;
                local_grid[y][x] = "a-u";
                break;
            case "a-r":
                console.log("agent right")
                local_grid[y][x] = "p-r";
                agents[iter].position.x += 1;
                x += 1;
                local_grid[y][x] = "a-r";
                break;
            case "a-d":
                console.log("agent down")
                local_grid[y][x] = "p-d";
                agents[iter].position.y += 1;
                y += 1
                local_grid[y][x] = "a-d";
                break;
            case "a-l":
                console.log("agent left")
                local_grid[y][x] = "p-l";
                agents[iter].position.x -= 1;
                x -= 1
                local_grid[y][x] = "a-l";
                break;
        }
    }

    function turnAgent(position, status, turn, iter){
        let x = position.x;
        let y = position.y;
        // console.log(status)

        switch(status){
            case "a-u":
                if(turn == "l"){
                    local_grid[y][x] = "a-l";
                    agents[iter].status = "a-l"
                }else{
                    local_grid[y][x] = "a-r";
                    agents[iter].status = "a-r"
                }
                break;
            case "a-r":
                console.log("agent right")
                if(turn == "l"){
                    local_grid[y][x] = "a-u";
                    agents[iter].status = "a-u"
                }else{
                    local_grid[y][x] = "a-d";
                    agents[iter].status = "a-d"
                }
                break;
            case "a-d":
                console.log("agent down")
                if(turn == "l"){
                    local_grid[y][x] = "a-r"
                    agents[iter].status = "a-r"
                }else{
                    local_grid[y][x] = "a-l";
                    agents[iter].status = "a-l"
                }
                break;
            case "a-l":
                if(turn == "l"){
                    local_grid[y][x] = "a-d"
                    agents[iter].status = "a-d"
                }else{
                    local_grid[y][x] = "a-u";
                    agents[iter].status = "a-u"
                }
                break;
        }
    }

    async function runAgents(){
        console.log("runAgents")
        for(let i = 0; i < longestPath; i++){
            for(let j = 0; j < agents.length; j++){
                run(agents[j], agents[j].sequince[i], j)
            }
            await new Promise(r => setTimeout(r, 500));
        }
    }

    function run(agent, cmd, iter){
        console.log(cmd)
        if(cmd == 'm'){
            moveAgent(agent.position, agent.status, iter)
        } else{
            turnAgent(agent.position, agent.status, cmd, iter)
        }
    }

    // reset function
    function reset(){
        loading = true;
        local_grid = to_be_fetched.grid;
        agents = to_be_fetched.agents;
        loading = false;
    }
    
    // user input
	let gridSize = 0;
	let numberOfBlocks = 0;
	let search = ""

	let searchTypes = to_be_fetched.searchTypes;

</script>

<h1 class="text-center text-6xl my-10">TRUCK AGENT WORLD</h1>

<div class="flex justify-center gap-3">

	<div class="bg-white p-3 grid gap-3" style:height={"32rem"}>

		<div class=" grid grid-cols-2 gap-3 justify-evenly align-center">
			
			<button class="btn btn-primary" on:click={runAgents}>Run</button>
			<button class="btn btn-secondary" on:click={reset}>Reset</button>
		</div>
		
		<h1 class="text-3xl bold p-5 text-center">Set Options</h1>
		<div class="bg-gray-500 p-2 justify-evenly">
			<h1 class="py-3 text-center">Select Search Type</h1>
			<select class="select w-full max-w-xs" bind:value={search}>
				{#each searchTypes as s}
					<option value={s}>
						{s}
					</option>
				{/each}
			  </select>
		</div>
		<div class="bg-gray-500 p-2 grid gap-3">
			<h1 class="text-center">Grid Size</h1>
			<input type="text" placeholder="Type here" class="input w-full" bind:value={gridSize}/>
			<h1 class="text-center">Blocked Cells</h1>
			<input type="text" placeholder="Type here" class="input w-full" bind:value={numberOfBlocks}/>
		</div>
	</div>

	<div>
		{#if loading}
			<progress class="progress"></progress>
		{/if}
		{#if !loading}
			<Grid rows={local_grid} size={size}></Grid>
		{/if}
		{#if loading}
			<Grid rows={local_grid} size={size}></Grid>
		{/if}

		<!-- <Grid rows={local_grid} size={size}></Grid> -->
	</div>

    <div class="bg-white p-3">
		<h1 class="text-3xl bold p-5 text-center">Stats</h1>
		<div>
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
                    <div class="stat-title">Path Lenght</div>
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

