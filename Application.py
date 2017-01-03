import random
#Подключаем обучающую выборку

num0 = list('111101101101111')
num1 = list('001001001001001')
num2 = list('111001111100111')
num3 = list('111001111001111')
num4 = list('101101111001001')
num5 = list('111100111001111')
num6 = list('111100111101111')
num7 = list('111001001001001')
num8 = list('111101111101111')
num9 = list('111101111001111')

nums = [num0, num1, num2, num3, num4, num5, num6, num7, num8, num9]

#Виды цифр пять (Тестовая выборка)
num51 = list('111100111000111')
num52 = list('111100010001111')
num53 = list('111100011001111')
num54 = list('110100111001111')
num55 = list('110100111001011')
num56 = list('111100101001111')

#Опишем весы

w = []


#Заполняем весы нулями
for i in range(15):
    w.append(0)

#Порог активации

bias = 7

#Функция проверки цифры пять

def check(number):
    net = 0
    for i in range(15):
        net += int(number[i])*w[i]

    return net >= bias



#Теперь функции, которые будут уменьшать и увеличивать весы

def minus(number):
    for i in range(15):
        if int(number[i]) == 1:
            w[i] -= 1

def plus(number):
    for i in range(15):
        if int(number[i]) == 1:
            w[i] += 1

for i in range(10000):
    option = random.randint(0,9)

    #Если не пятёрка
    if option != 5:
        if check(nums[option]):
            minus(nums[option])

    else:

            if not check(num5):
                plus(num5)

#Вывод весов для пятёрки

print(w)

print("0 это 5? ", check(num0))
print("1 это 5? ", check(num1))
print("2 это 5? ", check(num2))
print("3 это 5? ", check(num3))
print("4 это 5? ", check(num4))
print("5 это 5? ", check(num5))
print("6 это 5? ", check(num6))
print("7 это 5? ", check(num7))
print("8 это 5? ", check(num8))
print("9 это 5? ", check(num9), '\n')

# Прогон по тестовой выборке
print("Узнал 5? ", check(num5))
print("Узнал 5 - 1? ", check(num51))
print("Узнал 5 - 2? ", check(num52))
print("Узнал 5 - 3? ", check(num53))
print("Узнал 5 - 4? ", check(num54))
print("Узнал 5 - 5? ", check(num55))
print("Узнал 5 - 6? ", check(num56))
