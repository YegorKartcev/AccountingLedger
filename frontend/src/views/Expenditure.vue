<template>
  <div class="mt-5">
    <transition name="slide-6">    
      <div v-show="show_expenditure" class="container">
        <div class="row justify-content-center">
          <div class="card expenditure my-3 col-10 col-sm-10 col-md-4 col-lg-4  text-center" style="max-width: 18rem;">
            <div class="row justify-content-center">
              <div class="card-header container-fluid">The expenditure</div>
            </div>
            <div class="row justify-content-center">
              <div class="container-fluid c-body-full">
                <h5 class="card-title mt-3">{{ expenditure.amount }}</h5>
                <p class="card-text mb-3">for {{ expenditure.target }}</p>
                <p class="card-text mb-3">category: {{ getCategoryName }}</p>
              </div>
            </div>
            <div class="row justify-content-center">          
              <div class="card-footer text-muted container-fluid">
                <small>
                  <p class="my-0">Created by:
                    <span class="author-name">{{ expenditure.author }}</span>
                  </p>
                  <p class="my-0">{{ expenditure.created_at }}</p>
                </small>
              </div>
            </div>
          </div>
        </div>
        <expenditureActions
          v-if="isExpenditureAuthor"
          :slug="expenditure.slug"
        />
      </div>
    </transition>    
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
import ExpenditureActions from "@/components/ExpenditureActions.vue";
export default {
  name: "Expenditure",
  props: {
    slug: {
      type: String,
      required: true
    }
  },
  components: {
    ExpenditureActions
  },
  data() {
    return {
      expenditure: {},
      show_expenditure: false,
      requestUser: null,
      categories: [],
      nextCat: null
    }
  },
  computed: {
    isExpenditureAuthor() {
      // return true if the logged in user is also the author of the expenditure instance
      return this.expenditure.author === this.requestUser;
    },
    getCategoryName() {
      let categoryName;
      let categoryID = this.expenditure.category;
      this.categories.forEach(function(entry) {
        if (entry.id ===  categoryID) {
          categoryName = entry.title
        }
      });
      return categoryName;    
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
    getExpenditureData() {
      // get the details of a expenditure instance from the REST API and call setPageTitle
      let endpoint = `/api/expenditures/${this.slug}/`;
      apiService(endpoint)
        .then(data => {
          if (data) {
            this.expenditure = data;
            this.show_expenditure = true;
            this.setPageTitle(data.slug)
          } else {
            this.expenditure = null;
            this.show_expenditure = false;
            this.setPageTitle("404 - Page Not Found")
          }

        })
    },
    getCategories() {
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
          this.getExpenditureData()
        })
    },    
  },
  created() {
    this.getCategories()
    this.setRequestUser()
  }
}
</script>

<style scoped>

  .c-body-full {
    background-color: white;
  }
</style>
