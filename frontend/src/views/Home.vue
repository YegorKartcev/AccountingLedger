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
            <p class="error" v-if="error">{{ error }} 😢</p>
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

    <transition name="slide-5" mode="out-in">
      <div v-show="expenditureTotal"><h5 class="text-center">Expenditures dashboard</h5></div>
    </transition>
    <div>
      <transition name="slide-6" mode="out-in">
        <div v-show="expenditureTotal">
          <vc-donut
            background="white" foreground="grey"
            :size="250" unit="px" :thickness="30"
            has-legend legend-placement="top"
            :sections="expendituresGrouped" :total="100"
            :start-angle="0" :auto-adjust-text-size="true"
            >
            <transition name="fade" mode="out-in">
              <h2 v-if="expenditureTotal">{{ formatPrice(expenditureTotal) }}</h2>
            </transition>
          </vc-donut>
        </div>
      </transition>
    </div>

    <div class="container mt-4">
      <!-- <transition-group name="slide-6"> -->
      <!-- <transition name="slide-6" mode="out-in"> -->
      <sequential-entrance delay="250">
        <!-- <div v-show="expenditureTotal"> -->
          <div role="tablist" class="my-1" v-for="(group, index) in expendituresGrouped" :key="index">
            <div class="row justify-content-center">
              <div class="col-10 col-sm-10 col-md-8 col-lg-6">
                <b-card no-body class="mb-1">
                  <b-card-header header-tag="header" class="p-1" role="tab">
                      <b-button block href="#" v-b-toggle="'accordion-' + index" variant="info">
                        <div class="row">
                          <div class="col-6"><span class="float-left">{{ group.label }}</span></div>
                          <div class="col-6"><span class="float-right">{{ group.amount }}</span></div>
                        </div>
                      </b-button>
                  </b-card-header>
                  <b-collapse :id="'accordion-' + index" accordion="my-accordion" role="tabpanel">
                  <!-- <b-card-body> -->
                    <div class="col-12" v-for="(record, index2) in group.records" :key="index2">
                      <div class="row justify-content-center">
                        <div class="card col-4">
                          <div class="container text-center px-0 mx-0">
                            <small>{{ record[0] }}</small>
                          </div>
                        </div>
                        <div class="card col-4">
                          <div class="container text-center px-0 mx-0">
                            <small>{{ record[1] }}</small>
                          </div> 
                        </div> 
                        <div class="card col-4">
                          <div class="container text-center px-0 mx-0">
                            <small>{{ record[2] }}</small>
                          </div> 
                        </div>                                
                      </div>
                    </div> 
                  <!-- </b-card-body> -->
                  </b-collapse>
                </b-card>
              </div>   
            </div> 
          </div>
        <!-- </div> -->
      </sequential-entrance>
      <!-- </transition> -->
      <!-- </transition-group> -->
    </div>

    <transition name="slide-4">
      <div v-if="expenditureTotal"><CarouselLogoComponent/></div>
    </transition>

  </div>

</template>

<script>
import { apiService } from "@/common/api.service.js";
import CarouselLogoComponent from "@/components/CarouselLogo.vue";

export default {
  name: "Home",
  components: {
    CarouselLogoComponent    
  },
  data() {
    return {
      expenditures: [],
      nextCat: null,
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
      categories: [],
      startAnimations: false,
      isActive: null,
      show: [0, false]
    }
  },
  methods: {
    toggleItem(index) {
      this.isActive = this.isActive === index ? null : index;
      this.show[0] = index;
      this.show[1] = true;
    },    
    formatPrice(value) {
      let val = (value/1).toFixed(0).replace('.', ',')
      return val.toString().replace(/\B(?=(\d{3})+(?!\d))/g, " ")
    },    
    refresh() {
      if (this.isCorrectYear(this.chosenYear.toString())) {
        //this.startAnimations = !this.startAnimations
        this.expenditures = [],
        this.categories = [],
        this.error = null,
        this.getCategories()
        //this.startAnimations = !this.startAnimations
      } else {
        this.error = "Incorrect Year input"
        //this.startAnimations = false
      }
    },
    getCurrentDate() {
      this.chosenMonth = this.monthNames[this.currentMonth].name;
      this.chosenYear = this.currentYear;
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
          if (data.results.length !== 0) {
            this.expenditures.push(...data.results)
          } else {
            this.error = "No records on chosen date"
          }
          this.loading = false;
          // for pagination
          if (data.next) {
            this.nextExp = data.next;
          } else {
            this.nextExp = null;
          };
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
          this.getExpenditures()
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
  mounted() {
    this.startAnimations = !this.startAnimations;
  },
  created() {
    this.getCurrentDate(),
    this.getCategories(),    
    document.title = "Accounting Ledger";
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
      return dates;
    },
    expenditureTotal() {
      let amountEx = 0
      this.expenditures.forEach(function(entry) {
          amountEx += entry.amount
      });
      return amountEx;     
    },
    expendituresGrouped() {
      function groupBy(objectArray, property) {
        return objectArray.reduce((acc, obj) => {
            const key = obj[property];
            if (!acc[key]) {
              acc[key] = [];
            }
            // Add object to list for given key's value
            acc[key].push(obj);
            return acc;
        }, {});
      }
      const grouped = groupBy(this.expenditures, 'category'); 
      // console.log("this.expenditures", this.expenditures)
      // console.log("grouped", grouped)
      let matrix = []
      Object.entries(grouped).forEach(item =>
        matrix.push(item)
      );      
      // console.log("matrix", matrix)
      const categories = this.categories  
      // console.log("categories", categories)     
      const total = this.expenditureTotal
      let data2 = []
      matrix.forEach(function(entry1) {
        // console.log("entry1[0]", entry1[0])
        // console.log("entry1[1]", entry1[1])
        const category = entry1[0]
        let records = []
        let amount = 0
        entry1[1].forEach(function(entry2) {
          let record = [`${entry2.created_at}`, `${entry2.target}`, `${entry2.amount}`]
          // `${entry2.created_at} | ${entry2.amount} | ${entry2.target}`
          records.push(record)
          amount = amount + entry2.amount 
        });
        let amountPercentage = Math.floor(((amount/total)*100 + Number.EPSILON) * 100) / 100

        var label = categories.find(x => x.id === parseInt(category)).title;
        data2.push({ "label":label, "value":amountPercentage, "amount":amount, "records":records })
      });
      //console.log("data2", data2)

      data2.sort(function(a, b) { 
          return b.amount - a.amount;
      })

      return data2
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
