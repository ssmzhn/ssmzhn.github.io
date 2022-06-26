---
layout: posts
title: Termux 使用指南
date: 2022-06-25 16:50:50
tags:
  - 随笔
---

很多时候我们会遇到这种情况：

> 某群里大佬：快来试试这串代码，github.com/1145141919810...
> 我：这东西干嘛的？
> 大佬：你运行了就知道了（

但你身边没有电脑，怎么办呢？于是你摸出了手机，打开了龟速的 GitHub，等待着下载进度条缓缓走完。然后你打开酷安，搜索一个手机能用的编译器 App，打开源代码，编译，运行。

可是大多数这类软件不仅画风犹如三星堆出土，而且手感稀烂，贼鸡儿难用，况且 GitHub 网页在中国大陆的体验并不是太好（即使您可以用 fastgit, [GitHub520](https://github.com/521xueweihan/GitHub520) 之类的工具优化加载速度），这时，一个趁手的软件就显得极为重要，它就是 [Termux](https://termux.com)。

# 使用前提

1. 一双巧手
2. 对 Linux 有初步了解
3. 手机剩余存储空间最好 ≥ 8GB
4. 一点耐心

# 安装

Termux 是一款 Android 终端模拟器和 Linux 环境应用程序，无需 root 或设置即可直接运行。

您可以在 [GitHub](https://github.com/termux/termux-app/releases) 或 [F-Droid](https://f-droid.org/en/packages/com.termux/) 里直接下载安装包安装。

<div class="warning">

> 不要在 Google Play 或酷安下载 Termux！它们的 Termux 版本太低，已经停止维护。

</div>

# 配置

Termux 可玩性非常高，本文只给出一种建议选择，供大家参考。

## 换源

输入 
```shell
termux-change-repo
```

会出现以下的画面：
[![termux-change-repo](https://s1.ax1x.com/2022/06/25/jkNhX8.jpg)](https://imgtu.com/i/jkNhX8)

此时按箭头键，选择 `Mirrors in China`，按下空格键，使前面的 `( )` 中带 `*`，回车继续，接下来会自动更新软件包。

当出现 `Do you want to continue? (y/N)` 时，输入 `y` ，按回车继续，等待跑完。此时保持网络畅通，您的软件包就更新完辣！

## 必备软件包

### Git

强大的版本控制系统！它可以让您方便地管理代码，背后还有 GitHub 作为生态。使用该工具能帮您轻松使用 GitHub，使用方法敬请百度。

输入

```shell
pkg install git -y
```

或

```shell
pkg i git -y
```

来安装 Git。

> 此处的 `install` 可以换成 `i`，以后不再赘述。
> 关于 `pkg` 指令，下文介绍。

### 编辑器
为了方便地编辑文本文件而不是到 Termux 外再找个程序编辑，请务必安装一个终端编辑器。

Termux 上的编辑器有很多，任选其一即可。我个人用 `vim` 习惯了，但仁者见仁，智者见智。

常用的编辑器：

 - vi
 - vim
 - nvim
 - emacs
 - nano

### 编译/解释器

把 Workflow 丢到命令行上，从此告别繁杂的编译器 App！

直接使用

```shell
pkg i <软件包> -y
```

即可，软件包与 Debian 几乎一样。

如：

| 软件包 | 说明                      |
| :-------: |:------------------------|
| `clang`, `gcc` | 用于编译 C, C++, ObjectC 等语言 |
| `python` | 用于解释运行 Python 语言        |
| `openjdk-17` | 用于编译 Java 等语言           |
| `kotlin` | 用于编译 Kotlin 语言          |
| `Swift` | 用于编译 Swift 语言           |
| `nim` | 用于编译 Nim 语言             |

### 网络请求

通过

```shell
pkg i curl -y
pkg i wget -y
```

来安装 `curl` 和 `wget`。

### Z Shell

对于刚上手，不想浪费过多时间的人，建议使用 [tmoe](https://github.com/2moe/tmoe)。

安装：

```shell
curl -LO l.tmoe.me/tinor.deb
apt install ./tinor.deb
apt update
```

然后运行

```shell
tmoe m
```

来打开 `tmoe` 主程序。

接下来您会看到这样的画面：
[![jkd7Ae.jpg](https://s1.ax1x.com/2022/06/25/jkd7Ae.jpg)](https://imgtu.com/i/jkd7Ae)

用方向键移动光标到 `“Configure zsh美化终端`，按回车，再选择 `Installation and configuration 安装与配置`，按回车。期间如果有`Do you want to continue? (y/N)`的提示，直接 `y` 到底。

[![jkwjPJ.jpg](https://s1.ax1x.com/2022/06/25/jkwjPJ.jpg)](https://imgtu.com/i/jkwjPJ)

这里让你选主题，个人建议选 `powerlevel10k`，输入 `171` 回车继续。

[![jk0FaD.jpg](https://s1.ax1x.com/2022/06/25/jk0FaD.jpg)](https://imgtu.com/i/jk0FaD)

按 `q`，继续。

[![jk01Ig.jpg](https://s1.ax1x.com/2022/06/25/jk01Ig.jpg)](https://imgtu.com/i/jk01Ig)

随便选个配色继续。

[![jk0NMq.jpg](https://s1.ax1x.com/2022/06/25/jk0NMq.jpg)](https://imgtu.com/i/jk0NMq)

选字体，这里推荐 `JetBrains Mono Regular` (就是本博客所使用的等宽字体)，输入 `25`，回车继续。

这样，宁的炫酷 zsh 就装完辣！

# 正式使用

## 整体布局

[![jkWLdA.jpg](https://s1.ax1x.com/2022/06/25/jkWLdA.jpg)](https://imgtu.com/i/jkWLdA)

注意看这幅图。

最下方是快捷键，光标处是您的终端。

[![jkfKL4.jpg](https://s1.ax1x.com/2022/06/25/jkfKL4.jpg)](https://imgtu.com/i/jkfKL4)

从屏幕最左侧往右滑，上面的 `[1]`, `[2]` 等是正在运行的会话，您可以长按来给某一会话命名。

下方的 `KEYBOARD` 为弹出和收起键盘，`NEW SESSION` 为开启新的会话。

## Termux 的亿些小技巧

1. 双指缩放屏幕可以放大和缩小文字；
2. 下方的快捷键可以自定义，配置文件在 `~/.termux/termux.properties`；
3. 下方快捷键左滑出现一个对话框，可以在其中输入内容，按回车发送到终端。
4. 亿些快捷键：
    - Ctrl + A -> 将光标移动到行首
	- Ctrl + C -> 中止当前进程
	- Ctrl + D -> 注销终端会话
	- Ctrl + E -> 将光标移动到行尾
	- Ctrl + K -> 从光标删除到行尾
	- Ctrl + U -> 从光标删除到行首
	- Ctrl + L -> 清除终端
	- Ctrl + Z -> 挂起（发送 SIGTSTP 到）当前进程
	- Ctrl + alt + C -> 打开新会话（仅适用于 黑客键盘）
	> 注：音量- 相当于 Ctrl。
5. 环境变量 `$PREFIX` 的值为 `/data/data/com.termux/files/usr`
6. `$PREFIX/etc/profile` 即为初始化脚本，修改该脚本即可实现新建会话时自启动。
7. 开始进程会显示问候语，默认问候语如下：

```
Welcome to Termux!

Communities: https://termux.org/community
Gitter chat: https://gitter.im/termux/termux
IRC channel: #termux on libera.chat

Working with packages:

 * Search packages:   pkg search <query>
 * Install a package: pkg install <package>
 * Upgrade packages:  pkg upgrade

Subscribing to additional repositories:

 * Root:     pkg install root-repo
 * X11:      pkg install x11-repo

Report issues at https://termux.org/issues
```

太长了，对吧？
该文本文件保存在 `$PREFIX/etc/motd`，修改即可。

## Linux (Termux) 的一些知识和指令

这一段主要针对小白，大佬请跳过（逃）

### 目录和路径

`cd` 指令用于进入某一目录，首先我们来了解一下目录这个概念，通俗地来说，目录就是文件夹。

我们知道，在 Windows 系统中，每个盘符下都有若干文件夹，如系统盘（默认为 C: ） 下有 `Windows`, `Users`, `Program files` 等文件夹。这些文件夹又叫目录。目录间有层级关系，一个目录可以套着另一个目录。

那么怎么描述这些目录呢？这就要引入路径这个概念了。

路径用来描述文件和文件夹（目录）的位置，你可以把它理解为文件的地址，通过这个地址就能准确地找到一个文件。

路径分为绝对路径和相对路径。

绝对路径从根目录（Linux 下为 `/`）或环境变量开始，通过目录间的层级关系来表示一个目录或文件。

举几个栗子：

在 Windows 下，如果 `C:` 盘里有 `Windows` 文件夹，`Windows` 文件夹又套着 `System32` 文件夹，那么这个 `System32` 文件夹就可以表示为：

```
C:\Windows\system32
```

在 Linux 下，若 `~` 下有 `114514` 目录，`114514` 目录里边又有 `1919810` 目录，然后里边又套着 `hao_jun_jin_qu.mp3`，那么这个文件就可以表示为：

```
~/114514/1919810/hao_jun_jin_qu.mp3
```

这里可以看到， Windows 和 Linux 连接目录的符号是不一样的。Windows 中使用 `\`，而 Linux 使用 `/`。

相对路径相对描述一个目录，什么意思？看看您的终端：

[![jAt4Nd.jpg](https://s1.ax1x.com/2022/06/26/jAt4Nd.jpg)](https://imgtu.com/i/jAt4Nd)

这是我的终端，光标上方是不是有一行

```
~/test-ssh
```

这就代表我现在所处的目录在 `~/test-ssh` 。

现在这个目录里有一个 `test` 目录，如何描述这个目录？

如果用绝对路径描述的话，应该表示成

```
~/test-ssh/test
```

但是这样表示既冗长，又容易出错。那怎么办呢？

因为您现在正处于 `~/test-ssh`，所以直接使用

```
test
```

就可以表示这个目录，这就叫相对路径。

再来巩固一下：

设当前所在目录在 `~/example` 那么如何表示其中的 `linux` 文件夹？

答案是

```
linux
```

### 父目录和当前目录的简略表达

若当前目录为 `~/test/termux/linux`，怎么表示 `~/test/termux`？

一种方法是使用绝对路径

```
~/test/termux
```

那么怎么使用相对路径表示呢？

可以看到，`~/test/termux` 是 `~/test/termux/linux` 上一级的目录（简称父目录），可以用

```
..
```

来表示。

此时，`..` 就表示 `~/test/termux`。

那么还有一个问题，怎么表示当前目录 `~/test/termux/linux`？

一种方法是使用绝对路径，另一种方法，使用

``` 
.
```

来表示当前目录。

这个东西可能现在看上去没用，但是在执行脚本时非常有用。

### cd

`cd` 指令可以切换当前目录。

使用方法：

```shell
cd <目录路径>
```

这里的目录路径可以填绝对路径，也可以填相对路径。

> 注：下文若不另行提示，“目录”可填绝对路径和相对路径。

如当前目录为 `~/test/termux/linux`，使用

```shell
cd ..
```

来回到上一级目录。

### ls

`ls` 是 list 的缩写，顾名思义，这个指令能列出给出目录的所有文件和目录。若不给出路径，则列出当前目录的所有文件和目录。

用法：

```shell
ls [选项] [目录]
```

其中选项和目录均可选可不选。

若要获得详细的帮助，使用

```shell
ls --help
```

来获取帮助。

> 注：若用 `tmoe` 配置过 Termux，则可以用 `la`， `l` 来代替  `ls`，且更炫酷（

### rm

`rm` 代表 remove，意为删除。使用该指令可以删除文件。

用法：

```shell
rm [选项] <文件路径>
```

选项可选可不选，文件可以指派多个，不同文件用空格隔开。

选项里有几个用得特别多：

- `-r` 递归，可直接删除目录。若无此选项则只能删除单个文件。
- `-f` 强制删除（慎用！）

获取更多信息，参见

```shell
rm --help
```

### cp & mv

`cp` 意为 copy ，`mv` 意为 move，是 Linux 下的复制和剪切操作，用法差不多。

```shell
cp [选项] <源文件> <目标文件（夹）>
```

此处目标文件（夹）可以是一个不存在的文件，也可以是存在的文件夹。如果是一个不存在的文件，则将源文件复制到目标文件所在的文件夹，再重命名为该文件。如果是一个存在的文件夹，则将源文件复制到该文件夹，文件名不变。

> 1. 若目标文件为一个存在的文件，则会覆盖该文件，慎用！
> 2. 如果目标文件为一个不存在的文件，那么该文件所在的目录一定要是存在的，否则会报错。
> 3. 选项使用 `-r` 可复制整个文件夹。

`mv` 用法类似，不再赘述了。

For more information, `--help` 大法好。

---

先写到这。（摸了一天，好累哦.jpg）
