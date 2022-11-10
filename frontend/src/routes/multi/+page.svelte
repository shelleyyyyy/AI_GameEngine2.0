
<script>
	import Grid from "$lib/main/Grid.svelte";
    import axios from 'axios'

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

    var newData = {}
	
    $: loading = false;
    $: searchTypes = to_be_fetched.searchTypes

    $: local_grid = to_be_fetched.grid

    $: size = to_be_fetched.stats.size
    $: longestPath = to_be_fetched.stats.longestPath
    $: agents = to_be_fetched.agents

    const fetchData = () => {
        loading = true
        axios.post('http://127.0.0.1:5000/search', {
            "trucks": numberOfTrucks,
            "seed": seed,
            "goals": numberOfTrucks,
            "gridsize": gridSize,
            "search": search
        })
        .then(function (response) {
            console.log(response)
            to_be_fetched = response.data
            
            loading = false
            runAgents()
        })
    }

    function moveAgent(position, status, iter){
        let x = position.x;
        let y = position.y;
        switch(status){
            case "a-u":
                local_grid[x][y] = "p-u";
                agents[iter].position.x -= 1;
                x -= 1;
                local_grid[x][y] = "a-u";
                break;
            case "a-r":
                local_grid[x][y] = "p-r";
                agents[iter].position.y += 1;
                y += 1;
                local_grid[x][y] = "a-r";
                break;
            case "a-d":
                local_grid[x][y] = "p-d";
                agents[iter].position.x += 1;
                x += 1
                local_grid[x][y] = "a-d";
                break;
            case "a-l":
                local_grid[x][y] = "p-l";
                agents[iter].position.y -= 1;
                y -= 1
                local_grid[x][y] = "a-l";
                break;
        }
    }

    function turnAgent(position, status, turn, iter){
        let x = position.x;
        let y = position.y;

        switch(status){
            case "a-u":
                if(turn == "l"){
                    local_grid[x][y] = "a-l";
                    agents[iter].status = "a-l"
                }else{
                    local_grid[x][y] = "a-r";
                    agents[iter].status = "a-r"
                }
                break;
            case "a-r":
                if(turn == "l"){
                    local_grid[x][y] = "a-u";
                    agents[iter].status = "a-u"
                }else{
                    local_grid[x][y] = "a-d";
                    agents[iter].status = "a-d"
                }
                break;
            case "a-d":
                if(turn == "l"){
                    local_grid[x][y] = "a-r"
                    agents[iter].status = "a-r"
                }else{
                    local_grid[x][y] = "a-l";
                    agents[iter].status = "a-l"
                }
                break;
            case "a-l":
                if(turn == "l"){
                    local_grid[x][y] = "a-d"
                    agents[iter].status = "a-d"
                }else{
                    local_grid[x][y] = "a-u";
                    agents[iter].status = "a-u"
                }
                break;
        }
    }

    async function runAgents(){
        for(let i = -1; i < longestPath; i++){
            for(let j = 0; j < agents.length; j++){
                run(agents[j], agents[j].sequence[i], j)
            }
            await new Promise(r => setTimeout(r, 1000));
        }
    }

    function run(agent, cmd, iter){
        if(cmd == 'm'){
            moveAgent(agent.position, agent.status, iter)
        } else{
            turnAgent(agent.position, agent.status, cmd, iter)
        }
    }

    // reset function
    function reset(){
        loading = true;
        local_grid = 5
        agents = 0
        loading = false;
    }
    
    // user input
	let gridSize = 0;
	let seed = 0;
    let numberOfTrucks = 0;
	let search = ""

</script>

<h1 class="text-center text-6xl my-10">TRUCK AGENT WORLD</h1>

<div class="flex justify-center gap-3">

	<div class="bg-white p-3 grid gap-3" style:height={"32rem"}>

		<div class=" grid grid-cols-2 gap-3 justify-evenly align-center">
			
			<button class="btn btn-primary" on:click={fetchData}>Run</button>
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
			<h1 class="text-center">Seed</h1>
			<input type="text" placeholder="Type here" class="input w-full" bind:value={seed}/>
			<h1 class="text-center">Number of Trucks</h1>
			<input type="text" placeholder="Type here" class="input w-full" bind:value={numberOfTrucks}/>
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

