# """PRACTICE QUESTIONS"""
# #write a programme to ask the user to enter names of their 3 favorite movies and store them in a list.
# movie_1= input("Enter name of 1st favorite movie:")
# movie_2= input("Enter name of 2nd favorite movie:")
# movie_3= input("Enter name of 3rd favorite movie:")
# movie_list = []
# movie_list.insert(0,movie_1)
# movie_list.insert(1,movie_2)
# movie_list.insert(2,movie_3)
# print(movie_list)

# #.append() can also be used(adding element to the end of the list.)
# movie_1= input("Enter name of 1st favorite movie:")
# movie_2= input("Enter name of 2nd favorite movie:")
# movie_3= input("Enter name of 3rd favorite movie:")
# movie_list = []
# movie_list.append(movie_1)
# movie_list.append(movie_2)
# movie_list.append(movie_3)

# print(movie_list)

# # to use append directly
# movie_list = []
# movie_list.append(input("Enter the first movie: "))
# movie_list.append(input("Enter the second movie: "))
# movie_list.append(input("Enter the 3rd movie: "))
# print(movie_list)
# # in this way shortest cleann code can be obtained.



#2.WAP to check if a list contains a palidrome of elements.(Hint:use copy()method)
#          [1,2,3,2,1]          [1,"abc","abc",1]

list_1 = [1,2,3,2,1]# original list

copy_list_1= list_1.copy() # we used copy to make original list list_1 unouched and same .
print(copy_list_1)
copy_list_1.reverse() # to check if the reversed list is same or not(palindrome)
print(copy_list_1)
print(list_1)

if copy_list_1 == list_1:
    print('The list is palindrome.')
else:
    print("its not palidrome>")


# 3. WAP to count the number of students with the "A" grade in the following tuple.
#("C",'D',"A","A","B","B","A")

Grades = ("C",'D',"A","A","B","B","A")
print(Grades.count("A"))

#4. store the above values in a list and sort then from "A"to "D".

# covert tuple to list
grade_list = list(Grades)
print(grade_list)

# sorting list
grade_list.sort()
print(grade_list)