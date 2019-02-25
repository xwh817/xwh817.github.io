
### RxJava是什么:     
https://www.daidingkang.cc/2017/05/19/Rxjava/
> &emsp;&emsp;Rxjava和我们平时写的程序有什么不同。我们一般写的程序统称为命令式程序，是以流程为核心的，每一行代码实际上都是机器实际上要执行的指令。而Rxjava这样的编程风格，称为函数响应式编程。函数响应式编程是以数据流为核心，处理数据的输入，处理以及输出的。  
&emsp;&emsp;这种思路写出来的代码就会跟机器实际执行的指令大相径庭。所以对于已经习惯命令式编程的我们来说，刚开始接触Rxjava的时候必然会很不适应，而且也不太符合我们平时的思维习惯。但是久而久之你会发现这个框架的精髓，尤其是你运用到大项目中的时候，简直爱不释手，随着程序逻辑变得越来越复杂，它依然能够保持代码简洁。

- 被观察者
- 观察者
- 事件、响应（响应式编程）
- 

> - [很好的将链式编程风格和异步结合在一起](https://www.jianshu.com/p/cd3557b1a474)
> - [给 Android 开发者的 RxJava 详解](https://gank.io/post/560e15be2dca930e00da1083)


### RxJava 有四个基本概念：
- Observable (被观察者)，它决定什么时候触发事件以及触发怎样的事件。 RxJava 使用 create() 等方法来创建一个 Observable ，并为它定义事件触发规则。
- Observer (观察者) ，实现：Observer、Subscriber（Observer 接口进一步扩展）
- subscribe (订阅)，创建了 Observable 和 Observer 之后，再用 subscribe() 方法将它们联结起来，整条链子就可以工作了。 observable.subscribe(observer);
- 事件，事件回调方法除了普通事件 onNext() （相当于 onClick() / onEvent()）之外，还定义了两个特殊的事件：onCompleted() 和 onError()。


### 线程调度
- 调度器，相当于线程控制器，RxJava 通过它来指定每一段代码应该运行在什么样的线程。RxJava 已经内置了几个 Scheduler ，它们已经适合大多数的使用场景：
- Schedulers.immediate(): 直接在当前线程运行，相当于不指定线程。这是默认的 Scheduler。
- Schedulers.newThread(): 总是启用新线程，并在新线程执行操作。
- Schedulers.io(): I/O 操作（读写文件、读写数据库、网络信息交互等）所使用的 Scheduler。行为模式和 newThread() 差不多，区别在于 io() 的内部实现是是用一个无数量上限的线程池，可以重用空闲的线程，因此多数情况下 io() 比 newThread() 更有效率。不要把计算工作放在 io() 中，可以避免创建不必要的线程。
- Schedulers.computation(): 计算所使用的 Scheduler。这个计算指的是 CPU 密集型计算，即不会被 I/O 等操作限制性能的操作，例如图形的计算。这个 Scheduler 使用的固定的线程池，大小为 CPU 核数。不要把 I/O 操作放在 computation() 中，否则 I/O 操作的等待时间会浪费 CPU。
- 另外， Android 还有一个专用的 AndroidSchedulers.mainThread()，它指定的操作将在 Android 主线程运行。


### 操作符
对事件序列进行处理
```
    /**
    * map：对事件进行转换，将参数转换为期望的结果
    */
    .map(new Func1<String, Bitmap>() {  // 将String类型转成Bitmap
        @Override
        public Bitmap call(String filePath) { // 参数类型 String
            return getBitmapFromPath(filePath); // 返回类型 Bitmap
        }
    })
    
    
    
    Observable.just("images/logo.png") // 输入类型 String
    .map(new Func1<String, Bitmap>() {
        @Override
        public Bitmap call(String filePath) { // 参数类型 String
            return getBitmapFromPath(filePath); // 返回类型 Bitmap
        }
    })
    .subscribe(new Action1<Bitmap>() {
        @Override
        public void call(Bitmap bitmap) { // 参数类型 Bitmap
            showBitmap(bitmap);
        }
    });
    
    // 上面的结构使用Lambda表达式，就会变得很清晰！！
    Observable.just("images/logo.png") // 输入类型 String
    .map(filePath -> getBitmapFromPath(filePath)) // 返回类型 Bitmap
    .subscribe(bitmap -> showBitmap(bitmap));
    
    
    
    //flatMap，扁平化Map，将传入的事件对象封装成Observerable,然后进行统一的事件分发。
    
```
&emsp;&emsp;map() 方法将参数中的 String 对象转换成一个 Bitmap 对象后返回，而在经过 map() 方法后，事件的参数类型也由 String 转为了 Bitmap。这种直接变换对象并返回的，是最常见的也最容易理解的变换。不过 RxJava 的变换远不止这样，它不仅可以针对事件对象，还可以针对整个事件队列，这使得 RxJava 变得非常灵活。

### 应用场景
- 获取Token -> 访问接口获取数据 -> 对数据进行逻辑处理 -> 界面更新
- 如果使用传统的回调方式，会有一层层的回调，而且要在不同的线程之间调用。
- 如果用RxJava，看到的是一条流式的处理流程。
- 随着程序逻辑变得越来越复杂，RxJava依然能够保持简洁。
- 使用Lambda，(参数 -> 结果) 的形式，逻辑会更清晰。









