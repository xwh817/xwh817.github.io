### adb无线连接手机进行调试
1. 先用USB连接手机，然后
1. adb tcpip 5555
1. 就可以成功adb connect了。


### adb 命令
- adb shell input keyevent 26        // 模拟按键 Power
- adb shell dumpsys battery        // 查看电池信息
- adb shell mount -o remount,rw /system    //  重新挂载system目录，可以对下面只读文件进行操作
- adb shell am start -n com.android.settings/.DisplaySettings        // 启动Activity（进入显示设置页）
- adb pull 远程文件 本地目录     // pull 拉取文件，push 推文件
- adb shell am broadcast -a 广播名        // 发送广播
>adb shell am broadcast -a com.Android.test --es test_string "this is test string" --ei test_int 100 --ez test_boolean true  
说明：test_string为key，后面为value，分别为String类型，int类型，boolean类型
- 重启ADB脚本
```
cd D:\ProgramFiles\Android\sdk\platform-tools
adb kill-server
adb start-server
adb remount
```
- [busybox](https://baike.baidu.com/item/busybox/427860?fr=aladdin) 当遇到adb没有的命令时，试一下前面加上busybox.
> 它集成压缩了 Linux 的许多工具和命令，也包含了 Android 系统的自带的shell。

### 快捷键
- logt  自动生成以类为名的TAG
- logd 自动生成Log.d(...
- Ctrl+Alt+空格键   代码提示 相当于eclipse的ctrl+/
- Ctrl+shift+↑ ↓        代码向上下移动
- Ctrl+D                 复制代码到下一行
- Ctrl+Y                 删除整行代码
- Alt+↑ （↓）         类中方法快速上下浏览
     

### debug时条件断点、setValue
- 断点上右键，condition:设置断点条件，例如 i==10 才停止
- Android studio 在断点调试过程中，在“Variables”窗口中可以右键set value，中途修改变量值。


### sqlite命令行下乱码解决
更改dos窗口编码：打开dos窗口，输入chcp 65001然后回车；注：65001即为UTF-8格式，936是GBK；
对着dos窗口的标题右键，在弹出来的窗口中选择属性，在弹出的窗口中将字体更改为：Lucida Console


### 一些功能点
- 展开侧边Gradle工具栏，可以对Module进行各种组装、编译，生成aar, jar等
- react-native无线调试碰到的问题 https://blog.csdn.net/tuyoucheng/article/details/78288389

