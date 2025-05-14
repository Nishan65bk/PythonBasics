 # used to store data vlaues in      key:value pairs
# unordered,mutable(changeable) and dont allow duplicate keys.

info = {"key":"value",
        "name": "Symphonic Samrajya",
        "Learning": "coding",
        "age":35,
        "is_adult":True,
        "marks":94.4
        }
print(info)
print(info["name"])

# we can store lists and tuples as value inside dictionary. i.e

info = {"key":"value",
        "name": "Symphonic Samrajya",
        "Learning": ["pyhton","C","Java",8848,3435],    # list
        "age":(1,2,3,4,45,3,4,56,43),  #tuple    
        "is_adult":True,
        "marks":94}
print(info["key"])

# For keys
# we must use immutable datatypes:strings,int,float,boolean,tuple
# mutbale data ypes cannot be used: lists,dict,sets.
"""valid keys"""
details = {"name":"Nishan",
        20 : "age",
        20.8 :"length",
        (23,34,54,65,90):"marks",
        True :"Its is True"
        }
"""invalid keys"""
# details2 = {["nsihan",23,54,65]:"List",  # list key
#          {"nishan":"name","age":24}:"dict",
#          {1,2,3,4,5,"ram"}:"set"
#          }
# print(details2({1,2,3,4,5,"ram"}))



# for values
# any datatype can be used.
# when a dict is stored as value inside a dict.its known as Nested dict.i,e
students = {
    "student1": {
        "name": "Alice",
        "age": 20,
        "marks": 85
    },
    "student2": {
        "name": "Bob",
        "age": 22,
        "marks": 90
    }
}

print(students["student1"]["name"])  # Output: Alice
print(students["student2"]["marks"])  # Output: 90


#to re assign the value(since dict i s mutable)
info = {"key":"value",
        "name": "Symphonic Samrajya",
        "Learning": "coding",
        "age":35,
        "is_adult":True,
        "marks":94.4
        }
info["key"]= "word" 
print(info)# {'key': 'word', 'name': 'Symphonic Samrajya', 'Learning': 'coding', 'age': 35, 'is_adult': True, 'marks': 94.4}

# to add new key and value
info["country"] = 'Nepal'
print(info) # "country"="Nepal" will be added in the last of dictonary.


# To create empty dictionary
null_dict = {}
print(null_dict)

# to add values
null_dict["Nishan"] = "Hero"
print(null_dict)

#Nested dictonar example:
student = {
    "name":"rahul kumar",
    "subjects":{"phy":78,
                "chem": 98,
                "math":95,
    }
}
print(student["subjects"]) # to print subject

# to print vlaue of phy,chem
print(student["subjects"]["chem"])  # using another [] and the reuqierd key.


# Dictonary Methods

#1.            .keys()
info = {"key":"value",
        "name": "Symphonic Samrajya",
        "Learning": "coding",
        "age":35,
        "is_adult":True,
        "marks":94.4
        }
print(info.keys())     #dict_keys(['key', 'name', 'Learning', 'age', 'is_adult', 'marks'])
#to type cast output in lists
print(list(info.keys()))
print(len(info)) # to print total number of key:value pairs.
# another method
print(len(list(info.keys())))


#2       .values()
# returns all values
print(info.values()) #dict_values(['value', 'Symphonic Samrajya', 'coding', 35, True, 94.4])

#to convert outout in lists(TYPECASTING)
print(list(info.values()))

#3             .items()
#returns all(key,value)pairs as tuples
student = {
    "name":"rahul kumar",
    "subjects":{"phy":78,
                "chem": 98,
                "math":95,
    }
}
print(student.items()) #dict_items([('name', 'rahul kumar'), ('subjects', {'phy': 78, 'chem': 98, 'math': 95})])

#Typecasting
print(list(student.items())) # reutns tuples inside a List

# to acces pair values
pairs = list(student.items())
print(pairs[0])   #('name', 'rahul kumar')  indexing concept,

#4.                      .get("key")
# returns the key according to the value.
# used to avoid errors(for more professionalism.)
#print(student["name2"]) #gives error.   stops the code to run.
print(student.get("name2")) # gives none . doesnot gives error.

#eg1.
student = {
    "name":"rahul kumar",
    "subjects":{"phy":78,
                "chem": 98,
                "math":95,
    }
}
# print("before")
# print(student["name3"]) # error(since name3 is not present in student dictionary). the after this doesnot  runs which disturbs while coding
# print("after") 

#TO avoid this .get(key) is used. i,e
print("before")
print(student.get("name3")) # None . doesnot disturns the code after this.(more professional way to avoid errors.)
print("after")


#5.                        .update(newDict)
#inserts the specified items(key:value pair)oe new dictionary to the dictionary
student.update({"city":"delhi"}) #adds the item at last in the student dictionary.
print(student) #{'name': 'rahul kumar', 'subjects': {'phy': 78, 'chem': 98, 'math': 95}, 'city': 'delhi'}

# adding new dicitionary
student1 = {"city":"delhi","roll no":23456}
student.update(student1)

print(student) # student1 dict will bw added to student dict.

#when new dict which has same key as old dit is added..purano key ko value update hunxa.(since, dict cant have same muliple keys.) i.e
student = {
    "name":"rahul kumar",
    "subjects":{"phy":78,
                "chem": 98,
                "math":95,
    }
}



new_dict1 = {"name":"Nishan","home":"Parbat"} 
student.update(new_dict1)
print(student) #







