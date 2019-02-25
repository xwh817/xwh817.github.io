# 处理流程
- NativeCrash会在控制台输出C里面的堆栈，但是又没有具体的代码位置。
- 要查看c/c++的堆栈信息就要使用到源码环境里的==addr2line==工具（prebuilts/tools/gcc-sdk）。

> addr2line -fe  libstagefright “/out/target/product/appassionato/symbols/system/lib/libstagefright.so” 000df22b

- 当使用完上述命令，便会输出详细的代码出错位置。
- 找到出错位置，根据crashlog显示的提示进行定位。