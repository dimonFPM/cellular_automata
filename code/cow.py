import os
import random
import time

animal_list = []  # текущий список животных



def paint_list(animal_list: list) -> None:
    '''Функция получает на вход список количества животных, которых надо вывести в консоль.'''
    for i in range(len(animal_list)):
        for j in range(len(animal_list)):
            match animal_list[i][j]:
                case x if 10 <= x < 100:
                    print(x, end="  ")
                case x if 0 <= x < 10:
                    print(x, end="   ")
                case x if x >= 100:
                    print(x, end=" ")
        print("\n")


def create_list(N: int) -> None:
    '''Создаёт список размерности N заполненый нулями. Один рандомный элемент имеет значение 100.'''
    global animal_list
    animal_list = [[0 for j in range(N)] for i in range(N)]
    animal_list[random.randint(0, N - 1)][random.randint(0, N - 1)] = 100
    paint_list(animal_list)


def sosedi(x: int, i: int, j: int) -> (int, int, int, int):
    '''Функция получает на вход количество коров в клетке, индекс i и j данной клетки. Возвращает количество оставшихся
     коров в клетке, количество ушедших коров, координаты клетки куда ушли коровы'''
    match (i, j):
        case 0, 0:
            t = random.randint(1, 2)
            if t == 1:
                j = j + 1
            elif t == 2:
                i = i + 1
        case 0, n if n == N - 1:
            t = random.randint(1, 2)
            if t == 1:
                j = j - 1
            elif t == 2:
                i = i + 1
        case n, 0 if n == N - 1:
            t = random.randint(1, 2)
            if t == 1:
                i = i - 1
            elif t == 2:
                j = j + 1
        case nn, n if n == nn == N - 1:
            t = random.randint(1, 2)
            if t == 1:
                i = i - 1
            elif t == 2:
                j = j - 1
        case 0, _:
            t = random.randint(1, 3)
            if t == 1:
                j = j - 1
            elif t == 2:
                i = i + 1
            elif t == 3:
                j = j + 1
        case n, _ if n == N - 1:
            t = random.randint(1, 3)
            if t == 1:
                i = i - 1
            elif t == 2:
                j = j - 1
            elif t == 3:
                j = j + 1
        case _, 0:
            t = random.randint(1, 3)
            if t == 1:
                i = i - 1
            elif t == 2:
                j = j + 1
            elif t == 3:
                i = i + 1
        case _, n if n == N - 1:
            t = random.randint(1, 3)
            if t == 1:
                i = i - 1
            elif t == 2:
                j = j - 1
            elif t == 3:
                i = i + 1
        case _, _:
            t = random.randint(1, 4)
            if t == 1:
                i = i - 1
            elif t == 2:
                j = j - 1
            elif t == 3:
                j = j + 1
            elif t == 4:
                i = i + 1
    if x != 1:
        k = x // 2
        x = x - k
        y = k + animal_list[i][j]
    else:
        y = x + animal_list[i][j]
        x = 0

    return (x, y, i, j)


def action(age: int) -> None:
    '''Основная функция. Проходит список коров в циклах, вызывая функцию sosedi'''
    global animal_list
    list = [[0 for j in range(N)] for i in range(N)]
    for k in range(age):
        for i in range(N):
            for j in range(N):
                if animal_list[i][j] != 0:
                    if sum([sum(k) for k in animal_list]) == 100:
                        xx, yy, ii, jj = sosedi(animal_list[i][j], i, j)
                        list[i][j] = xx
                        list[ii][jj] = yy
                else:
                    continue
        # print(5 * "\n") # для запуска из IDE
        os.system("cls")  # для запуска из проводника
        paint_list(list)
        animal_list = list[:]
        time.sleep(1)  # пауза между итерациями


def action1(age: int) -> None:
    '''Основная функция. Проходит список коров в циклах, вызывая функцию sosedi'''
    global animal_list
    list = [[0 for j in range(N)] for i in range(N)]
    for k in range(age):
        for i in range(N):
            for j in range(N):
                if animal_list[i][j] != 0:
                    if sum([sum(k) for k in animal_list]) == 100:
                        xx, yy, ii, jj = sosedi(animal_list[i][j], i, j)
                        animal_list[i][j] = xx
                        animal_list[ii][jj] = yy
                    else:
                        print("Ошибка")
                        break
                else:
                    continue
        # print(5 * "\n") # для запуска из IDE
        os.system("cls")  # для запуска из проводника
        paint_list(animal_list)
        # animal_list = list[:]
        time.sleep(1)  # пауза между итерациями


if __name__ == "__main__":
    while True:
        N = input("Введите размерность поля(целое положительное число):")
        age = input("Ведите количество поколений(целое положительное число):")
        if N.isnumeric() and age.isnumeric():
            N = int(N)
            age = int(age)
            if N != 0:
                break
            else:
                print("Вы ввели недопустимые значения, попробуйте заново.\n")

        else:
            print("Вы ввели недопустимые значения, попробуйте заново.\n")
    create_list(N)
    action(age)
    # action1(age)
    print("Конец")
    input("Нажмите Enter для выхода.")
