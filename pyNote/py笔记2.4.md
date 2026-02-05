# 数据类型

## int整形（就像是整数）

## float浮点形（带小数点的）

## bool布尔型（True为1，False为0）

## complex虚数（a+bj）



# 字符串



## 字符串运算符

“+”是字符串连接

“*”是重复输出结果

“[]”通过索引获取字符串中的某一部分

“[:]”截取字符串中的一部分

“in”如果字符串中包含给定的字符返回True

“not in”如果不在就True

```python
a = "Hello"
b = "Python"
print(a+b)  #"HEello Python"
print(a*2)  #“Hello Hello”
print(a[1])  #"e"
print(a[1:4])  #"ello"
print('H' in a)  #True
print('M' not in a)  #True

# 切片可以选步长，不写默认一，正负号表示切取方向,第三个空的位置便是步长
st = "abcdefghijk"
print(st[3:])  #defghijk
print(st[0:7:2])  #aceg  
```

## 字符串常见操作

find()  检测字符是否包含在字符串中，找不到会返回-1，找到了输出下标位置  #xxx.find(“xxx”,开始,结束)

count()  返回出现的次数  #xxx.count(‘’)

replace()  替换  #xxx.replace(‘老的’,’新的)

split()  分割  #xxx.split(‘以什么分割’)

index()  跟find一样，但是找不到会报错

startwith(‘子字符串’，开始，结束)  判断某个字符串是否以某个子字符串开头，是就True，否就False

endwith()  判断是否以某个字符结尾

isupper() 判定所有字母是否大写

capitalize()变为第一个字母大写，其他全小写

title() 则是将每个单词的开头大写

lower()大写字母转为小写

upper()全部大写

```python
print(a.find("H",开始位置，结束位置))  #0#省略与结束表示整个字符串寻找
xxxx.index("xxxx",开始,结束)
```

# 列表

## 添加元素

append()  整体添加‘four’

extend()  分散添加‘f’,’o’,’u’,’r’  添加内容得是可迭代对像如字符串和列表

insert()  指定位置插入  xxx.insert(0,’four’)

## 修改内容

xxx.[下标] = ‘xxx’

## 删除元素

del xxx 删除整个列表

del xxx[下标] 删除下标的元素

pop 删除指定下标的元素 xxx.pop未指定则删除列表最后一个元素

xxx.remove(‘xxx’)  按照元素删除，若重复则删除第一次出现位置的元素

## 其他操作

xxx.sort()  排序

reverse  倒序

## 列表推导式

[表达式 for 变量 in 列表]

[li.append(i) for i in range(1,6)]  #1~5添加至列表

[表达式 for 变量 in 列表 if 条件]

[li.append(i) for i in range(1,6) if i%2 ==1]  #把奇数添加入列表

# 元组

元组tuple只支持查询，不支持增删改

len()  可以给出列表与元组的长度

# 字典

字典以键值对保存，键具有唯一性，值可以重复

dic = {‘name’:’xxxx’,’age’:’18’}

键名重复不会报错，但是会把前面的覆盖掉

## 字典操作

### 查看元素

xxx.get(键名)

xxx.[键名]

### 添加元素

xxx[‘键名’] = 数据

### 修改

通过键找到即可修改（直接赋值）

用update方法批量操作

```python
# 创建原始字典
my_dict = {'key1': 'value1', 'key2': 'value2'}

# 批量更新和追加
my_dict.update({'key1': 'new_value1', 'key3': 'value3'})

print(my_dict)  # 输出: {'key1': 'new_value1', 'key2': 'value2', 'key3': 'value3'}
```

### 删除元素

del xxx 删除指定元素

xxx.clear 清空整个字典

xxx.pop(‘xxx’) 删除指定键值对]

xxx.popitem()  默认删除最后一个

### 取出值

xxx.values()

xxx.items()  以元组形式返回

# 集合

无序性 唯一性

可用于元组或列表的去重



集合可以是数字，字符串，元组（可哈希）

不能是列表，其他集合，字典或自定义对象

## 集合常见操作

add()  添加一个整体

update()  把传入元素拆分一个个放入集合中  #得是可迭代对象

pop()  随便删一个

discard 选择元素删，有就删，无就无事发生



交集&  并集|

