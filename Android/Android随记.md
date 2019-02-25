### 参考
- [掘金 Android 文章精选合集](https://www.jianshu.com/p/5ad013eb5364)


### 一些知识点
- 自定义属性时，可以不自己取名字，直接用之前已经存在的。
- 获取哪个app包名，就打开哪个app，adb下面输入： adb shell "dumpsys window | grep mCurrentFocus" 即可获取当前包名和LauchActivity
- [Android几种强大的下拉刷新库](http://www.cnblogs.com/foxy/p/7825073.html)， [android-Ultra-Pull-To-Refresh](https://github.com/liaohuqiu/android-Ultra-Pull-To-Refresh)
- [从手机中导出 apks](https://blog.csdn.net/lincyang/article/details/44418379) 


### CoordinatorLayout之自定义Behavior
> CoordinatorLayout作为support:design库里的核心控件，在它出现之前，要实现View之间嵌套滑动等交互操作可不是件容易的事，复杂、难度大，基本绕不开View的事件机制，CoordinatorLayout很大程度上解决了这个痛点，方便我们实现各种炫酷的交互效果。链接：https://www.jianshu.com/p/b987fad8fcb4
其实Behavior就是一个应用于View的观察者模式，一个View跟随者另一个View的变化而变化，或者说一个View监听另一个View。https://www.cnblogs.com/hexihexi/p/6143716.html


### 通过Theme来全局修改App控件样式
在<application>中指定AppTheme之后，在style.xml文件中进行自定义扩展。[link](https://www.cnblogs.com/H-BolinBlog/p/5972077.html)
```xml
<!-- Base application theme. -->
<style name="AppTheme" parent="Theme.AppCompat.Light.NoActionBar">
    <!-- Customize your theme here. -->
    <item name="buttonStyle">@style/ButtonStyle</item>
    <item name="android:windowIsTranslucent">true</item>
</style>

<style name="ButtonStyle" parent="@android:style/Widget.Button">
    <item name="android:textAllCaps">false</item> <!--不要默认大写-->
</style>
```

### ActivityLifecycleCallbacks管理Activity和区分App前后台
> API 14之后，在Application类中，提供了一个应用生命周期回调的注册方法，用来对应用的生命周期进行集中管理，这个接口叫registerActivityLifecycleCallbacks，可以通过它注册自己的ActivityLifeCycleCallback，每一个Activity的生命周期都会回调到这里的对应方法。 [link](http://note.youdao.com/noteshare?id=2a655250b46421aa4ef755eb935af1f3&sub=DA1B9E173D914D82B204D55F7A8C1603)


### 使用XML绘制矢量图：
- [矢量图形与矢量动画](https://blog.csdn.net/u013478336/article/details/52277875?utm_source=blogxgwz0)
- [例子](https://blog.csdn.net/lyric_315/article/details/72842659)

- 命令详解(大写代表后面的参数是绝对坐标，小写表示相对坐标)：
- M (x y) 移动到x,y
- L (x y) 直线连到x,y，还有简化命令H(x) 水平连接、V(y)垂直连接
- Z，没有参数，连接起点和终点
- C(x1 y1 x2 y2 x y)，控制点x1,y1 x2,y2，终点x,y
- Q(x1 y1 x y)，控制点x1,y1，终点x,y
- A（圆的x轴半径，y轴半径，x轴旋转角度，0/1-小/大弧度，0/1-逆/顺时针，圆的终点位置x点，圆的终点位置y点）
- https://blog.csdn.net/qq_35323561/article/details/80018898
- https://www.jianshu.com/p/a3cb1e23c2c4


### px、dp、sp
- px，像素单位，在不同屏幕密度设备上会显示不同的效果。
- dp，屏幕密度无关，会根据不同的设备进行转化，适配不同机型。
- sp，字体大小单位,和dp类似，但会随着系统的字体大小改变。（修改系统字体，得到的大小会变化）


### ANR解决
- https://www.jianshu.com/p/8964812972be
- /data/anr/traces.txt文件
```
"main" prio=5 tid=1 MONITOR        // 进程状态，等待锁
  | group="main" sCount=1 dsCount=0 obj=0x415e3ca8 self=0x4151c570
  | sysTid=23957 nice=0 sched=0/0 cgrp=apps handle=1074614612
  | state=S schedstat=( 0 0 0 ) utm=357 stm=118 core=0
  at com.turingcat.knob.speech.google.VoiceRecorder.stop(VoiceRecorder.java:~112)    // 代码定位
```


