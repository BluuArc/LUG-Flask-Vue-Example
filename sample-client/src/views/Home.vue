<template>
  <div class="container is-fluid">
    <section class="hero">
      <div class="hero-body">
        <div class="container">
          <h1 class="title">LUG</h1>
          <h2 class="subtitle">For individuals interested in Linux, Unix, and byproducts.</h2>
        </div>
      </div>
    </section>
    <section class="section">
      <div class="container">
        <div class="tile is-ancestor">
          <div class="tile is-parent is-8">
            <div class="tile is-child">
              <h1 class="title">Welcome</h1>
              <div class="content">
                <p>
                  This is the home page for LUG at UIC. LUG stands for Linux Users Group, this means that we focus on learning all things related to Linux. Linux is an open source operating system that uses the Linux kernel. Because of its open nature Linux and the Linux kernel can be modified to suit a particular purpose. Thanks to this you can find Linux in many places such as your phone, a car, and even the United States Postal Service use Linux. 
                </p>
                <p>
                  Want to know more? Signup for the Listserv or come to a meeting.
                </p>
              </div>
            </div>
          </div>
          <div class="tile is-4 is-parent is-vertical">
            <div class="tile is-child">
              <div class="content">
                <div class="level">
                  <div class="level-item">
                    calendar here
                  </div>
                </div>
              </div>
            </div>
            <div class="tile is-child">
              <div class="content">
                <div class="level">
                  <div class="level-item">
                    LUG officer info here
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <post-list/>
      </div>
    </section>
  </div>
</template>

<script>
import PostList from '@/components/PostList';

export default {
  components: {
    PostList,
  },
};
</script>
