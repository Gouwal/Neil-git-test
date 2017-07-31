# Git基础操作
1. 设置Git的user name and email:<br>
2. 生成 ssh key $ ssh-keygen -t rsa -C "email"<br>
3. 上传key 到 github; 其中复制key的命令为 clip<~/.ssh/id_rsa.pub<br>
4. 测试 ssh-T<br>
5. git init 生成快照并存入项目索引<br>
6. git add  项目索引提交<br>
7. git commit -m "message" 类似于发布<br>
8. git push -u origin master 推送本地更新到github远程<br>
9. git pull origin master 更新远程更新到本地<br>
10. git merge <branch> 把一个分支或某个commit的修改合并到现在的分支上<br>
11. git remote -v 参看远程主机的网址
