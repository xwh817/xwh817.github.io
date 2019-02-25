# Activity是干什么，用户交互的入口。
-  Activity生命周期，4中状态：running/paused/stopped/killed
-  onCreate()     启动、不可见
-  onStart()          启动中、可见、无焦点
-  onResume()     前台、有焦点可以交互
-  onPause()     退出中
-  onStop()     处于后台了
-  onDestory()     结束
-  onRestart()     重后台再次进入前台的时候

# android进程优先级：
前台（onResume） / 可见(onStart) / 服务（Service） / 后台 / 空

# android任务栈

# activity启动模式
- standard 每次都生成新的Activity
- singleTop 栈顶唯一
- singleTask 栈内唯一，如果已经存在，会把其上的Activity移出。
- singleInstance 全局唯一
> 复用之前的Activity会调用onNewIntent()

# Fragment
-  大屏复用、动态的加载到Activity之中。
-  FragmentManager通过FragmentTransaction来对fragment进行管理。
-  ViewPager + Fragment   
-  FragmentPagerAdapter     并不回收fragment内存，适合页面少需要重用的情况。
-  ==FragmentStatePagerAdapter==     回收了内存，适合页面较多的情况。

# Fragment生命周期
-  onAttach...onCreate...onCreateView.....
-  onDestoryView...onDestory...onDetach

# 判断Fragment是否可见
-  普通情况：onResume/onPause
-  使用show()/hide()时：onHiddenChanged 回调
-  在ViewPager中时：setUserVisibleHint 回调
    
# Service 一种在后台长时间执行的、没有用户界面的应用组件。
-  后台运行，长时间默默执行的任务
-  运行在主线程，不能进行耗时操作（区别长时间运行）
-  优先级比后台Activity高，不容易被系统回收。

# Service和Thread的区别，其实没啥关系
-  子线程用来执行耗时操作。
-  Service是后台、在主线程。例如音乐后台播放、监听广播、日志统计、后台下载等。
-  Service不依附于Activity，用户界面关闭了，也可以继续执行。
-  在Activity中启动的子线程，界面退出时通常也要退出，不然可能造成内存泄露。
-  想要在Service中进行耗时操作，那就启一个单独的线程。

# Service两种启动方式 
- [区别](https://www.jianshu.com/p/d870f99b675c)
 1. startService     通过Intent, startService(intent)
 2. bindService     需要一个ServiceConnection;
 > 返回IBinder（android提供的进程间和跨进程调用机制的接口）。调用多次bindService，onCreate和onBind都只在第一次会被执行，onServiceConnected会执行多次。
可以在onServiceConnected方法里拿到了MyService服务的内部类MyBinder的对象，以此调用这个内部类的非私有成员对象和方法。
调用者和绑定者绑在一起，调用者一旦退出服务也就终止了。

# Service生命周期
-  onBind     // 只用在bindService
-  onCreate
-  onStartCommand
-  onDestory
> onCreate只执行一次，startService(intent)可以多次调用，对应于onStartCommand。（有个返回值表示复活时是否自动启动。）


# Broadcast / Receiver
- 进程间通信
- 全局通知
> 原理，观察者模式，通过Binder机制向AMS Activity Manager Service进行注册。通过消息循环队列通知注册的Receiver

# Receiver
-  静态注册
-  动态注册、注意注销防止内存泄露。

# LocalBroadcastManager
-  内部广播，其他App收不到也不能发送该广播，安全。
-  和普通广播不同，其原理是使用Handler来发送Message，高效。

# WebView
> api 16之前，全程代码执行漏洞，通过javascript调用任意java对象和方法。  
 @JavascriptInterface注解来提高安全等级，没有注解的方法，js无法调用

- [javascript和Java之间交互](https://www.jianshu.com/p/07f2e1364f35)，约定好方法之后，就可以相互调用了。
- 可以使用[第三方库JsBridge](https://www.jianshu.com/p/910e058a1d63)
```
     // java调用javascript：
     webView.loadUrl("javascript:setICCID('" + No:007 + "')")
     // javascript调用java：
     window.WebViewJavascriptBridge.callHandler('submitFromWeb', {'param': str1}, function(responseData) ...
 ```
 
# 判断网页是否加载完成。
-  webviewClient.onPageFinished,不推荐使用，网页跳转时会多次调用。
-  WebChromeClient.onProgressChanged, 推荐

# WebView硬件加速
- 打开可能造成页面渲染问题，白屏、闪烁。可暂时关闭。

# WebView内存泄露
-  webView持有所在的Activity，webView内部线程不能和Activity一致，导致可能Activity退出了WebView还在执行。
-  解决：  
1. 使用独立进程运行Activity。节省App自己最大内存、但是进程间通信比较麻烦。
2. 使用弱引用，同时把WebView放在子View中，Activity退出时动态Remove掉。


# Binder  AIDL
- Linux用许多进程间通信机制（IPC），为什么选用Binder? 安全、高效
- 不同的进程 通过系统的Binder驱动 进行IPC
- 系统Binder内核驱动是一个中介。

> 什么是Binder，回答：  
Binder是一种通信机制。  
对本地Server对象来说Binder是本地对象，对Client来说Binder是一个代理对象。  
传输过程中，Binder是可以在不同进程间传递的对象，完成Server和Client之间数据的转换。



# Handler

# AsyncTask
-  本质是一个封装了线程池和handler的异步框架。
-  三个泛型参数：传入的参数、中间进度、执行结果。
-  方法： onPreExecute --- doInBackground --- onProgressUpdate --- onPostExecute

# HandlerThread
-  handler + thread + looper
-  子线程中没有默认开启looper

# IntentService 对Service进行了扩展，封装了进行异步操作的handlerThread
-  默认的Service里面不能直接进行耗时操作
-  在IntentService中onHandleIntent里面实现异步操作



# ProGuard 代码混淆
> 文件Java编译好后的class字节码非常容易被反编码，为了很好的保护Java源代码，我们需要对class文件进行混淆。   
ProGuard是一个混淆代码的开源项目。通过在Gradle中配置proguardFile...
- 压缩(Shrink)：检测并移除代码中无用的类、字段、方法和特性（Attribute）。
- 优化(Optimize)：对字节码进行优化，移除无用的指令。
- 混淆(Obfuscate)：使用a，b，c，d这样简短而无意义的名称，对类、字段和方法进行重命名。
- 预检(Preveirfy)：在Java平台上对处理后的代码进行预检，确保加载的class文件是可执行的。


# 网络请求框架
-  OkHttp、Retrofit、Volley等等
-  对网络请求过程、线程池、并发管理、缓存进行了封装。


# HTTP协议
- 简单快速、无连接、单向请求
- 无状态，对事务没有记忆，没有Session
- Response：304 Not Modified 告诉浏览器本次请求内容没有修改，直接使用本地缓存。
- 通过ETag来标识是否更新了。

# get / post
-  get 获取资源 数据放在url之后，大小有限制，数据暴露不安全
-  post 提交资源 数据放在body，无大小限制，安全。
# cookie
-  放在客户端的信息，下次请求时带上这些数据，服务端就可以知道之前的会话。
# session
-  放在服务端的信息，当服务端收到请求时，查询session获取会话信息。

# https
- 在http之上加了一层加密连接（SSL/TLS）
- 在握手阶段采用非对称加密，连接成功之后对称加密。

# 数字证书，非对称加密
> 私钥/公钥  
 非对称验证原理：客户端发送一个随机数到服务端，服务端返回用私钥加密过的结果，客户端拿公钥去解，如果结果不一致，说明服务端私钥和公钥不匹配，服务端可能是伪造的。
数字证书，保证客户端得到的信息是可靠的，如果伪造或篡改，客户端拿数字证书公钥解不出来。
  
# TCP/IP模型
- 应用层：应用程序的数据通信格式。HTTP、FTP、DNS
- 传输层：端口到端口之间的通信
- 网络层：ip地址（子网划分），ip数据包、arp协议（ip地址得到mac地址）
- 链接层：mac地址、广播
- 物理层：网线、无线











     
    