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

    def create_triangle(self, other1, other2):
        """ Возвращает три вектора, являющиеся сторонами треугольник, потсроенного на трёх заданных точках """
        a = self - other1
        b = self - other2
        c = other1 - other2
        return a, b, c

    def p_of_triangle(self, other1, other2):
        """ Вычисляет периметр треугольника, построенного на векторах """
        a = self.length()
        b = other1.length()
        c = other2.length()
        return a + b + c

    def s_of_triangle(self, other1, other2):
        """ Вычисляет площадь треугольника, построенного на векторах """
        a = self.length()
        b = other1.length()
        c = other2.length()
        p = (self.p_of_triangle(other1, other2))/2
        s = (p*(p-a)*(p-b)*(p-c))**0.5
        return s

V = Vector()
N = int(input())
Vectors = []
S_max = 0
for i in range(N):
    next_vector = input()
    next_vector = Vector(next_vector)
    Vectors.append(next_vector)
for j in range(N - 2):
    for k in range(j + 1, N - 1):
        for n in range(k + 1, N):
            a, b, c = Vectors[j].create_triangle(Vectors[k], Vectors[n])
            S = a.s_of_triangle(b, c)
            if S > S_max:
                S_max = S
print('Максимальная площадь = ' + str(S_max))
