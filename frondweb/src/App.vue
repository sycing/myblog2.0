    <template>
      <div id="app">
        <el-container>
          <el-header>
            <NavMenu/>
          </el-header>
          <el-main>
            <!-- 路由出口 -->
              <router-view/>
          </el-main>
          <el-footer></el-footer>
        </el-container>
      </div>
    </template>
     
    <script>
    import nav from "./components/nav";
     
    export default {
      name: "app",
      components: {
        NavMenu: nav
      }
    };
    </script>
     
<style scoped>

  /* @import "./assets/css/common.css"; */
    .el-header {
      /* background-color: #0850f8ea; */
      /* color: #fdf8f8; */
      text-align: center;
      height: 100px;
      padding: 0px;
      line-height: 60px;
    }
     
    .el-main {
      background-color: #a7cbf06b;
      /* color: #333; */
      /* text-align: center;
      line-height: 160px; */
      padding: 0px;
    } 
    /* .el-aside{
    background-color:#b6b4b5;
    color:#3331; 
    text-align: center;
    line-height: 200px;
    } */
     
    /* .el-container{
    margin-bottom: 40px;
    } */

</style>
