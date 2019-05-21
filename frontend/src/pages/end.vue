<template>
  <div>

    <div v-if='this.$session.get("result")'>Your result comes from {{this.$session.get("result")}} method of the test.</div>
    The test is completed,
    Please complete 
    
    <a href="https://forms.gle/YJJM7buRzT1UQfrW9">this survey</a>, thank you.
  </div>
</template>
<script>
export default {
  data() {
    return {};
  }
};
</script>
