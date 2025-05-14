# store folloing word meanings in a python ditionary:
#table: "a piece of furniture" , "list of facts and figures"
#cat : "a small animal"

dictionary = {"cat" : "a small animal",
              "table":("a piece of furniture", "list of facts and figures")}
print(dictionary)

# qn 2. you are given a list of subjects for students. Assume one classroom is required for 1 subject.
# how many class rooms are needed by all students.

#"Python","java",'C++',"Python","javascript',"java","python","java","C++","C"

subject_list = {"Python","java","C++","Python","Javascript","java","Python","java","C++","C"}
print(subject_list) #{'Javascript', 'Python', 'java', 'C++', 'C'}
print(len(subject_list))  # 5 = total number of unique subjects = total number of class.



#qn3. WAP to enter marks of 3 subjects from the user and store them in a dictionary. 
#start with an empty dictionary and add one by one. Use Subject name as key and marks as value.

marksheet = {} # empty dict
marksheet["Science"] = int(input("Enter your marks in Science:"))
marksheet["Maths"] = int(input("Enter your number in Maths:"))
marksheet["physics"] = int(input("Enter your number in physics:"))
print(marksheet)

# by using .update() method 
marksheet = {}

x = int(input('Enter teh marks in maths:'))
marksheet.update({"maths": x})

y = int(input('Enter teh marks in chem:'))
marksheet.update({"chem": y})

z = int(input('Enter teh marks in phy:'))
marksheet.update({"phy": z})


print(marksheet)


#qn4. Fiure out a way to store 9 and 9.0 as separate values in set.(You cna tale helo of buit _in data types)

values = set()
values.add(9)
values.add("9.0")
print(values)