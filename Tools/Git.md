## Git的四个区、五种状态
#### 四个区
1. 工作区(Working Area)
1. 暂存区(Stage)
1. 本地仓库(Local Repository)
1. 远程仓库(Remote Repository)
#### 五种状态
1. 未修改(Origin)
1. 已修改(Modified)&未追踪(Untracked)
1. 已暂存(Staged)
1. 已提交(Committed)
1. 已推送(Pushed)
 
![image](http://gzdaijie.coding.me/imtuzi-blog-posts/git/img/git-four-areas-five-states.png)

#### 操作撤销
处于不同的status,操作也不同。
- 已修改，但未暂存：checkout
- 已暂存，未提交：reset
- 已提交，未推送：reset
- 已推送到远程: revert
> reset参数：  
    --mixed会保留源码,只是将git commit和index 信息回退到了某个版本.  
    --soft(默认)保留源码,只回退到commit   信息到某个版本.不涉及index的回退,如果还需要提交,直接commit即可.  
    --hard源码也会回退到某个版本,commit和index   都回回退到某个版本.(注意,这种方式是改变本地代码仓库源码)

## 基本概念
### 仓库
- origin是指向这个远程代码库的标签，==origin不是分支，是仓库标签==。[参考](https://www.zhihu.com/question/27712995/answer/39946123)
- master是默认创建的第一个==分支==
- git remote -v 可以查看到远程仓库标签。

### 分支
- git checkout -b temp origin/master    // 基于远程仓库新建分支temp,并切到该分支
- git ls-remote origin // 查看所有tag和分支
- git ls-remote --heads origin
- git branch -d xxxxx    // 删除本地分支
- git push origin --delete Chapater6   // 删除远程分支Chapater6

### tag
- git tag -a 20160108_v1.0.3 // 新建tag
- git tag 查看tag
- git push origin tagName 推送本地tag到远程仓库
- git tag -d tagName 删除tag
- git ls-remote --tags origin     // 查看远程tag
- git fetch origin --tags         // remote tags are fetched
- git fetch origin tag <tagname> # 获取某个远程tag
- git push origin --delete tag 20170220_1.2.0 // 删除远程tag




## 常用操作
- git --help push        // 查看帮助
- git reflog        // 查看历史记录
- git checkout . && git clean -df   // 放弃本地所有修改包括新增的文件
> git clean是从工作目录中移除没有track的文件  
    通常的参数是git clean -df  
    -d表示同时移除目录,-f表示force,因为在git的配置文件中, clean.requireForce=true,如果不加-f,clean将会拒绝执行.

- 撤销commit --amend
> [【参考】](https://segmentfault.com/a/1190000014272359)如果只 amend 了一次, 那么直接用 git reset HEAD@{1} 就可以撤销这次 amend. 
如果 amend 多次, 就参考 git reflog，找到amend之前最后一个HEAD{}进行撤销.


- cherry-pick 挑选其他的分支进行合入
- git rebase -i HEAD~3  当前版本的倒数三次提交，进行修改或合并。
> 这个命令出来之后，会出来三行东东：  
如果你要修改哪个，就把那行的pick改成edit，然后退出。  
修改之后：git rebase --continue

- 更新代码
1. fetch    // 获取远程代码到缓存区
2. rebase   // 更新工作目录代码
3. merge    // 合并分支
2. pull = fetch + merge
>  pull origin master:test  // 拉取远程主机origin的master分支合并到本地test分支



#### rebase和merge区别： 
- git rebase提取操作有点像git cherry-pick一样，执行rebase后依次将当前的提交cherry-pick到目标分支上，然后将在原始分支上的已提取的commit删除。
- merge的效果，简单来说就合并两个分支并生成一个新的提交。（被合并的分支记录依然在）
1. 可以看出merge结果能够体现出时间线，但是rebase会打乱时间线。 
2. 而rebase看起来简洁，但是merge看起来不太简洁。 
3. 最终结果是都把代码合起来了，所以具体怎么使用这两个命令看项目需要。
4. 


#### 暂存代码
1. stash
```
git stash // 保存当前工作
git stash list // 查看
git stash pop // 恢复
```
2. 临时commit
```
git commit -m "temp"
git reset --soft(默认) HEAD~1 回退刚才的一个commit
```