module.exports = {
  lintOnSave: false,
  // devServer:{
  //   proxy:'http://127.0.0.1:8000'
  // }

      //开发模式反向代理配置，生产模式请使用Nginx部署并配置反向代理
    //   devServer: {
    //     port: 8080,
    //     proxy: {
    //         '/api': {
    //             //本地服务接口地址
    //             target: 'http://127.0.0.1:8000',
    //             ws: true,
    //             pathRewrite: {
    //                 '^/api': '/'
    //             }
    //         }
    //     }
    // }
}