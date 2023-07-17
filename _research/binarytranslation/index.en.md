---
layout: research
title: Binary Translation
description: Through binary translation, applications of X86, ARM, RISC-V and other architectures are run on the Loongson processor. Combining hardware innovations in instruction set and processor design to achieve an efficient binary translation system that combines dynamic and static, software and hardware, seeking a breakthrough in both efficiency and completeness of the binary translation system.
advisors:
  - Fuxin Zhang
maintainers:
  - Gen Niu
  - Benyi Xie
  - Xinyu Li
  - Yanzhi Lan
contributors:
  - Dongru Zhao
  - Weiming Guo
  - Zhuangzhuang Zhang
  - Zhaoxin Yang
  - Liangpu Wang
date: 2023-07-06
permalink: research/binarytranslation
lang: en
construct: true
---

If you have some interest in **Instruction Flow Analysis**, **Compilation**, **Virtualization** and **Operating Systems**, then hopefully this page will give you some relevant content on **Binary Translation**.

## What is Binary Translation

TLDR; Binary Translation allows applications from X86, ARM, RISC-V and other architectures to run on a Loongson processor (LoongArch).

Since programs of different architectures contain different machine codes, cross-architecture programs cannot be run directly. For example, programs on X86 cannot be run on ARM or LoongArch.
In order to allow programs of different architectures to run on the target platform without recompilation, we need to use [binary translation techniques](https://en.wikipedia.org/wiki/Binary_translation).

Altman proposes that binary translation can be divided into three main categories, namely **interpreted execution**, **static binary translation**, and **dynamic binary translation**[^1]. Of course combining their advantages, we also have the existence of **hybrid binary translation systems**.

* interpreted execution interprets each instruction in real time, without optimisation or caching;
* Static binary translation uses "offline" translation, where the original binary file is analysed, translated and optimised without the program running;
* Dynamic binary translation is "online", translating a fragment only when the program reaches it;
* Hybrid binary translation combines the advantages of the previous types to find a balance between performance and correctness.

[^1]: E. R. Altman, D. Kaeli and Y. Sheffer, "Welcome to the opportunities of binary translation," in Computer, vol. 33, no. 3, pp. 40-45, March 2000, doi: 10.1109/2.825694.

The common binary translations that we have access to now are [QEMU](https://www.qemu.org/), [Rosetta2](https://support.apple.com/zh-cn/HT211861), [DynamoRIO](https://dynamorio.org/), which uses binary translation techniques and [Pin](https://www.intel.cn/content/www/cn/zh/developer/articles/tool/pin-a-dynamic-binary-instrumentation-tool.html).

## What we're doing

The research is in the areas of [Binary Translation Optimisation](#binary-translation-optimisation), [Dynamic Library Packaging](#dynamic-library-packaging), [Micro-translator](#micro-translator) and [Full system Binary Translation](#full-system-binary-translation).

### Binary Translation Optimisation

### Dynamic Library Packaging

Dynamic Libaray Packaging is an enxtention of application of binary translation, compared to binary translation, which is focus on translating full excution file of guest, dunamic library packaging is focus on how to combie host excution file and guest dynamic library smoothly.

The difficulties in dynamic library packaging lie in correctly and efficiently switch between guest code and host code, which usually happens in function calls between guest and host. Because the calling conventions of host and guest are usually not the same, a switch code is needed between these function calls. From this perspective, library packaging is a virtualization of call convention of different ISAs.

Packaging for a specific library is cumbersome and not universal. We hope to use compiler-related technologies to automate and generalize this process, and finally enable it to be put into practical applications.

There is currently no well-known work in the field of library packaging; library passthrough is a similar work, library passthrough focuses on using native library functions to speed up the execution of translated guest programs. FEX, BOX64, etc. use library passthrough technology to accelerate their binary translator.

### Micro-translator

### Full system Binary Translation

### Complie Optimization Guided Binary Translation
The efficiency of a binary translation system heavily relies on the quality of the **translated code** it generates.
Currently, most binary translators for code translation, such as QEMU and Rosetta2, use a one-to-one/many mapping approach, which does not fully explore **the optimization space between instructions**.

COGBT is a compile optimization guided binary translator. 
Its goal is to explore the optimization space between instructions through compilation techniques.
Additionally, the scalability of LLVM makes it easier to implement specific optimization passes.

Some optimization techniques has been implemented:
- Stack variables translation model: this model achieves fixed register mapping in the LLVM IR stage.
- Specific optimization passes: Flag Elimination Pass, Pattern Analysis Pass, etc.
- Translation Units (TUs): Combining multiple Translation Blocks (TBs) to explore the optimization space between them.
- Profile-guided optimization: Collecting hot paths of traces, collecting targets of indirect jumps, etc.

Some optimization techniques that could be explored in the future:
- Automatic vectorization of floating-point operations.
- Promotion of stack variables to register variables.
- Precise exceptions.

## Introductory Experiments

In order to give you a better and faster understanding of binary translation, we have designed some introductory experiments.
We hope that these experiments will complement your understanding of "a binary program", but they are not limited to binary translation only.

* [address for introductory experiments](http://172.17.103.58/lanyanzhi/LAT-Guide) (requires intranet access)
