### 配置ndk环境搭建  
[参考](https://blog.csdn.net/young_time/article/details/80346631)
- 使用AndroidStudio SDK Manager -> SDK tool -> 勾选 NDK 和一个 LLDB 版本
- 先说明一下，跟着网上的视频和文档，被坑了一逼。莫名其妙的出现各种问题。
- 新版本会带来新的工具和更简便的方式，所以最好搜索最新版本的。
- 将javah, ndk-build 配置成菜单工具，这是新版本带来的便捷方式，不然以前的方式要一大堆命令行。遇到的坑：Window和Ubuntu、IOS路径不同问题，文档里面的javah.exe在其他平台肯定是没有的。
- Android.mk, Application.mk视频上面讲的不需要配置，实践动手后发现报错，添加后可以了。
- 编写的hello.cpp有问题，视频教程里面居然只是编译一下就生成了so，没有说出现问题了怎么办，没有提到用ndk-build去编译cpp文件，出错后可以知道哪行报错。

### HelloNDK
- https://www.jianshu.com/p/09ff3300f453
- https://www.cnblogs.com/guanmanman/p/6769240.html
1. 编写native方法
2. 通过javah 生成头文件：（新的方式，将javah配置成External Tools）
> 手动命令行方式：进入项目java目录，执行javah 包含native定义的Java文件。
NDKTest/app/src/main/java$ javah -d ../jni com.xwh.ndktest.JNITest
../jni表示头文件保存的目录
3. 实现头文件档c/cpp代码
4. 添加Android.mk,Application.mk文件
5. build.gradle配置生成的so名称和支持的cpu类型，build一下生成so文件。
```
    /**
     * 配置ndk模块，如果只是调用so文件，这儿可以去掉。
     */
    ndk{
        moduleName "hello"  // ndk模块名
        //abiFilters "armeabi", "armeabi-v7a", "x86" //CPU类型
    }
```
6. 在要使用的地方，通过 static { System.loadLibrary("hello"); } 引入so库。
```
     sourceSets.main{
        jni.srcDirs = []
        jniLibs.srcDir "src/main/libs"  // 用来指定so文件目录
    }
```

### 使用External Tools 配置的两个工具
- javah：将定义好的java native代码转成.h头文件
- ndk-build：对c/cpp文件进行编译。每次修改了c/cpp代码之后，执行一下更新so。（动手实验修改cpp代码，直接点执行，不会同步。）


