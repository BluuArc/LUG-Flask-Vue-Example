import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    posts: [],
  },
  mutations: {
    setPosts (state, posts = []) {
      state.posts = posts;
    },
  },
  getters: {
    isInDevMode: () => !!window.webpackHotUpdate,
  },
  actions: {
    async updatePostList ({ commit, getters }) {
      try {
        const posts = await axios.get(getters.isInDevMode ? 'http://localhost:5000/api/posts' : '/api/posts')
          .then(response => {
            console.debug('response', response);
            return response.data;
          });
        console.debug('got posts', posts);
        commit('setPosts', posts);
      } catch (err) {
        console.error(err);
      }
    },
  },
});
