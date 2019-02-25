### 资源
- [Python2 基础教程](http://www.runoob.com/python/python-tutorial.html)
- [Python3 基础教程](http://www.runoob.com/python3/python3-tutorial.html)
- [Python教程 廖雪峰](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000)
- [在线代码学习](https://www.imooc.com/learn/177)

### Python
- Python的哲学就是简单优雅，尽量写容易看明白的代码，尽量写少的代码。
- 那Python适合开发哪些类型的应用呢？  
首选是网络应用，包括网站、后台服务等等；
其次是许多日常需要的小工具，包括系统管理员需要的脚本任务等等；
另外就是把其他语言开发的程序再包装起来，方便使用。

### 语法
- 动态语言：变量本身类型不固定，同一个变量可以反复赋值，而且可以是不同类型。
- 为Python把0、空字符串''和None看成 False，其他数值和非空字符串都看成 True
- Python代码的缩进规则。具有相同缩进的代码被视为代码块
- 布尔运算：and or
- 命名：以下划线开头的标识符是有特殊意义的，单下划线（不能直接访问的类属性性）、双下划线（类的私有成员）、双下划线开头和结尾代表 Python 里特殊方法专用的标识
- 注释：单行#、多行'''三个引号
- 行尾不用分号，同一行多条语句使用分号分割，一长行语句分行显示 使用 \ 连接。
- 字符串
```python
    # 字符串输入
    name = input('please input your name:')
    no = int(input('your no:'))     # 输入并且类型转换
    
     # 格式化输出
    print("name: %s, no: %d" % (name, no))
```
- 列表，有序集合 **list** []
```python
    L = ['Adam', 'Lisa', 'Bart']
    print L[2]    # 打印Bart
    print L[-1]    # 打印倒数第一个
    L.append('Paul')    # 追加元素
    L.insert(0, 'Paul')    # 插入
    L.pop()    # 删除最后一个
    L.pop(2)    # 删除指定位置元素
    L[2] = 'Paul'    # 替换元素
    
    List切片 L[from:to:step]
        L = range(1, 100)
        L[2:50:3]     # 取出小于50的3的倍数
```
- 元祖，固定的有序列表 **tuple** ()
```python
    # tuple没有 append()方法，也没有insert()和pop()方法。
    t = ('Adam', 'Lisa', 'Bart')
    t = ('Adam',)    # 只用一个元素的时候
```


-  ==for循环==
```python
    L = ['Adam', 'Lisa', 'Bart']
    for name in L:
    print name
    
    # Python中没有i++的表达式
```

- dict 字典 键值对 {'key':value}
```python
    d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59
    }
    
    for key in d:
    ... print key
    
    if 'Paul' in d:
    print d['Paul']
    print d.get('Paul')
```

- set 集合
```python
# 没有重复，而且是无序的
    s = set(['A', 'B', 'C'])
    s.add('D')
    s.remove('B')
    # 没有get(2)，因为是无序的，不能通过下标访问。
```


- 函数
```python
    def my_abs(x):
     ...
     # return x, y 函数可以返回多个值（其实是一个tuple）
     # 可变参数，*args
     def fn(*args):
         print args
         
         
```

- 导入导出
```python
    # 普通导入
    import 模块名
    # 使用的时候
    模块名.函数名
    
    # 部分导入
    from 模块名 import 函数名
    
    # 全部导入
    from 模块名 import *
  
```

- Ubuntu下面切换python版本：
```
    update-alternatives # 查看可替换版本
    cd /usr/bin    ls |grep python  # 查看本机已安装的python
    
    # 设置各版本优先级
    update-alternatives --install /usr/bin/python python /usr/bin/python2.7 1
    update-alternatives --install /usr/bin/python python /usr/bin/python3.5 2

```

- pylint误报的问题
> 误报：在当报错的对象是动态创建的，并且确实是在访问的同时已经存在的时候pylint仍然会报错。  
解决办法
在代码的开头加上注释：# pylint: disable=no-member

- [anaconda](https://www.jianshu.com/p/eaee1fadc1e9) 是一个开源的包、环境管理器，可以用于在同一个机器上安装不同版本的软件包及其依赖，并能够在不同的环境之间切换。

- 闭包：内层函数引用了外层函数的变量（参数也算变量），然后返回内层函数的情况，称为闭包（Closure）。