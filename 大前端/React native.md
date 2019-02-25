
## React Native开发环境的配置
1. 安装Homebrew
2. 安装npm和Node.js // npm安装不成功时，[配置镜像](https://blog.csdn.net/csdnear/article/details/79185856)  ，[淘宝镜像](https://npm.taobao.org/)
3. 安装React-native
4. 开发工具：[Nuclide + ATOM](https://blog.csdn.net/nimeghbia/article/details/82381482)
5. Github上下载的项目，在本地执行run-android不识别，需要==npm install==一下，把项目依赖的库下载下来并安装。

## 学习文档
- [官方文档](http://facebook.github.io/react-native/docs/tutorial)   
- [中文文档](https://reactnative.cn/docs/getting-started/)
- http://www.runoob.com/react/react-tutorial.html
- http://caibaojian.com/react

## React
- React 的核心思想是：封装组件。
- 各个组件维护自己的状态和 UI，当状态变更，自动重新渲染整个组件。
- 基于这种方式的一个直观感受就是我们不再需要不厌其烦地来回查找某个 DOM 元素，然后操作 DOM 去更改 UI
- 将 HTML 直接嵌入了 JS 代码里面，这个就是 React 提出的一种叫 JSX 的语法。React 发明了 JSX 让 JS 支持嵌入 HTML 不得不说是一种非常聪明的做法，让前端实现真正意义上的组件化成为了可能。
- Virtual DOM：当组件状态 state 有更改的时候，React 会自动调用组件的 render 方法重新渲染整个组件的 UI。
- 当然如果真的这样大面积的操作 DOM，性能会是一个很大的问题，所以 React 实现了一个Virtual DOM，组件 DOM 结构就是映射到这个 Virtual DOM 上，React 在这个 Virtual DOM 上实现了一个 diff 算法，当要重新渲染组件的时候，会通过 diff 寻找到要变更的 DOM 节点，再把这个修改更新到浏览器实际的 DOM 节点上，所以实际上不是真的渲染整个 DOM 树。这个 Virtual DOM 是一个纯粹的 JS 数据结构，所以性能会比原生 DOM 快很多。


## React定义组件
- 继承Component
- 原生 HTML 元素名以小写字母开头，而自定义的 React 类名以大写字母开头
- 组件类只能包含一个顶层标签，否则也会报错。

## props和state
- state 和 props 主要的区别在于 props 是不可变的，而 state 可以根据与用户交互来改变。
- 容器组件需要定义 state 来更新和修改数据。 而子组件只能通过 props 来传递数据。
- React 里，只需更新组件的 state，然后根据新的 state 重新渲染用户界面（不要操作 DOM，之前的做法是getElementById....）。
- props不能在代码内手动赋值，赋值无效！！this.props.max =100，其实取到的还是之前的。
    

## refs 
相当于给组件起个名字，在其他地方中就可以用这个名字来调用组件了。 
> 尽量不要自己去更新DOM  
this.refs.seekBar.setProgress(Math.round(data.currentTime));


## bind函数，fun.bind(this) 
- 将当前的上下文绑定到函数内部，这样函数内部可以直接使用this了（不然函数内部this是自己的上下文）。
- ES6语法中，使用 =>来自动引入this
- 如果不加bind直接this.onClick()，可能出现在界面加载的时候就执行了onClick，而不是将函数绑定到点击事件。

## Flow
> flow是有facebook推出的JavaScript静态类型检查工具。弱类型语言有个很大的问题，就是一些类型错误引起的bug，可能产品上线后才会被发现。导致很多事故的发生。  
flow很好的解决了JavaScript弱类型引发的一系列问题。对于习惯了强类型语言的我来说，只有借助flow这种类型检查工具，才能找到安全感。这里不对flow的用法进行详细的介绍。只是说一下一些使用的技巧。具体的使用可以查看官方网站    链接：https://www.jianshu.com/p/ccba80f34f33


## 注释
不是所有的地方都可以用 // 注释的。在<View></View>里是不可以使用 // 注释的，不然会报错
>后注释一般用 {/* */}，如果不在任何标签内，可以用 //， } 后注释用 //


## React Navigation 路由导航，
> 坑！版本更新快，网上的例子函数名字和结构都变了，跑不起来。得看英文最新文档,，具体参数[API参考](https://reactnavigation.org/docs/en/navigation-prop.html)

- 通过createStackNavigator来创建路由表、配置跳转后页面信息。
- 在所有页面中可通过this.props.navigation访问到导航对象。
- 通过navigation.navigate('路由名',{携带参数})进行跳转。



## react中父级props改变，更新子级state的多种方法
- 推荐使用：componentWillReceiveProps
- 做到数据驱动界面的变化，而不是自己手动去更新界面。
- 当props发生变化时执行，初始化render时不执行，在这个回调函数里面，你可以根据属性的变化，通过调用this.setState()来更新你的组件状态，旧的属性还是可以通过this.props来获取,这里调用更新状态是安全的，并不会触发额外的render调用


## 踩坑记
- React Native unable to load script from assets...  
发现是由于连接的调试ip并不是对应的电脑，修改后解决。手机调试菜单 -> Dev Settings -> 点击Debug server host & port for device






















