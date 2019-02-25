### 参考
- [一个查看例子的好网站](https://try.kotlinlang.org)

### 语法
#### when
依次匹配每个条件、直到有符合的并跳出（后面的条件不再去匹配）
```
fun cases(obj: Any) {
  when (obj) {
      1 -> println("One")
      "Hello" -> println("Greeting")
      is Long -> println("Long")
      !is String -> println("Not a string")
      else -> println("Unknown")
  }
}
```
#### for
```
    // 获取index
    for (i in args.indices)
        println("$i = ${args[i]}")

    // 遍历Map
    for ((key, value) in map) {
        println("key = $key, value = $value")
    }
```

#### Array、List
```
    // 各种新建方式
    var arr = arrayOf(1, 2, "3")
    var list = listOf<String>("a", "b", "c")
    val array = arrayListOf<String>()
    var arr = Array(5, {i -> i*2})
    
    if ("aaa" in array)
    if (x !in 0..array.size - 1)
```