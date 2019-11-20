
def bfs(parent, child, graf): # обход графа
    filo = [child]
    trash = []
    while True:
        if len(filo) == 0: return False
        tmp = filo.pop(0)
        if tmp not in graf: continue
        if tmp in trash: continue
        if parent in filo: break
        if tmp == parent: break
        filo = filo + graf[tmp]
        trash.append(tmp)
    return True


gr = {'Obj': []}

for _ in range(int(input())):
    cl = input().split()
    name = cl.pop(0)
    gr[name] = []
    if len(cl) == 0: continue
    cl.pop(0)
    for el in cl:
        gr[name].append(el)
        if el not in gr: gr[el] = []
cl=[]
for _ in range(int(input())):
    chld = input()
    if any(bfs(el, chld, gr) for el in cl): print(chld)
    cl.append(chld)

