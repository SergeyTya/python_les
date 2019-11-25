class multifilter:
    def judge_half(pos, neg):
        # допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg)
        if pos >= neg: return True
        return False

    def judge_any(pos, neg):
        # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)
        if pos >= 1: return True
        return False

    def judge_all(pos, neg):
        # допускает элемент, если его допускают все функции (neg == 0)
        if neg == 0: return True
        return False

    def __init__(self, iterable, *funcs, judge=judge_any):
        # iterable - исходная последовательность
        # funcs - допускающие функции
        # judge - решающая функция
        self.iterable = iterable
        self.funcs = funcs
        self.judge = judge

    def __iter__(self):
        for el in self.iterable:
            pos = 0; neg = 0
            for fun in self.funcs:
                if fun(el): pos += 1
                else: neg += 1
            if self.judge(pos, neg): yield el


def mul2(x):
    return x % 2 == 0


def mul3(x):
    return x % 3 == 0


def mul5(x):
    return x % 5 == 0


a = [i for i in range(31)]  # [0, 1, 2, ... , 30]
multifilter1 = multifilter(a, mul2, mul3, mul5)

print(list(multifilter1))