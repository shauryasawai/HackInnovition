<script>
	import Navbar from "$lib/my_components/navbar.svelte";
	import LeftCol from "./leftCol.svelte";
	import ShowcaseCarousel from "./showcaseCarousel.svelte";
</script>
<div id="canvas" class="relative flex flex-col items-center min-h-screen h-full w-full">
    <div id="bg_canvas" class="fixed h-screen w-screen"></div>
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

<style>
    #bg_canvas {
        z-index: -10;
        background-image: url("./static/Images/bg-final.jpeg");
        background-size: cover;
        background: #0F2027;  /* fallback for old browsers */
        background: -webkit-linear-gradient(to left, #183846, #0e313d, #021a24);  /* Chrome 10-25, Safari 5.1-6 */
        background: linear-gradient(to left, #183846, #0e313d, #021a24); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
    }
</style>