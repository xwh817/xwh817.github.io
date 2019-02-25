## Shell
下面是遍历目录下的文件夹，然后将子文件夹中的m3u8片段文件合并
命令不知道就搜[参考文档](http://www.runoob.com/linux/linux-shell-variable.html)，现学现用。
- 在shell代码里面执行shell命令，使用反单引号（和～一起的）`cd dir...`，注意不是字符串单引号。
- 使用grep+正则过滤结果

```
    #!/bin/bash
    files=`ls | grep '^[0-9]'`
    for file in $files
    do
        echo $file
        `./file.sh $file`
    done

    #!/bin/bash
    files=`ls $1 | grep '^[0-9]'`
    count=0
    for file in $files
    do
        ((count++))
    done
    
    i=0
    while [ $i -lt $count ]
    do
        cat ''$1'/'$i'' >> 'output/'$1'.mp4'
        ((i++))
    done
```


