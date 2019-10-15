"""
a=int(input("Enter First Number :"))
b=int(input("Enter Second Number :"))
c=int(input("Enter Third Number :"))

max_value= a if a>b and a>c else b if b>c else c

print("Max Value=",max_value)
"""

'''
a=int(input("Enter First Number :"))
b=int(input("Enter Second Number :"))

print("Both are Equal" if a==b else "A is greater than B" if a>b else "A is smaller than B")
'''


'''
list1=[1,2,3]
list2=[1,2,3]

print(id(list1))
print(id(list2))
print(list1 is list2)
print(list1==list2)

print("------------------------")
list3="Hello World"
print("o" in list3)
'''


#a,b=[int(x) for x in input("Enter 2 no. :").split()]
#print(a+b)

# Command Line arguments
# Name of file is first argument
from  sys import argv
print(type(argv))
print(argv)
print(argv[1:])













