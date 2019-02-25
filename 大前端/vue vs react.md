## 相同点
- 都支持服务器端渲染
- 都有Virtual DOM,组件化开发,通过props参数进行父子组件数据的传递,都实现webComponent规范
- 数据驱动视图
- 都有支持native的方案,React的React native,Vue的weex
## 不同点
- React严格上只针对MVC的view层,Vue则是MVVM模式
- virtual DOM不一样,vue会跟踪每一个组件的依赖关系,不需要重新渲染整个组件树.而对于React而言,每当应用的状态被改变时,全部组件都会重新渲染,所以react中会需要shouldComponentUpdate这个生命周期函数方法来进行控制
- 组件写法不一样, React推荐的做法是 JSX + inline style, 也就是把HTML和CSS全都写进JavaScript了,即'all in js'; Vue推荐的做法是webpack+vue-loader的单文件组件格式,即html,css,jd写在同一个文件;
- state对象在react应用中不可变的,需要使用setState方法更新状态;在vue中,state对象不是必须的,数据由data属性在vue对象中管理