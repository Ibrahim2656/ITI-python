import random

# 1 - Ask the user to enter 5 numbers.
    # Store them, then display them in ascending order and descending order.

def sortedNumbers():
    numbers=[]
    for i in range(5):
        while True:
            try:
                number=int(input("Enter Number : "))
                numbers.append(number)
                break
            except ValueError:
                print("Input Must be Numbers!!:")
    print("Ascending order:", sorted(numbers))
    print("Descending order",sorted(numbers,reverse=True))

# 2 - Write a function that takes two numbers: (length, start).
#         Generate a sequence of numbers with the given length,
#         starting from the given start number and increasing by one each time.
#         Print the result.

def increment(length, start):
    numbers = list(range(start, start + length))
    print("Generated sequence:", numbers)


#  3 - Keep asking the user for numbers until they type "done".
#         When finished, print:
#             * The total of all numbers entered
#             * The count of valid entries
#             * The average
#         If the user enters something invalid, show an error and continue.

def sumNumbers():
    total = 0
    count = 0

    while True:
        value = input("Enter a number (or type 'done' to finish): ")
        if value.lower() == "done":
            break
        try:
            num = float(value)
            total += num
            count += 1
        except ValueError:
            print("Invalid input! Please enter a number or 'done'.")

    if count > 0:
        average = total / count
    else:
        average = 0

    print(f"Total of numbers entered: {total}")
    print(f"Count of valid entries: {count}")
    print(f"Average: {average}")

#  4 - Ask the user to enter a list of numbers.
#         Remove any duplicates, sort the result, and display it.

def removeDuplicatesSort():
    while True:
        try:
            user_input = input("Enter a list of numbers separated by spaces: ")
            numbers = list(map(float, user_input.split()))
            break
        except ValueError:
            print("Invalid input! Please enter numbers only.")

    unique_numbers = sorted(set(numbers))

    print("List without duplicates, sorted:", unique_numbers)


#     6 - Ask the user to enter a sentence.
#         Count how many times each word appears in the sentence
#         and display the result.
def wordCount():
    sentence = input("Enter a sentence: ")

    words = sentence.split()

    counts = {}
    for word in words:
        word_lower = word.lower()
        if word_lower in counts:
            counts[word_lower] += 1
        else:
            counts[word_lower] = 1

    print("Word counts:")
    for word, count in counts.items():
        print(f"{word}: {count}")

#     7 - Create a small gradebook system:
#         - The user enters 5 students names and their scores.
#         - At the end, show:
#             * The highest score
#             * The lowest score
#             * The average score.
def gradebook():
    students = []
    scores = []

    for i in range(5):
        name = input(f"Enter the name of student {i+1}: ")
        while True:
            try:
                score = float(input(f"Enter the score for {name}: "))
                break
            except ValueError:
                print("Score must be a number!")
        students.append(name)
        scores.append(score)
        
    highest_score = max(scores)
    lowest_score = min(scores)
    average_score = sum(scores) / len(scores)

    print("\nGradebook Summary:")
    print(f"Highest score: {highest_score}")
    print(f"Lowest score: {lowest_score}")
    print(f"Average score: {average_score:.2f}")

#     8 - Write a program that simulates a shopping cart:
#         - The user can add items with a name and a price.
#         - The user can remove items by name.
#         - The user can view all items with their prices.
#         - At the end, display the total cost.
def shoppingCart():
    cart = {}

    while True:
        print("\nShopping Cart Menu:")
        print("1. Add item")
        print("2. Remove item")
        print("3. View cart")
        print("4. Checkout / Exit")

        choice = input("Enter your choice: ")

        if choice == "1":  
            name = input("Enter item name: ")
            while True:
                try:
                    price = float(input(f"Enter price for {name}: "))
                    break
                except ValueError:
                    print("Price must be a number!")
            cart[name] = price
            print(f"{name} added to cart.")

        elif choice == "2":  
            name = input("Enter the name of the item to remove: ")
            if name in cart:
                del cart[name]
                print(f"{name} removed from cart.")
            else:
                print(f"{name} is not in the cart.")

        elif choice == "3":  
            if not cart:
                print("Your cart is empty.")
            else:
                print("Items in your cart:")
                for item, price in cart.items():
                    print(f"{item}: ${price:.2f}")

        elif choice == "4":  
            total = sum(cart.values())
            print("Final cart:")
            for item, price in cart.items():
                print(f"{item}: ${price:.2f}")
            print(f"Total cost: ${total:.2f}")
            break

        else:
            print("Invalid choice! Enter 1-4.")


#     9 - Create a number guessing game:
#         - The program randomly selects a number between 1 and 20.
#         - The user keeps guessing until they get it right.
#         - After each guess, show if the guess was too high or too low.
#         - When correct, display the number of attempts.

def numberGuessingGame():
    secret_number = random.randint(1, 20)
    attempts = 0

    print("Guess the number between 1 and 20!")

    while True:
        guess = input("Enter your guess: ")

        try:
            guess = int(guess)
        except ValueError:
            print("Please enter a valid number!")
            continue

        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
            break

def program():
    menu = {
        1: ("Sort 5 Numbers (ascending and descending)", sortedNumbers),
        2: ("Generate a sequence (length & start)", increment),
        3: ("Sum numbers until done", sumNumbers),
        4: ("Remove duplicates and sort list", removeDuplicatesSort),
        5: ("Count words in a sentence", wordCount),
        6: ("Gradebook system", gradebook),
        7: ("Shopping cart simulation", shoppingCart),
        8: ("Number guessing game", numberGuessingGame),
    }

    while True:
        print("\n==== Menu ====")
        for key, (description, _) in menu.items():
            print(f"{key}. {description}")
        print("-1. Exit")

        try:
            choice = int(input("Enter your choice: "))
            if choice == -1:
                print("Program is done!")
                break
            if choice in menu:
                func = menu[choice][1]
                if func:
                    if choice == 2:
                        while True:
                            try:
                                length = int(input("Enter the length of the sequence: "))
                                start = int(input("Enter the starting number: "))
                                break
                            except ValueError:
                                print("Input must be a number!")
                        func(length, start)
                    else:
                        func()
                else:
                    print("This feature is not implemented yet.")
            else:
                print("Invalid choice. Enter a number from 1-8 or -1 to exit.")
        except ValueError:
            print("Input must be a number!")


if __name__ == "__main__":
    program()