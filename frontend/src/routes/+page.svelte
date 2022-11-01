<script>
	import Row from "$lib/main/Row.svelte";
	import Grid from "$lib/main/Grid.svelte";
	import { GridSharp } from "svelte-ionicons";
	import axios from 'axios'
	
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

	let sequince = data.sequince;

	$: local_grid = data.grid;

	let x = data.x;
	let y = data.y;

	let dir = data.dir;

	let size = 10

	function runSimulation(trucks, blocks, goals, gridsize, search) {
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
			run()
		})
		.catch(function (error) {
			console.log(error);
		});
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
				console.log("up")
				local_grid[x][y] = "p-u"
				x -= 1
				break;
			case 1:
				// move right
				console.log("right")
				local_grid[x][y] = "p-r"
				y += 1
				break;
			case 2:
				// move down
				console.log("down")
				local_grid[x][y] = "p-d"
				x += 1
				break;
			case 3:
				// move left
				console.log("left")
				local_grid[x][y] = "p-l"
				y -= 1
				break;
		}
		local_grid[x][y] = "a"
		
	}

	async function run(){
		for(let i = 0; i < sequince.length; i++){

			await new Promise(r => setTimeout(r, 200));
			// sleep for 1 second

			switch (sequince[i]){
				case "l":
					// move left
					console.log("left")
					dir = (dir + 3) % 4
					console.log(dir)
					break;
				case "r":
					// move right
					console.log("right")
					dir = (dir + 1) % 4
					console.log(dir)
					break;
				case "m":
					// move forward
					move()
					break;
					
			}
		}
	}

	function pleaseWork(){
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
		"Uniform Cost Search"
	];

</script>

<h1 class="text-center text-6xl my-10">TRUCK AGENT WORLD</h1>

<div class="grid justify-center">
	<div class="border-1 grid grid-cols-3 border-black">
		<div class="p-5 grid grid-cols-2 h-40 gap-3 ">
			<div class="flex justify-center">
				<button  class="w-36 py-5 my-5 bg-blue-500 hover:bg-blue-700 text-white font-bold rounded" on:click={pleaseWork}>Run</button>
			</div>
			<div class="flex justify-center">
				<button  class="w-36 py-5 my-5 bg-blue-500 hover:bg-blue-700 text-white font-bold rounded" on:click={reset}>Reset</button>
			</div>
		</div>
		<div class="grid grid-cols-2">
			<div class="grid justify-center">
				<h1 for="gridSize" class="text-2xl text-center">Grid Size</h1>
				<input type="text" class="w-36 py-5 my-5 bg-blue-500 hover:bg-blue-700 text-white font-bold rounded" bind:value={gridSize}>
			</div>
			<div class="grid justify-center">
				<h1 for="gridSize" class="text-2xl text-center"># of Blocks</h1>
				<input type="text" class="w-36 py-5 my-5 bg-blue-500 hover:bg-blue-700 text-white font-bold rounded" bind:value={numberOfBlocks}>
			</div>
		</div>
		<div>
			<h1 for="gridSize" class="text-2xl text-center mb-5">Select Search Type</h1>
			<select bind:value={search}>
				{#each searchTypes as s}
					<option value={s}>
						{s}
					</option>
				{/each}
			</select>
		</div>
	</div>
	<div>
		<Grid dir={dir} rows={local_grid} size={size}></Grid>
	</div>
</div>
