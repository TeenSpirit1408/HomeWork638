class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        if y == 0:
            if type(x) == str:
                self.x, self.y = list(map(int, self.x.split(',')))
            else:
                pass

    def __str__(self):
        """ Приводит вектор к удобному для чтения формату """
        return str(self.x) + ',' + str(self.y)

    def __add__(self, other):
        """ Вычисляет вектор, являющийся суммой двух данных векторв """
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """ Вычисляет вектор, являющийся разностью двух данных векторв """
        return Vector(self.x - other.x, self.y - other.y)

    def __neg__(self):
        """ Вычисляет вектор, являющийся обратным данному вектору """
        self.x *= (-1)
        self.y *= (-1)
        return Vector(self.x, self.y)

    def delenie_na_chislo(self, n):
        """ Вычисляет вектор, являющийся частным вектора на число """
        self.x /= n
        self.y /= n
        return Vector(self.x, self.y)

    def length(self):
        """ Вычисляет длину данного вектора """
        return (abs(self.x) ** 2 + abs(self.y ** 2)) ** 0.5

V = Vector()
sum_of_vectors = Vector(0, 0)
n = 0
N = int(input())
for i in range(N):
    next_vector = input()
    next_vector = Vector(next_vector)
    sum_of_vectors += next_vector
    n += 1
center_mass = sum_of_vectors.delenie_na_chislo(n)
print('Координаты точки центра масс = ' + '(' + str(center_mass) + ')')
