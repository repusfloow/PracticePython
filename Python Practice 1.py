Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 3+4
7
>>> 44/2
22.0
>>> 2**3
8
>>> 3*4+5*6
42
>>> 
>>> 
>>> (72-32)/(9.0*5)
0.8888888888888888
>>> x=2
>>> print x
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(x)?
>>> print (x)
2
>>> y=x
>>> print (y)
2
>>> z = x + 1
>>> print (z)
3
>>> x = 5
>>> print (x)
5
>>> print (y)
2
>>> print (z)
3
>>> 22 >4
True
>>> 22 < 4
False
>>> 22 == 4
False
>>> x = 100
>>> 22 = 4
SyntaxError: can't assign to literal
>>> x >= 5
True
>>> x >= 100
True
>>> x >= 200
False
>>> not True
False
>>> not (x >= 200)
True
>>> 3 < 4 and 5<6
True
>>> 4<3 or 5<6
True
>>> temp = 72
>>> water is liquid = temp > 32 and temp < 212
SyntaxError: can't assign to comparison
>>> water_is_liquid = temp >32 and temp < 212
>>> this_class = "CSE 160"
>>> print (this_class)
CSE 160
>>> len (this_class)
7
>>> "Spencer" + "Ma"
'SpencerMa'
>>> "Spencer " + "Ma"
'Spencer Ma'
>>> '0' in this_class
True
>>> "O" in this_class
False
>>> 3.0 + 4.0
7.0
>>> 3 + 4
7
>>> 3 + 4.0
7.0
>>> "3" + "4"
'34'
>>> 3 + "4"
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    3 + "4"
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> 3 + True
4
>>> 15.0 / 4.0
3.75
>>> #15 divided by 4
