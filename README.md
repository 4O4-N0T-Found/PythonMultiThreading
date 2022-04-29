# Python 多线程 demo
实验中经常遇到大量文件读写、网络收发数据等任务，多线程在这种情况下能够加速任务执行速度。本项目是一个demo：利用Python多线程来批量处理文件。
## 需求&场景
1. 文件夹 `/bytecode` 中包含大量待处理文件。
2. 需要用程序 `oyente.py`，将这些待处理文件全部处理一遍。`python3 oyente.py [文件]`
3. 程序 `Oyente.py` 的作用是：计算待处理文件中的内容的MD5，输出形如 `[待处理文件名]#[MD5]` 的字符串。
4. 处理的结果需要保存在一个文本文件 `addr2hash.txt` 中。
## 使用
```$python3 getAddr2hash.py ./bytecode```

实际使用时：
+ `./bytecode` 替换为待处理文件夹
+ `oyente.py` 替换为处理程序
+ `getAddr2hash.py` 中可能需要修改调用 `oyente.py` 的方式
+ 其他
## 效果
10000个待处理文件。16核32G平台。
+ 单线程耗时：213s
+ 四线程耗时：55s
+ 十线程耗时：36s