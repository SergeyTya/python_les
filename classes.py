class MoneyBox:     # задание про копилку
    def __init__(self, capacity=0): # конструктор с аргументом – вместимость копилки
        self.capacity = capacity
        self.counter = 0

    def can_add(self, v): # True, если можно добавить v монет, False иначе
        if self.capacity - self.counter >= v:
            return True
        else:
            return False

    def add(self, v): # положить v монет в копилку
        self.counter += v


x = MoneyBox(10)
print(x.capacity)
print(x.can_add(10))
x.add(5)
print(x.counter)


class Buffer:
    def __init__(self):     # конструктор без аргументов
        self.buff = []

    def add(self, *a):      # добавить следующую часть последовательности
        self.buff += a
        while len(self.buff) >= 5:
            print(sum(self.buff[0:5]))   # подсписок списка
            self.buff = self.buff[5:]
          #  self.add() #  замени while  -> if

    def get_current_part(self):     # вернуть сохраненные в текущий момент элементы последовательности в порядке, в котором они были добавлены
        return self.buff


print("Задание про буфер")
buf = Buffer()
buf.add(1, 2, 3)
buf.get_current_part() # вернуть [1, 2, 3]
buf.add(4, 5, 6) # print(15) – вывод суммы первой пятерки элементов
buf.get_current_part() # вернуть [6]
buf.add(7, 8, 9, 10) # print(40) – вывод суммы второй пятерки элементов
buf.get_current_part() # вернуть []
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1) # print(5), print(5) – вывод сумм третьей и четвертой пятерки
buf.get_current_part() # вернуть [1]


class A:
    val = 1

   # def __init__(self):
       # self.val = 1

    def foo(self):
        A.val += 2

    def bar(self):
        self.val += 1


a = A()
b = A()
print("Const")
print(id(a.val), "a=", a.val)
print(id(b.val), "b=", b.val)
print(id(A.val), "A=", A.val)
a.bar()
print("bar")
print(id(a.val), "a=", a.val)
print(id(b.val), "b=", b.val)
print(id(A.val), "A=", A.val)
a.foo()
print("foo")
print(id(a.val), "a=", a.val)
print(id(b.val), "b=", b.val)
print(id(A.val), "A=", A.val)


c = A()

print("Вопрос про класс")
print(a.val)
print(b.val)
print(c.val)
print(id(a.val))
print(id(b.val))
print(id(c.val))