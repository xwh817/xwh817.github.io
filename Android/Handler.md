### Android Handler机制
- 原理:线程间通信
- 一句话: 为了实现往一个线程中插入任务和消息。
- 一个线程（HandlerThread），不断循环（looper）检查和执行进入的任务（runnable）。
- 使用消息队列（MessageQueue）来管理任务和消息。

### Handler
- 其实它只做推送和处理，
- post 在其他线程推送任务
- sendMessage 在其他线程推送消息
- handleMessage 在主线程中处理消息。


### ThreadLocal
- 用来包装变量，使之在每个线程都是独立的。原理类似使用map来记录每个线程对应的一份值。
- 在这里用于管理Looper，使每一个对象调用getLooper时返回的都是自己独立。

### HandlerThread
- 通过prepare，设置当前线程对应的Looper。 new Handler()时会默认指定当前线程的Looper，主线程默认设置好了，所以要在自定义线程中得手动调用。
- 通过loop，开启消息队列。


### Looper
- 循环检查和执行任务。

### Handler和AsyncTask内存泄露
- ==本质原因==: 在退出时，耗时操作没结束并持有了view的引用（间接持有了activity）。
- 定义为局部变量警告:持有了当前activity，子线程又持有了handler，在子线程中有耗时操作不退出时，就内存泄露了。