def quadratic_equation(a, b, c):
    """Prints the quadratic equation ax^2 + bx + c = 0"""
    equation = f"{a}x² {'+ ' if b >= 0 else '- '}{abs(b)}x {'+ ' if c >= 0 else '- '}{abs(c)} = 0"
    print(equation)

quadratic_equation(2, -5, 3)  
quadratic_equation(1, 4, -7)  
