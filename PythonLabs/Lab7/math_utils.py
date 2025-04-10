def add(x, y):
    return x + y

def substract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def division(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        print("Division by zero is not defined!")

def power(x, y):
    return x ** y

def mod(x, y):
    return x % y

def main():
    print("x: 1\ty: 1\tx + y: " + add(1, 1))
    print("x: 1\ty: 1\tx - y: " + substract(1, 1))
    print("x: 2\ty: 5\tx * y: " + multiply(2, 5))
    print("x: 21\ty: 7\tx / y: " + division(21, 7))
    print("x: 3\ty: 4\tx ^ y: " + power(3, 4))
    print("x: 8\ty: 5\tx % y: " + mod(8, 5))

if __name__ == "__main__":
    main()