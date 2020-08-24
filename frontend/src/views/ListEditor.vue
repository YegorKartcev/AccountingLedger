<template>
  <div class="container mt-2">
    <h4 class="mb-3" v-if="createNotUpdate">Create a Task record</h4>
    <h4 class="mb-3" v-else>Update the Task record</h4>
    <form @submit.prevent="onSubmit">
      <transition name="slide-5" appear>
        <div class="row">
          <div class="form-group col-9">      
            <input
              v-model="task_title"
              class="form-control"
              placeholder="List title"
            >
            <small class="form-text text-muted mb-3">List title</small>
          </div> 
        </div>
      </transition>
      <div v-if="!task_update">
        <transition-group name="slide-6" appear>
          <div v-for="(run, index) in task_content.runs" :key="index">
            <div class="row">
              <div class="form-group col-9">
                <input class="form-control input-group-lg" placeholder="List element" type="text"
                      :name="'run'+index" v-model="task_content.runs[index]" />
                <small class="form-text text-muted mb-3">List element</small>
              </div>
              <div class="form-group col-1">
                <button class="btn btn-danger" @click.prevent="removeField(index)">
                  <svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-trash icon" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                    <path d="M5.5 5.5A.5.5 0 0 1 6 6v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm2.5 0a.5.5 0 0 1 .5.5v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm3 .5a.5.5 0 0 0-1 0v6a.5.5 0 0 0 1 0V6z"/>
                    <path fill-rule="evenodd" d="M14.5 3a1 1 0 0 1-1 1H13v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V4h-.5a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1H6a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1h3.5a1 1 0 0 1 1 1v1zM4.118 4L4 4.059V13a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1V4.059L11.882 4H4.118zM2.5 3V2h11v1h-11z"/>
                  </svg>
                </button>
              </div> 
            </div>
          </div>
        </transition-group>
      </div>
      <div v-else>
        <transition-group name="slide-6" appear>
          <div v-for="(run, index) in task_content.read" :key="index">
              <div class="row">
                <div class="form-group col-9">
                  <input class="form-control input-group-lg" placeholder="List element" type="text"
                        :name="'run'+index" v-model="task_content.read[index].text" />
                  <small class="form-text text-muted mb-3">List element</small>
                </div>
                <div class="form-group col-1">
                  <button class="btn btn-danger" @click.prevent="removeField(index)">X</button>
                </div> 
              </div>
          </div>
        </transition-group>       
      </div>

    
      <br>
      <transition name="slide-4" appear>
        <button class="btn btn-success" @click.prevent="addField()">
          <span class="px-2">Add field</span>
        </button>
      </transition>
      <br>
      <br>
      <button type="submit" class="btn btn-success" v-if="redyToSubmit" :disabled="isSubmitting">
        <svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-cloud-arrow-up icon" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
          <path fill-rule="evenodd" d="M4.406 3.342A5.53 5.53 0 0 1 8 2c2.69 0 4.923 2 5.166 4.579C14.758 6.804 16 8.137 16 9.773 16 11.569 14.502 13 12.687 13H3.781C1.708 13 0 11.366 0 9.318c0-1.763 1.266-3.223 2.942-3.593.143-.863.698-1.723 1.464-2.383zm.653.757c-.757.653-1.153 1.44-1.153 2.056v.448l-.445.049C2.064 6.805 1 7.952 1 9.318 1 10.785 2.23 12 3.781 12h8.906C13.98 12 15 10.988 15 9.773c0-1.216-1.02-2.228-2.313-2.228h-.5v-.5C12.188 4.825 10.328 3 8 3a4.53 4.53 0 0 0-2.941 1.1z"/>
          <path fill-rule="evenodd" d="M7.646 5.146a.5.5 0 0 1 .708 0l2 2a.5.5 0 0 1-.708.708L8.5 6.707V10.5a.5.5 0 0 1-1 0V6.707L6.354 7.854a.5.5 0 1 1-.708-.708l2-2z"/>
        </svg>
        <span class="px-2" v-if="createNotUpdate">Create</span>
        <span class="px-2" v-else>Update</span>
      </button>
    </form>
    <p v-if="error" class="muted mt-2 error">{{ error }}</p>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
export default {
  name: "ListEditor",
  props: {
    slug: {
      type: String,
      required: false
    }
  },
  data() {
    return {
      task_title: null,
      task_id: null,
      task_update: false,
      error: null,
      task_content: {
        runs: [""],
        read: null
      },
      hideElementField: false,
      create: true,
      isSubmitting: null
    }
  },
  methods: {
    onSubmit() {
      if (this.redyToSubmit) {
        this.isSubmitting = true
        let endpoint = "/api/tasks/";
        let method = "POST";
        let data = {
          "choices": [],
          "title": `${ this.task_title }`
        }
        if (!this.task_update) {
          this.task_content.runs.forEach(function(entry) {
          let block = {
              "text": entry,
              "checked": false
          };
          data.choices.push(block)
          });
        }
        if (this.slug !== undefined) {
          endpoint += `${ this.slug }/`;
          method = "PUT";
          data = Object.assign({"id": `${ this.task_id }`}, data)
          this.task_content.read.forEach(function(entry) {
            // console.log("entry: " + entry)
            let block = {
                "id": entry.id,
                "text": entry.text,
                "checked": false
            };
            data.choices.push(block)
          });
       
        } 
        apiService(endpoint, method, data)
          .then(list_data => {
            this.$router.push({ 
              name: 'List', 
              params: { slug: list_data.slug }
            })          
          })
      }
    },
    addField() {
      if (this.task_update) {
        let temp =  {
          "text": "",
          "checked": false
        }
        this.task_content.read.push(temp)
      } else {
        this.task_content.runs.push("")
      }

    },
    removeField: function(i) {
      this.hideElementField = !this.hideElementField
      if (this.task_update) {
        this.task_content.read.splice(i,1);
      } else {
        this.task_content.runs.splice(i,1);
      }
    }   
  },
  async beforeRouteEnter(to, from, next) {
    // if the component will be used to update a Income, then get the Income's data from the REST API
    if (to.params.slug !== undefined) {
      let endpoint = `/api/tasks/${ to.params.slug }/`;
      let data = await apiService(endpoint);
      return next(vm => (vm.task_title = data.title,
                        vm.task_content.read = data.choices,
                        vm.task_id = data.id,
                        vm.task_update = true
                        ))
    } else {
      return next();
    }   
  },
  created() {
    // console.log("this.task_update: "+this.task_update)
    document.title = "Editor - Accounting Ledger";
  },
  computed: {
    createNotUpdate() {
      if (this.task_update == false) {
        return true
      } else {
        return false
      }
    },
    redyToSubmit() {
      let forbidden = null;
      if (this.task_update) {
        this.task_content.read.forEach(function(entry) {
          if (entry === "" || entry === " " || entry === null) {
            forbidden = true
          }
        });
        if (forbidden) {
          return false
        };      
        if (this.task_title === "" || this.task_title === " " || this.task_title === null) {
          return false
        }
        return true
      } else {
        this.task_content.runs.forEach(function(entry) {
          if (entry === "" || entry === " " || entry === null) {
            forbidden = true
          }
        });
        if (forbidden) {
          return false
        };      
        if (this.task_title === "" || this.task_title === " " || this.task_title === null) {
          return false
        }
        return true
      }

    }
  } 
}
</script>

<style scoped>

</style>
