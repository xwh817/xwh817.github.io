
# 参考：
- [自定义View和ViewGroup](https://www.jianshu.com/p/7a77bfd0680a)
- [我的Test例子](https://github.com/xwh817/ViewTest/blob/master/app/src/main/java/xwh/demo/view/MyViewGroup.java)

# View树的绘制流程、树形的递归执行
- measure -> layout -> draw

# MeasureSpec 测量规格
- 整数32位，前2位是模式，后30位是对应模式下的测量值。

# View的3种测量模式
- EXACTLY：父view已经强制设置了子view的大小。一般是子View为match_parent和固定值；
- AT_MOST：表示子布局被限制在一个最大值内。一般是子View为wrap_content时；
- UNSPECIFIED：父view对子view没有任何限制，子view可以是任何大小。

# onMeasure
- View或者ViewGroup用来测量并设置自己的大小。
- 需求根据定义的测量模式来计算，
- 例如widthMode == MeasureSpec.EXACTLY时，（当在布局中指定了宽度为match_parent或是固定值），不用计算了，直接使用指定的值。


# onLayout(boolean changed, int l, int t, int r, int b)
- 指定子View的位置，参数是当前View在其父控件中的位置（由父控件指派的）

# invalidte 和 requestLayout 的区别
-  invalidate，重新绘制，在自定义View中体现为触发了onDraw方法。
-  requestLayout，请求重新布局view，但不会触发draw方法。


# 事件分发机制： 其实就是为了确定触摸事件到底有谁去处理。
三个方法：
-  dispatchTouchEvent               分发
-  onInterceptTouchEvent         拦截
-  onTouchEvent                          处理  
> 经典的责任链设计模式：
- 从顶层View开始向下分发、子View判断是否拦截、如果拦截了就处理。
- 如果子View没有拦截处理，那么事件就返回给父View，如果都没处理才丢掉。
- 体现出来的是，界面上层的View会优先相应事件，子View可以决定是否消耗掉事件。  
> 默认情况下，执行顺序：
- Parent : dispatchTouchEvent
- Parent : onInterceptTouchEvent
- Child : dispatchTouchEvent
- Child : onTouchEvent
- Parent : onTouchEvent

> [link](https://www.cnblogs.com/linjzong/p/4191891.html)  
ViewGroup的dispatchTouchEvent是真正在执行“分发”工作，而View的dispatchTouchEvent方法，交给了onTouchEvent去处理。
当某个View或者ViewGroup的onTouchEvent事件Acition_Down返回true时，便表示它是真正要处理这次请求的View，之后的Aciton_UP和Action_MOVE将由它处理。当所有子View的onTouchEvent都返回false时，这次的Touch请求就由根ViewGroup，即Activity自己处理了。
onInterceptTouchEvent有两个作用：1.拦截Down事件的分发。2.中止Up和Move事件向目标View传递，使得目标View所在的ViewGroup捕获Up和Move事件。



# GestureDetector 手势
简单的事件可以通过setOnTouchListener进行处理。onTouch(View v, MotionEvent event)  
复杂的事件，需要使用GestureDetector，进行手势处理。
- this.mGestureDetector = new GestureDetector(mContext, this.onGestureListener);
- 在onTouch事件时返回：return mGestureDetector.onTouchEvent(event);
- 由OnGestureListener去处理手势。
- 有个已经封装好的：SimpleOnGestureListener implements OnGestureListener, OnDoubleTapListener,
- 已经对双击等等做了处理回调。





