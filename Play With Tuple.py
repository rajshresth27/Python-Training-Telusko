# Play With Tuple
'''
similar to list but with ()
and it is inmutable
iteration is faster in tupel
also stores multiple type of data
order is unchangeable
'''
"""
methods
count()	Returns the number of times a specified value occurs in a tuple
index()	Searches the tuple for a specified value and returns the position of where it was found
"""

a = ('1','2','3','4','5','6')
print(a)
print(list(a))
print(a.index('5'))
a = list(a)
print(a)