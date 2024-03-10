    <template>
        <el-menu :default-active="activeIndex" class="nav el-menu-demo" mode="horizontal" @select="handleSelect" router>
          <template v-for="(item,pk) in navMenuData">
            <el-menu-item :index="item.index" v-if="!item.child" :key="pk">{{item.name}}</el-menu-item>
            <el-submenu :index="item.index" v-if="item.child" :key="pk">
              <template slot="title">{{item.name}}</template>
              <!-- <template v-for="(item2, jk) in item.child">
                <el-menu-item :key="jk">{{item2.name}}</el-menu-item>
              </template> -->
            </el-submenu>
          </template>
        </el-menu>
    </template>

    <script>
    export default {
      name: "NavMenu",
      data() {
        return {
          activeIndex: "home",
          navMenuData: [
            { index: "/home", name: "首页" },
            { index: "/article", name: "文章" },
            {
              index: "/about",
              name: "关于我",
              //  child: [{ index: "2-1", name: "选项1" },{ index: "2-2", name: "选项2" },{ index: "2-3", name: "选项3" }]
            }

          ]
        };
      },
      methods: {
        handleSelect(key, keyPath) {
          console.log(key, keyPath);
        }
      },
      mounted(){
          console.log(this.activeIndex)
          console.log(this.$route.path)
          this.activeIndex = this.$route.path.substring(1,this.$route.path.length);

      }
    };
    </script>
    <style scoped>
   @import "../assets/css/nav.css"
  </style>