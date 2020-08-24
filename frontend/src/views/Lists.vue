<template>
  <div class="home">
    <div class="container mt-2">
        <div class="row justify-content-center mt-3">
            <div class="container-fluid px-1 col-10 col-sm-10 col-md-4 col-lg-4">
              <div class="input-group mb-3">
                <div class="input-group-prepend">
                  <span class="input-group-text">Year</span>
                </div>
                <input type="text" v-model="chosenYear" class="form-control text-right">
              </div>
            </div>
            <div class="container-fluid px-1 col-10 col-sm-10 col-md-4 col-lg-4">
              <div class="input-group mb-3">
                  <div class="input-group-prepend">
                    <span class="input-group-text">Month</span>
                  </div>
                  <select v-model="chosenMonth"  class="form-control text-right">
                      <option v-for="month in monthNames" :key="month.id">{{ month.name }}</option>
                  </select>
              </div>
            </div>
            <div class="container-fluid px-1 col-10 col-sm-10 col-md-4 col-lg-4">
              <div class="input-group mb-3">
                <div class="input-group-prepend">
                  <span class="input-group-text">Day</span>
                </div>
                <input type="text"
                  v-model="chosenDay"
                  class="form-control text-right"
                >
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
            class="btn btn-sm btn-outline-success wdt150"
            v-if="!loading">
            <svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-cloud-arrow-down icon" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
              <path fill-rule="evenodd" d="M4.406 3.342A5.53 5.53 0 0 1 8 2c2.69 0 4.923 2 5.166 4.579C14.758 6.804 16 8.137 16 9.773 16 11.569 14.502 13 12.687 13H3.781C1.708 13 0 11.366 0 9.318c0-1.763 1.266-3.223 2.942-3.593.143-.863.698-1.723 1.464-2.383zm.653.757c-.757.653-1.153 1.44-1.153 2.056v.448l-.445.049C2.064 6.805 1 7.952 1 9.318 1 10.785 2.23 12 3.781 12h8.906C13.98 12 15 10.988 15 9.773c0-1.216-1.02-2.228-2.313-2.228h-.5v-.5C12.188 4.825 10.328 3 8 3a4.53 4.53 0 0 0-2.941 1.1z"/>
              <path fill-rule="evenodd" d="M7.646 10.854a.5.5 0 0 0 .708 0l2-2a.5.5 0 0 0-.708-.708L8.5 9.293V5.5a.5.5 0 0 0-1 0v3.793L6.354 8.146a.5.5 0 1 0-.708.708l2 2z"/>
            </svg><span class="px-2">Load</span>
          </button> 
          <div v-else>
            <span><b-spinner label="Loading..."></b-spinner></span>  
          </div>
        </div>
    </div>

    
      <div class="container">
        <sequential-entrance fromTop delay="150">
        <!-- <transition-group name="fade"> -->
          <div v-for="list in lists" :key="list.id">
            <div class="row justify-content-center">
              <div class="card task my-1 col-10 col-sm-10 col-md-8 col-lg-6">
                <div class="row">
                  <div class="card-header container-fluid text-center">
                    <h6>
                      <router-link
                        :to="{ name: 'List', params: { slug: list.slug } }"
                        class="pulse-animation"
                        >{{ list.title }}
                      </router-link>
                    </h6>
                  </div>
                </div>
                <div class="row c-body-full">
                  <div class="card-body">
                    <div v-for="record in list.choices" :key="record.id">
                      <div class="row">
                          <p class="striked-through text-muted ml-3 mr-3" v-if="record.checked">{{ record.text }}</p>
                          <p class="ml-3 mr-3" v-else>{{ record.text }}</p>
                      </div>
                    </div>
                  </div>
                </div>
                <div class="row">
                  <div class="card-footer text-muted container-fluid text-center">
                    <small>
                      <p class="my-0">{{ list.created_at }}</p>
                    </small>
                  </div>
                </div>
              </div>
            </div>
          </div>
        <!-- </transition-group> -->
        </sequential-entrance>
        <div class="row justify-content-center mb-4 mt-2" v-show="next">
          <button
            @click="getLists"
            class="btn btn-sm btn-outline-success wdt230"
            v-if="!loading">
            <svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-cloud-arrow-down icon" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
              <path fill-rule="evenodd" d="M4.406 3.342A5.53 5.53 0 0 1 8 2c2.69 0 4.923 2 5.166 4.579C14.758 6.804 16 8.137 16 9.773 16 11.569 14.502 13 12.687 13H3.781C1.708 13 0 11.366 0 9.318c0-1.763 1.266-3.223 2.942-3.593.143-.863.698-1.723 1.464-2.383zm.653.757c-.757.653-1.153 1.44-1.153 2.056v.448l-.445.049C2.064 6.805 1 7.952 1 9.318 1 10.785 2.23 12 3.781 12h8.906C13.98 12 15 10.988 15 9.773c0-1.216-1.02-2.228-2.313-2.228h-.5v-.5C12.188 4.825 10.328 3 8 3a4.53 4.53 0 0 0-2.941 1.1z"/>
              <path fill-rule="evenodd" d="M7.646 10.854a.5.5 0 0 0 .708 0l2-2a.5.5 0 0 0-.708-.708L8.5 9.293V5.5a.5.5 0 0 0-1 0v3.793L6.354 8.146a.5.5 0 1 0-.708.708l2 2z"/>
            </svg><span class="px-2">Load more on chosen date</span>
          </button> 
          <div v-else>
            <transition name="fade" mode="out-in">
              <span><b-spinner label="Loading..."></b-spinner></span>
            </transition>  
          </div>
        </div>

      </div>
    
    <transition name="slide-4">
      <div v-if="!loading"><CarouselLogoComponent/></div>
    </transition>
  </div>  
</template>

<script>
import { apiService } from "@/common/api.service.js";
import CarouselLogoComponent from "@/components/CarouselLogo.vue";
export default {
  name: "Lists",
  components: {
    CarouselLogoComponent
  },  
  data() {
    return {
      lists: [],
      next: null,
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
      chosenDay: null,
      error: null
    }
  },
  methods: {
    refresh() {
      if (this.isCorrectYear(this.chosenYear.toString())) {
        this.lists = [],
        this.next = null,
        this.error = null,
        this.getLists()
      } else {
        this.error = "Incorrect Year input";
      }
    },
    getCurrentDate() {
      this.chosenMonth = this.monthNames[this.currentMonth].name;
      this.chosenYear = this.currentYear;
      this.chosenDay = "";
    },
    getLists() {
      var monthNumber = this.getKeyOfValue(this.monthNames, this.chosenMonth);
      // make a GET Request to the Tasks list endpoint and populate the tasks array
      let endpoint = `/api/tasks/`;
      let search_month = this.monthNames[monthNumber-1].id
      let search_day = ""
      if (search_month.toString().length === 1) {
        search_month = "0"+search_month
      }
      if (this.isCorrectDay(this.chosenDay.toString())) {
          search_day = this.chosenDay
      } 
      if (search_day.toString().length === 1) {
        search_day = "0"+search_day
      }
      endpoint = `/api/tasks/?search=${this.chosenYear}-${search_month}-${search_day}`

      if (this.next) {
        endpoint = this.next;
      }
      this.loading = true;
      apiService(endpoint)
        .then(data => {
          if (data.results.length !== 0) {
            this.lists.push(...data.results)
          } else {
            this.error = "No lists on chosen date"
          }
          this.loading = false;
          if (data.next) {
            this.next = data.next;
          } else {
            this.next = null;
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
    },
    isCorrectDay(day) {
      var text = /^[0-9]+$/;
      if(day.length==1 || day.length==2) {
        if (day != 0) {
          if ((day != "") && (!text.test(day))) {
              return false;
          }
          return true;
        } else {
          return false
        }
      } else {
        return false
      }
    }
  },
  created() {
    this.getCurrentDate(),
    this.getLists()
    document.title = "Lists";
  },
  computed: {
    getDates() {
      let datesLists = [];
      this.lists.forEach(function(entry) {
          datesLists.push(entry.created_at)
      });
      let dates = [...new Set([...datesLists])];          
      return dates;
    }
  }
};
</script>

<style scoped>
  .flex-row {
    display: flex;
    flex-wrap: wrap;
  }

  .card-header:hover {
    font-weight: bold;
  }
  .card-header a:hover {
    text-decoration: none !important;
    font-weight: bold;
  }
  .card-header a {
    color:black;
  }


  [type="checkbox"]
  {
      vertical-align:middle;
  }
  .striked-through {
    text-decoration: line-through;
    background-color: #ffe6e2;
  }
  .c-body-full {
    background-color: white;
  }



.pulse-animation {
  border-radius: 3%;

	box-shadow: 0 0 0 0 rgba(0, 0, 0, 1);
	transform: scale(1);
	animation: pulse 2s infinite;
}

@keyframes pulse {
	0% {
		transform: scale(0.95);
		box-shadow: 0 0 0 0 rgba(0, 204, 255, 0.9);
	}

	70% {
		transform: scale(1);
		box-shadow: 0 0 0 10px rgba(224, 249, 255, 0);
	}

	100% {
		transform: scale(0.95);
		box-shadow: 0 0 0 0 rgba(224, 249, 255, 0);
	}
}
</style>
