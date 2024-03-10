<template>
  <el-container>
    <el-aside>
     <contentLeft />  
    </el-aside> 
    <div class="container-right">
      <el-breadcrumb separator="/">
          <el-breadcrumb-item :to="{ path: '/article' }">文章</el-breadcrumb-item>
          <el-breadcrumb-item>
            <a>{{article.title}}</a>
          </el-breadcrumb-item>
        </el-breadcrumb>
        <div>
        <ul>
        <li>{{ $route.query.id }}</li>  &nbsp; 
        <li>{{article.author}}</li>&nbsp; 
        <li>{{article.visiting}}</li>&nbsp; 
        <!-- <li>{{article.created_time}}</li> -->
        <li>{{article.modifyed_time}}</li>&nbsp; 
        <li>{{article.title}}</li>
      </ul>

         
        <span>{{article.body}}</span>
       
      </div>
      </div>>
  </el-container>
  </template>

  <script>
  import axios from 'axios'
  import contentLeft from "../components/contentleft.vue"

  export default {
   name: 'detail',
   components:{
     contentLeft: contentLeft
    },
   data() {
    return {
        test1: "detail",
        artId: this.$route.params.id,
        article: {}
    }
   },
   methods: {
    getTest()
      {
        axios.get(`http://127.0.0.1:8080/api/entry/${this.artId}/`).then(
        respones=>{
           console.log('请求成功了',respones.data)
           this.article=respones.data
          },
        error=>{
           console.log('请求失败了',error.message)}
      )
      }
  },

   mounted(){
    this.getTest()
  console.log(this.$route)
  }
  }
</script>

<style>
  .el-main{
    background-color: #fff;
}
.el-container{
  color: CanvasText;
}
.container-right {
  margin-top: 0px;
  margin-left: 20px;
  margin-bottom: 5px;
  color: #000;
}
ul{
  list-style: none;
  display: flex; 
  flex-direction: row;
}
</style>
