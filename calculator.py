# calculator.py

# add function
def add(a:int, b:int):
    return a + b

# subtract function
def subtract(a:int, b:int):
    return a - b 

if __name__ == "__main__":
    # Test cases
    print("Add 5 + 3 =", add(5, 3))           # Expected: 8
    print("Subtract 10 - 4 =", subtract(10, 4))  # Expected: 6
# multiplication 
def multiply(a: int, b: int):
    return a * b
# division
def divide(a: int, b: int):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
if __name__ == "__main__":
    print("Multiply 6 * 7 =", multiply(6, 7))      # 42
    print("Divide 10 / 2 =", divide(10, 2))        # 5.0
