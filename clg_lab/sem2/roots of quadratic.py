import cmath

# Function to find the roots of a quadratic equation
def find_roots(a, b, c):
    # Calculate the discriminant
    discriminant = (b ** 2) - (4 * a * c)
    
    # Find two solutions using the quadratic formula
    root1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
    root2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
    
    return root1, root2

print("Write coefficients of equation ax^2 + bx + c")

a = int(input("Enter coeff a:"))
b = int(input("Enter coeff b:"))
c = int(input("Enter coeff c:"))

root1, root2 = find_roots(a, b, c)
print(f"The roots of the quadratic equation are {root1} and {root2}")


