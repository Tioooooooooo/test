#1
password = input("Введите пароль: ")
check = input("Подтвердите пароль: ")

if password == check:
    print("Пароль принят")
else:
    print("Пароль не принят")


#2
seat = int(input("Введите номер места: "))

if 1 <= seat <= 54:

    if seat % 2 == 0:
        place = "верхнее"
    else:
        place = "нижнее"

    if seat <= 36:
        type_place = "в купе"
    else:
        type_place = "боковое"

    print(place, type_place)

else:
    print("Такого места нет")


#3
year = int(input("Введите год: "))

if year % 4 == 0 and year % 100 != 0:
    print("Год", year, "- високосный")
elif year % 400 == 0:
    print("Год", year, "- високосный")
else:
    print("Это год не високосный")


#4
color1 = input("Введите первый цвет: ").lower()
color2 = input("Введите второй цвет: ").lower()

main_colors = ["красный", "синий", "желтый"]

if color1 not in main_colors or color2 not in main_colors:
    print("Ошибка: введён неправильный цвет")
else:
    if (color1 == "красный" and color2 == "синий") or \
            (color1 == "синий" and color2 == "красный"):
        print("фиолетовый")

    elif (color1 == "красный" and color2 == "желтый") or \
            (color1 == "желтый" and color2 == "красный"):
        print("оранжевый")

    elif (color1 == "синий" and color2 == "желтый") or \
            (color1 == "желтый" and color2 == "синий"):
        print("зеленый")

    else:
        print("Цвета одинаковые")


