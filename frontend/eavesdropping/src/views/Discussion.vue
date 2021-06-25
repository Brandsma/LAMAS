<template>
  <div class="blog">
    <h1>{{ $route.name }}</h1>

    <p>
      In this project we have shown the epistemical developments and
      computational model of three different communication situations in a
      relatively simple logical manner. In addition, we have shown that it is
      possible to detect eavesdroppers and that this can be modelled using
      Action Logic models. There are some caveats that need to be considered
      with this project. For instance, while the interlock protocol is currently
      defined using Action Logic models. However, it does not capture the
      essence of the entire situation, such as half of a message not leading to
      the answer. Some more extensive logic (such as GNY [<router-link
        :to="{ name: 'References' }"
        >5</router-link
      >]) might be used to further model these situations, in addition to Action
      Logic. We do still believe that Action Logic is the right way to go as it
      naturally lends itself to eavesdropping situations where not everyone gets
      the same information and where not everyone believes the same truths.
    </p>
  </div>
</template>

<script>
export default {
  name: "Discussion",
};
</script>

<style scoped></style>
