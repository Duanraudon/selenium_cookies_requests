## Selenium自动登录百度搜索资源平台并转requests请求

### 网页分析

目标站点是[https://ziyuan.baidu.com/login](https://ziyuan.baidu.com/login)， 但是这里有一个问题，在用selenium模拟登录的时候应用click（）点击密码登录无效，我尝试过很多种方法最终以失败结局，随即我又想出一种间接登陆的方式，首先登录百度首页，在百度搜索框中直接搜索百度资源平台，这个时候点击进去是默认登录的，于是之后获取cookies信息然后进行处理生成requests请求需要的cookies信息。

### 注意事项
- 需要安装Google Chrome浏览器，还有chromedriver.exe

- 路径要加载正确  executable_path='你的路径'

- ​    chrome_options = Options()

​           chrome_options.add_argument('--headless')

​           chrome_options.add_argument('--disable-gpu')

​           如遇错误可注释这三行并删除参数chrome_options=chrome_options用以调试
