'''
作业一：
区分以下类型哪些是容器序列哪些是扁平序列，哪些是可变序列哪些是不可变序列：
list    可变序列    容器序列
tuple   不可变序列  容器序列
str     不可变序列  扁平序列
dict    可变序列    容器序列
collections.deque   可变序列    容器序列
'''
import time

'''
实现 map() 函数的功能。
用法：map(function, iterable, ...)
当iterable只有一个时，将函数func作用于这个iterable的每个元素上
当iterable多于一个时，map可以并行（注意是并行）地对每个iterable执行
func为None时，默认实现zip() 函数
'''
def my_map(func, *args):
    if func:
        for a in zip(*args):
            yield func(*a)
    else:
        for a in zip(*args):
            yield a

# 实现一个 @timer 装饰器，记录函数的运行时间，注意需要考虑函数可能会接收不定长参数。
def timer(func):
    def inner(*args,**kwargs):
        start = time.time()
        ret = func(*args, **kwargs)
        end = time.time()
        print(f"该函数运行的时长为{end - start}")
        return ret
    return inner

@timer
def foo(x,y):
    time.sleep(1)
    return x**y

if __name__ == '__main__':
    print(list(my_map(None, range(7))))
    print(list(my_map(None, [1,2,3],[4,5,6,7,8])))
    print(foo(3, 4))