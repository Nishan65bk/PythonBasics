# # used for decision making
# Earning = 2000
# if Earning < 1000 :
#     print("good lifestyle")
# else:
#     print("You have to work more.") 


# #1. Write a python program to input one number from the user. Print"I am greater than 15"if the number is greater than 15

# a = int(input("Enter th number:"))
# if a > 15 :
#     print("I am greater than 15")

# #2.#Write a python program to input one number from the user. Print “Intelligent” if the number is 100, otherwise print “Mehenat Garnu Paryo”.

# number = int(input("Enter the number:"))
# if a == 100:
#     print("INTELLIGENT")
# else:
#     print("Mehenat garnu paryo.")





# """3.Write a program that asks the user for a number in the range of 1 to 7. The program should display the corresponding day of the week,
# where 1=sunday, 2=monday,3=tuesday,4=wednesday,5=thursday,6=friday,7=saturday.
# The program should display an error message if the user enters a number that is outside the range of 1 to 7."""

# # a = int(input("Enter the number"))
# # if a == 1:
# #     print("Sunday")
# # elif a == 2:
# #     print("Monday")
# # elif a == 3:
# #     print("Tuesday")
# # elif a == 4:
# #     print("Wednesday")
# # elif a == 5:
# #     print("Thursday")
# # else:
# #     print( "error")


# """NESTED IF STATEMENT"""
# # when an if statement is present inside another if statement.

# """ Eg1. We have a number, and we’re going to check if the number is greater or less than 25. 
# If the number is less than 25, we’ll check if it is an odd number or an even number. 
# If the number is greater than 25, we will print that the number is greater than 25."""

# a = int(input("Enter he Number:"))
# if a < 25 :  # condition1 starts here
#   #condition 1 satisfy vayesi balla condition 2 ma janxa.
#   if a%2 == 0 :  # condition 2 starts here
#     print("number is even and smaller than 25.")
#   else:         # condition 2 ends here
#     print("number is odd and smaller than 25.")
# elif a == 25 :
#    print("Number is 25")
# else:   # condition 1 ends here
#     print("number is greater than 25")



# """If num is greater than 0, check if num is even by checking if the remainder when num is divided by 2 is 0.
# If the remainder is 0, execute the code block that prints the message “The number is positive and even.”
# If the remainder is not 0, execute the code block that prints the message “The number is positive but odd.”
# If num is not greater than 0, execute the code block that prints the message “The number is not positive.”
# Now we can implement this case scenario with Python nested if else statement:"""


# a = int(input("Enter the nuumber:"))
# if a > 0:
#    if a % 2 == 0 :
#       print("the number id positive. and even")
#    else:
#       print("the number is positive but odd")
# else:
#    print("The number is not positive.") 


# """Write a Python program that asks the user to input a username and password, then checks the following conditions:

# If the username is "admin":
# If the password is "password", print:
# Login successful! Welcome. admin.
# If the password is "12345", print:
# Weak password!
# Please reset your password.
# Otherwise, print:
# Incorrect password. Please try again.
# If the username is "guest":
# If the password is "guest", print:
# Login successful ! Welcome , guest.
# Otherwise, print:
# Incorrect password. Please try again.
# For any other username, print:
# Unknown user. Please tryy again."""

# username = input("Enter the username:")
# password = input("Enter the password:")
# #cond = condition
# if username == "admin":  #cond 1 starts
#    if password == "password": #cond 2 starts
#       print("Login successful! Welcome.admin")
#    elif password =="12345": #cond 3 starts
#       print("Weak Password \n Please reset your password.")
#    else: # cond 2 and 3 ends here
#       print("Incorrect Password.Please try again.")
# elif username == "guest": #cond 4 starts
#    if password == "guest": # cond 6 starts
#       print("Login sucessful! Welcome , guest.")
#    else:#cond 6 ends
#       print("incorrect password. please try again later.")
# else: #cond 1 and 4 ends here.
#    print("Unknown user.Please try again.")


# ram is going to create a faebook account. write code such that:
# if user name is "Ram" and if password contain @ 
#display account created
#otherwise display (password must contain '@")
# username = input("Enter the Username:")
# password = input("Enter the password:")
# if username == "ram":
#    if "@" in password:
#       print("Account created")
#    else:
#       print("password must contain \"@\"")   # using escape characters


"""Write a Python program that takes the following inputs from a user:

Name
Email address
Password
Your program should validate the inputs using nested if-else statements as follows:
If the name is empty (""), print:
➤ Name cannot be empty.
Else, check the email:
If the email does not contain "@", print:
➤ Invalid email address.
Else, check the password:
If the password is less than 8 characters long, print:
➤ Password must be at least 8 characters long.
If all validations pass, print:
➤ Registration successful."""

Name = input("Enter your name:")
if Name == "":
   print("Name cannot be empty.")
else:
   print("check the email")
email = input("Enter your email address:")
if "@"not in email:
   print("Invalid email address.")
else:
   print("check the password")
password = input("Enter the password :")
if len(password) < 8 :
   print("password must be at least 8 characters.")



#correct one

# Nested "if else" for validation.

name = input("Enter your name:")
email = input("Enter your email address:")
password = input("Enter your password:")

if name == "":
    print("Name cannot be empty.")
else:
    if "@" not in email:      # membership operator(not in)
        print("Invalid email address.")
    else:
        if len(password) < 8 : #len is a built-in function that returns the length (the number of items) of an object or sequence(string,list or tuple)or collection like dictionary
           print("Password must be at least 8 characters long.")
        else:
            print("Registration successful.")
            
    
