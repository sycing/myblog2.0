    <template>
      <div id="NavMenu">
        <el-menu
          :default-active="activeIndex"
          class="el-menu-demo"
          mode="horizontal"
          @select="handleSelect"
          router>
          <template v-for="item in navMenuData" :key="" >
            <el-menu-item :index="item.index" v-if="!item.child">{{item.name}}</el-menu-item>

            <el-submenu :index="item.index" v-if="item.child">
              <template slot="title">{{item.name}}</template>
              <template v-for="item2 in item.child" :key="">
                <el-menu-item>{{item2.name}}</el-menu-item> -->
             </template> 
            </el-submenu>
          </template>
        </el-menu>
      </div>
    </template>

    <script>
    // import home from "./components/home"
    // import articlelist from './articlelist.vue'
    export default {
      name: "NavMenu",
      components: {
        home,
        articlelist

      },
      data() {
        return {
          activeIndex: "hoem",
          navMenuData: [
            { index: "home", name: "首页" },
            { index: "articlelist", name: "文章" },
            {
              index: "2",
              name: "关于我",
              //  child: [{ index: "2-1", name: "选项1" },{ index: "2-2", name: "选项2" },{ index: "2-3", name: "选项3" }]
            },

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
    </style>
