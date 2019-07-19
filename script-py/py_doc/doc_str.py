import string

s = 'The quick brown fox jumped over the lazy dog.'
print (s)
print(string.capwords(s))
#用字典的键值对来实现参数的替换，用$符号时要用{}作为包裹体
values = {'var':'foo'}
print(type(values))
t = string.Template("""
Variable        :$var
Escape          :$$
Variable in text:${var}iable
""")
#TypeError: 'set' object is not subscriptable:{'var','foo'}#<class 'set'>
#上面的错打成逗号之后values类型就是集合（set）了吐过是冒号的话就是字典了，造成后面的错误。动态类型的问题
print('TEMPLATE',t.substitute(values))

s = """
Variable        : %(var)s
Escape          : %%
Variable in text: %(var)siable
"""
#用%符号时要用（）作为包裹体
print('INTERPOLATION',s %values)

s = """
Variable        : {var}
Escape          : {{}}
Variable in text: {var}iable
"""
print('FORMAT',s.format(**values))
"""
上面三种方法的一个关键不同点是：没有考虑参数的类型。这些值被转换成字符串，然后插入到结果当中，没有可用的格式化选项。例如，无法控制用来表示浮点数的数字的个数。
"""

values = {'var3': 'foo3'}
t = string.Template("$var3 is here but $missing is not provided")
try:
    print('substitute()     :', t.substitute(values))
except KeyError as err:
    print('ERROR:', str(err))
#KeyError: 'missing'如果不使用safe的话
print('safe_substitute():', t.safe_substitute(values))
print("default pattern is :",t.pattern.pattern)

import inspect

def is_str(value):
    return isinstance(value,str)
for name,value in inspect.getmembers(string,is_str):
    if name.startswith("_"):
        continue
    print('%s=%r\n' % (name,value))



