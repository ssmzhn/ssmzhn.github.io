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


但你身边没有电脑，怎么办呢？于是你摸出了手机，打开了龟速的 github，等待着下载进度条缓缓走完。然后你打开酷安，搜索一个手机能用的编译器app，打开源代码，编译，运行。

可是大多数这类软件不仅画风犹如三星堆出土，而且手感稀烂，贼鸡儿难用，况且 Github 网页在中国大陆的体验并不是太好（即使您可以用 fastgit, [GithHub520](https://github.com/521xueweihan/GitHub520)之类的工具优化加载速度），这时，一个趁手的软件就显得极为重要，它就是 [Termux](https://termux.com)。

# 使用前提
1. 一双巧手
2. 对 Linux 有初步了解
3. 手机剩余存储空间最好 ≥ 8GB
4. 一点耐心

# 安装
Termux 是一款 Android 终端模拟器和 Linux 环境应用程序，无需 root 或设置即可直接运行。

您可以在 [Github](https://github.com/termux/termux-app/releases) 或 [F-Droid](https://f-droid.org/en/packages/com.termux/) 里直接下载安装包安装。

<div class="warning">

> 注意：
> 不要在 Google Play 里安装 Termux！Google Play 中 Termux 版本太低，已经停止维护。

</div>

# 配置
Termux 可玩性非常高，本文只给出一种建议选择，供大家参考。
## 换源
输入 
```shell
termux-change-repo
```
会出现以下的画面：
[![termux-change-repo](https://s1.ax1x.com/2022/06/25/jkNhX8.jpg)](https://imgtu.com/i/jkNhX8)

此时按箭头键，选择 `Mirrors in China`，按下空格键，使前面的`( )`中带`*`，回车继续，接下来会自动更新软件包。

当出现 `Do you want to continue? (y/N)` 时，输入`y`，按回车继续，等待跑完。此时保持网络畅通，您的软件包就更新完辣！

## 必备软件包
### Git
强大的版本控制系统！它可以让您方便地管理代码，背后还有 Github 作为生态。使用该工具能帮您轻松使用 Github，使用方法敬请百度。

输入
```shell
pkg install git
```

或
```shell
pkg i git
```
来安装 Git。

> 注：此处的 `install` 可以换成 `i`，以后不再赘述。

### 编辑器
为了方便地编辑文本文件而不是到 termux 外再找个程序编辑，请务必安装编辑器。

Termux 上的编辑器有很多，任选其一即可。我个人用 `vim` 习惯了，但仁者见仁，智者见智。

常用的编辑器：
 - vi
 - vim
 - nvim
 - emacs
 - nano

等等。

### 编译/解释器
把 workflow 丢到命令行上，从此告别繁杂的编译器 app！
直接使用
```shell
pkg i <软件包>
```
即可，软件包和在 Linux 上是一样一样的。
如：

| 软件包 | 说明 |
| :-------: | :------- |
| `clang`, `gcc` | 用于编译 C, C++ 等语言 |
| `python` | 用于解释运行 Python 语言 |
| `openjdk-17` | 用于编译 Java 等语言 |

### 网络请求
通过
```shell
pkg i curl
pkg i wget
```
来安装 `curl` 和 `wget`。
### shell（zsh）
对于刚上手，不想浪费过多时间的人，建议使用 [tmoe](https://github.com/2moe/tmoe)。
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
来打开 `tmoe` 主程序。

接下来您会看到这样的画面：
[![jkd7Ae.jpg](https://s1.ax1x.com/2022/06/25/jkd7Ae.jpg)](https://imgtu.com/i/jkd7Ae)

用方向键移动光标到 “Configure zsh美化终端”，按回车，再选择“Installation and configuration 安装与配置”，按回车。期间如果有`Do you want to continue? (y/N)`的提示，直接 `y` 到底。

[![jkwjPJ.jpg](https://s1.ax1x.com/2022/06/25/jkwjPJ.jpg)](https://imgtu.com/i/jkwjPJ)

这里让你选主题，个人建议选 `powerlevel10k`，输入`171`回车继续。

[![jk0FaD.jpg](https://s1.ax1x.com/2022/06/25/jk0FaD.jpg)](https://imgtu.com/i/jk0FaD)

按 `q` ，继续。

[![jk01Ig.jpg](https://s1.ax1x.com/2022/06/25/jk01Ig.jpg)](https://imgtu.com/i/jk01Ig)

随便选个配色继续。

[![jk0NMq.jpg](https://s1.ax1x.com/2022/06/25/jk0NMq.jpg)](https://imgtu.com/i/jk0NMq)

选字体，这里推荐 `JetBrains Mono Regular`（就是本文用的等宽字体），输入`25`，回车继续。

这样，宁的炫酷 zsh 就装完辣！

---

先写到这。（摸了一天，好累哦.jpg）
