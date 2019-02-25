### 参考
- [作为 Android 开发者必须了解的 Gradle 知识 (译)](https://juejin.im/post/58ca92192f301e007e39be9d)


### config.gradle配置使用 
- 将公共的配置抽取出来
>开发比较大的项目，或是进行组件化开发的时候，一个project会有多个app，这时候每个app中的compile工程如果不能统一，在未来的升级里会很麻烦。 [参考](https://blog.csdn.net/silence_jjj/article/details/73740293)  
> gradle支持自定义config.gradle,使用关键字ext(对应ExtraPropertitesExtension的实例)来定义动态属性。[参考](https://blog.csdn.net/kenway090704/article/details/76930451)  
这里要在想使用这个config.gradle，我们要在project下的build.gradle中添加 apply from : "config.gradle（相对路径）"  
使用这种方式的好处是当Android Support Repository有更新时可以直接在gradle文件中展现提示,又有提示,又能统一管理依赖版本号,一举两得。


### jcenter, mavenCentral
是网络上的代码仓库，  
我们也可以直接进入bintray网站搜索包名，来查找某个第三方库的版本情况。https://bintray.com/search?query=com.baidu.speech ，但是在国内就是个坑，经常网上慢同步失败。可以配置国内代码仓库，例如阿里提供的仓库。[参考](https://www.jianshu.com/p/c360c2c3002e)
```
    allprojects {
        repositories {
            jcenter()
            google()
            maven { url 'http://maven.aliyun.com/nexus/content/groups/public/' }
            maven{ url 'http://maven.aliyun.com/nexus/content/repositories/jcenter'}
        }
    }
```



### implementation & compile
implementation不可以传递依赖，compile可以传递依赖。
因此使用compile会使得module之间的耦合性增大，目前android stuidio推荐使用implementation。
