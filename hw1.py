####################################### Почему такие варианты не могут работать корректно?


# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

# N = int(input("You see the value: "))
# Result = N % 10 + N % 100 + N % 1000
# print(Result)

##############################   Тут уже предположение, что переменная N изменяется во время выполнения мат. операций....
# N = int(input("You see the value: "))
# Result = N % 10 + N % 10 + N % 10
# print(Result)




############################################# Работпющая программка, задача № 2....


# N = int(input("You see thr value: "))
# Result = N % 10 + N % 100 // 10 + N // 100
# print(Result)







############################################# Работпющая программка, задача № 4....

# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, 
# если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, 
# чем Петя и Сережа вместе?

# *Пример:*

# 6 -> 1  4  1
# 24 -> 4  16  4
#     60 -> 10  40  10


# S = int(input("Enter the number of birds: "))
# if not S % 3:
#      print(f'Катя {(S / 3 ) * 2}')
#      print(f'Сережа {((S / 3 ) * 2) / 2 / 2} ')
#      print(f'Петя {((S / 3 ) * 2) / 2 / 2}')
# else:
#     print("An incorrect value was entered!")




############################################# Работпющая программка, задача № 6....

#Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*

# 385916 -> yes
# 123456 -> no


# N = int(input("Enter the ticket number: "))
# Sum2 = round((N % 10 + N % 100 // 10 + N % 1000 // 100), 0)
# N2 = (-N / 1000) * (-1)
# Sum1 = int(N2 % 10 + N2 % 100 // 10 + N2 % 1000 // 100)

# if Sum1 == Sum2:
#     print("Yes")
# else:
#     print("No")
 



# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no

m = int(input("Enter the size of the chocolate bar on the X axis: "))
n = int(input("Enter the size of the chocolate bar on the Y axis: "))
k = int(input("Enter the size of the chocolate bar that you want to break off: "))

if k < m * n and k != m * n and (k % m == 0 or k % n == 0):
    print("Yes")
else:
    print("No")
