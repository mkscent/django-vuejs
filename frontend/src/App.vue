<template>
  <div id="app">
    {{msg}}
    <form @submit.prevent="submitNote">
      <label>Title</label>
      <input type="text" v-model="formData.title"/>
      <label>Content</label>
      <textarea v-model="formData.content"></textarea>

      <br/>
      <button type="submit">Submit</button>
    </form>
  </div>
</template>

<script>
import api from './api/index'
export default {
  name: 'app',
  data () {
    return {
      msg: '',
      formData: {
        title: '',
        content: ''
      }
    }
  },
  methods: {
    submitNote () {
      api.fetchNotes('post', null, this.formData).then(res => {
        this.msg = 'Saved'
      }).catch((e) => {
        this.msg = e.response
      })
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  max-width: 500px;
  margin: 0 auto;
  text-align: left;
}

h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
  input, textarea{
    width: 100%;
    display: block;
    padding: 6px 10px;
    border: 1px solid #ddd;
    border-radius: 4px;
  }

  label{
    margin-top: 15px;
    display: block;
  }

  button{
    background: #000;
    color: #fff;
    border-radius: 3px;
    padding: 6px 10px;
  }
</style>
