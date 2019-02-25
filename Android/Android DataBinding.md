### Android DataBinding
https://www.jianshu.com/p/0fe0b6b7dae1
> Google官方提供的一个MVVM数据绑定框架。（MVVM: ModelView View Model）  
DataBinding在Web开发中已经很普遍，因此借鉴了Web端成熟的经验，其语法与使用方式都和JSP中的EL表达式非常类似。  
解决了Android UI 编程的一个痛点。

### DataBinding其主要优势
- 官方原生支持 MVVM 模型可以让我们在不改变既有代码框架的前提下，非常容易地使用这些新特性；
- 去掉Acitivity和Fragments中更新UI数据的代码，让业务逻辑和UI代码分离；
- XML成为UI数据的唯一真实来源；
- 减少定义view id，不必使用findViewById();
- 充分考虑了性能因素，高效的绑定和更新数据；
- 更安全，在编译时会发现由于错误的ID而引起的Errors；
- 保证代码在主线程更新界面；

### 类似第三方库
在DataBinding推出之前，市面上已经有类似的第三方库在被使用，比如：
- ButterKnife;
- Android Annotations;
- RoboBinding;

### 双向绑定：
- 把后台的数据绑定到前台显示出来，前台显示的数据改变也会自动影响后台的数据。




