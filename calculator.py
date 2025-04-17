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