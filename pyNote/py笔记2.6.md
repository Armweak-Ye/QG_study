# 简介类

- **类(Class):** 用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。
- **类变量：**类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。
- **数据成员：**类变量或者实例变量, 用于处理类及其实例对象的相关的数据。
- **方法重写：**如果从父类继承的方法不能满足子类的需求，可以对其进行改写，这个过程叫方法的覆盖（override），也称为方法的重写。
- **局部变量：**定义在方法中的变量，只作用于当前实例的类。
- **实例变量：**在类的声明中，属性是用变量来表示的。这种变量就称为实例变量，是在类声明的内部但是在类的其他成员方法之外声明的。
- **继承：**即一个派生类（derived class）继承基类（base class）的字段和方法。继承也允许把一个派生类的对象作为一个基类对象对待。例如，有这样一个设计：一个Dog类型的对象派生自Animal类，这是模拟"是一个（is-a）"关系（例图，Dog是一个Animal）。
- **实例化：**创建一个类的实例，类的具体对象。
- **方法：**类中定义的函数。
- **对象：**通过类定义的数据结构实例。对象包括两个数据成员（类变量和实例变量）和方法。

## 创建类

```python
class 类名：
	'类的说明性文字'
```

一个完整的整体大致如下

```python
class 类名：
	'说明性文字'
    类属性
创建类方法
    def __init__(self):
    	代码
    def funa():
        代码
实例化对象
利用对象使用类方法
```

例如

```python
class Employee:
    '所有员工的基类'
    '创建类属性'
	empCount = 0
	' 创建类方法'
   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print "Total Employee %d" % Employee.empCount
 
   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary
 
"创建 Employee 类的第一个对象"
emp1 = Employee("Zara", 2000)
"创建 Employee 类的第二个对象"
emp2 = Employee("Manni", 5000)
"利用对象调用类方法"
emp1.displayEmployee()
emp2.displayEmployee()
print "Total Employee %d" % Employee.empCount
```

输出结果如下

```python
"""
Name :  Zara ,Salary:  2000
Name :  Manni ,Salary:  5000
Total Employee 2
"""
```

## 创建类方法

第一个方法要有def \_\_init\_\_ (self)  这个\_\_init\_\_一种特殊的方法，被称为类的构造函数或初始化方法，当创建了这个类的实例（实例化时）时就会调用该方法  **用此方法传参**

剩余的方法直接def 方法名(self)即可

self 代表类的实例，self 在定义类的方法时是必须有的，虽然在调用时不必传入相应的参数

## 实例化对象

==对象名 = 类名（）==

## 使用

==对象名.类方法名()==

你可以使用以下函数的方式来访问属性：

- getattr(obj, name[, default]) : 访问对象的属性。
- hasattr(obj,name) : 检查是否存在一个属性。
- setattr(obj,name,value) : 设置一个属性。如果属性不存在，会创建一个新属性。
- delattr(obj, name) : 删除属性。

```python
# 前面记得加print
hasattr(emp1, 'age')    # 如果存在 'age' 属性返回 True。
getattr(emp1, 'age')    # 返回 'age' 属性的值
setattr(emp1, 'age', 8) # 添加属性 'age' 值为 8
delattr(emp1, 'age')    # 删除属性 'age'
```

## Python内置类属性

- __dict__ : 类的属性（包含一个字典，由类的数据属性组成）
- __doc__ :类的文档字符串
- __name__: 类名
- __module__: 类定义所在的模块（类的全名是'__main__.className'，如果类位于一个导入模块mymod中，那么className.__module__ 等于 mymod）
- __bases__ : 类的所有父类构成元素（包含了一个由所有父类组成的元组）

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
class Employee:
   '所有员工的基类'
   empCount = 0
 
   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print "Total Employee %d" % Employee.empCount
 
   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary
 
print "Employee.__doc__:", Employee.__doc__
print "Employee.__name__:", Employee.__name__
print "Employee.__module__:", Employee.__module__
print "Employee.__bases__:", Employee.__bases__
print "Employee.__dict__:", Employee.__dict__
```

```python
'''
Employee.__doc__: 所有员工的基类
Employee.__name__: Employee
Employee.__module__: __main__
Employee.__bases__: ()
Employee.__dict__: {'__module__': '__main__', 'displayCount': <function displayCount at 0x10a939c80>, 'empCount': 0, 'displayEmployee': <function displayEmployee at 0x10a93caa0>, '__doc__': '\xe6\x89\x80\xe6\x9c\x89\xe5\x91\x98\xe5\xb7\xa5\xe7\x9a\x84\xe5\x9f\xba\xe7\xb1\xbb', '__init__': <function __init__ at 0x10a939578>}
'''
```

# 封装

**封装是指将数据（属性）和操作数据的方法（方法）捆绑在一起的机制。**在封装中，对象的内部细节被隐藏起来，只有特定的方法才能访问和操作这些细节。这有助于确保数据的安全性和代码的可维护性。

## 如何实现封装？

封装可以通过访问控制和访问修饰符来实现。主要有两种访问修饰符：**公有属性和方法、私有属性和方法。**

- **公有属性和方法 (Public Attributes and Methods)**

可以被类的外部访问。在 Python 中，默认情况下，类的所有属性和方法都是**公有的**。

```python
class Person:
    def __init__(self, name, age):
        self.name = name   # 公有属性
        self.age = age     # 公有属性

    def get_name(self):
        return self.name   # 公有方法

# 使用公有属性和方法
person1 = Person("Tiyong", 30)
print(person1.name)  # 输出: Tiyong
print(person1.get_name())  # 输出: Tiyong
```

在这个例子中，Person类有一个公有方法 `get_name()`，那么其他类或代码可以通过调用这个方法来获取对象的名称。同样，有一个公有属性 **age**，那么其他类或代码可以直接访问和修改这个属性。所以，**我们的实例对象就可以访问公共的属性和方法。**

- **私有属性和方法 (Private Attributes and Methods)**

只能在类的内部访问，外部无法直接访问。在 Python 中，可以在属性名或方法名前加上双下划线 ‘`**__**`’ 来定义私有属性和方法。

如果是单下划线的私有方法只是导包时不能用，子类还是可以继承的

```python
class Person:
    def __init__(self, name, age):
        self.__name = name   # 私有属性
        self.__age = age     # 私有属性

    def __display_info(self):
        return f"Name: {self.__name}, Age: {self.__age}"   # 私有方法

# 外部无法直接访问私有属性和方法
person1 = Person("TiYong", 25)
# print(person1.__name)  # 这会引发错误，因为__name是私有属性
# print(person1.__display_info())  # 这会引发错误，因为__display_info()是私有方法
```

在上面的例子中：person1对象就不能访问__name私有属性和__display_info()私有方法。

尽管外部无法直接访问私有属性和方法，但我们仍然可以通过公有方法来间接访问和操作它们。这种间接访问的方式使得我们可以控制对象的状态和行为，确保数据的一致性和安全性。

```python
class Person:
    def __init__(self, name, age):
        self.__name = name   # 私有属性
        self.__age = age     # 私有属性

    def get_name(self):
        return self.__name   # 公有方法

    def set_name(self, new_name):
        self.__name = new_name   # 公有方法，用于修改私有属性

    def display_info(self):
        return f"Name: {self.__name}, Age: {self.__age}"   # 公有方法

# 通过公有方法访问和修改私有属性
person1 = Person("TiYong", 30)
print(person1.get_name())  # 输出: TiYong
person1.set_name("Toy")
print(person1.display_info())  # 输出: Name: Toy, Age: 30
```

#  继承

继承就是允许一个类（称为子类或派生类）**继承**另一个类（称为父类或基类）的属性和方法。子类可以**继承**父类的特性，并且可以在此基础上添加自己的**新特性**。这种机制允许代码的重用和层次化的设计。继承，就是字面上意思，继承。

## 调用父类方法可用super函数

```python
class Animal(object):
    def __init__(self, name):
        self.name = name

    def greet(self):
        print('Hello, I am %s.' % self.name)


class Dog(Animal):
    def greet(self):
        super(Dog, self).greet()  #调用父类Animal的greet方法
        print('WangWang...')


d=Dog("xiaohuang")

d.greet()
```

```python
'''
Hello, I am xiaohuang.
WangWang...
'''
```

```python
class Base(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b


class A(Base):
    def __init__(self, a, b, c):
        super(A, self).__init__(a, b)  # Python3 可使用 super().__init__(a, b)
        self.c = c

a=A(100,200,300)

print("a=%d, b=%d, c=%d" % (a.a,a.b,a.c))

```

```python
'''
a=100, b=200, c=300

Process finished with exit code 0
'''
```



## 单继承

```python
class parrnt:
    xxxxx
class child(parent):
```

##  多继承

```python
class ParentClass1:
    def method1(self):
        print("Method 1 from ParentClass1")

class ParentClass2:
    def method2(self):
        print("Method 2 from ParentClass2")

class ChildClass(ParentClass1, ParentClass2):
    def child_method(self):
        print("Child method")

# 子类继承多个父类的方法
child = ChildClass()
child.method1()  # 输出: Method 1 from ParentClass1
child.method2()  # 输出: Method 2 from ParentClass2
child.child_method()  # 输出: Child method
```

父类的方法是可以被覆盖的

子类可以覆盖父类的方法，即在子类中重新定义与父类同名的方法。这样做可以根据子类的需求修改方法的实现。

```python
class Bird:
    def speak(self):
        return "Chirp!"

class Parrot(Bird):
    def speak(self):
        return "Polly wants a cracker!"

parrot = Parrot()
print(parrot.speak())  # 输出: Polly wants a cracker!
```

# 多态

**多态**是指允许对象在不同的情况下表现出不同的行为。简单地说，多态性意味着相同的方法调用可能会有不同的实现方式，具体取决于调用该方法的对象的类型或类的实现

* 方法重写
* 方法重载

方法重写是实现多态的一种方式，它允许子类覆盖（重写）父类的方法，以便在子类中实现特定的行为。当子类重新定义了与父类**同名的方法时**，调用这个方法时会执行子类的实现。通过一个例子展示方法重写：

```python
class Animal:
    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# 多态性的体现
def animal_sound(animal):
    return animal.speak()

dog = Dog()
cat = Cat()

print(animal_sound(dog))  # 输出: Woof!
print(animal_sound(cat))  # 输出: Meow!
```

方法重载是一种在**同一个类中**，方法名称相同但参数列表不同的技术。但是，在Python中，并没有像其他编程语言那样直接支持方法重载的特性，不过，可以通过一些技巧来模拟。

比如：使用默认参数值或者 `*args` 和 `**kwargs` 参数来实现类似方法重载的效果。

```python
class Calculator:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c

calc = Calculator()
print(calc.add(2, 3))    # 输出: TypeError: add() missing 1 required positional argument: 'c'
print(calc.add(2, 3, 4))  # 输出: 9
```

