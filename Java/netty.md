### Netty
> Netty is an asynchronous event-driven network application framework 
for rapid development of maintainable high performance protocol servers & clients.  
Netty是一个异步事件驱动的网络应用框架，用于快速开发可维护的高性能服务器和客户端。  
关键词：异步、事件驱动


### 传统IO
&emsp;&emsp;传统IO（BIO）,服务端通信模型：通常在一个循环线程中监听客户端的连接，接收到每个客户端的请求时为之创建一个新的线程进行任务处理，是一请求一应答的通信模型。  
&emsp;&emsp;当客户端并发访问量增加后，服务端的线程个数增加，线程数量快速膨胀，系统的性能将急剧下降。
### 阻塞
```java
/**
* 这里是两个阻塞点
*/
server.accept();    // 等待客户端连接
inputStream.read(); // 连上之后，等待客户端数据
```
### 普通的解决方法
- 使用线程，每次有Client连接时，启动一个线程进行服务。
- 使用线程池，对于短连接的情景，达到线程复用。

### 传统IO带来的问题
- 采用循环等待，如果出现异常可能出现死循环。
- 每个线程只能为一个客户端服务。
- 高并发的场景，线程开销很大，无法满足。

### NIO带来的改进
- 非阻塞的单线程
- 一个线程可以为多个客户端服务
- 基于事件驱动
- 后面补充……

### java nio
一个java nio服务端例子：
```java
    /**
	 * 获得一个ServerSocket通道，并对该通道做一些初始化的工作
	 * 
	 * @param port 绑定的端口号
	 * @throws IOException
	 */
	public void initServer(int port) throws IOException {
		// 获得一个ServerSocket通道
		ServerSocketChannel serverChannel = ServerSocketChannel.open();
		// 设置通道为非阻塞
		serverChannel.configureBlocking(false);
		// 将该通道对应的ServerSocket绑定到port	端口
		serverChannel.socket().bind(new InetSocketAddress(port));
		// 获得一个通道管理器
		this.selector = Selector.open();
		// 将通道管理器和该通道绑定，并为该通道注册SelectionKey.OP_ACCEPT事件,注册该事件后，
		// 当该事件到达时，selector.select()会返回，如果该事件没到达selector.select()会一直阻塞。
		serverChannel.register(selector, SelectionKey.OP_ACCEPT);
	}
```

### Netty Server端
```java
    private void init() {
        // 连接处理group
        EventLoopGroup boss = new NioEventLoopGroup();
        // 事件处理group
        EventLoopGroup worker = new NioEventLoopGroup();
        mServerBootstrap = new ServerBootstrap();
        // 绑定处理group
        mServerBootstrap.group(boss, worker);
        mServerBootstrap.channel(NioServerSocketChannel.class);
        
        // 处理新连接
        mServerBootstrap.childHandler(new ChannelInitializer<SocketChannel>() {
            @Override
            protected void initChannel(SocketChannel sc) {
                // 增加管道任务处理
                ChannelPipeline p = sc.pipeline();
                // 添加过滤器，将传输数据封装成自己的对象，不添加则是默认的ByteBuffer
                p.addLast(
                        new MessageDecoder(),
                        new MessageEncoder(),
                        new NettyServerHandler()
                );
            }
        });
    }

    public static void main(String[] args) {
        try {
            // ServerBootstrap负责初始化netty服务器，并且开始监听端口的socket请求。
            NettyServerBootstrap server = new NettyServerBootstrap();
            server.mServerBootstrap.bind(Const.SERVER_PORT).sync();
        } catch (Exception e) {
            e.printStackTrace();
        }

```


### Netty Server端
```java
    public NettyClientBootstrap(int port, String host) {
        this.host = host;
        this.port = port;
	    init();
    }
    private void init() {
        EventLoopGroup eventLoopGroup = new NioEventLoopGroup();
	    mBootstrap = new Bootstrap();
        mBootstrap.channel(NioSocketChannel.class);
        mBootstrap.group(eventLoopGroup);
        mBootstrap.remoteAddress(this.host, this.port);
        mBootstrap.handler(new ChannelInitializer<SocketChannel>() {
            @Override
            protected void initChannel(SocketChannel socketChannel) {
	            mSocketChannel = socketChannel;
	            mSocketChannel.pipeline().addLast(
	            		new MessageDecoder(),
			            new MessageEncoder(),
			            new NettyClientHandler()
	            );
            }
        });
    }
    public static void main(String[] args) {
        // 初始化的过程和Server对应
        NettyClientBootstrap bootstrap = new NettyClientBootstrap(Const.SERVER_PORT, "127.0.0.1");
        ChannelFuture future = mBootstrap.connect(this.host, this.port).sync();
        
        // 发送消息对象
        bootstrap.sendMessage(new Message());
    }
```


### 心跳检测
- 通过idleStateHandler来检测会话状态
- 心跳就是一个普通的确认请求。
- 心跳对于服务端可以定时清除闲置的会话，释放资源。
- 对于客户端，用来检测是否断开了、是否要重连、计算网络延时。


### 消息流转
- 一个管道中会有多个Handler,不管是MessageEncoder还是Decoder,会发现它们都继承自Handler
- handler往下传递的方法是sendUpstream(event)

### 粘包拆包
- 现象重现：使用StringEncoder发送多个短消息，一次返回多条连在一起的消息。
- 解决方法：自定义消息编解码，长度 + 内容，读取到全部内容才做处理。
- Netty提供的FrameDecoder,使用cumulation缓存，解出一个完整的对象之后才往下传递。
- Netty5里面，FrameDecoder变成了ByteToMessageDecoder
- 避免恶意攻击（故意定义数据长度很长，会造成一直读取），所以需要，限定最大长度，定义一个包头，如果超过就略过，等出现包头才认为是一个包。

---
- Netty版本3\4\5，方法和流程发生了一些变化，网上查资料时注意版本。
- [Netty是什么](https://juejin.im/book/5b4bc28bf265da0f60130116/section/5b4bc28b5188251b1f224ee5)
- [粘包问题](https://blog.csdn.net/a123638/article/details/54377934)