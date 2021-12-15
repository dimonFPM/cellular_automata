import random
import matplotlib.pyplot as plt
import numpy as np


class Sosedi:
    N = 10
    procent = 35

    def random_place(self) -> np.ndarray:  # генерит начальный список
        col = self.N * self.N / 100 * self.procent
        check = 0
        list = np.zeros((self.N, self.N))
        while check <= col:
            x, y = random.randint(0, self.N - 1), random.randint(0, self.N - 1)
            if list[x][y] == 0:
                list[x][y] = 1
                check += 1
        print(*list, sep="\n")
        print("\n")
        return list

    def check_sosedi(self, list: np.ndarray) -> np.ndarray:
        z = np.zeros((self.N - 2, self.N - 2))
        for i in range(1, len(list) - 1):
            for j in range(1, len(list) - 1):
                z[i - 1][j - 1] = sum((list[i - 1][j - 1], list[i - 1][j], list[i - 1][j + 1],
                                       list[i][j - 1], list[i][j], list[i][j + 1],
                                       list[i + 1][j - 1], list[i + 1][j], list[i + 1][j + 1]))
        print(*z, sep="\n")
        return z

    def grah(self, z: np.ndarray) -> None:
        x, y = np.mgrid[0:self.N - 2:1, 0:self.N - 2:1]
        figure1 = plt.figure("График")
        ax1 = figure1.add_subplot(111, projection="3d")
        ax1.plot_surface(x, y, z)
        plt.show()

    def __init__(self, N=10, procent=35):
        self.N = N
        self.procent = procent
        self.grah(self.check_sosedi(self.random_place()))


if __name__ == "__main__":
    a = Sosedi()
