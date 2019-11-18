objects = [1, 2, 3, 3, 5, 3, 1, 6]

# 1.2
print("lesson 1.2 - links")
ans = 0
list_fo_id = []
for obj in objects:
    if id(obj) not in list_fo_id:
        list_fo_id.append(id(obj))
        ans += 1

print(ans)
