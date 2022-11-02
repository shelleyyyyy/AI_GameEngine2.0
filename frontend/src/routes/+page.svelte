<script>
	import Row from "$lib/main/Row.svelte";
	import Grid from "$lib/main/Grid.svelte";
	import axios from 'axios'
	// import ProgressBar from 'svelte-progress-bar'
	
	const data = {
			grid: [
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

	let sequince = data.sequince;

	$: local_grid = data.grid;

	let x = data.x;
	let y = data.y;

	let dir = data.dir;

	let size = 10

	function runSimulation(trucks, blocks, goals, gridsize, search) {
		loading = true;
		console.log("Ran call")
		console.log(trucks, blocks, goals, gridsize)
		axios.post('http://127.0.0.1:5000/search', {
			
			"trucks": trucks,
			"blocks": blocks,
			"goals": goals,
			"gridsize": gridsize,
			"search": search
		})
		.then(function (response) {
			console.log(response);
			local_grid = response.data.grid
			x = response.data.rootX
			y = response.data.rootY
			dir = response.data.direction
			sequince = response.data.solution
			let time = response.data.time
			console.log("Time: ", time)
			run()
		})
		.catch(function (error) {
			console.log(error);
		});

		// loading = false;
	}

	
	function reset(){

		sequince = data.sequince;

		local_grid = data.grid;

		x = data.x;

		y = data.y;

		dir = data.dir;

		size = 10
	}

	function move(){
		switch(dir){
			case 0:
				// move up
				//console.log("up")
				local_grid[x][y] = "p-u"
				x -= 1
				break;
			case 1:
				// move right
				//console.log("right")
				local_grid[x][y] = "p-r"
				y += 1
				break;
			case 2:
				// move down
				//console.log("down")
				local_grid[x][y] = "p-d"
				x += 1
				break;
			case 3:
				// move left
				//console.log("left")
				local_grid[x][y] = "p-l"
				y -= 1
				break;
		}
		local_grid[x][y] = "a"
		
	}

	async function run(){
		loading = false;
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
					move()
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

	<div class="bg-white p-3 grid gap-3 max-h-200">
		

		<div class=" grid grid-cols-2 gap-3 justify-evenly align-center">
			
			<button class="btn btn-primary" on:click={pleaseWork}>Run</button>
			<button class="btn btn-secondary" on:click={reset}>Reset</button>
		</div>
		{#if loading}
		<!-- <ProgressBar/> -->
		<h1>Loading...</h1>
		{/if}
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
		<Grid dir={dir} rows={local_grid} size={gridSize}></Grid>
	</div>
</div>

