<script>
	import Navbar from "$lib/my_components/navbar.svelte";
	import ShowcaseCarousel from "$lib/my_components/showcaseCarousel.svelte";
</script>
<div id="canvas" class="relative flex flex-col items-center min-h-screen h-full w-full">
    <Navbar></Navbar>
    <span class="font-greatVibes text-[10rem] mt-20">Life Quest</span>

    <ShowcaseCarousel></ShowcaseCarousel>
</div>