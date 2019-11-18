
def bfs(parent, child, graf): # обход графа
    global gr
    filo = [child]
    trash = []
    while True:
        if len(filo) == 0: return []
        child = filo.pop(0)
        if child not in graf: continue
        if child in trash: continue
        if parent in filo: break
        if child == parent: break
        filo = filo + graf[child]
        trash.append(child)
    trash.append(parent)
    return trash


def get_path(graf, parents): # востановление пути
    path = []
    while True:
        if len(parents) <= 1: break
        el = parents.pop()
        if len(path)==0: path.append(el)
        el1 = parents[-1]
        if el in graf[el1]: path.append(el1)

    return path




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
for _ in range(int(input())):
    cl = input().split() # из input.txt
    print("Parent=", cl[0], "Child=", cl[1])
    par = bfs(cl[0], cl[1], gr)
    print(par)
    print(get_path(gr , par))