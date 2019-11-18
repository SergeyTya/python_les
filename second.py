# 1.3



def closest_mod_5(x):
    tmp = x % 5
    if tmp == 0:
        return x
    return x-tmp+5


z = 0


def c(n, k):
    global z
    z += 1
    if k == 0:
        return 1
    if k > n:
        return 0
    return c(n-1, k) + c(n-1, k-1)


#z = 0
# n, k = map(int, input().split())
print(c(10, 5), z)

