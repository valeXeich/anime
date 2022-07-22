import { createStore } from "vuex";

export default createStore({
  state: {
    token: "",
    isAuthenticated: false,
    userrname: "",
  },
  getters: {
    username(state) {
      return state.userrname;
    },
    isAuthenticated(state) {
      return state.isAuthenticated;
    }
  },
  mutations: {
    initializeStore(state) {
      if (localStorage.getItem("auth_token")) {
        state.token = localStorage.getItem("auth_token");
        state.isAuthenticated = true;
        state.userrname = localStorage.getItem("username");
      } else {
        state.token = "";
        state.isAuthenticated = false;
        state.userrname = "";
      }
    },
  },
  actions: {},
  modules: {},
});
