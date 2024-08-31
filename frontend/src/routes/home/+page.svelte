<script>
	import Navbar from "$lib/my_components/navbar.svelte";
	import ShowcaseCarousel from "$lib/my_components/showcaseCarousel.svelte";
	import LeftCol from "./leftCol.svelte";
</script>
<div id="canvas" class="relative flex flex-col items-center min-h-screen h-full w-full">
    <Navbar></Navbar>
    <span class="font-greatVibes text-[10rem] mt-20">Health Track</span>


    <div class="w-full flex flex-row">
        <LeftCol></LeftCol>
        <div class="w-1/2" id="right-div">
            <div class="h-[300px]"></div>
            <ShowcaseCarousel></ShowcaseCarousel>
        </div>
    </div>
</div>