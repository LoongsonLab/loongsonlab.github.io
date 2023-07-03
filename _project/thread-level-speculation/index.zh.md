---
layout: project
title: 异构计算组
description: 硬件线程级推测并行系统
advisors:
  - 王剑
maintainers:
  - 程鑫
contributors:
  - 李文青
  - 叶锦鹏
date: 2023-07-03
permalink: project/thread-level-speculation
lang: zh
construct: true
---

## 线程级推测并行

如果你对并行计算、多核处理、缓存一致性协议感兴趣，希望本页面能为你提供你想了解的内容

### 🎯  背景知识

直奔主题，该项目的核心技术就是线程级推测并行（TLS，Thread Level Speculation），当然你可能也听说过别的名称，在论文中提到的，比如有序并行（Ordered Parallelism），多读多写缓存一致性（MRMW Cache Coherency）。

从缓存一致性的角度讲，TLS具有的鲜明特征即是Multi-Versioned，毕竟并行技术，考究的就是共享资源的读写控制。这项技术可以追溯到1995年，伴着当时提的火热的CMP，理想情况下一核有难多核支援，但是想让多核用起来，并行编程是个难题，常见的就是加锁，依赖处理器提供的原子操作，但是对于用户程序而言，使用这些调用的代价并不小，同时想写出一个高效的还不出错的并行程序也很困难，稍不留神就死锁，因此想了些奇技淫巧，干脆不用这种东西不就好了，其实本质上就是把原子指令这中原子性粒度局限在一条指令的行为扩展到一个代码片段。但是想想利用两条原子指令是不是就能实现这种东西，临界区不就是这个概念，但是临界区是真的只能允许一个在跑，那可不行，意味着多核资源的浪费，得让所有的核都要跑起来还不出错，那才完美。

其实你也清楚程序能否并行执行，就看资源是否存在冲突，像共享变量这些，大家都是读都好说，多个人写并且不在意顺序也好说，但是多个人写还要在意顺序（例如内存一致性，程序序等），那就得掂量掂量风险了。因此TLS就是为了解决这种复杂的场景而提出来的，要求在运行期间解决并行程序之间的资源冲突问题。如果把问题缩小，这里的资源无非就是某个内存块，冲突就是load/store操作不符合程序的行为要求，举个例子：For循环N次，现在有N个核，我先什么都不管，让N个迭代直接在N核上一起跑，显然，如果迭代之间存在同一个内存块的load/store操作，那么是有可能出错的（迭代i < j，Store j先于Load i发生）。这个例子包含TLS技术实现中重点关注的难点：

- 如何检查出错误
- 如何恢复

关于更多的技术内容在这里不作展开，相信到这里，你已经大致清楚线程级推测并行要达到怎样的目的，更多的内容可以在后续跟进的过程中深入了解，比如：

1. Hardware/Software TLS
2. Transactional Memory和TLS在实际应用中的关联
3. Eager/Lazy conflict detection、eager/lazy versioning、lazy commit
4. False sharing、privatilization、word detection
5. Spwan programming model, what/why?
6. Software/Hardware rollback
7. 任务切分、冷启动、缺页异常、编程模型对于硬件设计的辅助性能提升的关系

### ⛳️  进展

在之前一年的时间中，已经在Gem5平台搭建出线程级推测并行系统（迭代了若干个很挫的版本然后得到了一个相对较好的挫版本），支持：

1. OoO CPU
2. Cache Coherency Design

当前处在寻找Benchmark的阶段（当然要找合适的程序来体现出它的价值，可不敢乱测，理想很丰满）：

1. SPEC2006，排除了lbm、libquantum、milc、h264ref、sphinx3，它们的程序行为不合适，都是parallel的，但是部分在编译器静态期间是分析不出来的（存在指针等影响因素），mcf倒是可以考虑修改一下
2. Olden Benchmark，这个是测事务访存的，但是无妨，也是可以用的
3. STAMP，同样是事务访存，目前修改了kmeans，效果理想
4. Graph benchmark，这个目前是手写了两个算法，Bellman-Ford和BFS，效果都不是很理想，问题在于编程模型不好使，程序调优有较大的提升空间

---

快速体验方式参考这里：
如果不想自己搭建环境，想快速体验下，可以通过浏览器上[gitlab](http://10.208.129.89/)在repo中手动启动流水线跑ci感受推测并行相较于串行执行的加速效果（如何上gitlab？可以私下沟通）
以下是本地开发环境的配置

- Ubuntu 18/20，如果想用Windows，推荐使用WSL2
- 依赖安装可能需要翻墙
- [WSL2配置方法（推荐使用CLion，如果你熟练VScode或者Vim等其他手动搭建环境则忽略CLion配置）](https://zhuanlan.zhihu.com/p/272522594)
- [GEM5配置（推荐额外安装libpng、graphviz库）](https://www.gem5.org/documentation/general_docs/building)
- 项目正在开发的分支为[TinyTLS](http://foxsen.3322.org:33336/chengxin/speculative-cache.git)

```
  git clone http://foxsen.3322.org:33336/chengxin/speculative-cache.git HardwareTLS
  cd HardwareTLS && git submodule update --init --recursive
  scons build/TinyTLS/gem5.fast -j`nproc`
  # run kmeans benchmark
  cd benchmark/STAMP/kmeans/run && ./run.sh 4 && grep 'Time' -r ./m5out
```

### ⭐️  参考资料

#### 文献

[Speculative Versioning Cache](https://ieeexplore.ieee.org/document/650559)

[LogTM](http://ieeexplore.ieee.org/document/1598134/)

[Swarm Architecture](https://dl.acm.org/doi/10.1145/2830772.2830777)

### 💡  帮助

[想要获取更多参考内容，欢迎加入飞书](https://www.feishu.cn/invitation/page/add_contact/?token=2ffh6bc6-81bd-4ee9-aa9f-fcce094d684d&amp;unique_id=zL3Ft_Z7fOT7g7mCfmXQrA==)