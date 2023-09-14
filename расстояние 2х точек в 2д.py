#Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

#Math.Sqrt(Math.Pow(x2 - x1, 2) + Math.Pow(y2 - y1,2))

import math
print("Введите координаты первой точки через пробел")
a = input()

print("Введите координаты второй точки через пробел:")
b = input()

coords_a = a.split()
coords_b = b.split()

coords_a[0] = float(coords_a[0])
coords_a[1] = float(coords_a[1])
coords_b[0] = float(coords_b[0])
coords_b[1] = float(coords_b[1])

result = math.sqrt((coords_a[0] - coords_b[0])**2 + (coords_b[1] - coords_b[1])**2)
print('Расстояние: ')
print(result)