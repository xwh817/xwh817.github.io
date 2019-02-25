#### 打开文件夹
- Finder -> 顶部菜单，前往 -> 前往文件夹。 
- 波浪符号 (~) 表示您的个人文件夹。

#### 快捷键图标
- ⌘——Command () win键
- ⌃ ——Control ctrl键
- ⌥——Option (alt)
- ⇧——Shift
- ⇪——Caps Lock
- fn——功能键就是fn

#### bash 命令
- pwd 打印当前路径
- open  ./ 用图形界面打开路径


#### 修改环境变量
```
sudo vim /etc/profile
JAVA_HOME="/Library/Java/JavaVirtualMachines/jdk1.8.0_131.jdk/Contents/Home"
export JAVA_HOME
CLASS_PATH="$JAVA_HOME/lib"
PATH=".$PATH:$JAVA_HOME/bin"
source /etc/profile 运行profile配置。
echo $JAVA_HOME  打印环境变量
```
            

#### 权限
- sudo chown -R xwh /usr/local        // 赋予用户xwh对文件夹的权限

