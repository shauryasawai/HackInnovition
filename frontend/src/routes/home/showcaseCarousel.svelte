<script lang="ts">
    import * as Card from "$lib/components/ui/card/index.js";
    import * as Carousel from "$lib/components/ui/carousel/index.js";
    import type { CarouselAPI } from "$lib/components/ui/carousel/context.js";
	import Button from "$lib/components/ui/button/button.svelte";

    // import { EnvelopeOpen } from 'svelte-radix';
    
    let api: CarouselAPI;
    // let current = 0;
    // let count = 0;
    
    // $: if (api) {
    //  count = api.scrollSnapList().length;
    //  current = api.selectedScrollSnap() + 1;
    
    //  api.on("select", () => {
    //   current = api.selectedScrollSnap() + 1;
    //  });
    // }
  let images = [
    '/src/assets/Screenshot 2024-09-01 091036.png',
    '/src/assets/Screenshot 2024-09-01 093623.png',
    '/src/assets/Screenshot 2024-09-01 093314.png',
    '/src/assets/Screenshot 2024-09-01 094732.png',
    '/src/assets/book-a-call.jpeg',
    '/src/assets/nutrition-page.jpeg'
  ];
</script>
<div id="showcaseCarouselContainer" class="sticky flex flex-col justify-center items-center top-[50vh] -translate-y-[50%]">
    
    <div>
        <!-- <div class="text-muted-foreground py-2 text-center text-sm">
            Slide {count} of {count}
        </div> -->
    <Carousel.Root bind:api class="w-[650px]">
        <Carousel.Content>
            {#each images as image}
                <Carousel.Item>
                    <Card.Root>
                        <Card.Content
                        class="flex bg-zinc-900
                            h-[350px] 
                        items-center justify-center"
                        >
                        <img src="{image}" alt="Image" class="object-contain w-full h-full">
                        </Card.Content>
                    </Card.Root>
                </Carousel.Item>
            {/each}
        </Carousel.Content>

        
        <Carousel.Previous />
        <Carousel.Next />
    </Carousel.Root>
    <div class="flex flex-row justify-center gap-4 items-center mt-4">
        <Button variant="default" class="w-30" href="http://127.0.0.1:8000/">
            Login
        </Button>
        <Button class="w-30" href="http://127.0.0.1:8000/signup/">Signup</Button>
    </div>
    </div>
</div>