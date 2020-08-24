<template>
    <div class="not-found">
      <div class="container" id="notfound">
        <transition name="bounce">
          <h1 v-if="show">{{ message }} 😢</h1>
        </transition>
      </div>
    </div> 
</template>

<script>
export default {
  name: "NotFound",
  data() {
    return {
      message: "404 - Page Not Found",
      show: false
    }
  },
  mounted() {
    this.show = true; // might need this.$nextTick
  }  
}
</script>

<style scoped>
.not-found {
  width: 80%;
  height: 50%;
  overflow: auto;
  margin: auto;
  position: absolute;
  top: 0; left: 0; bottom: 0; right: 0;
  text-align: center;
}
#notfound {
  position: relative;
  top: 50%;
  -webkit-transform: translateY(-50%);
  -ms-transform: translateY(-50%);
  transform: translateY(-50%);
  color: red;
  text-align: center;
}
</style>


