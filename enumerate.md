# enumerate
enumerate() 是 Python 的一个内置函数，用来在遍历可迭代对象（如列表、字符串、元组等）时，同时获取每个元素的索引和值。
## 基本语法
```Python
enumerate(iterable, start=0)
```

|参数|说明|
|:----:|:---|
iterable|任何可迭代对象（如列表、字符串、元组等）
start|索引起始值，默认是 0

##  返回值
返回一个枚举对象，每次迭代会生成一个 (index, value) 的元组。
##  小结一句话
enumerate() 就是“边遍历边计数”，让你不用手动写 i = 0 和 i += 1，代码更简洁、安全。