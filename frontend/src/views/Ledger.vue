<template>
  <div class="home">
    <div class="container mt-2">
        <div class="row justify-content-center mt-3">
            <div class="container-fluid px-0 col-10 col-sm-10 col-md-4 col-lg-4">
              <div class="input-group mb-3">
                <div class="input-group-prepend">
                  <span class="input-group-text">Year</span>
                </div>
                <input type="text" v-model="chosenYear" class="form-control text-right">
              </div>
            </div>
            <div class="container-fluid px-0 col-10 col-sm-10 col-md-4 col-lg-4">
              <div class="input-group mb-3">
                  <div class="input-group-prepend">
                    <span class="input-group-text">Month</span>
                  </div>
                  <select v-model="chosenMonth"  class="form-control  text-right">
                      <option v-for="month in monthNames" :key="month.id">{{ month.name }}</option>
                  </select>
              </div>
            </div>
        </div>
        <div class="row justify-content-center">
          <transition name="slide-fade">
            <p class="error" v-if="(error)">{{ error }} 😢</p>
          </transition>
        </div>

        <div class="row justify-content-center mb-4 mt-2">
          <button
            @click="refresh()"
            class="btn btn-sm btn-outline-success"
            v-if="!loading">
            <svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-cloud-arrow-down icon" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
              <path fill-rule="evenodd" d="M4.406 3.342A5.53 5.53 0 0 1 8 2c2.69 0 4.923 2 5.166 4.579C14.758 6.804 16 8.137 16 9.773 16 11.569 14.502 13 12.687 13H3.781C1.708 13 0 11.366 0 9.318c0-1.763 1.266-3.223 2.942-3.593.143-.863.698-1.723 1.464-2.383zm.653.757c-.757.653-1.153 1.44-1.153 2.056v.448l-.445.049C2.064 6.805 1 7.952 1 9.318 1 10.785 2.23 12 3.781 12h8.906C13.98 12 15 10.988 15 9.773c0-1.216-1.02-2.228-2.313-2.228h-.5v-.5C12.188 4.825 10.328 3 8 3a4.53 4.53 0 0 0-2.941 1.1z"/>
              <path fill-rule="evenodd" d="M7.646 10.854a.5.5 0 0 0 .708 0l2-2a.5.5 0 0 0-.708-.708L8.5 9.293V5.5a.5.5 0 0 0-1 0v3.793L6.354 8.146a.5.5 0 1 0-.708.708l2 2z"/>
            </svg><span class="px-2">Load</span>
          </button> 
          <div v-else>
            <transition name="fade" mode="out-in">
              <span><b-spinner label="Loading..."></b-spinner></span> 
            </transition> 
          </div>
        
        </div>
    </div>

    <div class="container">
      <div class="row justify-content-center">
        <div class="card col-10">
          <div class="container-fluid px-0">
            <div class="row justify-content-center">
              <div class="col-6 text-center income">
                <div class="container text-center ">
                  <strong>Income</strong>
                </div>
              </div>
              <div class="col-6 text-center expenditure">  
                <div class="container text-center">
                  <strong>Expenditure</strong>
                </div> 
              </div>              
            </div>
          </div>
        </div>
      </div>
      <div class="row justify-content-center">
        <div class="card col-10">
          <div class="container-fluid px-0">
            <div class="row justify-content-center">
              <div class="col-6 text-center income">
                <div class="container text-center mt-3">
                  <p>Total:
                    <transition name="fade">
                      <span v-if="incomeTotal != 0"><strong>{{ incomeTotal }}</strong></span>
                    </transition>
                  </p>
                </div>
              </div>
              <div class="col-6 text-center expenditure">  
                <div class="container text-center mt-3">
                  <p>Total:
                    <transition name="fade">
                      <span v-if="expenditureTotal != 0"><strong>{{ expenditureTotal }}</strong></span>
                    </transition>
                  </p>
                </div>
              </div>              
            </div>
          </div>
        </div>
      </div>
      <sequential-entrance fromTop delay="150">
      <!-- <transition-group name="slide-6"> -->
        <div class="row justify-content-center" v-for="date in getDates" :key="date">
          <div class="card col-10">
            <div class="container text-center">
              <strong>{{ date }}</strong>
            </div>
            <div class="container-fluid px-0">
              <div class="row justify-content-center">
                <div class="col-6 text-center income">
                  <div class="" v-for="income in incomes" :key="income.pk">
                    <p class="card-text" v-if="income.created_at == date">
                      <span>
                        <router-link
                          :to="{ name: 'Income', params: { slug: income.slug } }"
                          class=""
                          >{{ income.amount }} - {{ income.source }}
                        </router-link>
                      </span>
                    </p>
                    <p class="card-text" v-else>
                    </p>  
                  </div>
                </div>
                <div class="col-6 text-center expenditure">  
                  <div class="" v-for="expenditure in expenditures" :key="expenditure.pk">          
                    <p class="card-text" v-if="expenditure.created_at == date" >
                      <span>
                        <router-link
                          :to="{ name: 'Expenditure', params: { slug: expenditure.slug } }"
                          class=""
                          >{{ expenditure.amount }} - {{ expenditure.target }}
                        </router-link>
                      </span></p>                     
                  </div> 
                </div>              
              </div>
            </div>
          </div>
        </div>
      <!-- </transition-group>   -->
      </sequential-entrance>

    </div>
    <transition name="slide-4">
      <div v-if="expenditureTotal != 0"><CarouselLogoComponent/></div>
    </transition>

  </div>  
</template>

<script>
import { apiService } from "@/common/api.service.js";
import CarouselLogoComponent from "@/components/CarouselLogo.vue";
export default {
  name: "Ledger",
  components: {
    CarouselLogoComponent
  },
  data() {
    return {
      incomes: [],
      next: null,
      expenditures: [],
      nextExp: null,
      loading: false,
      currentYear: new Date().getFullYear(),
      currentMonth: new Date().getMonth(),
      currentDay: new Date().getDay(),
      monthNames: [{id: 1, name: "January"},
                  {id: 2, name: "February"},
                  {id: 3, name: "March"},
                  {id: 4, name: "April"},
                  {id: 5, name: "May"},
                  {id: 6, name: "June"},
                  {id: 7, name: "July"},
                  {id: 8, name: "August"},
                  {id: 9, name: "September"},
                  {id: 10, name: "October"},
                  {id: 11, name: "November"},
                  {id: 12, name: "December"}],
      chosenMonth: null,
      chosenYear: null,
      error: null,
      noIncome: true,
      noExpenditure: true
    }
  },
  methods: {
    noRecordsOnDate() {
      if (this.incomes.length === 0 && this.expenditures.length === 0) {
        this.error = "No records on chosen date"
      }
    },
    refresh() {
      if (this.isCorrectYear(this.chosenYear.toString())) {
        this.incomes = [],
        this.expenditures = [],
        this.error = null,
        this.getIncomes(),
        this.getExpenditures()
      } else {
        this.error = "Incorrect Year input";
      }
    },
    getCurrentDate() {
      this.chosenMonth = this.monthNames[this.currentMonth].name;
      this.chosenYear = this.currentYear;
    },
    getIncomes() {
      var monthNumber = this.getKeyOfValue(this.monthNames, this.chosenMonth);
      // make a GET Request to the incomes list endpoint and populate the incomes array
      let endpoint = `/api/incomes/`;
      if(this.currentYear!==''||this.currentMonth!==null) {
        if (this.currentMonth.toString().length == 1) {
          endpoint = `/api/incomes/?search=${this.chosenYear}-0${this.monthNames[monthNumber-1].id}`
        } else {
          endpoint = `/api/incomes/?search=${this.chosenYear}-${this.monthNames[monthNumber-1].id}`
        }
      }
      if (this.next) {
        endpoint = this.next;
      }
      this.loading = true;
      apiService(endpoint)
        .then(data => {
          this.incomes.push(...data.results)
          this.loading = false;
          this.noRecordsOnDate();
          if (data.next) {
            this.next = data.next;
          } else {
            this.next = null;
          }
        })
    },
    getExpenditures() {
      var monthNumber = this.getKeyOfValue(this.monthNames, this.chosenMonth);
      // make a GET Request to the Expenditures list endpoint and populate the expenditures array
      let endpoint = "/api/expenditures/";
      if(this.currentYear!==''||this.currentMonth!==null) {
        if (this.currentMonth.toString().length == 1) {
          endpoint = `/api/expenditures/?search=${this.chosenYear}-0${this.monthNames[monthNumber-1].id}`
        } else {
          endpoint = `/api/expenditures/?search=${this.chosenYear}-${this.monthNames[monthNumber-1].id}`
        }
      }      
      if (this.nextExp) {
        endpoint = this.nextExp;
      }
      this.loading = true;
      apiService(endpoint)
        .then(data => {
          this.expenditures.push(...data.results)
          this.loading = false;
          this.noRecordsOnDate();
          if (data.next) {
            this.nextExp = data.next;
          } else {
            this.nextExp = null;
          }
        })
    },
    getKeyOfValue(object, value) {
      for (var key in object) {
        if (object[key].name === value) {
          return object[key].id
        }
      }
    },
    isCorrectYear(year) {
      var text = /^[0-9]+$/;
      if(year.length==4) {
        if (year != 0) {
          if ((year != "") && (!text.test(year))) {
              return false;
          }
          if (year.length != 4) {
              return false;
          }
          var current_year=new Date().getFullYear();
          if((year < 2020) || (year > current_year))
              {
              return false;
              }
          return true;
        }
      }
    }
  },
  created() {
    this.getCurrentDate(),
    this.getIncomes(),
    this.getExpenditures(),
    document.title = "Ledger";
  },
  computed: {
    getDates() {
      let datesIncome = [];
      this.incomes.forEach(function(entry) {
          datesIncome.push(entry.created_at)
      });
      let datesExp = [];
      this.expenditures.forEach(function(entry) {
          datesExp.push(entry.created_at)
      });
      let dates = [...new Set([...datesIncome, ...datesExp])]; 
      return dates.sort().reverse();
    },
    incomeTotal() {
      let amountIn = 0
        this.incomes.forEach(function(entry) {
            amountIn += entry.amount
        });
      return amountIn;
    },
    expenditureTotal() {
      let amountEx = 0
        this.expenditures.forEach(function(entry) {
            amountEx += entry.amount
        });
      return amountEx;     
    }
  }
};
</script>

<style scoped>
  .flex-row {
    display: flex;
    flex-wrap: wrap;
  }
  .card-text:hover {
    font-weight: bold;
  }
  .card-text a:hover {
    text-decoration: none !important;
  }
  .card-text a {
    color:black;
  }

</style>
