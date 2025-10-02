#  write a program that prints hello world
print("Hello World!") 


# application to take a number in binary form from the user, and print it as a decimal
while True:
    binary_str= input("Enter a binary number: ")
    try:
        deciaml_num=int(binary_str,2)
        print(f"The deciaml value of {binary_str} is : {deciaml_num}")
        break
    except ValueError:
        print("Invalid input! Please enter only 0s and 1s.")

# - write a function that takes a number as an argument and if the number
# 		divisible by 3 return "Fizz" and if it is divisible by 5 return "buzz" and if is is
# 		divisible by both return "FizzBuzz"

def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return str(num)   


for i in range(1, 21):
    print(fizzbuzz(i))

# Ask the user to enter the radius of a circle print its calculated area and circumference
import math

radius = float(input("Enter the radius of the circle: "))

area = math.pi * radius ** 2
circumference = 2 * math.pi * radius

print("Area of circle:", area)
print("Circumference of circle:", circumference)

# Ask the user for his name then confirm that he has entered his name (not an empty string/integers). then proceed to ask him for his email and print all this data
while True:
    name = input("Enter your name: ")
    if name.strip() and not name.isdigit():  # ensure not empty or integer
        break
    else:
        print("Invalid name, please try again.")

email = input("Enter your email: ")

print("\nUser Data:")
print("Name:", name)
print("Email:", email)


# Write a program that prints the number of times the substring 'iti' occurs in a string
text = input("Enter a string: ")
count = text.count("iti")

print("The substring 'iti' occurs", count, "times.")

