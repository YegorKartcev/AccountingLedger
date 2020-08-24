<template>
  <div class="mt-5">
    <transition name="slide-6"> 
      <div v-show="show_task" class="container">
        <div class="row justify-content-center">
          <div class="card task my-3 col-10 col-sm-10 col-md-8 col-lg-6  text-center">
            <div class="row justify-content-center">
              <div class="card-header container-fluid">{{ task.title }}</div>
            </div>
            <div class="row justify-content-center">
              <div class="container-fluid c-body-full py-3">
                  <div class="" v-for="record in task.choices" :key="record.id">
                    <div class="row">
                      <label style="word-wrap:break-word">
                        <input class="ml-3 mr-2 pulse-animation" type="checkbox" v-model="record.checked" @change="onSave()">
                        <span class="striked-through text-muted" v-if="record.checked">{{ record.text }}</span>
                        <span class="" v-else>{{ record.text }}</span>
                      </label><br>
                    </div>
                  </div>
              </div>
            </div>
            <div class="row justify-content-center">          
              <div class="card-footer text-muted container-fluid">
                <small>
                  <p class="my-0">Created by:
                    <span class="author-name">{{ task.author }}</span>
                  </p>
                  <p class="my-0">{{ task.created_at }}</p>
                </small>
              </div>
            </div>
          </div>
        </div>

        <listActions
          v-if="isListAuthor"
          :slug="task.slug"
        />
      </div>
    </transition> 
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
import ListActions from "@/components/ListActions.vue";
export default {
  name: "List",
  props: {
    slug: {
      type: String,
      required: true
    }
  },
  components: {
    ListActions
  },
  data() {
    return {
      task: {},
      show_task: false,
      requestUser: null
    }
  },
  computed: {
    isListAuthor() {
      // return true if the logged in user is also the author of the Task instance
      return this.task.author === this.requestUser;
    }
  },
  methods: {
    setPageTitle(title) {
      // set a given title string as the webpage title
      document.title = title;
    },
    setRequestUser() {
      // the username has been set to localStorage by the App.vue component
      this.requestUser = window.localStorage.getItem("username");
    },
    getTaskData() {
      // get the details of a Task instance from the REST API and call setPageTitle
      let endpoint = `/api/tasks/${this.slug}/`;
      apiService(endpoint)
        .then(data => {
          if (data) {
            this.task = data;
            this.show_task = true;
            this.setPageTitle(data.slug)
          } else {
            this.task = null;
            this.show_task = false;
            this.setPageTitle("404 - Page Not Found")
          }

        })
    },
    onSave() {
      this.task.choices.forEach(function(entry) {
        let endpoint = `/api/choices/${ entry.id }/`;
        let method = "PUT"; 
        // console.log("entry.text: " +entry.text)
        // console.log("entry.checked: " +entry.checked)
        // console.log("entry.id: " +entry.id)
        apiService(endpoint, method, {  text: entry.text,
                                        checked: entry.checked,
                                        id: entry.id })

      });
 
    }    
  },
  created() {
    this.getTaskData()
    this.setRequestUser()
  }
}
</script>

<style scoped>
  .c-body-full {
    background-color: white;
  }
  .striked-through {
    text-decoration: line-through;
  }
  label {
    display: block;
    padding-left: 15px;
    text-indent: -15px;
  }
  input {
    width: 13px;
    height: 13px;
    padding: 0;
    margin:0;
    vertical-align: bottom;
    position: relative;
    top: -5px;
    *overflow: hidden;
    transform: scale(1.5) !important;
  }
  .pulse-animation {
    animation: pulse 2s infinite;
  }

  @keyframes pulse {
    0% {
      transform: scale(0.95);
      box-shadow: 0 0 0 0 rgba(104, 225, 255, 0.7);
    }

    70% {
      transform: scale(1);
      box-shadow: 0 0 0 5px rgba(224, 249, 255, 0);
    }

    100% {
      transform: scale(0.95);
      box-shadow: 0 0 0 0 rgba(224, 249, 255, 0);
    }
  }

</style>
