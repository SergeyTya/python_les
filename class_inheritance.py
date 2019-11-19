import time


class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))


class LoggableLis (list, Loggable):
    def append(self, el):
        list.append(self, el)
        Loggable.log(self, el)
       # super(LoggableLis, self).append(el)
       # super(LoggableLis, self).log(el)


x = LoggableLis([])
x.append('sdc')



