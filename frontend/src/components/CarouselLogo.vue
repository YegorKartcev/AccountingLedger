<template>
    <div class="container">
 
        <br>
        <br>
        <div class="row justify-content-center">
            <div class="col-8">

                <b-carousel
                    class="text-center"
                    id="carousel-1"
                    v-model="slide"
                    :interval="3000"
                    fade
                    background="white"
                    img-width="1024"
                    img-height="480"
                    style="text-shadow: 1px 1px 2px #000;"
                    @sliding-start="onSlideStart"
                    @sliding-end="onSlideEnd"
                >
                <!-- Slides with img slot -->
                <!-- Note the classes .d-block and .img-fluid to prevent browser default image alignment -->
                <b-carousel-slide>
                    <template v-slot:img>
                    <img
                        class="im1"

                        src="/static/Django_logo.png"
                        alt="image slot"
                    >
                    </template>
                </b-carousel-slide>

                <b-carousel-slide>
                    <template v-slot:img>
                    <img
                        class="im2"

                        src="/static/DR_logo.png"
                        alt="image slot"
                    >
                    </template>
                </b-carousel-slide>

                <b-carousel-slide>
                    <template v-slot:img>
                    <img
                        class="im3"

                        src="/static/Vue_logo.png"
                        alt="image slot"
                    >
                    </template>
                </b-carousel-slide>

                </b-carousel>

            </div>

        </div>
 
    </div>

</template>

<script>
export default {
    name: "CarouselLogoComponent",
    data() {
      return {
        slide: 0,
        sliding: null
      }
    },
    methods: {
      onSlideStart() {
        this.sliding = true
      },
      onSlideEnd() {
        this.sliding = false
      }
    }

}
</script>

<style scoped>
    .carousel-item img {
        height:12vh !important ;
    }

.carousel-control-next-icon,
.carousel-control-prev-icon {
   filter: invert(1);
}
</style>