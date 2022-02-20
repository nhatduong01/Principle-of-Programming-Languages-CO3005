from functools import reduce


def compose(fun1,fun2,*funs):
    a = reduce(lambda x,y: lambda z: x(y(z)),funs[::-1],lambda x: x)
    return lambda x: fun1(fun2(a(x)))
def compose1(fun1, fun2):
    return lambda x: fun1(fun2(x))
def compose2(*funs):
    return reduce(lambda x,y: lambda z: x(y(z)),funs,lambda x: x)
def inc1(x):
    return x +1
def square(x):
    return x *x
def cube(x):
    return x**3
def fouth(x):
    return x + 4 
a = compose(inc1, square, cube,fouth)
print(a(3))