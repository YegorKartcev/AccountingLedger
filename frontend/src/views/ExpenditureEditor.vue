<template>
  <div class="container mt-2">
    <h4 class="mb-3" v-if="createNotUpdate">Create an expenditure record</h4>
    <h4 class="mb-3" v-else>Update the expenditure record</h4>
    <form @submit.prevent="onSubmit">
      <transition name="slide-6" appear mode="out-in">
        <div class="row">
          <div class="form-group col-12">         
            <input
              v-model="expenditure_amount"
              class="form-control"
              placeholder="Expenditure amount"
            >
            <small class="form-text text-muted mb-3">How much did you spend?</small>
          </div> 
        </div>
      </transition>
      <transition name="slide-5" appear mode="out-in">
        <div class="row">
          <div class="form-group col-12">                    
            <input
              v-model="expenditure_target"
              class="form-control"
              placeholder="For..."
            >
            <small class="form-text text-muted mb-3">What did you spend it for?</small>
          </div> 
        </div>
      </transition>
      <transition name="slide-6" appear mode="out-in">
        <div class="col-12 border rounded dropdownArea">
          <div class="row">
            <div class="col-10">                 
              <b-form-select class="mt-3" v-model="categoryChosen" :options="getOptions"></b-form-select>
              <small class="form-text text-muted mb-1">Category</small>
            </div> 
            <div class="col-2">
              <span class="float-right">
                <button class="btn btn-danger mt-3 mx-0 pl-2 pr-1" @click.prevent="deleteCategoryConfirm">
                  <svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-trash icon" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                    <path d="M5.5 5.5A.5.5 0 0 1 6 6v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm2.5 0a.5.5 0 0 1 .5.5v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm3 .5a.5.5 0 0 0-1 0v6a.5.5 0 0 0 1 0V6z"/>
                    <path fill-rule="evenodd" d="M14.5 3a1 1 0 0 1-1 1H13v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V4h-.5a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1H6a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1h3.5a1 1 0 0 1 1 1v1zM4.118 4L4 4.059V13a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1V4.059L11.882 4H4.118zM2.5 3V2h11v1h-11z"/>
                  </svg> 
                </button>
              </span>
            </div> 
          </div>
          <transition name="fade" appear mode="out-in">
            <div class="row mb-2" v-show="deleteCategory">
              <div class="col-6">
                <button type="submit" class="btn btn-danger" @click.prevent="removeCategory" :disabled="isSubmitting">
                <svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-trash icon" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                  <path d="M5.5 5.5A.5.5 0 0 1 6 6v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm2.5 0a.5.5 0 0 1 .5.5v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm3 .5a.5.5 0 0 0-1 0v6a.5.5 0 0 0 1 0V6z"/>
                  <path fill-rule="evenodd" d="M14.5 3a1 1 0 0 1-1 1H13v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V4h-.5a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1H6a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1h3.5a1 1 0 0 1 1 1v1zM4.118 4L4 4.059V13a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1V4.059L11.882 4H4.118zM2.5 3V2h11v1h-11z"/>
                </svg> 
                  <span class="px-2">Yes!</span>
                </button>
              </div>
              <div class="col-6">
                <span class="float-right">
                  <div class="btn btn-info" @click.prevent="deleteCategoryConfirm">
                    <span class="px-2">No!</span>
                  </div>
                </span>
              </div>
            </div>
          </transition>
        </div> 
      </transition>
      <transition name="slide-3" appear mode="out-in">
        <div v-show="moreCategories" class="col-12 border rounded categoryAdd mt-3">
          <div class="row">
            <div class="col-10"> 
              <input
                v-model="categoryTitle"
                class="form-control mt-3"
                placeholder="Title"
              >
              <small class="form-text text-muted mb-1">Title of a new category to add</small>
            </div>
            <div class="col-2">
              <span class="float-right">
                <button class="btn btn-success mt-3 mx-0 pl-2 pr-1" @click.prevent="createCategory" :disabled="isSubmitting">
                  <svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-cloud-arrow-up icon" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                    <path fill-rule="evenodd" d="M4.406 3.342A5.53 5.53 0 0 1 8 2c2.69 0 4.923 2 5.166 4.579C14.758 6.804 16 8.137 16 9.773 16 11.569 14.502 13 12.687 13H3.781C1.708 13 0 11.366 0 9.318c0-1.763 1.266-3.223 2.942-3.593.143-.863.698-1.723 1.464-2.383zm.653.757c-.757.653-1.153 1.44-1.153 2.056v.448l-.445.049C2.064 6.805 1 7.952 1 9.318 1 10.785 2.23 12 3.781 12h8.906C13.98 12 15 10.988 15 9.773c0-1.216-1.02-2.228-2.313-2.228h-.5v-.5C12.188 4.825 10.328 3 8 3a4.53 4.53 0 0 0-2.941 1.1z"/>
                    <path fill-rule="evenodd" d="M7.646 5.146a.5.5 0 0 1 .708 0l2 2a.5.5 0 0 1-.708.708L8.5 6.707V10.5a.5.5 0 0 1-1 0V6.707L6.354 7.854a.5.5 0 1 1-.708-.708l2-2z"/>
                  </svg>
                </button>
              </span>              
            </div>
          </div>
        </div>
      </transition>

      <br>
      <transition name="slide-4" appear mode="out-in">
        <div class="row">
          <div class="col-6">
            <button type="submit" class="btn btn-success" :disabled="isSubmitting">
              <svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-cloud-arrow-up icon" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                <path fill-rule="evenodd" d="M4.406 3.342A5.53 5.53 0 0 1 8 2c2.69 0 4.923 2 5.166 4.579C14.758 6.804 16 8.137 16 9.773 16 11.569 14.502 13 12.687 13H3.781C1.708 13 0 11.366 0 9.318c0-1.763 1.266-3.223 2.942-3.593.143-.863.698-1.723 1.464-2.383zm.653.757c-.757.653-1.153 1.44-1.153 2.056v.448l-.445.049C2.064 6.805 1 7.952 1 9.318 1 10.785 2.23 12 3.781 12h8.906C13.98 12 15 10.988 15 9.773c0-1.216-1.02-2.228-2.313-2.228h-.5v-.5C12.188 4.825 10.328 3 8 3a4.53 4.53 0 0 0-2.941 1.1z"/>
                <path fill-rule="evenodd" d="M7.646 5.146a.5.5 0 0 1 .708 0l2 2a.5.5 0 0 1-.708.708L8.5 6.707V10.5a.5.5 0 0 1-1 0V6.707L6.354 7.854a.5.5 0 1 1-.708-.708l2-2z"/>
              </svg>
              <span class="px-2" v-if="createNotUpdate">Create</span>
              <span class="px-2" v-else>Update</span>
            </button>
          </div>
          <div class="col-6">
            <span class="float-right">
              <div class="btn btn-info" @click="moreCategories = !moreCategories, error = null">
                <svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-plus-circle icon" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                  <path fill-rule="evenodd" d="M8 3.5a.5.5 0 0 1 .5.5v4a.5.5 0 0 1-.5.5H4a.5.5 0 0 1 0-1h3.5V4a.5.5 0 0 1 .5-.5z"/>
                  <path fill-rule="evenodd" d="M7.5 8a.5.5 0 0 1 .5-.5h4a.5.5 0 0 1 0 1H8.5V12a.5.5 0 0 1-1 0V8z"/>
                  <path fill-rule="evenodd" d="M8 15A7 7 0 1 0 8 1a7 7 0 0 0 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"/>
                </svg>
                <span class="px-2">Category</span>
              </div>
            </span>
          </div>
        </div>
       </transition> 

    </form>
    <p v-if="error" class="muted mt-2 error">{{ error }}</p>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
export default {
  name: "ExpenditureEditor",
  props: {
    slug: {
      type: String,
      required: false
    }
  },
  data() {
    return {
      expenditure_amount: null,
      expenditure_target: null,
      error: null,
      categories: [],
      nextCat: null,
      categoryChosen: null,
      moreCategories: false,
      categoryTitle: '',
      loading: false,
      deleteCategory: false,
      expenditure_update: false,
      isSubmitting: null
    }
  },
  methods: {
    deleteCategoryConfirm() {
      this.deleteCategory = !this.deleteCategory
      this.error = null
    },
    async removeCategory() {
      if (this.categoryChosen==="" || this.categoryChosen===null) {
        this.error = "Select a category to be deleted";
      } else {
        this.isSubmitting = true      
        let endpoint = `/api/categories/${this.categoryChosen}/`;
        // console.log(endpoint);
        try {
          await apiService(endpoint, "DELETE");
        }
        catch (err) {
          console.log(err);
        };
        this.deleteCategoryConfirm();
        this.getCategories();
        this.categoryChosen = null;
        this.isSubmitting = false
      }
    },
    createCategory() {
      this.error = null
      this.moreCategories = !this.moreCategories
      if (this.categoryTitle === "") {
        this.error = "You need to input some data!";
      } else {
          if (this.categoryExists(this.categoryTitle)) {
            this.error = "The category already exists!";
          } else {
              this.isSubmitting = true
              let endpoint = "/api/categories/";
              let method = "POST"; 
              apiService(endpoint, method, { title: this.categoryTitle })
                .then(data => {
                  this.categories.push(data);
                  this.isSubmitting = false;
                })
            }
        }
    },
    getCategories() {
      this.categories = []
      // console.log("called")
      // make a GET Request to the Categories list endpoint and populate the categories array
      let endpoint = "/api/categories/";
      if (this.nextCat) {
        endpoint = this.nextCat;
      }
      this.loading = true;
      apiService(endpoint)
        .then(data => {
          this.categories.push(...data.results)
          this.loading = false;
          if (data.next) {
            this.nextCat = data.next;
          } else {
            this.nextCat = null;
          };
        })
    },    
    onSubmit() {
      this.error = null
      // Tell the REST API to create or update an Expenditure Instance
      if (this.expenditure_amount===null || this.expenditure_target===null || this.categoryChosen==="" || this.categoryChosen===null) {
        this.error = "You need to input some data!";
      } else {
        if (this.isNumberPositive(Number(this.expenditure_amount))) {
          this.isSubmitting = true
          let endpoint = "/api/expenditures/";
          let method = "POST"; 
          if (this.slug !== undefined) {
            endpoint += `${ this.slug }/`;
            method = "PUT";
          }     
          apiService(endpoint, method, { amount: Number(this.expenditure_amount),
                                        target: this.expenditure_target,
                                        category: this.categoryChosen })
            .then(expenditure_data => {
              this.$router.push({ 
                name: 'Expenditure', 
                params: { slug: expenditure_data.slug }
              })          
            })
        } else {
          this.error = "Expenditure must be a positive integer!";
        }
      }
    },
    isNumberPositive(value) {
      if (typeof value !== 'number') {
        return false;
      }
      if (value !== Number(value)) {
        return false;
      }
      if (value === Infinity || value === !Infinity) {
        return false;
      }
      if (Number(value) < 0) {
        return false;
      }
      if (Number(value) % 1 !== 0) {
        return false;
      }              
      return true;
    },
    categoryExists(name) {
      let exist = false
      this.categories.forEach(function(entry) {
        if (entry.title.toLowerCase() === name.toLowerCase()) {
          exist = true
        }
      });
      return exist;     
    }
  },
  async beforeRouteEnter(to, from, next) {
    // if the component will be used to update a Expenditure, then get the Expenditure's data from the REST API
    if (to.params.slug !== undefined) {
      let endpoint = `/api/expenditures/${ to.params.slug }/`;
      let data = await apiService(endpoint);
      return next(vm => (vm.expenditure_amount = data.amount,
                        vm.expenditure_target = data.target,
                        vm.categoryChosen = data.category,
                        vm.expenditure_update = true))
    } else {
      return next();
    }
  },
  created() {
    this.getCategories()
    document.title = "Editor - Accounting Ledger";
  },
  computed: {
    createNotUpdate() {
      if (this.expenditure_update == false) {
        return true
      } else {
        return false
      }
    },
    getOptions() {
      // console.log("this.categories", this.categories)
      let options = [];
      this.categories.forEach(function(entry) {
        options.push({"value":entry.id, "text":entry.title})
      });
      // console.log("options", options)
      return options      
    },
    getCategoryName() {
      let categoryName;
      let categoryID = this.categoryChosen;
      this.categories.forEach(function(entry) {
        if (entry.id ===  categoryID) {
          categoryName = entry.title
        }
      });
      return categoryName;     
    }     
  }
}
</script>

<style>
.categoryAdd {
  background-color: #e7f1f1;
}
.dropdownArea {
  background-color: #fcf1f1;
}
</style>
