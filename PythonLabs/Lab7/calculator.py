import math_utils as mu


def main():
    # Set of operations
    operations = {
                "+": mu.add, 
                "-": mu.substract, 
                "x": mu.multiply, 
                "/": mu.division, 
                "^": mu.power, 
                "%": mu.mod
                }

    # Inputs & Validitations
    try:
        num1 = int(input("Please, enter the first number: "))
        num2 = int(input("Please, enter the second number: "))  
    except ValueError:
        print("Enter valid numbers !!!")


    opt = input("Please, enter an operation: ")
    for operation, method in operations.items():
        if opt == operation:
            print(method(num1, num2))
        else:
            print("Enter a valid operation !!!")

if __name__ == "__main__":
    main()