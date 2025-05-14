"""Lists in Python"""
#a built in datatype that store set of values 
#it can store elements of different types(integer,float,string,etc)
 
 #store marks of 5 students :
marks1 = 20.4
marks2 = 30.45
marks3 = 20.2
marks4 = 25.5
marks5 = 12.9
#here many variable are used to store different values 
#it makes work more complex
#so to store difffernt values in only one variable List datatype is used. i.e,
marks= [20.4,30.45,20.2,25.5,12.9]  #[] is used .
print(marks)
print(type(marks))  #class "list" 

#indexing
#[20.4,30.45,20.2,25.5,12.9]  
#  0      1    2   3     4

print(marks[0]) #20.4
print(marks[1]) #30.45

#For list length
print(len(marks))  #len() function is used   # 5 (since there are 5 values.)

# multiple values of different datatypes can be stored in list.
student = ["Nishan",98.5,17,"Kathamandu","Anamnagar"]
print(student)

# strings and lists are simialr but major difference is:

# String - immutable (value cannot be changed):-
# str ="Fender"
# print(str[0])
# str [0] = "T"  # TypeError: 'str' object doesnot support item assignment
# print(str) # F will not be changed to T. its not allowed in strings

#whereas,
#List - mutable (value can be changed):-
student = ["Nishan",98.5,17,"Kathamandu","Anamnagar"]
print(student[0])
student[0] = "Mohan"  # Nishan will be changed to Mohan
print (student)  #["Mohan",98.5,17,"Kathamandu","Anamnagar"]

#List Slicing

#similar to string slicing
 #list_name = [starting index : ending index] #ending index is not included

marks = [85,94, 76, 63,48]
print(marks[1:4]) #[94,76,63] 48(ending index 4 )is not included.
print(marks[:4]) # when starting index is missed :- marks[0:4]
print(marks[1:])#when ending index is missed :- marks[1:4]
print(len(marks))

#using negative indexing
# marks = [85,94, 76, 63,48]
#          -5 -4 -3   -2 -1
print(marks[-3:-1]) #[76,63] ending index is not included



#LIST  METHODS

# 1                 .append():
# adds element at the end.

#i. Adding 1 element to a List
List = [1,2,3,4]

List.append(5)# adds 5 in last [1,2,3,4,5]
print(List)

# ii. adding a list to list 
List_1 = [1,3,4,5,6]
List_2 = ["Nishan",678,1,2,34]
List_1.append(List_2)
print(List_1)




#2                  .sort():
# arrange(sorts) the list in ascending order
a = [2,4,7,5,6,8]
a.sort()
print(a) # sorts in ascending order(2,4,5,6,7,8)

#3              .clear()
# removes all teh elements from the list
b = [234,65,45,56,"bachhus"]
b.clear()
print(b)  #[] all elements are removed


#4              .copy()
#returns a copy of the list
list_A = [23,45,600,456,3345]
list_A.copy()
print(list_A) #[23,45,600,456,3345] 

#5               .count()
# returns the number ofelements with specified value.
A = [1,2,3,4,1,1,345,1,234,345]
A.count(1)
print(A)




"""TUPLES"""
#- a built in data type that lets us create immutable sequences of values.
#() parenthessess is used to store sequence ofvalues.
tup = (87,64,35,23,21)  
print(tup[0]) # 87
# TUPLE is IMMUTABLE(value cannot be changed) i.e,
#tup[0] = 5 # ERRROR # since it is immutable (assignement is not possible.)

#1.Empty tuple
tup = ()
print(tup)

#2.Single value tuple
tup = (1,)  # , must be used after simgle valu e in tuple 
print(tup)
print(type(tup))

#note if there is no coma in single value, python take it as integer .
tup = (1) # integer
print(type(tup))

# similarly, if the single value is string , python take it as a string , not tuple
tup = ("Hello")
print(type(tup)) # string
# to make it tuple (,) must be used .
tup = ("hello",) # , is used
print(type(tup)) # tuple

#3. Multi value tuple
tup = (1,2,3,4) # here (,) after last value is compeletly optional.
print(type(tup)) # tuple
tup1 = (1,2,3,4,5,)# , is used at last
print(type(tup1)) # tuple

# Slicing in tuple
tup = (1,2,3,4)
    #  0  1 2 3
print(tup[1:3]) # (2,3) last index ko vlaue aaudaina


# Tuple Methods

#1   .index(ele)
#- returns index of 1st occurence of ele(element)

tup =(1,2,3,4,5)
print(tup.index(1)) # prints index of 1st occuurence of element = 1 in tuple
# prints 0

tup = ("ram",3,4,5,"ram")
print(tup.index("ram")) # prints index of 1st occurence of ram
# prints 0

tup = (2,1,3,1,4,1)
print(tup.index(1)) # 1 = eemnt to be searched
# prints 1 = index of 1st occurence of element 1


#2    .count(ele)
#- counts total occurences of passed element(ele)

tup = (1,2,3,)
print(tup.count(1)) # 1(since total number 1 = 1)

tup = (1,2,3,1,4,2,1)
print(tup.count(1)) # 3 (since total number of 1 = 3)










