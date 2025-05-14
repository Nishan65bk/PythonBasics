# Datatypes
# 1.Numeric:-
#i. integer= 1,2 10, 12
a = 1
b = 2
print(a-b)
#ii. complex number = 3+ij , 1+4j
a = 1+2j
b = 3+4j
print(a+b)
#iii. float = 1.1, 1.2,2.33, 2.45
Nishan = 45.55
ram = 34.45
print(Nishan // ram)
 
 #2. Dictonary (Mapping or Dict)
"""have to study detailly"""

data_1 = {101:"Nishan",102:"Ram",103:"rohan"} #here datatypes can be stored in number.i,e "Nishan" dtatype sis tored 101 number.
print(data_1[102])
print(data_1[103])

   #when dict funtion is used ##  ()and = are used 
   #the datatypes are stored in variables
data_2 = dict(electric_guitar="nishan",Acoustic_Guitar="Sarowar",keyboard="Aayush",drums="srastanshu",bass="Arpit")
#since dict()funstion is used ,dataypes are stored in variables like keyboard, drums, acoutis-guitar,etc.

print(data_2["drums"])  #"" shoud be used to print the value of variables
print(data_2["electric_guitar"])


#3. Boolean
a = True 
b = False
print(not(a))


#4. Set
#unorders collection of elements
#elements may not appear in the same order as they enter in to the set.
#dosnot accept duplicate elements
data_samrajya = {"hyatt regency",5150,1,2,3,"taj hotel"}


#5. Sequence type

#i. String
a = 'Python' # words or sentences or number enclosed by single quotes, double quotes, triple quotes
a= "Python"
print(a)

b = "12"#number is also string if kept in quotes
print(b)


#ii. List
#can store different types of elements which can be modified
ListOfConcert = [1,2,3,4,1,2,"hard rock cafe","nishan","chelesea college", "global college"]

#iii. Tuple
#cannot be modified
success = ('Nishan',"soch",1,'2',{"hyatt regency",1,2,3,}, 24) ## string ,set,int inside tuple since tuple can store different datatypes
print(success)

data_3 = 1,2,3,"bacchus","guitar",1.1 #tuple without parenthessess
print(data_3)
print(type(data_3)) #to print the datatype store din variable "type()" function is used.)

single_element_tuple = (1,)
print(type(single_element_tuple))

a = (1)
print(type(a))  # int

b = 1,
print(type(b)) # tuple

      

