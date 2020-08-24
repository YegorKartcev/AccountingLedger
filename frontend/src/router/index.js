import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Ledger from "../views/Ledger.vue";
import Income from "../views/Income.vue";
import IncomeEditor from "../views/IncomeEditor.vue";
import Expenditure from "../views/Expenditure.vue";
import ExpenditureEditor from "../views/ExpenditureEditor.vue";
import Lists from "../views/Lists.vue";
import List from "../views/List.vue";
import ListEditor from "../views/ListEditor.vue";
import NotFound from "../views/NotFound.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home
  },
  {
    path: "/ledger/",
    name: "Ledger",
    component: Ledger
  },  
  {
    path: "/income/:slug",
    name: "Income",
    component: Income,
    props: true
  },
  {
    path: "/income/:slug?",
    name: "Income-editor",
    component: IncomeEditor,
    props: true
  },  
  {
    path: "/expenditure/:slug",
    name: "Expenditure",
    component: Expenditure,
    props: true
  },
  {
    path: "/expenditure/:slug?",
    name: "Expenditure-editor",
    component: ExpenditureEditor,
    props: true
  },
  {
    path: "/lists",
    name: "Lists",
    component: Lists
  },
  {
    path: "/list/:slug",
    name: "List",
    component: List,
    props: true
  },
  {
    path: "/list/:slug?",
    name: "List-editor",
    component: ListEditor,
    props: true
  },
  {
    path: "*",
    name: "page-not-found",
    component: NotFound
  },
];

const router = new VueRouter({
  mode: "history",
  // base: process.env.BASE_URL,
  routes,
  linkExactActiveClass: "active"

});

export default router;
