def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def culculate():
    while True:
        print("Enter 1, if You want to add two numbers")
        print("Enter 2, if You want to substract two numbers")
        print("Enter 3, if You want to quit")

        operation = input("Your choice is: ").strip()
        print("Great!")    
        
        if operation == "1":
            num1 = int(input("Choose the first number:"))
            num2 = int(input("Choose the second number:"))
            print(f"Result of adding {num1} and {num2} is: {add(num1, num2)}")
        
        elif operation == "2":
            num1 = int(input("Choose the first number:"))
            num2 = int(input("Choose the second number:"))
            print(f"Result of subtracting {num1} and {num2} is: {subtract(num1, num2)}")
        
        elif operation == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter or 1, or 2, or 3.")

if __name__ == "__main__":
    culculate()


        
        