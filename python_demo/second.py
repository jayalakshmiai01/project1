
String1 = "Hello, welcome"
print("String:") 
print(String1) 

string2 = list(String1) 
string2[2] = 'p'
String2 = ''.join(string2) 
print("\nUpdating string: ") 
print(String2) 
  

String3 = String1[0:2] + 'p' + String1[3:] 
print(String3) 

x = 5
y = 10

print('The value of x is {} and y is {}'.format(x,y))

import constant

print(constant.PI) # prints 3.14
print(constant.GRAVITY) # prints 9.8