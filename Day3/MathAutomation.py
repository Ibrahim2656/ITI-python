"""
1) Math Automation
   - Create a file called "math_report.txt".
   - Ask the user for multiple numbers (comma-separated).
   - For each number, calculate:
        - floor, ceil, square root, area of a circle
   - Write the results into "math_report.txt".
   - Confirm file was created and print its content.
"""


import math
from DecoratorsTask import log_time

def validate_numbers(user_input:str):
    try:
        numbers=[float(num.strip()) for num in user_input.split(',')]
        return numbers
    except ValueError:
        return None

@log_time
def math_report():
    while True:
        user_input=input("Enter numbers seprated by commas: ")
        numbers=validate_numbers(user_input)
        
        if numbers is None:
            print("Invaild input! please enter only numbers(e.g, 4, 7.5, -2)")
        else:
            break
    
    with open("math_report.txt","w") as file:
        file.write("Math Report\n")
        file.write("="*30+"\n\n")
        
        for num in numbers:
            floor_val=math.floor(num)
            ceil_val=math.ceil(num)
            sqrt_val=math.sqrt(num) if num>=0 else "undefined (negative)"
            circle_area= math.pi * num**2
            
            file.write(f"Number: {num}\n")
            file.write(f"   Floor: {floor_val}\n")
            file.write(f"   Ceil: {ceil_val}\n")
            file.write(f"   Square Root: {sqrt_val}\n")
            file.write(f"   Area of Circle (r={num}): {circle_area}\n")
            file.write("\n")
            
    print("\n 'math_report.txt' created successfully! Here is the content:\n")
    with open("math_report.txt","r") as file:
        print(file.read())