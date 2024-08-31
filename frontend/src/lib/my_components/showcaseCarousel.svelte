<script lang="ts">
    import * as Card from "$lib/components/ui/card/index.js";
    import * as Carousel from "$lib/components/ui/carousel/index.js";
    import type { CarouselAPI } from "$lib/components/ui/carousel/context.js";
	import Button from "$lib/components/ui/button/button.svelte";

    // import { EnvelopeOpen } from 'svelte-radix';
    
    let api: CarouselAPI;
    let current = 0;
    let count = 0;
    
    $: if (api) {
     count = api.scrollSnapList().length;
     current = api.selectedScrollSnap() + 1;
    
     api.on("select", () => {
      current = api.selectedScrollSnap() + 1;
     });
    }
</script>
<div id="showcaseCarouselContainer" class="sticky flex flex-col justify-center items-center top-[50vh] -translate-y-[50%]">
    
    <div>
        <div class="text-muted-foreground py-2 text-center text-sm">
            Slide {current} of {count}
        </div>
    <Carousel.Root bind:api class="w-[650px]">
        <Carousel.Content>
            {#each Array(5) as _, i (i)}
                <Carousel.Item>
                    <Card.Root>
                        <Card.Content
                        class="flex bg-zinc-900
                            h-[350px] 
                        items-center justify-center p-6"
                        >
                        <span class="text-4xl font-semibold">{i + 1}</span>
                        </Card.Content>
                    </Card.Root>
                </Carousel.Item>
            {/each}
        </Carousel.Content>

        
        <Carousel.Previous />
        <Carousel.Next />
    </Carousel.Root>
    <div class="flex flex-row justify-center gap-4 items-center mt-4">
        <Button variant="default" class="w-40">
            Login
        </Button>
        <Button class="w-40">Signup</Button>
    </div>
    </div>
</div>