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

> 列表类似于C语言中的数组，但不限制其中的元素。

##### 创建与访问

###### 创建列表

用`[ ]`框住，元素使用`,`间隔。

```python
list_name = [1,2,"hello","jachin"]
```

###### 访问列表元素

```python
>>> list_name = [1,2,"hello","jachin"]
# 下标从0开始。
>>> list_name[1]
2
# 可使用负数下标，以倒数访问，从-1开始。
>>> list_name[-1]
'jachin'
```

从列表中取值时，如果 **超出索引范围**，程序会报错。

```python
>>> list_name[4]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    list_name[4]
IndexError: list index out of range
>>> list_name[-5]
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    list_name[-5]
IndexError: list index out of range
```

###### 使用列表中的值

```python
>>> list_name = [1,2,"hello","jachin"]
>>> message = f"你好哇，{list_name[-1].title()}"
>>> print(message)
你好哇，Jachin
```

##### 修改、添加和删除元素

###### 修改

| 语法                | 备注 | 功能               |
| ------------------- | ---- | ------------------ |
| list[index] = value |      | 修改指定索引的元素 |

```python
>>> list_name = [1,2,"hello","jachin"]
>>> list_name[0] = "唐占"
>>> print(list_name)
['唐占', 2, 'hello', 'jachin']
```

###### 添加

| 语法                     | 备注              | 功能                      |
| ------------------------ | ----------------- | ------------------------- |
| list.insert(index,value) | insert:插入       | 在指定位置插入元素        |
| list.append(value)       | append:附加       | 在末尾追加元素            |
| list1.extend(list2)      | extend:延伸，扩大 | 将列表2 的元素追加到列表1 |

```python
>>> list_name = [1,2,"hello","jachin"]
>>> list_name.insert(1,'wujiao')
>>> print(list_name)
[1, 'wujiao', 2, 'hello', 'jachin']

>>> list_name.append("tangzhan")
>>> print(list_name)
[1, 'wujiao', 2, 'hello', 'jachin', 'tangzhan']

>>> list_age = [18,19,20]
>>> list_name.extend(list_age)
>>> print(list_name)
[1, 'wujiao', 2, 'hello', 'jachin', 'tangzhan', 18, 19, 20]
```

###### 删除

| 语法               | 备注              | 功能                     |
| ------------------ | ----------------- | ------------------------ |
| del list[index]    | delete:删除       | 删除指定索引的数据       |
| list.remove(value) | remove:开除，移除 | 删除第一个出现的指定数据 |
| list.pop()         | pop:弹出          | 弹出末尾数据             |
| list.pop(index)    |                   | 弹出指定索引数据         |
| list.clear()       | clear:清空        | 清空列表                 |

```python
>>> list_name = [1,2,"hello","jachin"]
>>> del list_name[1]
>>> print(list_name)
[1, 'hello', 'jachin']

>>> list_name.remove("hello")
>>> print(list_name)
[1, 'jachin']

# pop的理解源于栈这个数据结构。可以理解为“弹出并访问”，并不是单纯的删除。
>>> list_name = [1,2,"hello","jachin"]
>>> print(list_name.pop())
jachin
>>> print(list_name)
[1, 2, 'hello']

>>> list_name = [1,2,"hello","jachin"]
>>> print(list_name.pop(1))
2
>>> print(list_name)
[1, 'hello', 'jachin']

>>> list_name.clear()
>>> print(list_name)
[]
```

##### 组织列表

###### 获取表长

| 语法      | 备注        | 功能     |
| --------- | ----------- | -------- |
| len(list) | length:长度 | 列表长度 |

###### 统计某元素出现次数

| 语法              | 备注       | 功能                   |
| ----------------- | ---------- | ---------------------- |
| list.count(value) | count:总数 | 元素在列表中出现的次数 |

###### 排序

| 语法                    | 备注      | 功能     |
| ----------------------- | --------- | -------- |
| list.sort()             | sort:排序 | 升序排序 |
| list.sort(reverse=True) |           | 降序排序 |
| sorted(list)            |           | 临时排序 |

###### 逆序

| 语法           | 备注         | 功能       |
| -------------- | ------------ | ---------- |
| list.reverse() | reverse:反转 | 逆序、反转 |

###### 获取某元素下标

| 语法                                      | 备注              | 功能                                               |
| ----------------------------------------- | ----------------- | -------------------------------------------------- |
| list.index(value, start=0, end=len(list)) | index：索引，指针 | 在指定区间查找某元素，返回下标。若无此元素，报错。 |

###### 列表复制

| 语法        | 备注      | 功能                     |
| ----------- | --------- | ------------------------ |
| list.copy() | copy:复制 | 返回一个了列表的复制件。 |

##### 数值列表

###### 生成数值列表

| 语法                     | 备注             | 功能                               |
| ------------------------ | ---------------- | ---------------------------------- |
| range(start,stop[,step]) | range:序列，区间 | 生成一个指定区间和步长的数字列表。 |

###### 列表解析

###### 简单统计计算

| 语法      | 备注     | 功能               |
| --------- | -------- | ------------------ |
| min(list) | min:最小 | 找出列表中最小的数 |
| max(lsit) | max:最大 | 找出列表中最大的数 |
| sum(list) | sum:总和 | 将列表中所有数相加 |

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

#### 初步使用

##### 函数的定义

```python 
def function_name():
    """Docstring"""
    pass
```

`def`是英文`define`的缩写。

> 通常在定义函数时，与上段代码相隔两个空行。

##### 函数的调用

```python
function_name()
```

例：

```python 
def hello():
	"""打印：hello,world"""
	print("hello,world")

hello()
# hello,world
```

##### 文档注释

- 如果希望给函数添加注释，应该在**定义函数**的下方，使用**连续的三对引号**，在其之间编写对函数的说明文字。
- 在**函数调用**位置，使用快捷键`CTRL + Q`可以查看函数的说明信息。

#### 参数

##### 基本使用

在绝大多数时候，需要向函数传递信息，这时需要使用参数。• 在函数名的后面的小括号内部填写 参数
多个参数之间使用 , 分隔

```python 

```



### 面向对象

#### 面向对象基础

##### 类和对象

###### 类

`类`是对一系列具有相同*特征*和*行为*的事物的统称，是一个抽象的概念。例如：飞机的图纸。

特征：`属性`

行为：`方法`

###### 对象

`对象`是类创建出来的真实存在的事物，例如：某架飞机。

###### 实例

一般创建对象也叫实例化对象，即为一个`实例`。但有一种抽象对象，创建出的对象不是实例。

##### 创建类和对象

###### 创建类

```python
def ClassName():
    pass
# 一般使用大驼峰命名。
```

> PEP8中规范：
>
> 类名一般使用首字母大写的约定。
> 在接口被文档化并且主要被用于调用的情况下，可以使用函数的命名风格代替。
> 注意，对于内置的变量命名有一个单独的约定：大部分内置变量是单个单词（或者两个单词连接在一起），首字母大写的命名法只用于异常名或者内部的常量。

例：

```python
class Washer():
    def wash(self):
        print("洗衣机洗衣服")
```

上例也定义了一个`方法`，方法的定义与函数基本相同。

###### 创建对象

```python 
obj_name = ClassName()
```

例：

```python
# 定义一个类
class Washer():
    def wash(self):
        print("洗衣机洗衣服")
# 创建对象
haier = Washer()
# 对象调用实例方法
haier.wash()

#输出
洗衣机洗衣服
```

###### self

`self`指的是调用该函数的对象，一般打印为内存地址。

对象不同，即内存地址不同，即self不同。

```python
# 定义类
class Washer():
    def wash(self):
        print("洗衣机洗衣服")
        print(self)
# 创建2个对象
haier = Washer()
geli = Washer()
# 分别调用实例方法
haier.wash()
geli.wash()

#输出
洗衣机洗衣服
<__main__.Washer object at 0x000002264128BB20>
洗衣机洗衣服
<__main__.Washer object at 0x000002264128BB50>
```

##### 属性

###### 类外添加属性

```python
obj_name.attribute = value
```

例：

```python
# 使用上述Washer类
# 创建一个对象
haier = Washer()
haier.width = 500
haier.height = 800
```

###### 类外获取属性

```python
obj_name.attribute
```

例：

```python
# 使用上述Washer类
# 使用上述haier实例和属性
print(haier.width)
print(haier.height)
#输出
500
800
```

###### 类内获取对象属性

```python
# 定义类
class Washer():
    def print_info(self):
        # 类里面获取实例属性
        print(self.width)
        print(self.height)

# 创建对象
haier1 = Washer()

# 添加实例属性
haier1.width = 500
haier1.height = 800

haier1.print_info()

#输出
500
800
```

##### 魔法方法

###### \__init__()

`__init__()`方法可以初始化属性。上述属性都是在类外定义的， 这个魔法方法可以让属性在类内初始化定义。

例：

```python 
# 定义一个类
class Washer():
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def print_info(self):
        print(self.width)
        print(self.height)
# 创建一个对象，并使用实例方法
haier = Washer(500,800)
haier.print_info()

# 输出
500
800
```

```python
# 不接受参数的初始化属性
class Washer():
    def __init__(self):
        self.width = 500
        self.height = 800
```

###### \__str__()

通常用print打印对象的时候，会打印其内存地址。如果使用`__str__()`方法，可以打印该方法中返回的数据。

例：

```python
# 定义一个没有__str__方法的类
class Washer():
    def __init__(self):
        self.width = 500
# 创建一个对象
haier = Washer()
# 打印这个对象
print(haier)

# 输出
<__main__.Washer object at 0x0000014A5051BFA0>
```

```python
# 定义一个有__str__方法的类
class Washer():
    def __init__(self):
        self.width = 500
    def __str__(self):
        return "这是一个洗衣机"
# 创建一个对象
haier = Washer()
# 打印这个对象
print(haier)

# 输出
这是一个洗衣机
```

###### \__del__()

当删除一个对象是，Python解释器会默认调用`__del__()`方法。

例：

```python
# 定义一个没有__del__方法的类
class Washer():
    pass
# 创建一个对象
haier = Washer()
# 删除这个对象
del haier
```

```python
# 定义一个有__del__方法的类
class Washer():
    def __del__(self):
        print("该对象已经被删除")
# 创建一个对象
haier = Washer()
# 删除这个对象
del haier
# 输出
该对象已经被删除
```

#### 继承

##### 继承

###### 继承

继承通常为子女继承父母的财产。在面向对象编程中为`子类`继承`父类`的属性和方法。

###### 新式类和旧式类

旧式类，或称经典类。不由任意内置类型派生出的类。已经被Python3.0以后的版本淘汰。

```python
class ClassName():
    pass
```

新式类，继承自object类。`object`类为`基类`。子类也叫做`派生类`。

```python
class ClassName(object):
    pass
# Pyhton3.0以后的版本，默认继承object类，不写也会继承。
```



##### 单继承和多继承

###### 单继承

子类只继承一个父类，该种继承为`单继承`。

例：

```python
# 模拟一家有一个面条技术
# 定义一个父类
class Father(object):
    def __init__(self):
        self.recipe = "祖传面条配方"
    def make_noodles(self):
        print("使用"+self.recipe+"制作面条")
# 定义一个子类
class Son(Father):
    pass
# 使用子类创建一个对象，并调用父类方法和属性
jachin = Son()
print(jachin.recipe)
jachin.make_noodles()

#输出
祖传面条配方
使用祖传面条配方制作面条
```

###### 多继承

一个子类继承了多个父类，为`多继承`。

```python
# 模拟一家有一个祖传面条配方
# 儿子还在学校外学了一个面条配方
# 定义父亲父类
class Father(object):
    def __init__(self):
        self.recipe = "祖传面条配方"
    def make_noodles(self):
        print("使用"+self.recipe+"制作面条")
# 定义学校父类
class School(object):
    def __init__(self):
        self.recipe = "通用面条配方"
    def make_noodles(self):
        print("使用"+self.recipe+"制作面条")

# 定义一个子类
class Son(School,Father):
    pass
# 使用子类创建一个对象，并调用父类方法和属性
jachin = Son()
print(jachin.recipe)
jachin.make_noodles()

# 继承多个父类，遇见同名属性和方法。
# 会默认调用第一个父类的属性和方法。
# 输出
通用面条配方
使用通用面条配方制作面条
```

继承多个父类，遇见同名属性和方法，会默认调用第一个父类的属性和方法。

##### 重写父类同名属性和方法

子类和父类具有同名属性和方法，默认使用子类的同名属性和方法。

```python
# 模拟一家有一个祖传面条配方
# 儿子还在学校外学了一个面条配方
# 现在儿子将两个配方研究，创造了自己独创的秘方。
# 定义父亲父类
class Father(object):
    def __init__(self):
        self.recipe = "祖传面条配方"
    def make_noodles(self):
        print("使用"+self.recipe+"制作面条")
# 定义学校父类
class School(object):
    def __init__(self):
        self.recipe = "通用面条配方"
    def make_noodles(self):
        print("使用"+self.recipe+"制作面条")

# 定义一个子类
class Son(School,Father):
    def __init__(self):
        self.recipe = "独创面条配方"
    def make_noodles(self):
        print("使用"+self.recipe+"制作面条")
# 使用子类创建一个对象，并调用父类方法和属性
jachin = Son()
print(jachin.recipe)
jachin.make_noodles()

#输出
独创面条配方
使用独创面条配方制作面条
```

###### \__mro__属性

`__mro__`属性可以查看该对象所属类的继承关系。该算法用`拓扑排序`构成。

```python
class X(object):pass
class Y(object):pass
class A(X, Y):pass
class B(Y):pass
class C(A, B):pass
print(C.__mro__)
#输出
(<class '__main__.C'>, <class '__main__.A'>, <class '__main__.X'>, <class '__main__.B'>, <class '__main__.Y'>, <class 'object'>)
```

##### 调用父类同名属性和方法

如果子类仍然想调用父类的方法，可以重新写一个方法，让该方法调用父类的方法。但要注意，调用父类的属性则需要用父类重新初始化。

```python
# 模拟一家有一个祖传面条配方
# 儿子还在学校外学了一个面条配方
# 现在儿子将两个配方研究，创造了自己独创的秘方。
# 儿子目前会三种配方，顾客需要哪个就用哪个。
# 定义父亲父类
class Father(object):
    def __init__(self):
        self.recipe = "祖传面条配方"
    def make_noodles(self):
        print("使用"+self.recipe+"制作面条")
# 定义学校父类
class School(object):
    def __init__(self):
        self.recipe = "通用面条配方"
    def make_noodles(self):
        print("使用"+self.recipe+"制作面条")

# 定义一个子类
class Son(School,Father):
    def __init__(self):
        self.recipe = "独创面条配方"
    def make_noodles(self):
        self.__init__()
        print("使用"+self.recipe+"制作面条")
    def make_father_noodles(self):
        Father.__init__(self)
        Father.make_noodles(self)
    def make_school_noodles(self):
        School.__init__(self)
        School.make_noodles(self)

# 使用子类创建一个对象，并调用父类方法和属性
jachin = Son()
print(jachin.recipe)
jachin.make_noodles()
jachin.make_father_noodles()
jachin.make_school_noodles()

# 输出
独创面条配方
使用独创面条配方制作面条
使用祖传面条配方制作面条
使用通用面条配方制作面条
```

##### super()

上条调用父类的属性和方法虽然能实现，但是如果更改父类的类名，便需要大量修改代码，造成了代码的冗余。并且，当出现多继承时，都调用父方法，会出现` 钻石继承`的问题。

故可以使用`super()`函数减少冗余。

super()若不传入参数，便会根据`__mro__`属性的顺序选择第一个有相同方法的父类进行方法调用。

super()若传入参数，第一个参数为自己或一个父类名，第二个参数为`self`。若选择一个父类名，那么调用顺序就从`__mro__`属性中找到该父类名，按顺序从它下一个类开始选择。

例：

```python
# 模拟一家有一个祖传面条配方
# 儿子还在学校外学了一个面条配方
# 现在儿子将两个配方研究，创造了自己独创的秘方。
# 儿子目前会三种配方，顾客需要哪个就用哪个。
# 定义父亲父类
class Father(object):
    def __init__(self):
        self.recipe = "祖传面条配方"
    def make_noodles(self):
        print("使用"+self.recipe+"制作面条")
# 定义学校父类
class School(object):
    def __init__(self):
        self.recipe = "通用面条配方"
    def make_noodles(self):
        print("使用"+self.recipe+"制作面条")

# 定义一个子类
class Son(School,Father):
    def __init__(self):
        self.recipe = "独创面条配方"
    def make_noodles(self):
        self.__init__()
        print("使用"+self.recipe+"制作面条")
    def make_father_noodles(self):
        super(School,self).__init__()
        super(School,self).make_noodles()
    def make_school_noodles(self):
        super().__init__()
        super().make_noodles()

# 使用子类创建一个对象，并调用父类方法和属性
jachin = Son()
print(jachin.recipe)
jachin.make_father_noodles()
jachin.make_school_noodles()

# 输出
独创面条配方
使用祖传面条配方制作面条
使用通用面条配方制作面条
```



##### 多层继承

多层继承就是子类的子类可以继承祖先的属性和方法。

```python
# 模拟一家餐馆，爷爷创立门派。
# 父亲，孙子都继承了爷爷的能力。
class Grandfather(object):
    def __init__(self):
        self.recipe = "祖传面条配方"
    def make_noodles(self):
        print("使用"+self.recipe+"制作面条")
class Fahter(Grandfather):
    pass
class Son(Fahter):
    pass
# 利用Son创建一个对象
jachin = Son()
jachin.make_noodles()
# 输出
使用祖传面条配方制作面条
```

##### 私有属性和私有方法

###### 定义私有属性和私有方法

Python中，设置私有属性和私有方法，可让父类有些属性和方法可以不继承给子类。

设置私有权限的方法：在属性名和方法名前加上两个下划线`__`

```python
class Grandfather(object):
    def __init__(self):
        self.recipe = "祖传面条配方"
        self.__private_assets = "200000000RMb"
    def __private_noodle(self):
        print("不可传")
    def make_noodles(self):
        print("使用"+self.recipe+"制作面条")
class Fahter(Grandfather):
    pass
# 利用Son创建一个对象
jachin = Fahter()
print(jachin.__private_assets)

# 输出
发生异常：
'Fahter' object has no attribute '__private_assets'

jachin.__private_noodle()
# 输出
发生异常：
'Fahter' object has no attribute '__private_noodle'
```

私有属性和私有方法只能在类里面访问和修改。

###### 获取和修改私有属性值

在Python中，习惯使用定义方法名get_xx用来获取私有属性，定义set__xx用来修改私有属性。

```python
class Grandfather(object):
    def __init__(self):
        self.recipe = "祖传面条配方"
        self.__private_assets = "200000000RMb"
    def get_private_assets(self):
        return self.__private_assets
    def set_private_assets(self,money):
        self.__private_assets = money
    
    def __private_noodle(self):
        print("不可传")

    def make_private_noodle(self):
        print("我现在偷偷给你说")
        self.__private_noodle()
    
    def make_noodles(self):
        print("使用"+self.recipe+"制作面条")
class Father(Grandfather):
    pass
# 利用Father创建一个对象
jachin = Father()
jachin.set_private_assets("30RMB")
print(jachin.get_private_assets())
jachin.make_private_noodle()
# 输出
30RMB
我现在偷偷给你说
不可传
```

#### 多态

##### 多态

多态指的是一类事物有多种形态。

多态是一种使用对象的方式，子类重写父类方法，调用不同子类对象的相同父类方法，可以产生不同的执行结果

##### 使用方法

```python
class Animal(object):
    def calls(self):
        pass
class Dog(Animal):
    def calls(self):
        print("bark")
class Bee(Animal):
    def calls(self):
        print("buzz")
class Bird(Animal):
    def calls(self):
        print("tweet")
class Person(object):
    def play_with_animal(self,animal):
        animal.calls()
huahua = Dog()
jiji = Bee()
tutu = Bird()
jachin = Person()
jachin.play_with_animal(huahua)
jachin.play_with_animal(jiji)
jachin.play_with_animal(tutu)

# 输出
bark
buzz
tweet
```

#### 类属性和实例属性

##### 类属性

###### 设置类属性

`类属性`就是`类对象` 所拥有的属性，它被该类的所有实例对象所共有。

类属性可以使用`类对象`或`实例对象`访问。

因此，当需要**记录某项数据需要保存一致时**，则定义类属性。

`实例属性`要求每个对象为其开辟一份独立的内存空间来记录数据，但`类属性`为全类所共有，改一份，全类都会被改。

```python
class Dog(object):
    feet = 4

xiaotianquan = Dog()
xiaomei = Dog()

print(Dog.feet)
print(xiaotianquan.feet)
print(xiaomei.feet)
# 输出
4
4
4
```

###### 修改类属性

类属性只能通过类对象修改，不能通过实例对象修改，如果通过实例对象修改类属性， 表示的是为该实例对象创建了一个实例属性。

```python
class Dog(object):
    feet = 4

xiaotianquan = Dog()
xiaomei = Dog()


# 修改类属性
Dog.feet = 2
print(Dog.feet)
print(xiaotianquan.feet)
print(xiaomei.feet)

# 用实例对象修改
xiaotianquan.feet = 3
print(Dog.feet)
print(xiaotianquan.feet)
print(xiaomei.feet)

# 输出
2
2
2
2
3
2
```

##### 实例属性

实例属性就是通常通过`__init__()`魔法方法创建的属性，它不能通过类访问。

#### 类方法和静态方法

##### 类方法

###### 类方法特点

需要使用装饰器`@classmethod`来标识其为类方法，对于类方法，**第一个参数必须是类对象**，一般以cls作为第一个参数。

###### 使用场景

当方法中需要使用`类对象`，比如访问私有类属性时，定义类方法。

类方法一般和类属性配合使用。

```python
class Dog(object):
    __feet = 4
    @classmethod
    def get_feet(cls):
        return cls.__feet
xiaotianquan = Dog()
print(xiaotianquan.get_feet())
# 输出
4
```

##### 静态方法

###### 静态方法特点

- 需要通过装饰器`@staticmethod`来进行修饰，**静态方法既不需要传递类对象也不需要传递实例对象（形参没有self/cls）**。
- 静态方法 也能够通过 `实例对象` 和 `类对象` 去访问。

###### 使用场景

- 当方法中 **既不需要使用实例对象**(如实例对象，实例属性)，**也不需要使用类对象** (如类属性、类方法、创建实例等)时，定义静态方法
- **取消不需要的参数传递**，有利于 **减少不必要的内存占用和性能消耗**

```python
class Dog(object):
    @staticmethod
    def info_print():
        print('这是一个狗类，用于创建狗实例....')
wangcai = Dog()
# 静态方法既可以使用对象访问又可以使用类访问
wangcai.info_print()
Dog.info_print()
# 输出
这是一个狗类，用于创建狗实例....
这是一个狗类，用于创建狗实例....
```

### 

### 文件和异常

### 常用库函数

#### `random`库
