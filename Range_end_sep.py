 #RANGE FUNCTION

#range() function returns an immutable sequence type of numbers.
#works only with integers(not with floating numbers) 

rg = range(20)
print(rg) # generates number from 0 to 19

#rg1 = range(20.5)
#print(rg1) # error (since it doesnot work with float numbers)

#range() function with 1 argument
for i in range(6):
     print(i) # generates number from 0 to 6 (0,1,2,3,4,5)

# range function with 2 arguments
for i in range(2,6):
     print(i)  #  2,3,4,5 (print number from 2 to 6)

# range function with 3 arguments
for i in range(2,20,2):
     print(i) # prints number 2 to 20 increased by 2(2,4,6,8,10,12,14,16,18)

for i in range(20,10,-2):
     print(i) # prints number from 20 to 10 decreased by 2(20,18,16,14,12,)

"""STUDY DETAILLY ABOUT THIS"""
#indexing 
rg = range(20,30,2)
print(rg[4]) #output is 20,22,24,26,28 so r[4]=28

#Slicing
rg = range(20,30,2)
print(rg[1:4]) # 22,24,26 





"""Sep and End Parameters"""

#End
#end= "x"
#different lines  lai"x" le jodxa in same line.
print("hello",end = " ")
print("Nishan") # hello Nishan (to print different statements on same line)

print("hello",end ="--")
print("WORLD") # hello--WORLD end=" " yha vitra j haley tei le 1st ra 2nd line lai jodxa)

#Sep
#sep="x" different items in same line lai "x" le jodxa in output

print("apple","banana", "tree")
print("apple","banana", "tree", sep ="+") 
print("apple","banana", "tree", sep =",") 

#for foramting date
print("2025","01","20",sep = "/",end = " ")
print("is succesfull day")



