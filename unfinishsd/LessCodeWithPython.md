**摘要**：熟练掌握Python的map、filter、 reduce、 lambda以及list comprehension的用法，可以让你写出高效率的代码。

<h4>1. map</h4>

大多数的for循环可以用map来代替。`map(func,seq)`自动地将`func`施加到`seq`的每一个元素，并返回执行结果。

**例1** 返回list `array=[3,5,7,12,18]`每个元素的立方组成的新list。

用for循环的解法

```python
array = [3,5,7,12,18]
cube_array = []

def cube(x):
    return x**3
    
for a in array:
    cube_array.append(cube(a))
    
```

或者简单一点：

```python
array = [3,5,7,12,18]
cube_array = []

for a in array:
    cube_array.append(a**3)
```

用map只需要一行（array的定义不算啦）

```
array = [3,5,7,12,18]
cube_array = map(lambda a:a**3,array)
```

刚才我们说，map的第二个参数是一个sequence，这里的sequence是我们的array，而map的意思，是对这个array进行一种操作。什么操作呢？这个操作由第一个参数来定义。

这里的第一个参数，是一个lambda函数。lambda在Python里面称为匿名函数，就是说它是个函数，却没有名称。lambda关键词之后的冒号前面用来定义参数，冒号后面用来定义我们要返回的东西。在这里，我们传入的参数是一个a，返回a的立方。而a是什么呢？a是array里面的每一个元素。

如果map和lambda的交叉使用一下子让你招架不住的话，可以看看下面这个例子：

```python
array = [3,5,7,12,18]

def cube(a):
    return a**3

cube_array = map(cube,array)
```

这里map的第一个参数是一个函数名cube，我们另外定义了这个函数。但由于这个函数实在太简单，我们没有必要按照惯常的方法，给它一个名字，郑重其事地出来，而是用lambda这样一种取巧的方法。

什么时候可能用lambda呢？函数特别简单的时候可能可以用，但注意，这里这个函数最好是我们从头到尾只会调用一次的。如果是那种简单但却会被反复调用的函数模块，还是给它一个名字比较好。不然每次都要写出lambda函数也是很麻烦。

lambda的更多注意事项可以参考[这篇](https://pythonconquerstheuniverse.wordpress.com/2011/08/29/lambda_tutorial/)。

这个例子也可以用Python强大的list comprehension来实现：
```python
array = [3,5,7,12,18]
cube_array = [x**3 for x in array]
```

同样是一行。至于哪一种更好，就看你自己了。


<h4>2. filter</h4>
filter顾名思义，是对一个sequence中的每一个元素进行过滤，返回符合条件的那些元素。用法是`filter(func,seq)`，和map很像。

**例2** 返回array中的所有奇数。

```python
array = [1,3,5,7,9,12,14,33,35]
print filter(lambda x:x%2, array)
```

这里是对2取余，返回结果为True的元素。那么什么情况下结果为True？Python里面不为`0`，`None`或者`null`都是True。所以结果就是，偶数是False，奇数是True，返回所有奇数。

**例3** 返回含有'Hi'的字符串。

```python
s = ['Hi Steven!','Hi David','How are you?']
print filter(lambda x:x.count('Hi'),s)
```

count计算'Hi'的出现次数，只要不是0的都会返回。

filter的功能也可以用list comprehension来实现。

```python
s = ['Hi Steven!','Hi David','How are you?']
print [i for i in s if i.count('Hi')]
```

也是非常简洁。如果用普通的for循环，虽然也是简单，但可能就要多写几行了。

<h4>3. reduce</h4>

<h4></h4>
<h4></h4>
