# 学习积累要点
"""
1. git命令
    git --help 帮助命令
    git pull origin master 将远程仓库里面的项目拉下来
    dir  查看有哪些文件夹
    git rm -r --cached Photo\ albums  删除Photo albums文件夹(这里的文件夹名有空格命令行需要用"\ "来拼接）
    git commit -m '删除了Photo albums文件夹t'  提交,添加操作说明


2. 创建Gitbase账号：
        git config --global user.name "username"  创建帐号输入：名字
        git config --global user.email   "email"   创建帐号输入：邮箱

    生成ssh秘钥：
       ssh-keygen -t rsa -C "xxxxx@xxxxx.com"

    查看秘钥：
        cat ~/.ssh/id_rsa.pub
        C:\Users\Administrator\.ssh\id_rsa.pub


3. pycharm 如何更新文档到git
    说明：左侧栏灰色是同步的，红色是本地存在，但没有同步到github里的.

    a. commit
        点击菜单VCS->Commit
    b. 备注更新说明文字
    c. push
        点击菜单VCS->Git->Push
4. 删除github远程仓库的一个文件
     1. 先在本地建一个空文件夹                             git进入到该目录  cd 文件夹名
     2. 初始化文件夹                                       git init
     3. 与origin master建立连接:                           git remote add origin git@github.com:whp5924/sample.git
     4.
     5. 把远程分支拉到本地                                 git fetch origin dev（dev为远程仓库的分支名）
     6. 在本地创建分支dev并切换到该分支                    git checkout -b dev(本地分支名称) origin/dev(远程分支名称)
     7. 把某个分支上的内容都拉取到本地                     git pull origin dev(远程分支名称)
     8. 删除你需删除的文件                                 git rm -r --cached 文件名 (github需要删除的文件)
     9. 删除文件备注信息                                   git commit -m "删除文字备注
     5. 把本地仓库全部发送到远程仓库                       git push -u origin master  把本地仓库全部发送到远程仓库


     ssh -T git@github.com         判断本地git 与github是否连接成功
     git branch -al                查看本地和远程的所有分支
     git branch                    查看本地分支 当前分支用星号* 突出显示
     git branch -a                 查看本地和远程分支
     git branch -r                 查看远程分支
     git branch 本地分支           创建本地分支 如果有相同的分支 fatal: A branch nameed " " already exists.
     git checkout "本地分支'       切换分支
     git checkout -b "本地分支"    创建并切换分支
     git push remote-repo "本地分支"
# 如果拉取成功 没有文件
    git stash                      将本地修改储存起来
    Git pull                       成功
# 如果git push 报错
    git pull --rebase origin master
    git push -u origin master
# 如果pycharm git push 不成功  解决办法，打开你要上传代码的文件夹位置鼠标右键git Bash Here然后直接运行下面的命令解决问题
    方法一：
        git pull
        git pull origin master
        git pull origin master --allow-unrelated-histories
    方法二：
        git pull origin master --allow-unrelated-histories
        git push -u origin master -f

    git clean -dfx 可以直接全部干掉它

    PyQt5-5.14-5.14.1-cp35.cp36.cp37.cp38-none-win32.whl
    pip install PyQt5 -i https://pypy.douban.com/simple
    pip install PyQt5-tools -i https://pypi.douban.com/simple

222222225555555555555555555555

"""


