> FFmpeg的名称来自MPEG视频编码标准，前面的“FF”代表“Fast Forward”，FFmpeg是一套可以用来记录、转换数字音频、视频，并能将其转化为流的开源计算机程序。

## 参考
- [视音频编解码技术零基础学习方法](https://blog.csdn.net/leixiaohua1020/article/details/18893769)
- [FFmpeg基本术语概念](https://blog.csdn.net/qq_36688143/article/details/79162121)
 

## 视频笔记
### FFmpeg 编译
```
    # 得到的ffmpeg开源库，之后还需要编译得到可用的工具。
     git clone https://github.com/FFmpeg/FFmpeg.git
     # 查看编译配置参数、命令查询
     ./configure --help 
     # 设置编译结果的目录，这里还可以带上其他的编译配置
     ./configure --prefix=/media/xwh/Work/Code/FFmpeg/mkDefault 
     注：中途出现没有权限的错误提示时，使用sudo+命令
     
     # 编译，然后安装。将编译结果保存在前面配置的prefix目录下面。
     make && make install
     
     # 配置编译生成ffplay
```
- [ffmpeg configure配置选项](https://blog.csdn.net/momo0853/article/details/78043903)
- 遇到ffmpeg依赖的so文件找不到[参考](https://www.cnblogs.com/CoderTian/p/6655568.html) ，或者把ffmpeg相关的命令和库配置到[环境变量](https://blog.csdn.net/NCTU_to_prove_safety/article/details/70851634)。
    
    
### 各种ffmpeg命令
[参考](https://www.cnblogs.com/dwdxdy/p/3240167.html)
- 查询
- 录制
- 复用与分解（解复用），视频音频的抽取、转换
- 原始数据提取，YUV、PCM数据
- 滤镜，对解码后的数据进行过滤处理然后再编码输出。
- 裁剪与合并，

### FFmpeg代码结构(子模块)
- libavcodec            编解码器
- libavformat          多媒体文件流协议、容器格式
- libavutil                 包括了hash器、解码器和各种工具
- libavfilter              特效处理
- libavdevice           各种破获设备和回放设备接口
- libswresample      混音和重采样
- libswscale              色彩转换和缩放功能

### FFmpeg日志系统
```
     include<libavutil/log.h>
     av_log_set_level     // 设置日志级别AV_LOG_ERROR、WARNING、INFO...
     av_log(...)
```
### 文件操作，删除、移动、重命名...
    include<libavformat/avformat.h>
### 目录操作，打开、读取、关闭


### 多媒体文件基本概念
- 多媒体文件是个容器
- 很多流（Stream/Track），不同的编码器编码
- 从流中读取的数据称为包
- 包里面是一帧一帧
- 
- AVFormatContext     文件上下文、格式（复用）
- AVStream     流
- AVPacket     包
- AVFrame     帧

### 操作流数据的基本步骤
解复用     获取流     读取数据包     释放资源

### 抽取多媒体文件中的音频、视频数据
### 格式转换，读取不同的流，然后写入新的流。

### 使用ffmepeg进行h264编码
- 查找编码器
- 设置编码参数：视频分辨率、帧率、时间基、多久一个i帧p帧
- 编码：for循环一秒钟（帧率）进行编码

### 将视频转成图片
- formatContext -> 找到解码器
- 找到视频流 -> 读取数据包
-  -> 使用解码器读取到帧 -> 将帧保存为图片

### AAC编码
- 音频编码器，avcodec_find_encoder_by_name("libfak_aac")
- 设置参数，采样格式、采样率rate、声道channel及个数
- 使用编码器编码

### SDL (Simple DirectMedia Layer)
- 由C语音实现的跨平台的媒体开源库，用于游戏、模拟器、媒体播放器等多媒体应用。
- SDL下载、make、编译、安装。流程和FFmpeg的流程一样的。
- SDL基本步骤：初始化，创建窗口Window，渲染器Render，展示数据RenderPresent，销毁，退出。

### 纹理渲染
- 纹理（Texture）是一系列描述信息，占很少的主内存。
- 计算在GPU上进行的，加速图像的渲染。
- 内存图像 经过渲染器生成 纹理 交换给显卡 进行展示
- 格式：YUV、RGB

### 实现YUV播放器
- 创建线程，控制更新纹理、刷新速度。
- SDL更新纹理，SDL_UpdateTexture()、UpdateYUVTexture

### 音频播放
- 打开音频设备，设置音频参数（采样率、通道...）,向声卡发数据，播放，关闭。
- 声卡向你要数据，而不是你主动推给声卡。
- 声卡触发回调函数，把PCM数据取过去。
- 数据多少是由音频参数决定的
- SDL_OpenAudio、PauseAudio、MixAudio

### PCM播放器
- 初始化SDL_INIT_AUDIO，打开文件，分配缓冲区，
- SDL_AudioSpec设置音频参数（采样率、通道数、格式）、回调函数（用于取数据）
- 从文件读取数据放到我们自己的缓冲区，如果还有数据就等待。（单次的生产者/消费者）
- 在回调函数中，把我们自己缓冲区中的数据复制到SDL缓冲区。
    
### 播放器的核心功能开发
- FFmpeg和SDL结合：FFmpeg解码 + SDL渲染
- 多线程thread与锁mutex

