"""
6) Random Data Generator
   - Ask user how many random numbers to generate.
   - Save them into "random_numbers.csv" as:
        index,value
        1, 42
        2, 87
        ...
   - Print total count and average of the generated numbers.
"""
import random
import csv 

def random_data_generator():
    while True:
        try:
            count=int(input("Enter how many random numbers to generate: "))
            if count<=0:
                print(" Number must be positive.")
            else:
                break
        except ValueError:
            print("Invalid input! Please enter a number.")
    numbers=[random.randint(1,100) for _ in range(count)]
    
    csv_file="random_numbers.csv"
    
    with open(csv_file,"w",newline="")as f:
        writer=csv.write(f)
        writer.writerow(["index","value"])
        for i ,num in enumerate(numbers,1):
            writer.writerow([i,num])
    
    avg=sum(numbers)/len(numbers)
    print(f"\n Generated {count} random numbers.")
    print(f"Average value: {avg:.2f}")
    print(f"Saved into '{csv_file}'")