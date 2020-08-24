<template>
  <div class="container mt-2">
    <h4 class="mb-3" v-if="createNotUpdate">Create an income record</h4>
    <h4 class="mb-3" v-else>Update the income record</h4>
    <form @submit.prevent="onSubmit">
      <transition name="slide-6" appear>
        <div>
          <input
            v-model="income_amount"
            class="form-control"
            placeholder="Income amount"
          >
          <small class="form-text text-muted mb-3">How much did you get?</small>
        </div>
      </transition>
      <transition name="slide-5" appear>
        <div>
          <input
            v-model="income_source"
            class="form-control"
            placeholder="From..."
          >
          <small class="form-text text-muted mb-3">Where did you get it from?</small> 
        </div>
      </transition>     
      <br>
      <transition name="slide-4" appear>
        <button type="submit" class="btn btn-success" :disabled="isSubmitting">
          <svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-cloud-arrow-up icon" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
            <path fill-rule="evenodd" d="M4.406 3.342A5.53 5.53 0 0 1 8 2c2.69 0 4.923 2 5.166 4.579C14.758 6.804 16 8.137 16 9.773 16 11.569 14.502 13 12.687 13H3.781C1.708 13 0 11.366 0 9.318c0-1.763 1.266-3.223 2.942-3.593.143-.863.698-1.723 1.464-2.383zm.653.757c-.757.653-1.153 1.44-1.153 2.056v.448l-.445.049C2.064 6.805 1 7.952 1 9.318 1 10.785 2.23 12 3.781 12h8.906C13.98 12 15 10.988 15 9.773c0-1.216-1.02-2.228-2.313-2.228h-.5v-.5C12.188 4.825 10.328 3 8 3a4.53 4.53 0 0 0-2.941 1.1z"/>
            <path fill-rule="evenodd" d="M7.646 5.146a.5.5 0 0 1 .708 0l2 2a.5.5 0 0 1-.708.708L8.5 6.707V10.5a.5.5 0 0 1-1 0V6.707L6.354 7.854a.5.5 0 1 1-.708-.708l2-2z"/>
          </svg>
          <span class="px-2" v-if="createNotUpdate">Create</span>
          <span class="px-2" v-else>Update</span>
        </button>
      </transition> 
    </form>
    <p v-if="error" class="muted mt-2 error">{{ error }}</p>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
export default {
  name: "IncomeEditor",
  props: {
    slug: {
      type: String,
      required: false
    }
  },
  data() {
    return {
      income_amount: null,
      income_source: null,
      error: null,
      income_update: false,
      isSubmitting: null
    }
  },
  methods: {
    onSubmit() {
      // Tell the REST API to create or update an Income Instance
      if (!this.income_amount || !this.income_source) {
        this.error = "You need to input some data!";
      } else {
        if (this.isNumberPositive(Number(this.income_amount))) {
          this.isSubmitting = true
          let endpoint = "/api/incomes/";
          let method = "POST"; 
          if (this.slug !== undefined) {
            endpoint += `${ this.slug }/`;
            method = "PUT";
          }     
          apiService(endpoint, method, { amount: Number(this.income_amount),
                                        source: this.income_source })
            .then(income_data => {
              this.$router.push({ 
                name: 'Income', 
                params: { slug: income_data.slug }
              })          
            })  
        } else {
          this.error = "Income must be a positive integer!";
        }
      }
    },
    isNumberPositive(value) {
      if (typeof value !== 'number') {
        return false
      }
      if (value !== Number(value)) {
        return false
      }
      if (value === Infinity || value === !Infinity) {
        return false
      }
      if (Number(value) < 0) {
        return false
      } 
      if (Number(value) % 1 !== 0) {
        return false;
      }            
      return true
    }
  },
  async beforeRouteEnter(to, from, next) {
    // if the component will be used to update a Income, then get the Income's data from the REST API
    if (to.params.slug !== undefined) {
      let endpoint = `/api/incomes/${ to.params.slug }/`;
      let data = await apiService(endpoint);
      return next(vm => (vm.income_amount = data.amount, vm.income_source = data.source, vm.income_update = true))
    } else {
      return next();
    }   
  },
  created() {
    document.title = "Editor - Accounting Ledger";
  },
  computed: {
    createNotUpdate() {
      if (this.income_update == false) {
        return true
      } else {
        return false
      }
    }
  } 
}
</script>

<style>

</style>
