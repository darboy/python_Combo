'''
类所包含的最重要的两个成员就是方法和变量，其中类变量属于类本身，用于定义该类本身所包含的状态和数据，
实例变量则属于该类的对象，用于定义对象所包含的状态和数据，方法则用于定义该类的对象的行为或功能实现。
'''
class Person:
    hair = 'black'                      #类的变量
    def __init__(self, name = 'wangbadan', age = 8):            #构造方法，用于构造类的对象
        self.name = name            #实例变量
        self.age = age 
    def say(self, content):          #定义了一个方法
        print(content)
    
p = Person()
# print(p.name, p.age)
# p.name = 'gaoxiao'
# print(p.hair)
# p.say('sfdasdfa')
# w = Person()
# print(w.hair)

'''
python是动态语言，可以动态删除增加实例变量，也可以动态增加方法，不过有区别
'''
p.height = 12       #增加height变量
del p.name             #删除name变量，后面再访问就会出错,但是不会对其他对象造成影响，如下
w = Person()
# print(w.name)
# print(p.height)

'''
p对象动态增加方法，python不会自动将调用者自动绑定到第一个参数
'''
def addMethod(self, content):
    print('sdf',self, content)

p.add_method = addMethod            
# p.add_method(p, "sdfdf")     #手动绑定到第一个参数, 否则会报缺形参,不像本身存在的方法，self不用传入参数

'''
类方法和静态方法,类方法通常第一个参数为cls，会自动绑定到类本身，而静态方法则需要手动绑定
'''
class Bird:
    @classmethod
    def fly(cls):
        print("woshi", cls)
    @staticmethod
    def info(dsf):
        print('asdf', dsf)

b = Bird()
# b.fly()
# b.info('sdfsd')

'''
@函数装饰器
@函数A装饰函数B，将函数B作为参数传给函数A，将函数B替换成传入A后的返回值。
可以用来在被修饰的函数前面增加一些额外的处理逻辑
'''
def auth(fn):
    def auth_fn(*args):
        print('检查一下')
        fn(*args)
    return auth_fn

@auth
def test(a,b):
    print('a = ',a,' b = ',b)

# test(1,3)

'''
类的命名空间
python的类就像命名空间，并且允许在全局范围内放置可执行代码,执行一次就不再执行
'''
class NameSpace:
    if 1 :
        # print('试一下')
        1+1
    def info(self, ss):
        self.ss = ss

# name_space = NameSpace()
# name_space.info('sdfsdf')
# print(name_space.ss)
# dddd = NameSpace()          #这次实例化对象，不会执行类中的执行代码，代码执行一次就完了。 

'''
类变量和实例变量
类变量就像是在命名空间中定义变量一样，访问必须通过类访问。
通过对象访问类变量并对其赋值，实际上是定义一个新的实例变量，不会对类变量产生影响。
'''
class ClassVarAndInstanceVar:
    temp1 = 'sdfs'                  
    def info(self, temp1):
        print(self.temp1)
        self.temp1 = temp1      #不影响temp1类变量，等于新的实例变量

# print(ClassVarAndInstanceVar.temp1)
# class_var = ClassVarAndInstanceVar()
# class_var.info('ggg')
# print(class_var.temp1)
# print(ClassVarAndInstanceVar.temp1)

'''
property函数定义属性
如果类中定义了getter、setter等访问器的方法，可以使用property函数将它们定义成属性，相当于实例变量。
property(fget = None, fset = None, fdel = None, doc = None)
'''
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def setSize(self, size):
        self.width,self.height = size
    def getSize(self):
        return self.width, self.height
    def delSize(self):
        self.width,self.height =0,0
    size = property(getSize, setSize, delSize, '描述矩形大小的属性')

# print(Rectangle.size.__doc__)   #访问size属性的说明文档
# help(Rectangle.size)            #用help方法访问
# rect = Rectangle(12,32)
# print(rect.size)        #返回的是getSize的返回值
# rect.size = 32,43           #赋值的是setSize
# print(rect.height)
# del rect.size                #调用的是delSize
# print(rect.width)