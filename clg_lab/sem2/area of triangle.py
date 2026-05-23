def calculate_triangle_area(base, height):
    return 0.5 * base * height

base =  int(input("Enter the length of base of triangle:"))
height = int(input("Enter the length of height of triangle:"))
area = calculate_triangle_area(base, height)
print(f"The area of the triangle is {area}")