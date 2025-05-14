"""Set"""
# collection of unordered items.
# sets are mutable(assignment can be done.)
#each element in the set must be unique and immmutable.

# only int,float,strings,tuple can be stored inside a set since they are immutable.
#Lists,dict,set cannot be stored inside a set as they are mutable.

collection = {1,2,3,4}

print(collection)
print(type(collection))

# set ignore duplicate items and the output is unordered.

collection = {1,2,2,2,"hello","world","world"}
print(collection) #{'world', 1, 2, 'hello'} 

# len() ignores the same multiple values

collection1 = {1,1,1,"Nishan","Nishan","world"}
print(collection1)  #(1,"Nishan","world")
print(len(collection1)) # 3 (not 6)

#Empty set

collection = {} # this is empty dictionary not a empty set.

#to create a empty set

nums = set() #empty set : syntax

"""Set Methods"""

#1                      .add(el) #adds an element
collection = set()
collection.add(1)
collection.add(2)
collection.add(3)
print(collection) #{1,2,3}

student_set = set()
student_set.add("nishan")
student_set.add(20)
student_set.add(30.43)
student_set.add(True)
student_set.add(("music","airbus","A","320","lamo"))
# student_set.add(["music","airbus","A","320","lamo"]) # error ;list cannt be used since it is mutable.
# student_set.add({"nishan":"name","age":16}) # error: since dict is mutable

