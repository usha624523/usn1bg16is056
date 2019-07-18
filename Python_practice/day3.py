Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> i=1
>>> while i<=5:
	print(i)
	i=i+1

	
1
2
3
4
5
>>> i=1
>>> while i>=0:
	print(i)
	i=i-1

	
1
0
>>> i=3
>>> while i>=0:
	print(i)
	i=i-1

	
3
2
1
0
>>> x=0
>>> while x<=20:
	print(x)
	x=x+1

	
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
>>> x=0
>>> while x<=40:
	print(x)
	x=x+2

	
0
2
4
6
8
10
12
14
16
18
20
22
24
26
28
30
32
34
36
38
40
>>> a=10
>>> b=5
>>> temp=a
>>> a=b
>>> b=temp
>>> a
5
>>> b
10
>>> print('the value of %d after swapping:'.format(a))
the value of %d after swapping:
>>> if((year%4==0 and year%100!=0) or (year%400==0)):
	print("year is leap year")
else:
	print("not leap year")

	
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    if((year%4==0 and year%100!=0) or (year%400==0)):
NameError: name 'year' is not defined
>>> year=2000
>>> if((year%4==0 and year%100!=0) or (year%400==0)):
	print("year is leap year")
else:
	print("not leap year")

	
year is leap year
>>> x=100
>>> if(x%2==0)
SyntaxError: invalid syntax
>>> if(x%2==0):
	print("no is even")
else:
	print("no is odd")

	
no is even
>>> x=9
>>> if(x%2==0):
	print("no is even")
else:
	print("no is odd")

	
no is odd
>>> x=9
>>> y=10
>>> z=20
>>> if(x>y and x>z):
	print("x is greater")
elif y>z:
	print("y is greater")
else:
	print("z is greater")

	
z is greater
>>> x=-2
>>> if(x<0):
	print("no is negative")
elif x>0:
	print("no is positive")
else:
	print("no is zero")

	
no is negative
>>> x=0
>>> if(x<0):
	print("no is negative")
elif x>0:
	print("no is positive")
else:
	print("no is zero")

	
no is zero
>>> x=9
>>> if(x<0):
	print("no is negative")
elif x>0:
	print("no is positive")
else:
	print("no is zero")

	
no is positive
>>> 
