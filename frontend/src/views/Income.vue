<template>
  <div class="mt-5">
    <transition name="slide-6">
      <div v-show="show_income" class="container">
        <div class="row justify-content-center">
          <div class="card income my-3 col-10 col-sm-10 col-md-4 col-lg-4  text-center" style="max-width: 18rem;">
            <div class="row justify-content-center">
              <div class="card-header container-fluid">The Income</div>
            </div>
            <div class="row justify-content-center">
              <div class="container-fluid c-body-full">
                <h5 class="card-title mt-3">{{ income.amount }}</h5>
                <p class="card-text mb-3"> from {{ income.source }}</p>
              </div>
            </div>
            <div class="row justify-content-center">          
              <div class="card-footer text-muted container-fluid">
                <small>
                  <p class="my-0">Created by:
                    <span class="author-name">{{ income.author }}</span>
                  </p>
                  <p class="my-0">{{ income.created_at }}</p>
                </small>
              </div>
            </div>
          </div>
        </div>
        <incomeActions
          v-if="isIncomeAuthor"
          :slug="income.slug"
        />
      </div>
    </transition>    
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
import IncomeActions from "@/components/IncomeActions.vue";
export default {
  name: "Income",
  props: {
    slug: {
      type: String,
      required: true
    }
  },
  components: {
    IncomeActions
  },
  data() {
    return {
      income: {},
      show_income: false,
      requestUser: null
    }
  },
  computed: {
    isIncomeAuthor() {
      // return true if the logged in user is also the author of the income instance
      return this.income.author === this.requestUser;
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
    getIncomeData() {
      // get the details of a income instance from the REST API and call setPageTitle
      let endpoint = `/api/incomes/${this.slug}/`;
      apiService(endpoint)
        .then(data => {
          if (data) {
            this.income = data;
            this.show_income = true;
            this.setPageTitle(data.slug)
          } else {
            this.income = null;
            this.show_income = false;
            this.setPageTitle("404 - Page Not Found")
          }

        })
    }
  },
  created() {
    this.getIncomeData()
    this.setRequestUser()
  }
}
</script>

<style scoped>

  .c-body-full {
    background-color: white;
  }
</style>
