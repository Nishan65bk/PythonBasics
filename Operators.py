"""Revision"""

#ARITHMETIC OPERATORS(+,-,*,/,%,**)
a = 10    # a nd b are operands
b = 20
print(a+b) # Addition
print(a-b) # subtraction
print(a*b) # multiplication
print(a/b)# division (result will be float)
print(a//b)# floor division (prints only floor value) floor value = greatest integer value less than the actual decimal number(a/b.)
print(a%b) #  modulus(reminder while dividing a by b)
print(a**b)# a power b

#Floor division
a = -7
b = 2
print(a/b) #-3.5
print(a//b) # -4 as 4 is the greatest integer value less than -3.5)



#Assignment Operators(= , += ,-= , *=,%=, **=, //=)
a = 10 
b = 5
a -= b #a = a -b = 10 - 5 = 5
a += b # a = a+b = 10+5 = 15
a *= b # a = a*b
a /= b # a = a/b
a //=b # a =a//b
a **=b # a = a**b
a %= b # a = a%b
print(a)


'''COMPARISON OPERATORS'''

# ==
a= 10
b= 10
print(a==b) # true

#!= not equals to 
a = 10
b = 6
print(a!=b) #true since a is not equals to b.

#similarly <=,>=,<, > are comparison operators.



"""logical operators"""


                      #And
# when both expresiion are true then only true otherwise false
a = 10
b = 20
print (a>1 and b<1) # FALSE (a>1 is true but b <1 is false) duitai true hunu parxa to be true
print(a>5 and b < 25) # TRUE (a>5 is true and b<25 is true)

                 #or
#at least one expresion should be true then output = TRUE
Nishan = 85
mohan = 70
print(Nishan> 30 or mohan < 100) #TRUE(1st exp is true and 2nd exp is false.here at least 1 exp is true .)
print(Nishan > 0 or mohan < 80) # TRUE( both exp are true)
print(Nishan<70 or mohan<20) # FALSE(bothe exp are false.)

               # not
# it makes boolean value opposite.
a = True
print(not(a)) #false

b = False
print(not(b)) # True

x= 5
b = 10
print(not(x<10)) # False.since not(True) = False


"""IDENTITY OPERATORS"""
#compare the memory locations (object identity)of the 2 objects
#so it is possible to know whether 2 objects are same or not.


                  # is
a = 10 
b = 10
print(a is b) #True. since a,b both are same integers and has same memory address

a = 10
b = "10"
print(a is b) #False . since a is int and b is string (has diff memory address)

          #is not

a = 23.33
b = "23.33"
print(a is not b) #True
print(a is b) # False


""" Membership operators"""
# used check teh membership pf a value inside a python data structure

              # in
a = "Welcome to Symphonic samrajya"
print("Symphonic"in a) #True
               
                #not in
print("sugar"not in a) # True

a = 103
print(bin(a))  ### to obtain binary number.

a = "Nishan"
print(bin(a))
