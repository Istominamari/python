#Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
num = int(input())
for i in range(2, num // 2 + 1):
    if num % i == 0:
        for j in range(2, i // 2 + 1):
            if i % j == 0:
                break
        else:
            print(i)