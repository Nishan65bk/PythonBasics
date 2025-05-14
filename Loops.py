# used to repeat instructions
"""While Loop""" 

#while True :
  #  print('Hello') # prints hello infinitely (since condition is True and condition true vayesamma loop chaleko chalai garxa)
 
count = 1
while count <= 5 :
    print("hello")
    count += 1

# whole process = iteration
i = 1 # iterator
while i <= 5: # condition
    print("Nishan")  # work
    i = i + 1  # updation

# to print 1000 times      
i = 1 # iterator
while i <= 1000: # condition
    print("Nishan")  # work
    i = i + 1  # updation
        
# to print counts too
i = 1 # iterator
while i <= 1000: # condition
    print("Nishan", i)  # work
    i = i + 1  # updation

# print numbers from 1 to 5
i = 1
while i <= 5:
    print(i)
    i += 1
print("Loop Ended")

# print numbers form 5 to 1( reverse)
i = 5
while i >= 1:
    print(i) 
    i -= 1  # 5 4 3 2 1

 # avoid infintite loop while programming

# i = 5
# while i < 6:
#     print(i)  # prints i to - infinity since condition will be True for every iterator(i).
#     i -= 1  # 5 4 3 2 1


"""Practice questions"""

#qn1. Print numbers from 1 to 100.

i= 1
while i >= 100 :
    print(i)
    i += 1 
