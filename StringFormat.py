""" String Format() Method"""

#default arguments
print("Hello {},your balance is {}".format("Ram",20))

#positional arguments
print("Hello {0},your balance is {1}".format("Nishan","$200,000"))

#keyword arguments
print("Hello {name},your balance is {blc}".format(name = "Samrajya", blc = "3Lakhs"))

#mixed arguments
print("hello{0}, your balance is{blc}".format("Rohan",blc = 20000))
print("{0} is {1}.he is good {job}".format("Nishan","musician",job = "guitarist"))
#print("Hi {0},you look{}".format("Nishan","Cool")) # ERROR (positional and defualt arbuments cannot be used at the same time.)
print("hello {} {a} {}".format("Nishan","programmer",a = "python"))
#print("hello {} {a} {}".format("Nishan",a = "python","programmer")) ERROR

#Reusing Values
print("Bachhus is a{0}.it colour is {1}.{0} is first made by{brand}".format("Stratocaster","black", brand = "Fender"))

#ex1
guitar = "majesty"
price = "$3000"
quantity = 5
Shop_Name = "Nistars Guitar store"
print("I need {0} {1} guitars. its price is {2} in {3}.".format(quantity,guitar,price,Shop_Name))
                                                                #0         1    2     3  

#ex2
quantity = 3 #0
item_no = 567 #1
price = 49.95 #2
myorder = "I want to pay{2}, dollars for {0}, pieces of item{1}"
print(myorder.format(quantity,item_no,price))
                     #0        1      2
                       



"""f string"""

a = "summer"
b = 2025
c = "best season"
print(f"its {b}.This {a} is {c}")   # f or F string van used insetead of ("strings".format() method)
print(F"its {b}.This {a} is {c}")



print("Nishan is a {}. He is great {}.his dream is to be a {}".format("good boy","Guitarist","pilot"))


#extra

a = range(10,20) # its range function and it output is of range datatype
print(isinstance(a,range))
