<script>
	import Button from "$lib/components/ui/button/button.svelte";

</script>
<div class="top-0 fixed justify-center items-center flex flex-col w-full h-20">
    <div class="mt-2 flex flex-row gap-5 px-5 items-center grow bg-zinc-900 h-full w-2/3 rounded-2xl">
        <div class="relative bg-zinc-800 h-4 grow flex justify-center items-center">
            <div class="h-12 w-12 bg-zinc-700 rounded-[3rem]"></div>
        </div>
        <Button class="w-28" variant="outline">Home</Button>
        <Button class="w-28" variant="default">Nutrition</Button>
        <Button class="w-28" variant="default">Mental Health</Button>
        <Button class="w-28" variant="default">Fitness</Button>
        <Button class="w-28" variant="default">Yoga</Button>
        <Button class="w-28" variant="default">Feedback</Button>
        <Button class="w-28" variant="outline">About us</Button>
        <div class="relative bg-zinc-800 h-4 grow flex justify-center items-center">
            <div class="h-12 w-12 bg-zinc-700 rounded-[3rem]"></div>
        </div>
    </div>
</div>