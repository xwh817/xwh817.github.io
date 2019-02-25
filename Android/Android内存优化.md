
#### 内存优化
- 通过代码可以获取App运行过程中分配的最大内存、分配内存、使用内存、空闲内存。。。
- 使用Android Monitor获取图形化的内存使用情况。

#### App内存优化方法
1. 数据结构优化
- 例如使用StringBuilder而不是字符串相加，后者会产生中间对象。
- 使用ArrayMap、SparseArray替换HashMap。
- 避免内存抖动，短时间申请了很多临时对象，然后又不用了。体现为锯齿形波动。场景：在循环体内不断新建临时对象。
2. 对象复用
- 复用系统自带的资源。
- ListView/GridView中ConvertView复用。
- 自定义View时，避免在onDraw中新建对象，例如新建Paint
3. 避免内存泄漏
- Activity被长生命周期对象持有（静态变量、有耗时任务的Handler、循环执行的对象）。
- Handler泄漏原理：内部类会默认持有所在的对象（Activity）。
- 如果要使用上下文Context，使用ApplicationContext，而不是Activity。
- 数据库Cursor对象及时关闭。

#### OOM问题优化
- 内存泄漏，使用软引用、大对象及时置空。
- 大量图片加载，缩放比例、解码格式、局部加载（不影响视觉效果，太大的图片浪费，针对屏幕最大宽度做缩放）。
- jpg文件只有1Mb，可是转成Bitmap在内存中可能就20多Mb了。
- BitmapFactory.Options 设置比例、加载区域等等参数设置。


#### 强引用、软引用、弱引用
- 强引用只要被其他对象持有，就不是垃圾，就不能被回收。因此不使用时及时置空。
- SoftReference<T>对对象进行包装，运行过程中内存不足时优先被回收。




#### 查看进程内存使用情况
```
dumpsys meminfo com.turingcat.controller
Applications Memory Usage (kB):
Uptime: 7028791 Realtime: 7028791

** MEMINFO in pid 5429 [com.turingcat.controller] **
                   Pss  Private  Private  Swapped     Heap     Heap     Heap
                 Total    Dirty    Clean    Dirty     Size    Alloc     Free
                ------   ------   ------   ------   ------   ------   ------
  Native Heap    45077    45024        0        0    71540    52261      274
  Dalvik Heap    32442    32324        0        0    33988    29050     4938
 Dalvik Other     8864     8628        0        0
        Stack     1648     1648        0        0
       Ashmem      132        0        0        0
    Other dev       13        0       12        0
     .so mmap    21267     9956    10192        0
    .apk mmap      983        0      620        0
    .ttf mmap      579        0      232        0
    .dex mmap    18758     1408    12916        0
   Other mmap      304        4      224        0
      Unknown      412      412        0        0
        TOTAL   130479    99404    24196        0   105528    81311     5212

 Objects
               Views:      618         ViewRootImpl:        3
         AppContexts:       13           Activities:        2
              Assets:        2        AssetManagers:        2
       Local Binders:       64        Proxy Binders:       40
    Death Recipients:        1
     OpenSSL Sockets:        1

-------------------------------------
// 查看系统配置
$ cat /system/build.prop | grep dalvik.vm
...
dalvik.vm.heapstartsize=16m
dalvik.vm.heapgrowthlimit=192m
dalvik.vm.heapsize=512m
dalvik.vm.heaptargetutilization=0.75
dalvik.vm.heapminfree=512k
dalvik.vm.heapmaxfree=8m
...

碰到加载图片OOM的问题，解决方法 set prop dalvik.vm.heapminfree 2m  
原因是heapminfree太小了，突然加载图片直接崩溃。

```
#### dalvik与GC相关的属性有：

- dalvik.vm.heapstartsize：初始化dalvik分配的内存大小。
- dalvik.vm.heapgrowthlimit：没有在mainfest中设置android:largeheap="true"时，应用的最大内存，超过这个值会有OOM产生。
- dalvik.vm.heapsize：在mainfest中设置android:largeheap="true"时，应用的最大内存，超过这个值会有OOM产生。
- dalvik.vm.heaputilization、dalvik.vm.heapminfree 、dalvik.vm.heapmaxfree：dalvik GC时使用的参数。

dalvim GC策略是：
1. 在一次GC后，根据当前Heap中已分配的内存大小除以dalvik.vm.heaputilization(0.75),得到一个目标值。
2. 如果目标值不在（已分配的值+dalvik.vm.heapminfree）到（已分配的值+dalvik.vm.heapmaxfree）这个区间，即取区间边界值做为目标值(运行一段时间后第1步得到的目标值肯定会超过这个范围)。
3. 虚拟机记录这个目标值，当做当前允许总的可以分配到的内存。同时根据目标值减去固定值（200~500K),当做触发GC_CONCURRENT事件的阈值。
4. 当下一次分配内存，分配成功时。重新计算已分配的内存大小；若有达到GC_CONCURRENT的阈值，则产生GC。
5. 当下一次分配内存，开始分配失败时。则会产生GC_FOR_ALLOC事件，释放内存；然后再尝试分配。

可以通过调整dalvik.vm.heapminfree 和dalvik.vm.heapmaxfree属性的值，减少GC_FOR_ALLOC和GC_CONCURRENT的次数，如果这两个值设置的过大，则会导致一次GC的时间过长，从而会看到明显的卡顿现象，设置的值既要使GC的次数减少，也不能是一次GC的时间过长。



#### 程序中获取内存信息：
```java
	private void dumpMemoryInfo() {
		final ActivityManager activityManager = (ActivityManager) mContext.getSystemService(ACTIVITY_SERVICE);
		ActivityManager.MemoryInfo info = new ActivityManager.MemoryInfo();
		activityManager.getMemoryInfo(info);
		Log.i(TAG, "系统剩余内存:" + getFormatSize(info.availMem) + "， 当前是否处于低内存运行：" + info.lowMemory + "当系统剩余内存低于" + getFormatSize(info.threshold) + "为低内存运行");
		
		String maxMemory = getFormatSize(Runtime.getRuntime().maxMemory());
		String totalMemory = getFormatSize(Runtime.getRuntime().totalMemory());
		String freeMemory = getFormatSize(Runtime.getRuntime().freeMemory());
		Log.i(TAG, "当前应用---> 最大可分配内存=" + maxMemory + ", 当前已分配=" + totalMemory + ", 剩余=" + freeMemory);
	}
	
	private String getFormatSize(long size) {
		return Formatter.formatFileSize(mContext, size);
	}
```

---
- 使用Android Studio MAT(Memory Ala Tools)分析内存泄漏 [参考](https://blog.csdn.net/junhuahouse/article/details/79731529)
- 使用Android Profiler [参考](https://www.jianshu.com/p/bdfd2a6b2681)，比之前的MAT更加方便，不用导出hprof文件。


- ...Android\sdk\tools\monitor.bat 打开之前的Android Device Monitor

- 参考
https://www.cnblogs.com/linguanh/p/8496002.html
- [系统配置dalvik与GC相关的属性](https://blog.csdn.net/oujunli/article/details/12649017 )，
- [Android性能调优篇之探索JVM内存分配](https://www.cnblogs.com/ldq2016/p/8036464.html)