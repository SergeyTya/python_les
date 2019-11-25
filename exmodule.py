# работа с модулем Datetaime
import datetime

ils = list(map(int, input().split()))
mydt = datetime.date(ils[0], ils[1], ils[2]) + datetime.timedelta(int(input()))
print(mydt.strftime("%Y %-m %-d"))



