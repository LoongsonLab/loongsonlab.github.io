---
layout: research
title: 二进制翻译优化
description: 二进制翻译优化直接关系到翻译后程序的性能与体验，我们针对二进制翻译性能相关问题进行了一些探索和优化。
advisors:
  - 张福新
maintainers:
  - 李欣宇
  - 兰彦志
contributors:
  - 胡起
date: 2023-07-17
permalink: research/binarytranslation/optimization
lang: zh
construct: true
index_hide: true
---

二进制翻译中最关心的是翻译后程序性能。如果翻译后程序性能较差，不仅会影响用户的使用体验，
还会影响程序执行的正确性。如需要翻译的程序存在超时机制模块，二进制翻译性能较差可能会引发程序的超时错误，
使得程序无法正常运行。

## 开销来源

二进制翻译中开销往往来源于以下几个方面：

* 翻译过程的开销：动态二进制翻译的“边翻译边运行”的运行模式会引入翻译过程开销，尤其对含有大量冷代码的程序，翻译开销带来的影响较为明显；
* 指令膨胀带来的开销：翻译后指令数相较于翻译前指令数的增多，会带来最直接的性能降低，这也是是造成程序性能开销的主要原因；
* 间接跳转带来的开销：间接跳转需要通过多次上下文切换及查找才能完成，会导致巨量的指令膨胀，所以每次的间接跳转开销都是巨大的；
* 其他开销：上下文切换、基本块链接和系统调用等因素也会影响翻译后程序的性能。

## 研究方向

### 更加优秀的翻译后代码

为了得到更好的翻译后代码，有各种工作做了一些尝试。如Dynamo[^1]，通过识别热点路径并进行优化的方式，得到更优代码；
还有HQEMU[^2]，通过加入LLVM，将热点块交给编译器进行优化。

[^1]: Vasanth Bala, Evelyn Duesterwald, and Sanjeev Banerjia. 2000. Dynamo: a transparent dynamic optimization system. SIGPLAN Not. 35, 5 (May 2000), 1–12. https://doi.org/10.1145/358438.349303

[^2]: Hong, D., Hsu, C., Yew, P., Wu, J., Hsu, W., Liu, P., Wang, C., & Chung, Y. (2012). HQEMU: a multi-threaded and retargetable dynamic binary translator on multicores. IEEE/ACM International Symposium on Code Generation and Optimization.

针对现有LATX翻译器，实现了指令流分析制导的动态二进制翻译优化方案 IFADO（Instruction Flow Analysis Directing Optimization）。
主要有以下优化方案：

* EFLAGS 延迟（懒惰）计算
* “反馈式”指令语义化翻译
* SSE 标量指令高位运算消除

![]({{ '/assets/research/binarytranslation/spec2k-all.png' | relative_url }})

### 更低的翻译开销

### 间接跳转优化

### 其他
