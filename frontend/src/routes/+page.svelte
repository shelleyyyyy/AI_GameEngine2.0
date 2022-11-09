<script>
	import Row from "$lib/main/Row.svelte";
	import Grid from "$lib/main/Grid.svelte";
	import axios from 'axios'
	// import ProgressBar from 'svelte-progress-bar'
	
	const data = {
			grid: [
				[
					"o",
					"a-d",
					"a-d",
					"a-d",
					"c"
				],
				[
					"c",
					"c",
					"c",
					"c",
					"c"
				],
				[
					"c",
					"c",
					"c",
					"c",
					"c"
				],
				[
					"c",
					"c",
					"c",
					"c",
					"c"
				],
				[
					"c",
					"c",
					"c",
					"c",
					"c"
				],
			],
			sequince: [
				"l",
				"r",
				"r",
				"m",
				"m",
				"m",
				"m",
				'l',
				'm',
				'm',
				'm',
				'r',
				'm',
				'm',
			],
			x: 0,
			y: 0,
			dir: 1,
			size: 50,
	}

	$: loading = false;

	// let sequince = data.sequince;

	$: local_grid = data.grid;
	let size = 10
	let trucks = []

	// let x = data.x;
	// let y = data.y;

	// let trucks = [];
	

	// let dir = data.dir;

	

	function runSimulation(trucks, blocks, goals, gridsize, search) {
		// loading = true;
		// console.log("Ran call")
		// console.log(trucks, blocks, goals, gridsize)
		// axios.post('http://127.0.0.1:5000/search', {
			
		// 	"trucks": trucks,
		// 	"blocks": blocks,
		// 	"goals": goals,
		// 	"gridsize": gridsize,
		// 	"search": search
		// })
		// .then(function (response) {
		// 	// console.log(response);
		// 	local_grid = response.data.grid
		// 	size = local_grid.length
		// 	// x = response.data.rootX
		// 	// y = response.data.rootY
		// 	// dir = response.data.direction
		// 	// sequince = response.data.solution
		// 	// let time = response.data.time
		// 	// console.log("Time: ", time)

			
		// })
		// .catch(function (error) {
		// 	console.log(error);
		// });
		console.log("RUNNING SIMULATION")

		trucks = [
				{
					x: 0,
					y: 1,
					dir: 2,
					time: '1',
					sequince: ['m', 'm', 'm']
				},
				{
					x: 0,
					y: 2,
					dir: 2,
					time: '1',
					sequince: ['m', 'm', 'm']
				},
				{
					x: 0,
					y: 3,
					dir: 2,
					time: '1',
					sequince: ['m', 'm', 'm']
				},
			]
			multiAgentRun(trucks)

		// loading = false;
	}

	function multiAgentRun(trucks){
		loading = false;
		// for(let i = 0; i < trucks.lenght; i++){
		// 	let x = trucks[i].x
		// 	let y = trucks[i].y
		// 	let dir = trucks[i].dir
		// 	let sequince = trucks[i].sequince
		// 	run(x, y, sequince, dir)
		// }

		let x = trucks[0].x
		let y = trucks[0].y
		let dir = trucks[0].dir
		let sequince = trucks[0].sequince
		run(x, y, sequince, dir)
	}
	
	// function reset(){

	// 	sequince = data.sequince;

	// 	local_grid = data.grid;

	// 	x = data.x;

	// 	y = data.y;

	// 	dir = data.dir;

	// 	size = 10
	// }

	function move(x, y){
		console.log(local_grid[x][y])
		switch(local_grid[y][x]){
			case 'a-u':
				// move up
				//console.log("up")
				local_grid[x][y] = "p-u"
				x -= 1
				local_grid[x][y] = "a-u"
				break;
			case 'a-r':
				// move right
				//console.log("right")
				local_grid[x][y] = "p-r"
				y += 1
				local_grid[x][y] = "a-r"
				break;
			case 'a-d':
				// move down
				console.log("down")
				local_grid[x][y] = "p-d"
				x += 1
				local_grid[x][y] = "a-d"
				break;
			case 'a-l':
				// move left
				//console.log("left")
				local_grid[x][y] = "p-l"
				y -= 1
				local_grid[x][y] = "a-l"
				break;
		}
	}

	async function run(x, y, sequince, dir){
		for(let i = 0; i < sequince.length; i++){

			await new Promise(r => setTimeout(r, 200));
			// sleep for 1 second

			switch (sequince[i]){
				case "l":
					// move left
					//console.log("left")
					dir = (dir + 3) % 4
					//console.log(dir)
					break;
				case "r":
					// move right
					//console.log("right")
					dir = (dir + 1) % 4
					//console.log(dir)
					break;
				case "m":
					// move forward
					console.log("moveing")
					move(x, y)
					break;
					
			}

			switch(dir){
				case 0:
					local_grid[x][y] = "a-u"
					break;
				case 1:
					local_grid[x][y] = "a-r"
					break;
				case 2:
					local_grid[x][y] = "a-d"
					break;
				case 3:
					local_grid[x][y] = "a-l"
					break;
			}
		}
	}

	function pleaseWork(){
		loading = true;
		runSimulation(1, numberOfBlocks, 1, gridSize, search)
		//run();
	}

	let gridSize = 0;
	let numberOfBlocks = 0;
	let search = ""

	let searchTypes = [
		"Breadth First Search",
		"Depth First Search",
		"Depth Limit Search",
		"Uniform Cost Search",
		"Iterative Depth Limited Search"
	];

	// const progress = new ProgressBar({
	// 	target: document.querySelector('body'),
	// 	props: { color: '#0366d6' }
	// })

</script>

<h1 class="text-center text-6xl my-10">TRUCK AGENT WORLD</h1>

<div class="flex justify-center gap-3">

	<div class="bg-white p-3 grid gap-3" style:height={"32rem"}>
		

		<div class=" grid grid-cols-2 gap-3 justify-evenly align-center">
			
			<button class="btn btn-primary" on:click={pleaseWork}>Run</button>
			<button class="btn btn-secondary" >Reset</button>
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
</div>

