<template>    
  <el-container>
        <el-aside >  
          <contentLeft/>
        </el-aside>
        <div class="container-right">
              <!--  文章列表  -->
          <div class="blog"  v-for=" art in dataShow" :key="art.id">
                    <div class="title">{{art.title}}</div>
                    <div class="date">
                      <el-tag size="mini" class="datetag">{{ art.tags[0] }}</el-tag>
                      <el-tag size="mini" class="datetag" v-once>{{ art.author}}</el-tag>
                      <div>{{ art.created_time }}</div>
                    </div>
                    <div class="desc">{{ art.abstract }}</div>
                    <!-- <a class="detail"  href="article.html">查看正文 &gt;&gt;</a> -->
                    <router-link class="detail" :to="{
                        name: 'detailname',
                        params: {
                          id: art.id,
                        }
                      }" >查看详情 &gt;&gt;</router-link>
          </div>
          <div class="block">
            <el-pagination class="pagination"
              @size-change="handleSizeChange"
              @current-change="handleCurrentChange"
              :current-page="currentPage"
              :page-sizes="[5, 10, 20, 100]"
              :page-size="pageSize"
              layout="total, sizes, prev, pager, next, jumper"
              :total="totalPage">
            </el-pagination>
          </div>
        </div>
  </el-container>

</template>
    <script>
    import axios from 'axios'
    import contentLeft from "../components/contentleft.vue"

    export default {
     
     name: 'Myarticle',
     components:{
     contentLeft: contentLeft
    },
     data() {
      return {
        artlist: [],
        currentPage: 1,
        totalPage: 100,
        pageSize: 10,
        pageNum: 1,
        totalPageData: [],
        dataShow: []
      }
     },
     methods:{
      getTest()
      {
        axios.get('http://127.0.0.1:8080/api/entry/').then(
        respones=>{
           console.log('请求成功了',respones.data)
           this.artlist=respones.data
           this.totalPage=respones.data.length;
           this.calcPageData()
          },
        error=>{
           console.log('请求失败了',error.message)}
         )
      },
      calcPageData()
      {
        if(this.artlist.length>1)
        {
          this.pageNum = Math.ceil(this.artlist.length / this.pageSize) || 1;
          console.log('总页数:',this.pageNum);
        }
        for (let i = 0; i < this.pageNum; i++) 
        {
        // 每一页都是一个数组 形如 [['第一页的数据'],['第二页的数据'],['第三页数据']]
        // 根据每页显示数量 将后台的数据分割到 每一页,假设pageSize为5， 则第一页是1-5条，即slice(0,5)，第二页是6-10条，即slice(5,10)...
          this.totalPageData[i] = this.artlist.slice(this.pageSize * i, this.pageSize * (i + 1));
          }
          console.log("totalPageData"+this.totalPageData)
          console.log("currentPage"+this.currentPage)
        // 获取到数据后显示第一页内容,数组下标是从0开始的，这里一定要减去1，不然会丢失一组数据
        this.dataShow = this.totalPageData[this.currentPage - 1];
        console.log("dataShow"+this.dataShow);
      },
      handleSizeChange(val) {
        this.pageSize=val;
        this.calcPageData();
        // console.log(`每页 ${val} 条`);
      },
      handleCurrentChange(val) {
        this.currentPage=val;
        this.calcPageData();
        // console.log(`当前页: ${val}`);
      }
    },
    mounted(){
      this.getTest()
    }
    }

    </script>
    <style scoped>
    @import "../assets/css/index.css";
  

   .nav-left
   {
    width: 30%;
    float: left;
  }
  .art-rigth{
  width: auto;
  border: #13081b80;
  border: 1px;
 }
 .pagination{
   float: right;
}
.container-right {
  margin-top: 0px;
  margin-left: 20px;
  margin-bottom: 5px;
  color: #000;
}
.el-aside{
  margin-top: 0px;
}


 
    </style>