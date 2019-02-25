
#### java遍历Map [参考](https://www.cnblogs.com/imzhj/p/5981665.html)
```java
推荐的方式：
    // java8之后新增Lamda表达式    
    mMap.forEach((key,value) -> { ...key...value})
    // entry迭代    
    for(Map.Entry entry : mMap.entrySet()) {
        entry.getKey()
        entry.getValue()
    }
```

#### java可变参数 Object... args
```java
    public static void test(Object... args) {
        System.out.println("args:" + args.length);
    }
    test(1,2,"3");  // 返回3
    test();         // 返回0，不会报NullPointException
    
```


#### 垃圾回收算法
- 引用计数器
- GCRoot链可达