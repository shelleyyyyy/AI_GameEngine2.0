<script>
    import RowItem from "./RowItem.svelte";

    export let dir;
    export let arr;
    export let size;
</script>

<div class="flex gap-2">
    {#each arr as item}
        <RowItem dir={dir} diminsions={size} item={item}></RowItem>
    {/each} 
</div>

<style>
    .test{
        height: 20%;
    }
</style>