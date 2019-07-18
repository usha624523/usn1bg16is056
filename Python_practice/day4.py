Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> fruits=['apple','guava','mango','papaya','banana']
>>> print(fruits[3])
papaya
>>> print(fruits[0])
apple
>>> fruits[-1]
'banana'
>>> empty_list=[]
>>> x=[7,]
>>> print(len(x))
1
>>> x=[0,1,2,[3,4],"name",0.7]
>>> print(x[3[1]])
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    print(x[3[1]])
TypeError: 'int' object is not subscriptable
>>> print(x[3:1])
[]
>>> print(x[3,1])
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    print(x[3,1])
TypeError: list indices must be integers or slices, not tuple
>>> x[3][1]
4
>>> mobile=8789023952
>>> print(mobile[4])
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    print(mobile[4])
TypeError: 'int' object is not subscriptable
>>> name='usha'
>>> print(name[2])
h
>>> x=[1,2,3,4,5,5]
>>> x[5]=6
>>> x
[1, 2, 3, 4, 5, 6]
>>> print(x)
[1, 2, 3, 4, 5, 6]
>>> x=[1,2,3,4,5,5]
>>> x[3]=x[0]
>>> print(x[3])
1
>>> x
[1, 2, 3, 1, 5, 5]
>>> print(x[0])
1
>>> x=3*x
>>> x
[1, 2, 3, 1, 5, 5, 1, 2, 3, 1, 5, 5, 1, 2, 3, 1, 5, 5]
>>> x=x+[7,8,9]
>>> x
[1, 2, 3, 1, 5, 5, 1, 2, 3, 1, 5, 5, 1, 2, 3, 1, 5, 5, 7, 8, 9]
>>> print("apple" in fruits)
True
>>> print("aa" in fruits)
False
>>> num=[10,9,8,7,6,5]
>>> num[0]=num[1]-5
>>> num
[4, 9, 8, 7, 6, 5]
>>> if 4 in num:
	print(num[3])

	
7
>>> if 4 in num:
	print(num[3])
else:
	print(num[4])

	
7
>>> x=[1,2,3]
>>> 
 RESTART: C:/Users/usha kiran/AppData/Local/Programs/Python/Python37/not_pract.py 
True
True
False
False
>>> x=[1,2,3]
>>> x.append(4)
>>> x
[1, 2, 3, 4]
>>> x="hello"
>>> x.append("usha")
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    x.append("usha")
AttributeError: 'str' object has no attribute 'append'
>>> x=["hello"]
>>> x.append("usha")
>>> x
['hello', 'usha']
>>> x[1]
'usha'
>>> lex(x)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    lex(x)
NameError: name 'lex' is not defined
>>> len(x)
2
>>> dir__builtins__
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    dir__builtins__
NameError: name 'dir__builtins__' is not defined
>>> dir(__builtins__)
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'WindowsError', 'ZeroDivisionError', '_', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']
>>> x=["bangalore","capital","of","karnataka"]
>>> index=1
>>> x.insert(index,"is")
>>> x
['bangalore', 'is', 'capital', 'of', 'karnataka']
>>> x.index("karnataka")
4
>>> x.index("banagalore")
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    x.index("banagalore")
ValueError: 'banagalore' is not in list
>>> x.index("bangalore")
0
>>> x=[9,8,7,6,5]
>>> x.append(4)
>>> x.insert(2,11)
>>> x
[9, 8, 11, 7, 6, 5, 4]
>>> len(x)
7
>>> x=["jan","march"]
>>> n=input("enter b'day month:")
enter b'day month:june
>>> while n not in x:
	print("wrong guess")
	break
else:
	print("yes")

	
wrong guess
>>>  n=input("enter b'day month:")
 
SyntaxError: unexpected indent
>>> n=input("enter b'day month:")
enter b'day month:jan
>>> while n not in x:
	print("wrong guess")
	break
else:
	print("yes")

	
yes
>>> list=[99,87,65,1]
>>> max(list)
99
>>> min(list)
1
>>> list.sort()
>>> list
[1, 65, 87, 99]
>>> l1=[1,3,4,5]
>>> l2=[1,3]
>>> l1-l2
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    l1-l2
TypeError: unsupported operand type(s) for -: 'list' and 'list'
>>> print(diff(l1,l2))
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    print(diff(l1,l2))
NameError: name 'diff' is not defined
>>> filter(l1,l2)
<filter object at 0x00000220DB71AD48>
>>> slice(l1,l2)
slice([1, 3, 4, 5], [1, 3], None)
>>> set(l1)-set(l2)
{4, 5}
>>> l2=[1,4]
>>> set(l1)-set(l2)
{3, 5}
>>> import random
>>> list=["apple","orange","mango","grapes"]
>>> list
['apple', 'orange', 'mango', 'grapes']
>>> random.choice(list)
'mango'
>>> random.choice(list)
'orange'
>>> random.choice(list)
'grapes'
>>> random.choice(list)
'grapes'
>>> random.choice(list)
'mango'
>>> random.choice(list)
'apple'
>>> random.suffle(list)
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    random.suffle(list)
AttributeError: module 'random' has no attribute 'suffle'
>>> random.shuffle(list)
>>> list
['apple', 'mango', 'orange', 'grapes']
>>> random.shuffle(list)
>>> list
['mango', 'orange', 'apple', 'grapes']
>>> list=[1,1,1,2,3,4,4,5]
>>> l=[1,1,1,2,3,4,4,5]
>>> l=dict.fromkeys(l)
>>> l
{1: None, 2: None, 3: None, 4: None, 5: None}
>>> l=list(dict.fromkeys(l))
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    l=list(dict.fromkeys(l))
TypeError: 'list' object is not callable
>>> l = list(dict.fromkeys(l))
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    l = list(dict.fromkeys(l))
TypeError: 'list' object is not callable
>>> x=[1,1,1,2,3,4,4,5]
>>> x = list(dict.fromkeys(x))
Traceback (most recent call last):
  File "<pyshell#114>", line 1, in <module>
    x = list(dict.fromkeys(x))
TypeError: 'list' object is not callable
>>> x=list(dict.fromkeys(x))
Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    x=list(dict.fromkeys(x))
TypeError: 'list' object is not callable
>>> x=[1,2,3,3,4,4]
>>> x=list(dict.fromkeys(x))
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    x=list(dict.fromkeys(x))
TypeError: 'list' object is not callable
>>> x=[1,2,3]
>>> if len(x)==0:
	print("empty list")
else:
	print("not empty")

	
not empty
>>> x=[]
>>> if len(x)==0:
	print("empty list")
else:
	print("not empty")

	
empty list
>>> if len(x)!=0:
	print("not empty")
else:
	ptint("empty")

	
Traceback (most recent call last):
  File "<pyshell#131>", line 4, in <module>
    ptint("empty")
NameError: name 'ptint' is not defined
>>> if len(x)!=0:
	print("not empty")
else:
	print("empty")

	
empty
>>> x=[1,2,3]
>>> if len(x)!=0:
	print("not empty")
else:
	print("empty")

	
not empty
>>> if (len(x) is not 0):
	print("not empty")
else:
	print("empty")

	
not empty
>>> list.count(x)
0
>>> x=[1,2,3,4]
>>> list.count(x)
0
>>> x=[1,1,1,2,2,3,4]
>>> list.count(x)
0
>>> x=[1,1,1,2,3,4]
>>> list.count(x)
0
>>> x.count(1)
3
>>> x.reverse()
>>> x
[4, 3, 2, 1, 1, 1]
>>> 
