# Tyler Hegy
# UWYO COSC 1010
# Submission Date: 10/7/2024
# Lab 08
# Lab Section:12
# Sources, people worked with, help given to: Stack Overflow
# Comments: Used stack overflow to use the isinstance function in linear function. Also used to find the round function which helps limit 
#           float values to one decimal place


# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 
def check_convert(string):
    value = ""
    if string.isnumeric():
        if "." in string:
            converted = round(float(string),1)
            return converted
        elif "." not in string:
            converted = int(string)
            return converted
    elif string[0]=="-" and string[1:].isnumeric():
        if "." in string:
            converted = round(float(string),1)
            return converted
        elif "." not in string:
            converted = int(string)
            return converted
    else:
        return False

print("*" * 75)


# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

def linear(m,b,lower,upper):
    values=[]
    if isinstance(lower, int) and isinstance(upper, int) and lower<upper:
        for i in range(lower,upper+1,1):
            y = (m*i)+b
            values.append(y)
        return values 
    else:
        return False

# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list
print("y = mx+b\n")
while True:
    exit =''
    while exit.lower() != "exit":
        m = check_convert(input("Enter the slope of the line: "))
        b = check_convert(input("Enter the y intercept of the line: "))
        lower = check_convert(input("Enter a lower bound: "))
        upper = check_convert(input("Enter an upper bound: "))
        if m!=False and b!=False and lower!=False and upper!=False:
            values = linear(m,b,lower,upper)
            print(values)
            exit = input('Enter "exit" to end program. Enter anything else to do another equation: ')
            if exit.lower() == 'exit':
                break
            else:
                continue
        else:
            print('Values Entered were not numeric')
    break


print("*" * 75)


# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null
def square_root(a,b,c):
    output=0
    root = b**2 - 4 * a * c
    if root<0:
        output = 'null'
    else:
        output = root**(1/2)
    return output

def quadratic(a,b,c):
    answer1=0
    answer2=0
    root = square_root(a,b,c)
    if root=="null":
        answer1 = "null"
        answer2 = "null"
    else:
        answer1=(-b+root)/(2*a)
        answer2=(-b-root)/(2*a)
    both_values=[answer1, answer2]
    return both_values
        
print("Quadratic Function\n")
while True:
    exit =''
    while exit.lower() != "exit":
        a = check_convert(input("Enter the input for a: "))
        b = check_convert(input("Enter the input for b: "))
        c = check_convert(input("Enter the input of c: "))
        if a!=False and b!=False and c!=False:
            values = quadratic(a,b,c)
            print(values)
            exit = input('Enter "exit" to end program. Enter anything else to do another equation: ')
            if exit.lower() == 'exit':
                break
            else:
                continue
        else:
            print("Values entered were not numeric")
    break
