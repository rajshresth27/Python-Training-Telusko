# Play with operator
'''
Arithmetic operators
+ :- addition
- :- subtraction
* :- multiplication
/ :- division (with floating point)
% :- reminder
** :- power
// :- floor division

Assignment operators
=
+= / -= / *= / %= / /= / **= / //=
&= / |= / ^= / >>= / <<=

Comparison operators
==      >=      <=      !=      <       >

Logical operators
and   or   not

Identity operators
is      is not

Membership operators
in       not in

Bitwise operators
&       :- set each bit to 1 if both bits are 1
^       :- XOR  :- set each bit to 1 if only one of two bit is 1
|       :- OR :-
~       :- NOT
>>      :- Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off
<<      :- Shift left by pushing zeros in from the right and let the leftmost bits fall off
'''                     #  4321
a = 5       # in binary :- 0101
b = 6       # in binary :- 0110
c = 10      # in binary :- 1010
d = 15      # in binary :- 1111

print(a&b)      # here 3rd position is only 1 in both so output will be 0100 :- i.e: 4
print(c^d)      # here 1st and 3rd will is different in each case so the output will be 0101 :- ie: 5
print(a|b)      # here it will perform only basic bit addition operation so the output will be 0111 :- i.e: 7
print(a<<2)     # here we are shifting left by 2 bits so num = 10100 so output will be :- 20
print(a>>2)     # here we are shifting right by 2 bits so num = 0001 so output will be :- 1


