# Program checks if a number is divisble by 2 and 5 using and,or,not 

# ask user to enter any number 
number = int(input("Enter any number: "))
print(number)

# number is divisble by 2 
D2 = False 
if number % 2 == 0:
    D2 = True 

# number is divisble by 5 
D5 = False 
if number % 5 == 0:
    D5 = True 

# used if, elif and else statements to check the outcome 
if D2 and D5:
    print("The number is divisible by 2 and 5.")
elif D2:
    print("Number is divisible by 2.")
elif D5:
    print("Number is divisible by 5.")
else:
    print("Number is not divisble by 2 or 5.")

# from pyhton programming (Youtube ) - verify if a number is divisible by 3 and 5 
# this gave me insight on how to begin my task
# I changed the variables and structure , but i just wanted to bring it up ! 