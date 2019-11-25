# задача про исключения
# создаем собственное исключение


class NonPositiveError(Exception):
    pass

class PositiveList(list):
    def append(self, x):
        if x > 0 : super(PositiveList, self).append(x)
        else: raise NonPositiveError("x - is non positive")


poslist = PositiveList()
poslist.append(4)
print(poslist)
poslist.append(-4)
