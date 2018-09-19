<template>
  <div>
    <app-bar/>
    <router-view/>
    <footer class="footer has-background-white">
      <div class="has-text-centered">
        <img src="@/assets/BlackTux.png" width="40" height="40"/>
      </div>
    </footer>
  </div>
</template>

<script>
import AppBar from '@/components/AppBar';
export default {
  components: {
    AppBar,
  },
};
</script>


<style lang="less">
html {
  overflow: auto;
}
</style>
