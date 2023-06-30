# SMTP-mail-sender
A small application for computer networking

SMTP纵横天下邮件发送客户端
使用自己生成的ssl证书进行加密
实现用文件保存信息

图形化界面采用Qt Designer工具设计
用工具自动生成py文件

主要功能：
1.SSL加密
2.保存和加载草稿箱（仅能保存一份）
3.保存和载入用户名与密码（仅能为一个用户提供保存）
4.群发，利用分号隔开
5.查看联系人列表，按按钮自动为当前发送的对象生成联系人表。加号打开联系人文件，可以复制粘贴
（接下来可以在表内每行各加一个分号，方便群发。操作不难。是可以改进的点。我自己想到了。暂时没有实现。）
6.查看已发送。每次发送的头部有发送时间，精确到秒

因草稿箱有bug，故后面重新修复之后补录了草稿箱操作。

截图是谷歌邮箱，表示我的是加密邮件。另一份是我故意取消加密代码后发送的，不显示加密。
