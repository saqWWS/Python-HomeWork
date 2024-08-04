def area_of_circle(pi, radius):
    return pi * radius * radius 

def area_of_square(side):
    return side * side

def area_of_rectangle(height, width):
    return height * width

def area_of_triangle(tri_area, base, height):
    return tri_area * base * height

def calculate_area(shape, **kwargs):
    if shape in different_geo:
        return different_geo[shape](**kwargs)

different_geo = {
    "circle": area_of_circle,
    "square": area_of_square,
    "rectangle": area_of_rectangle,
    "triangle": area_of_triangle
}

shape = ["circle", "square", "rectangle", "triangle"]

first_num = int(input("Number for the following (circle, square, rectangle, triangle) expressions:\t"))
second_num = int(input("Number for the following (rectangle, triangle) expressions:\t"))

circle = calculate_area("circle", pi=3.14, radius=first_num)
square = calculate_area("square", side=first_num)
rectangle = calculate_area("rectangle", height=second_num, width=first_num)
triangle = calculate_area("triangle", tri_area=0.5, height=second_num, base=first_num)

print("area of circle:\t", circle)
print("area of square:\t", square)
print("area of rectangle:\t", rectangle)
print("area of triangle:\t", triangle)