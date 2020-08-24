<template>
  <div id="app">
    <NavbarComponent/>
    <transition name="router-anim" mode="out-in">
      <router-view/>
    </transition> 
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
import NavbarComponent from "@/components/Navbar.vue";
export default {
  name: "App",
  components: {
    NavbarComponent
  },
  methods: {
    async setUserInfo() {
      // add the username of the logged in user to localStorage
      const data = await apiService("/api/user/");
      const requestUser = data["username"];
      window.localStorage.setItem("username", requestUser);
    }
  },
  created() {
    this.setUserInfo()
  }
};
</script>

<style>
  html,
  body {
    height: 100%;
    font-family: "Playfair Display", serif;
  }
  .expenditure {
    background-color: #ffe6e2 !important;
    width:100% !important;
  }
  .author-name {
    font-weight: bold !important;
    color: #DC3545 !important;
  }
  .income {
    background-color: #ebffe2 !important;
    width:100% !important;
  }
  .task {
    background-color: rgb(224, 249, 255) !important;
    width:100% !important;
  }  
  .icon {
    height: 20px !important;
    width: 20px !important;
    vertical-align: middle !important;
    margin-right: 0.5ex;
  }
  .wdt230 {
    width: 250px !important;
  }
  .wdt150 {
    width: 150px !important;
  }
  .btn:focus {
    box-shadow: none !important;
  }
  .btn {
    transition: transform 0.8s !important; /* Animation */
  }
 
  .btn:hover{
    transform: scale(1.2, 1.2);
  }
  .error {
    color: red
  }


  .fade-enter-active, .fade-leave-active {
    transition: opacity 2.0s ease-out !important;
  }
  .fade-enter, .fade-leave-to {
    opacity: 0;
  }
  .slide-fade-enter-active {
    transition: all 0.8s ease !important;
  }
  .slide-fade-leave-active {
    transition: all 0.8s cubic-bezier(1.0, 0.5, 0.8, 1.0) !important;
  }
  .slide-fade-enter, .slide-fade-leave-to
  /* .slide-fade-leave-active до версии 2.1.8 */ {
    transform: translateY(30px) !important;
    opacity: 0;
  }

  .slide-fade2-enter-active {
    transition: all 1.5s ease !important;
  }
  .slide-fade2-leave-active {
    transition: all 1.5s cubic-bezier(1.0, 0.5, 0.8, 1.0) !important;
  }
  .slide-fade2-enter, .slide-fade2-leave-to
  /* .slide-fade-leave-active до версии 2.1.8 */ {
    transform: translateY(100px) !important;
    opacity: 0;
  }

  .slide-fade3-enter-active {
    transition: all 1.5s ease !important;
  }
  .slide-fade3-leave-active {
    transition: all 1.5s cubic-bezier(1.0, 0.5, 0.8, 1.0) !important;
  }
  .slide-fade3-enter, .slide-fade3-leave-to
  /* .slide-fade-leave-active до версии 2.1.8 */ {
    transform: translateX(-200px) !important;
    opacity: 0;
  }


  .slide-3-enter-active {
    animation: slide-3-in 1.5s;
  }
  .slide-3-leave-active {
    animation: slide-3-in 1.5s reverse;
  }
  @keyframes slide-3-in {
    0% {transform: translateY(-200px); opacity: 0}    
    100% {transform: translateY(0px); opacity: 1}
  }

  .slide-4-enter-active {
    animation: slide-4-in 1.5s;
  }
  .slide-4-leave-active {
    animation: slide-4-in 1.5s reverse;
  }
  @keyframes slide-4-in {
    0% {transform: translateY(200px); opacity: 0}    
    100% {transform: translateY(0px); opacity: 1}
  }

  .slide-5-enter-active {
    animation: slide-5-in 1.5s ease-out forwards;

  }
  .slide-5-leave-active {
    animation: slide-5-in 1.5s reverse ease-out forwards;
  }
  @keyframes slide-5-in {
    0% {transform: translateX(200px); opacity: 0}    
    100% {transform: translateX(0px); opacity: 1}
  }

  .slide-6-enter-active {
    animation: slide-6-in 1.5s ease-out forwards;
  }
  .slide-6-leave-active {
    animation: slide-6-in 1.5s reverse ease-out forwards;
  }
  @keyframes slide-6-in {
    0% {transform: translateX(-200px); opacity: 0}    
    100% {transform: translateX(0px); opacity: 1}
  }



.router-anim-enter-active {
  animation: coming 1s;
  opacity: 0;
}
.router-anim-leave-active {
  animation: going 1s;
}

@keyframes going {
  from {
    transform: translateX(0);
  }
  to {
    transform: translateX(-150px);
    opacity: 0;
  }
}
@keyframes coming {
  from {
    transform: translateX(-150px);
    opacity: 0;
  }
  to {
    transform: translateX(0);
    opacity: 1;
  }
}



  .slide-enter-active {
    animation: slide-in 2s !important;
  }
  .slide-leave-active {
    animation: slide-in 2s reverse !important;
  }
  @keyframes slide-in {
    0% {transform: translateY(0px);}
    100% {transform: translateY(30px);}
  }


  .bounce-enter-active {
    animation: bounce-in .5s;
  }
  .bounce-leave-active {
    animation: bounce-in .5s reverse;
  }
  @keyframes bounce-in {
    0% {
      transform: scale(0);
    }
    50% {
      transform: scale(1.5);
    }
    100% {
      transform: scale(1);
    }
  }


</style>
