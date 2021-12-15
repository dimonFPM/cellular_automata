import os
import random
import time


class Cow_model:
    #region Cow_model
    __N = None
    __age = None
    __animal_list = []

    def __paint_list(self, animal_list: list) -> None:
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

    def __create_list(self) -> None:
        '''Создаёт список размерности N заполненый нулями. Один рандомный элемент имеет значение 100.'''
        self.__animal_list = [[0 for j in range(self.__N)] for i in range(self.__N)]
        self.__animal_list[random.randint(0, self.__N - 1)][random.randint(0, self.__N - 1)] = 100
        self.__paint_list(self.__animal_list)

    def __sosedi(self, x: int, i: int, j: int) -> (int, int, int, int):
        '''Функция получает на вход количество коров в клетке, индекс i и j данной клетки. Возвращает количество оставшихся
         коров в клетке, количество ушедших коров, координаты клетки куда ушли коровы'''
        match (i, j):
            case 0, 0:
                t = random.randint(1, 2)
                if t == 1:
                    j = j + 1
                elif t == 2:
                    i = i + 1
            case 0, n if n == self.__N - 1:
                t = random.randint(1, 2)
                if t == 1:
                    j = j - 1
                elif t == 2:
                    i = i + 1
            case n, 0 if n == self.__N - 1:
                t = random.randint(1, 2)
                if t == 1:
                    i = i - 1
                elif t == 2:
                    j = j + 1
            case nn, n if n == nn == self.__N - 1:
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
            case n, _ if n == self.__N - 1:
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
            case _, n if n == self.__N - 1:
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
            y = k + self.__animal_list[i][j]
        else:
            y = x + self.__animal_list[i][j]
            x = 0

        return (x, y, i, j)

    def __action(self) -> None:#работает не правильно
        '''Основная функция. Проходит список коров в циклах, вызывая функцию sosedi'''
        list = [[0 for j in range(self.__N)] for i in range(self.__N)]
        for k in range(self.__age):
            for i in range(self.__N):
                for j in range(self.__N):
                    if self.__animal_list[i][j] != 0:
                        if sum([sum(k) for k in self.__animal_list]) == 100:
                            xx, yy, ii, jj = self.__sosedi(self.__animal_list[i][j], i, j)
                            list[i][j] = xx
                            list[ii][jj] = yy
                    else:
                        continue
            # print(5 * "\n") # для запуска из IDE
            os.system("cls")  # для запуска из проводника
            self.__paint_list(list)
            self.__animal_list = list[:]
            time.sleep(1)  # пауза между итерациями
        self.__N = self.__age = None#

    def __action1(self) -> None:
        '''Основная функция. Проходит список коров в циклах, вызывая функцию sosedi'''
        list = [[0 for j in range(self.__N)] for i in range(self.__N)]
        for k in range(self.__age):
            for i in range(self.__N):
                for j in range(self.__N):
                    if self.__animal_list[i][j] != 0:
                        if sum([sum(k) for k in self.__animal_list]) == 100:
                            xx, yy, ii, jj = self.__sosedi(self.__animal_list[i][j], i, j)
                            self.__animal_list[i][j] = xx
                            self.__animal_list[ii][jj] = yy
                        else:
                            print("Ошибка")
                            break
                    else:
                        continue
            # print(5 * "\n") # для запуска из IDE
            os.system("cls")  # для запуска из проводника
            self.__paint_list(self.__animal_list)
            # animal_list = list[:]
            time.sleep(1)  # пауза между итерациями
        self.__N = self.__age = None

    def setN(self, st: str):
        if st.isnumeric():
            self.__N = int(st)
        else:
            print("Вы ввели недопустимые значения N\n")

    def setAge(self, st: str):
        if st.isnumeric():
            self.__age = int(st)
        else:
            print("Вы ввели недопустимые значения age\n")

    # def grah(self):

    def __init__(self):
        while True:
            self.setN(input("Введите размерность поля(целое положительное число):"))
            if self.__N == None:
                continue
            else:
                break
        while True:
            self.setAge(input("Ведите количество поколений(целое положительное число):"))
            if self.__age == None:
                continue
            else:
                break
        self.__create_list()
        self.__action1()
    #endregion

if __name__ == "__main__":
    cow = Cow_model()
    print("Конец")
    input("Нажмите Enter для выхода.")
