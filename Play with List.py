# PLAY with LIST
"""
About List
built in data-type
mutable
support different types
changeable
allow duplicate
it also support list within list
ordered - i.e: it's position is fixed
"""
'''
List Functions:-
append()	Adds an element at the end of the list
listname.append(value/variable)
clear()	    Removes all the elements from the list
copy()	    Returns a copy of the list
variableName = listName.copy(value)
count()	    Returns the number of elements with the specified value
variableName = listName.count(value)
extend()	Add the elements of a list (or any iterable), to the end of the current list
listName.extend([list values-one-by-one]| AnoterListVariable)
index()	    Returns the index of the first element with the specified value
listName.indec(value)
insert(position,value)	Adds an element at the specified position
pop()	    Removes the element at the specified position
listName.pop(position) :- if position is not specified it will pop up the last element
remove()	Removes the item with the specified value
listName.remove(value)
reverse()	Reverses the order of the list
sort()	    Sorts the list
'''

# implementation

a = [1,2,3,4,5,6,4]
b = ['Riahu','Anji','Kiddo','Raj']
c = [a,b]       # it will create list within a list
d = ['a',['a','b','c'],'b','c','d']
e = []
print(a)
print(b)
print(c)
print(d)
print(e)
f = a.copy()
print(f)
print(a.count(4))
print(a.reverse())
print(a.sort(reverse=True))

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

# we can use different type of key and it's value
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)