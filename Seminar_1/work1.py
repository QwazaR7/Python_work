#n = int(input('Введите число: '))
#print(f'Результат: {n*n}') 



# Напишите программу, которая на вход принимает два числа и проверяет, является ли второе число квадратом первого.

# num1 = int(input('Input first number: '))
# num2 = int(input('Input second number: '))
# if num1**2 == num2:
#     print('Yes')
# else:
#     print('No')    



# Организуйте последовательный ввод чисел до тех
# пор, пока не будет введён 0. Подсчитайте среди введённых чисел те, которые кратны трём.


# number = float(input("Чтобы закончить введите 0. Введите число: "))
# count = 0
# while number != 0:
#     if number % 3 == 0:
#          count += 1
#     number = float(input("Чтобы закончить введите 0. Введите число: "))

# print(f"Чисел кратных трем: {count}")        

# 3. Напишите программу, которая будет на вход
# принимать число N и выводить числа от -N до N

# num = int(input("Введите число: "))
# if num < 0:
#     num = num * -1
# m = -num
# while m <= num:
#     print(f'{m} ', end = " ")
#     m += 1