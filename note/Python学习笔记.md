---
title: Python学习笔记
date: 2021-04-04 21:33:40
update:
tags:
	- Python
categories:
	- [信息技术,Python]
---

# Python学习笔记

<!-- more -->

## 基础

### 入门

#### Python简介

##### Python的起源

1991年，`Guido van Rossum`编写出了第一个`Python解释器（Python interpreter）`。它是用C语言实现的，并能够调用C语言的库文件。

##### 解释器

###### 编译型语言

程序在执行之前需要一个专门的编译过程，把程序编译成为机器语言的文件，运行时不需要重新翻译，直接使用编译的结果就行了。程序执行效率高，依赖编译器，跨平台性差些。如 C、C++。

###### 解释型语言

解释型语言编写的程序不进行预先编译，以文本方式存储程序代码，会将代码一句一句直接运行。在发布程序时，看起来省了道编译工序，但是在运行程序的时候，必须先解释再运行。**Python为解释型语言**。

##### Python设计哲学

在Python解释器内运行：import this 可以获得Tim Peters撰写的The Zen of Python。

```python 
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

#### 搭建Python环境

##### Windows安装

访问 https://www.python.org/downloads/windows/ 选择对应版本的安装程序下载安装，安装时注意勾选`add Python to path`选项。

#### 第一个Python程序

##### Hello,world程序

新建一个以`.py`为后缀的文件，如`py_00_hello.py`。填入以下代码后保存。

```python
print("hello,world")
```

在终端或cmd界面，输入：

```bash
python py_00_hello.py
```

便可显示运行结果：

```bash
Hello,world
```

##### 输出函数

上述语句中，`print`是一个输出`函数`，该函数可以在终端中打印相关内容，括号内为其`参数`。

##### 字符串

括号内用双引号包围的内容叫字符串。

#### 注释

##### 单行注释

```python
# 这是第一个单行注释
```

##### 多行注释

```python
"""
这是
多行注释的一种
"""
'''
这是多行注释的另一种
'''
```


### 变量和数据类型

#### 变量

##### 变量的定义

```python
variable = value
```
> python中变量的是赋给值的一个标签。

##### 标识符命名规则

- 只能包含字母，数字和下划线。
- 不能以数字开头。
- 不能与Python关键字冲突。

###### Python关键字

```python
>>> import keyword
>>> keyword.kwlist
['False', 'None', 'True', '__peg_parser__', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
```

#### 数据类型

- 数值
	- int（整型）
	- float（浮点型）
- Bool型
	- True
	- False
- str（字符串）
- list（列表）
- tuple（元组）
- set（集合）
- dict（字典）

##### 数据类型查看方法

使用`type()`函数可查看其数据类型。
```python
>>> i = 3.14
>>> type(i)
<class 'float'> 

>>> x = 30000
>>> type(x)
<class 'int'>

>>> j = "hello"
>>> type(j)
<class 'str'>

>>> t = True
>>> type(t)
<class 'bool'>

>>> k = [1,2,3]
>>> type(k)
<class 'list'>

>>> l = (1,2,3,4)
>>> type(l)
<class 'tuple'>

>>> m = {"hello":123}
>>> type(m)
<class 'dict'>

>>> n = {1,2,3}
>>> type(n)
<class 'set'>
```

##### 数据类型的转换

#### 数值

#### 常量

#### bool类型

#### 字符串

#### 列表

#### 元组

#### 集合

#### 字典


### 控制语句与输入输出

#### 运算符

##### 算数运算符

| 运算符 |  描述  | 实例                                                  |
| :----: | :----: | ----------------------------------------------------- |
|   +    |   加   | 1 + 1 输出结果为 2                                    |
|   -    |   减   | 1-1 输出结果为 0                                      |
|   *    |   乘   | 2 * 2 输出结果为 4                                    |
|   /    |   除   | 10 / 2 输出结果为 5                                   |
|   //   |  整除  | 9 // 4 输出结果为2                                    |
|   %    |  取余  | 9 % 4 输出结果为 1                                    |
|   **   |  指数  | 2 ** 4 输出结果为 16，即 2 * 2 * 2 * 2                |
|   ()   | 小括号 | 小括号用来提高运算优先级，即 (1 + 2) * 3 输出结果为 9 |

##### 赋值运算符

| 运算符 | 描述 | 实例                                |
| ------ | ---- | ----------------------------------- |
| =      | 赋值 | 将`=`右侧的结果赋值给等号左侧的变量 |
| +=     | 加法赋值运算符 | c += a 等价于 c = c + a    |
| -=     | 减法赋值运算符 | c -= a 等价于 c = c- a     |
| *=     | 乘法赋值运算符 | c *= a 等价于 c = c * a    |
| /=     | 除法赋值运算符 | c /= a 等价于 c = c / a    |
| //=    | 整除赋值运算符 | c //= a 等价于 c = c // a  |
| %=     | 取余赋值运算符 | c %= a 等价于 c = c % a    |
| **=    | 幂赋值运算符   | c ** = a 等价于 c = c ** a |

##### 比较运算符

| 运算符 | 描述                                                         | 实例                                                        |
| ------ | ------------------------------------------------------------ | ----------------------------------------------------------- |
| ==     | 判断相等。如果两个操作数的结果相等，则条件结果为真(True)，否则条件结果为假(False) | 如a=3,b=3，则（a == b) 为 True                              |
| !=     | 不等于 。如果两个操作数的结果不相等，则条件为真(True)，否则条件结果为假(False) | 如a=3,b=3，则（a == b) 为 True如a=1,b=3，则(a != b) 为 True |
| >      | 运算符左侧操作数结果是否大于右侧操作数结果，如果大于，则条件为真，否则为假 | 如a=7,b=3，则(a > b) 为 True                                |
| <      | 运算符左侧操作数结果是否小于右侧操作数结果，如果小于，则条件为真，否则为假 | 如a=7,b=3，则(a < b) 为 False                               |
| >=     | 运算符左侧操作数结果是否大于等于右侧操作数结果，如果大于，则条件为真，否则为假 | 如a=7,b=3，则(a < b) 为 False如a=3,b=3，则(a >= b) 为 True  |
| <=     | 运算符左侧操作数结果是否小于等于右侧操作数结果，如果小于，则条件为真，否则为假 | 如a=3,b=3，则(a <= b) 为 True                               |


##### 逻辑运算符

| 运算符 | 逻辑表达式 | 描述                                                         | 实例                                     |
| ------ | ---------- | ------------------------------------------------------------ | ---------------------------------------- |
| and    | x and y    | 布尔"与"：如果 x 为 False，x and y 返回 False，否则它返回 y 的值。 | True and False， 返回 False。            |
| or     | x or y     | 布尔"或"：如果 x 是 True，它返回 True，否则它返回 y 的值。   | False or True， 返回 True。              |
| not    | not x      | 布尔"非"：如果 x 为 True，返回 False 。如果 x 为 False，它返回 True。 | not True 返回 False, not False 返回 True |

##### 运算符优先级


#### 条件语句

##### if语句

```python
if 条件:
    条件成立执行的代码1
    条件成立执行的代码2
    ......
```

##### if...else语句

```python
if 条件:
    条件成立执行的代码
else:
    条件不成立执行的代码
```

##### if...elif语句

```python
if 条件1:
    条件1成立执行的代码
elif 条件2:
    条件2成立执行的代码
else:
    以上条件都不成立执行的代码
```

##### 三目运算符

```python
值1 if 条件 else 值2

a = 1
b = 2

c = a if a > b else b
print(c)
# 输出结果 2
```

#### 循环语句

##### while循环

```python
while 条件:
    条件成立重复执行的代码1
    条件成立重复执行的代码2
    ......
```

##### while...else循环

```python
while 条件:
    条件成立重复执行的代码
else:
    循环正常结束之后要执行的代码
```

##### for循环

```python
for 临时变量 in 序列:
    重复执行的代码1
    重复执行的代码2
    ......
```

##### for...else循环

```python
for 临时变量 in 序列:
    重复执行的代码
    ...
else:
    循环正常结束之后要执行的代码
```

##### `break`和`continue`

- `break`指打断本层循环，进行本层循环外的代码，循环并非正常结束。
- `continue`指跳过本次循环，继续本层循环的下一次循环。

#### 输入

#### 输出


### 函数

#### 

### 面向对象

### 文件和异常

### 常用库函数

#### `random`库
