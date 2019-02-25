## flux & redux & react-flux
- 参考 [从Flux到Redux，react-redux](https://www.jianshu.com/p/fe53e5fe189d)
> React框架本身只应用于View，如果基于MVC模式开发，还需要Model和Control层，这样催生了Flux的产生，而Redux是基于Flux理念的一种解决方式。  
组建直接传递参数或者事件都需要props一层层代理，对于复杂组件，它可能嵌套的子组件非常多，层级也比较深，那么，如果还采用props链条来维护组件通信或者数据共享，将非常困难，也不利于开发和维护。

### Flux
Flux框架也是一种MVC框架，不同于传统的MVC，它采用==单向数据流==，不允许Model和Control互相引用。Flux框架大致如下：
![Flux框架](https://upload-images.jianshu.io/upload_images/25750-c70caaecac305f9e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/585/format/webp)
- Actions: (type + value)，View中触发的用户行为，如点击事件等。
- Dispatcher: （路由器），接收Actions、执行回调函数。
- Store: （类似MVC中的Model）储存和处理数据（应用状态），一旦发生变动，就提醒Views要更新页面。
- View: 视图，在其中注册监听器，响应store回调更新界面。

原理（[参考](https://www.cnblogs.com/dreamingbaobei/p/8476984.html)）：
- 用户action分散在各个View中直接修改model，逻辑复杂后，页面会越来越难以维护。
- 类似Web后台的http请求，每个请求对应一个url action，将对model的操作进行集中管理和统一响应。
- 当用户在view上的action需要引起Model发生变化时，我们不直接修改model，而是简单地dispatch一个action以表达修改model的意图，这些action将被集中转移给数据端（models），然后数据端会根据这些action做出需要的自我更新。

> 总结一下：从代码层面而言，flux无非就是一个常见的event dispatcher，其目的是要将以往MVC中各个View组件内的controller代码片断提取出来放到更加恰当的地方进行集中化管理，并从开发体验上实现了舒适清爽、容易驾驭的“单向流”模式。

### Redux
相比Flux，Redux有如下两个特点：
1. 在整个应用只提供一个Store，它是一个扁平的树形结构，一个节点状态应该只属于一个组件。
2. 不允许修改数据。即不能修改老状态，只能返回一个新状态。
Redux数据流如下：
![Redux](https://upload-images.jianshu.io/upload_images/25750-4964f23278852286.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1000/format/webp)
不同于 Flux ，Redux 并没有 dispatcher 的概念（Store已经集成了dispatch方法，所以不需要Dispatcher）。它依赖纯函数来替代事件处理器，这个纯函数叫做Reducer。Reducer在Redux里是个很重要的概念，其封装了处理数据的逻辑。

> 纯函数：只要输入相同，无论调用多少次，输出都是一样的。

```javascript
// 定义一个Reducer
export default (state, action) => {
  switch (action.type) {
    case 'INCREMENT':
      return {...state, value: action.value + 1};
    default:
      return state;
  }
}
```
- Store就变得简单了。它的构造函数需要一个reducer对象（每个组件对应一个reducer，通过combineReducers函数合并N个子reducer为一个主reducer）
- View层通过store.dispatch触发动作
- React提供了Context,可以在所有组件中访问到。

#### reducer是什么
> reducer作为一个函数，可以根据web应用之前的状态（previousState）和交互行为（通过flux中提到的action来表征），决定web应用的下一状态（newState），从而实现state端的数据更新处理。这个函数行为和大名鼎鼎的“Map-Reduce”概念中的Reduce操作非常类似，因而称这个函数为“Reducer”。
- 从代码上说，其实就是一个函数，具有如下形式：(previousState, action) => newState，从概念上来说 Redux ＝ Reducer ＋ Flux。
- redux中的reducer机制，可以用来将state端的数据处理过程作“原子化”拆分。redux是来自函数式编程（Functional Programming）的一朵奇葩
- [todoList例子](https://redux.js.org/basics/example)中，在todos的函数体内调用了todo，并将action作为参数原样传递给了todo，这种干净利落地通过函数调用将action由 “parent reducer” 传递给 “child reducer”，是redux实现数据处理拆分的普遍方式。回味一下，我们应该可以体会到，这种数据处理“原子化”拆分的方式和react中view组件的拆分有异曲同工之妙，二者都会形成一种“树状”分流结构（在react的view hierarchy中，数据通过props的直接赋值实现单向流；在redux的reducer hierarchy中，数据通过action的函数传参实现单向流）。


### react-redux
要声明一点，Redux并不是专为React开发的，它可以应用在任何框架上。针对React工程，可以使用react-redux库帮助我们更快，更便捷得搭建Redux工程，让代码更加精简。react-redux库提供了如下功能：

1. 把组件拆分为容器组件和傻瓜组件，使用者只需要写傻瓜组件；
2. 使用React的Context提供了一个所有组件都可以直接访问的Context，即react-redux Provider；

于是，我们不需要自己写顶层组件了，只要导入react-redux的Provider


## 总结
俯瞰一下整个开发流程：
- 首先，react框架为我们理顺了 store --> view 的“单向”工作流（store是state的容器）；
- 然后，redux框架为我们理顺了 view --> store 的**“单向”**工作流。
- 并且，react和redux都以组件化的形式可以将各自负责的功能进行灵活地组装或拆分，最大程度上确保我们“一次只需要专注于一个局部问题”。
- 具体来说，分为以下步骤：

1. 单例store的数据在react中可以通过view组件的属性（props）不断由父模块**“单向”**传递给子模块，形成一个树状分流结构。如果我们把redux比作整个应用的“心肺” （redux的flux功能像心脏，reducer功能像肺部毛细血管），那么这个过程可以比作心脏（store）将氧分子（数据）通过动脉毛细血管（props）送到各个器官组织（view组件）
2. 末端的view组件，又可以通过flux机制，将携带交互意图信息的action反馈给store。这个过程有点像将携带代谢产物的“红细胞”（action）通过静脉毛细血管又泵回心脏（store）
3. action流回到store以后，action以参数的形式又被分流到各个具体的reducer组件中，这些reducer同样构成一个树状的hierarchy。这个过程像静脉血中的红细胞（action）被运输到肺部毛细血管（reducer组件）
4. 接收到action后，各个child reducer以返回值的形式，将最新的state返回给parent reducer，最终确保整个单例store的所有数据是最新的。这个过程可以比作肺部毛细血管的血液充氧后，又被重新泵回了心脏
5. 回到步骤1

用图示的方式来表达，即：
![image](https://pic4.zhimg.com/80/1f81a280ccdbedf6a3c6757f7ff4d9c7_hd.jpg)

## 参考
- [Flux 架构入门教程（阮一峰）
](http://www.ruanyifeng.com/blog/2016/01/flux.html)
- [从Flux到Redux，react-redux](https://www.jianshu.com/p/fe53e5fe189d)
- [理顺react，flux，redux这些概念的关系](https://www.cnblogs.com/dreamingbaobei/p/8476984.html)