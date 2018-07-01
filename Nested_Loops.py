Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> for i in [1, 2, 3]:
	print ("Before j loop i is ", i)
	for j in [50, 100]:
		print ("j is ", j)

		
Before j loop i is  1
j is  50
j is  100
Before j loop i is  2
j is  50
j is  100
Before j loop i is  3
j is  50
j is  100
>>> for i in [0, 1]:
	print ("Outer ", i)
	for j in [2, 3]
	
SyntaxError: invalid syntax
>>> for i in [0, 1]:
	print ("Outer ", i)
	for j in [2, 3]:
		print (" Inner", j)
		print (" Sum", i + j)
		print ("Outer", i)

		
Outer  0
 Inner 2
 Sum 2
Outer 0
 Inner 3
 Sum 3
Outer 0
Outer  1
 Inner 2
 Sum 3
Outer 1
 Inner 3
 Sum 4
Outer 1
>>> for i in [0, 1]:
	print ("Outer", i)
	for j in [2, 3]:
		print (" Inner", j)

		
Outer 0
 Inner 2
 Inner 3
Outer 1
 Inner 2
 Inner 3
>>> for i in [0, 1]
SyntaxError: invalid syntax
>>> print (i)
1
>>> for i in [0, 1]:
	print (i)
	print (i)

	
0
0
1
1
>>> i = 5
>>> for i in []:
	print (i)

	
>>> for i in [0, 1]:
	print ("Outer", i)
	for i in [2, 3]:
		print (" Inner", i)
		print ("Outer", i)

		
Outer 0
 Inner 2
Outer 2
 Inner 3
Outer 3
Outer 1
 Inner 2
Outer 2
 Inner 3
Outer 3
>>> 
