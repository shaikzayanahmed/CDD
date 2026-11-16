# Calculator Module for GitHub Actions CI
# Author: Shaik Zayan Ahmed (4ik25cs183)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

if __name__ == "__main__":
    print(f"Add(10, 5) = {add(10, 5)}")
    print(f"Subtract(10, 5) = {subtract(10, 5)}")
    print(f"Multiply(10, 5) = {multiply(10, 5)}")
    print(f"Divide(10, 5) = {divide(10, 5)}")
