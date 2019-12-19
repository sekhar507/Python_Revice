import functools
import operator

list=[1,2,3,4,5]
list.sort()
print(list)
print("The sum of lists is :")
print(functools.reduce(lambda a,b : a+b,list))

print("The maximum element from the list is: ")
print(functools.reduce(lambda a,b: a if a>b else b, list))
print(functools.reduce(operator.add,list))

