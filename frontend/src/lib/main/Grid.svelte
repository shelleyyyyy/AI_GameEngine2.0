<script>
	import Row from "$lib/main/Row.svelte";
	
	export let dir;
	export let rows;
    export let size;

</script>

<div class="flex justify-center">
	<span class="grid justify-center shadow-xl rounded-md gap-2 bg-white p-5">
		{#each rows as row}
			<Row dir={dir} size={size} arr={row}></Row>
		{/each}
	</span>
</div>
