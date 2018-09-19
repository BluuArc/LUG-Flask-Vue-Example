<template>
  <nav class="navbar is-fixed-top has-background-dark" id="appbar">
    <div class="navbar-brand">
      <router-link class="navbar-item" to="/">
        <b>LUG@UIC</b>
      </router-link>
      <a aria-label="menu" :class="{ 'navbar-burger': true, 'is-active': showMenu }" role="button" @click="showMenu = !showMenu">
        <span aria-hidden="true"/>
        <span aria-hidden="true"/>
        <span aria-hidden="true"/>
      </a>
    </div>
    <div :class="{ 'navbar-menu has-background-dark': true, 'is-active': showMenu }">
      <div class="navbar-start">
        <router-link
          v-for="link in navLinks" :key="link.to"
          :to="link.to"
          @click.native="showMenu = false"
          :class="{ 'navbar-item': true, 'is-active-link': $route.path === link.to }">
          {{ link.title }}
        </router-link>
      </div>
      <div class="navbar-end">
        <div class="navbar-item">
          <div class="field is-grouped">
            <p class="control">
              <a href="mailto:lug@uic.edu" rel="noopener" target="_blank" class="button">
                <span class="icon">
                  <i class="fas fa-at"></i>
                </span>
                <span>Email</span>
              </a>
            </p>
            <p class="control">
              <a href="mailto:lug@uic.edu" rel="noopener" target="_blank" class="button">
                <span class="icon">
                  <i class="fas fa-at"></i>
                </span>
                <span>Slack</span>
              </a>
            </p>
          </div>
        </div>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  computed: {
    navLinks: () => [
      {
        title: 'Home',
        to: '/'
      },
      {
        title: 'About',
        to: '/about',
      },
      {
        title: 'Events',
        to: '/events',
      },
      {
        title: 'Contact',
        to: '/contact',
      },
    ],
  },
  data: () => ({
    showMenu: false,
  }),
};
</script>

<style lang="less">
#appbar.navbar.has-background-dark {
  --color-light: hsl(0, 0%, 96%); // has-text-light
  --color-inactive: hsl(0, 0%, 48%); // has-text-grey

  .navbar-brand {
    .navbar-item, .navbar-burger {
      color: var(--color-light);
    }
  }

  .navbar-item {
    text-transform: uppercase;
    color: var(--color-inactive);

    &.is-active-link:not(:hover) {
      color: var(--color-light);
    }
  }
}
</style>
