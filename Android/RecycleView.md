### 相比较ListView,GridView
- 更灵活，可自定义LayoutManager进行子元素布局。
- 默认ViewHolder（adapter构造时范性定义）。ListView需要自己定义，还得用setTag来绑定。结构清晰，特别是对于多种子样式。
- 优秀的垃圾回收机制。
- 可指定部分元素更新，以及更新动画。

> RecycleView只关心元素怎样回收和复用，不关心元素位置，怎样布局，间隙。分给其他类去处理:
Adapter，泛型dnViewHolder
LayoutManager：子元素布局
ItemDecoration：子元素间距
ItemAnimator：增删改动画设置


> 关于RecyclerView你知道的不知道的
- https://www.jianshu.com/p/aff499a5953c
- https://www.jianshu.com/p/311df8be8633


### snapHelper
>SnapHelper是一个抽象类，官方提供了一个LinearSnapHelper的子类，可以让RecyclerView滚动停止时相应的Item停留中间位置。25.1.0版本中官方又提供了一个PagerSnapHelper的子类，可以使RecyclerView像ViewPager一样的效果，一次只能滑一页，而且居中显示。
https://www.jianshu.com/p/e54db232df62


#### 自定义RecycleView布局
https://www.jianshu.com/p/715b59c46b74
- 自定义LayoutManager主要要求我们完成三件事情：
- 计算每个ItemView的位置；
- 处理滑动事件；
- 缓存并重用ItemView；