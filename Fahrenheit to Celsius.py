Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> Fahrenheit = 30
>>> Celsius = (Fahrenheit - 32) / 9 * 5
>>> print (Fahrenheit, Celsius)
30 -1.1111111111111112
>>> Fahrenheit_40 = 40
>>> Celsius_2 = (Fahrenheit_40 - 32) / 9 * 5
>>> print (Farenheit_40, Celsius_2)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print (Farenheit_40, Celsius_2)
NameError: name 'Farenheit_40' is not defined
>>> print (Fahrenheit_40, Celsius_2)
40 4.444444444444445
>>> Fahrenheit_83 = 83
>>> Celsius_3 = (Fahrenheit_83 - 32) / 9 * 5
>>> print (Fahrenheit_83, Celsius_3)
83 28.333333333333336
>>> Fahrenheit_78 = 78
>>> Celsius_4 = (Fahrenheit_78 - 32) / 9 * 5
>>> print (Fahrenheit_78, Celsius_4)
78 25.555555555555554
>>> print int(Fahrenheit_78, Celsius_4)
SyntaxError: invalid syntax
>>> int (Fahrenheit_78, Celsius_4)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    int (Fahrenheit_78, Celsius_4)
TypeError: 'float' object cannot be interpreted as an integer
>>> print "I'm done!!!!!!!!!!!!!!!!!!!!!!!!!!"
SyntaxError: Missing parentheses in call to 'print'. Did you mean print("I'm done!!!!!!!!!!!!!!!!!!!!!!!!!!")?
>>> print ("I'm done!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!)
	   
SyntaxError: EOL while scanning string literal
>>> print ("I'm done!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
	   
I'm done!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
>>> 
