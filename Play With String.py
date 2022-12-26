nameString = "Hello Everyone How Are You, Hoping A Wonderfun Day Ahead"
# string are imutables
print(nameString)
print()
print(nameString[1:])
print()
print(nameString[:5])
print()
print(nameString[1:5])
print()
print(nameString[-10])
print()
print(nameString[-1])
print(nameString[1:80])   # this will not give error as it will go till last and end it there
print()
#capitalize : it converts the First character  in capital letter
print(nameString.capitalize())
#len() to get the whole length of string
print(len(nameString))
# casefold :- it converts string to lower case
print(nameString.casefold())
#print(nameString.casefold('False'))  : - wrong
# center(width,fillchar) :-   it will basically increase the length of the string  with the specifed character that we will specify from both side
print(nameString.center(80,"*"))
#count :- to find the occurance of a singe entity or a pattern which is connected.
print(nameString.count('[a-z]'))
#encode(encoding='UTF-8/ascii',errors='') :- return a encoded version of string
'''
'backslashreplace'	- uses a backslash instead of the character that could not be encoded
'ignore'	- ignores the characters that cannot be encoded
'namereplace'	- replaces the character with a text explaining the character
'strict'	- Default, raises an error on failure
'replace'	- replaces the character with a questionmark
'xmlcharrefreplace'	- replaces the character with an xml character
'''
print(nameString.encode(encoding="ascii",errors="backslashreplace"))
#endswith() :- if a string returns with a specifed value then it returns true otherwise it returns false.
print(nameString.endswith('Hello'))             # False
print(nameString.endswith('d'))                 # True
#expandtabs():- with tis we can manipulate the tab size by putting a integer
a= 'H\te\tl\tl\to'        # example for this fn
print(a)
print(a.expandtabs(5))
print(a.expandtabs(15))
#find('value',start,end) :- it search for the specifed string and if finds then it returns it's specifed position capital and small are different
print(nameString.find('a'))             # it returns value -1 if it is not found
print(nameString.find('Are'))           # it is same to index but if in index it is not found it will ras=ise an exception.
#format(value1,value2,...) :- it is used to specifify characters or string in certain places.
test = "{0} {1} {2} {3} {4}".format("Hi","My","Name","Is","Raj")
test1 = "Cost of this pen is {price:2f}".format(price=40)   # for using .2f there we need to specify variable name at that place
print(test)                         # . is basically used for neglecting the value in floating point
print(test1)
"""
:<		Left aligns the result (within the available space)
:>		Right aligns the result (within the available space)
:^		Center aligns the result (within the available space)
:=		Places the sign to the left most position
:+		Use a plus sign to indicate if the result is positive or negative
:-		Use a minus sign for negative values only
: 		Use a space to insert an extra space before positive numbers (and a minus sign before negative numbers)
:,		Use a comma as a thousand separator
:_		Use a underscore as a thousand separator
:b		Binary format
:c		Converts the value into the corresponding unicode character
:d		Decimal format
:e		Scientific format, with a lower case e
:E		Scientific format, with an upper case E
:f		Fix point number format
:F		Fix point number format, in uppercase format (show inf and nan as INF and NAN)
:g		General format
:G		General format (using a upper case E for scientific notations)
:o		Octal format
:x		Hex format, lower case
:X		Hex format, upper case
:n		Number format
:%		Percentage format
"""
# index() :- searches for the index of the specified string it will gite index of the first.
print(nameString.index('A'))
# isalnum() : this return's true if character in string is alphanumeric eg:- alphabet+number
# isdecimal() : this returns true if decimal is present in string
# isdigit() : this returns true if string contain digit     EG:- str = "123"
# isidentifier() : returns true if string is an identifier if a string contain (a-z)&(0-9) or _ then it is considered as a valid identifier
# islower() : it check weather a string is in lower case
# isnumeric() : it check wether string has number
# isprintable() :if a string contain special character then it is not printable
# isspace() : if a string is a space or not.
# istitle() : if each word(1st letter) starts with a upper case letter
# isupper() : if all the character are in uppercase
# join() : it makes string to join
str = "Bye".join(nameString)   # confused
print(str)                      #same as above
# ljust(n,'c') : Returns a left justified version of the string it will add character 'c'  no. of times to make length n of total
# lower() : Converts a string into lower case
# lstrip() : Returns a left trim version of the string it will remove specified characters form the string.
txt = ",,,,,ssaaww.....baaaaaannana"
x = txt.rstrip(",.asw")
print(x)
# maketrans() :  Bounced
# partition() : it will return a tuple and if specified string is not found it can return any of the 2
            # 1 - the whole string
            # 2 - an empty string
txt = "I could eat bananas all day"
x = txt.partition("bananas")
print(x)        # output ('I could eat ', 'bananas', ' all day')
# replace(old_value, new_value, count) : change in a specified position
# rfind() : Searches the string for a specified value and returns the last position of where it was found
# rindex() : find index of of characher from the end
# rjust() : similar like ljust but at the right side
# rpartition() : similar to partition but from the right end
# rsplit("symbol",n) : splits a string into a list, starting from the right. and n specifies the grouping of how many entity
# rstrip() : is used to remove character from the right side of the string.
# split() : Splits the string at the specified separator
# splitness() : splits a string into a list. on the occurance of \n in a sentance nd if it's parameter = 'True' then \n will also be include in list
# startswith() : returns true if a string returns a specified value
# strip('characters') : it is used to remove specific character from the beginning and from the end (generally whitespaces)
# swapcase() : converts lower to upper and vice versa character
# title() :  it converts the first letter of each case in upper
# translate() :  # didn't get
# upper() : convert a string into upper case
# zfill(n) : it adds 0 in the beg as specified