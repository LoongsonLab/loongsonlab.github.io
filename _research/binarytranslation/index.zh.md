---
layout: research
title: 二进制翻译组
description: 通过二进制翻译，将X86、ARM、RISC-V等架构的应用程序运行在龙芯处理器上。结合指令集和处理器设计的硬件创新，实现动静态结合、软硬件结合的高效二进制翻译系统，寻求二进制翻译系统效率和完备性两大方面的突破。
advisors:
  - 张福新
maintainers:
  - 牛根
  - 谢本壹
  - 李欣宇
  - 兰彦志
contributors:
  - 赵东儒
  - 郭伟明
  - 张壮壮
  - 杨兆鑫
date: 2023-07-06
permalink: research/binarytranslation
lang: zh
construct: true
---

如果你对**指令流分析**、**编译技术**、**虚拟化技术**以及**操作系统**等有一些兴趣，那么希望本页面能够给你一些有关二进制翻译的相关内容。

## 什么是二进制翻译

TLDR; 通过二进制翻译可以将X86、ARM、RISC-V等架构的应用程序运行在龙芯处理器（LoongArch）上。

由于不同架构的程序他们所包含的机器码不同，所以跨架构的程序无法直接运行。如X86上的程序无法在ARM以及LoongArch上运行。
为了让使得不同架构的程序能够在不进行重新编译的情况下，运行在目标平台上，我们需要使用[二进制翻译技术](https://en.wikipedia.org/wiki/Binary_translation)。

Altman 提出二进制翻译可以分成三大类，分别是**解释执行**、**静态二进制翻译**以及**动态二进制翻译**[^1]。当然综合了他们的优点，我们也存在着**混合二进制翻译系统**。

* 解释执行时会对每条指令进行实时的解释，不进行优化和缓存；
* 静态二进制翻译采用“离线”翻译方式，在程序不运行的情况下，对原二进制文件进行分析、翻译以及优化；
* 动态二进制翻译采用“在线”翻译方式，在程序执行到某个片段时才会对该片段进行翻译；
* 混合二进制翻译则结合了前面各类型的优点，寻找性能和正确性的平衡。

[^1]: E. R. Altman, D. Kaeli and Y. Sheffer, "Welcome to the opportunities of binary translation," in Computer, vol. 33, no. 3, pp. 40-45, March 2000, doi: 10.1109/2.825694.

现在我们能够接触到的，常见的二进制翻译有[QEMU](https://www.qemu.org/)，[Rosetta2](https://support.apple.com/zh-cn/HT211861)，以及使用二进制翻译技术的[DynamoRIO](https://dynamorio.org/)和[Pin](https://www.intel.cn/content/www/cn/zh/developer/articles/tool/pin-a-dynamic-binary-instrumentation-tool.html)。

## 我们在做什么

研究是方向包括了[二进制翻译优化](#二进制翻译优化)、[库包装](#库包装)、[微译器](#微译器)以及[系统态二进制翻译](#系统态二进制翻译)等。

### 二进制翻译优化

### 库包装

### 微译器

### 系统态二进制翻译

## 入门实验

为了让大家能够更好的，更快的了解二进制翻译，我们设计了一些入门实验。
当然这些实验并不完全局限于只了解二进制翻译，我们希望这些实验可以补充大家对于“一个二进制程序”的理解。

* [入门实验地址](http://172.17.103.58/lanyanzhi/LAT-Guide)（需要内网访问）
