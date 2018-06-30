Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def clinic():
    print ("You've just entered the clinic!")
    print ("Do you take the door on the left or the right?")
    answer = raw_input("Type left or right and hit 'Enter'.").lower()
    if answer == "left" or answer == "l":
      print ("This is the Verbal Abuse Room, you heap of parrot droppings!")
    elif answer == "right" or answer == "r":
      print ("Of course this is the Argument Room, I've told you that already!")
    else:
      print ("You didn't pick left or right! Try again.")
      clinic()

      
>>> clinic()
You've just entered the clinic!
Do you take the door on the left or the right?
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    clinic()
  File "<pyshell#1>", line 4, in clinic
    answer = raw_input("Type left or right and hit 'Enter'.").lower()
NameError: name 'raw_input' is not defined
>>> 
