numbers = input("Enter the list : ").split(',')
numbers = list(map(int,numbers))
def square(x):
    return x**2
squared_numbers = list(map(square, numbers))
print("Original list:", numbers)
print("Squared list:", squared_numbers)
