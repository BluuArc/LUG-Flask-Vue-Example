<template>
  <div class="container">
    <div class="title">Recent Posts</div>
    <div class="tile is-ancestor is-vertical">
      <template v-if="loadingPosts">
        <div class="tile is-parent is-12 loading-tile" v-if="loadingPosts">
          <div class="tile is-child">
            <div class="content">
              <div class="hero">
                <div class="hero-title">
                  <h2 class="subtitle">Loading posts...</h2>
                </div>
              </div>
            </div>
          </div>
        </div>
      </template>
      <template v-else>
        <div class="tile is-parent is-12 post" v-for="(post, i) in posts" :key="i">
          <div class="tile is-child">
            <div class="subtitle"><b>{{ post.title }}</b></div>
            <div class="content">{{ post.content }}</div>
          </div>
        </div>
        <div class="tile is-parent is-12" v-if="posts.length === 0">
          <div class="tile is-child">
            <div class="content">No posts found.</div>
          </div>
        </div>
      </template>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex';
export default {
  computed: {
    ...mapState(['posts']),
  },
  methods: {
    ...mapActions(['updatePostList']),
  },
  data () {
    return {
      loadingPosts: true,
    };
  },
  async mounted () {
    this.loadingPosts = true;
    await new Promise((resolve) => {
      console.debug('mocking 3s delay');
      setTimeout(resolve, 3000);
    });
    await this.updatePostList();
    this.loadingPosts = false;
  },
};
</script>

<style lang="less">
.tile.post:nth-child(odd) {
  background-color: hsl(0, 0%, 96%);
}

.loading-tile {
  animation-duration: 1s;
  animation-iteration-count: infinite;
  animation-name: loading-flash;
  animation-direction: alternate;

  .hero .hero-title {
    display: flex;
    align-items: center;
    justify-items: center;
  }
}

@keyframes loading-flash {
  from { opacity: 1; }
  to { opacity: 0; }
}
</style>
