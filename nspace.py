stack = {'global': ('none', [])}


def add_space(name, parent):
    global stack
    stack[name] = (parent, [])


def add_arg(space, name):
    global stack
    stack.get(space)[1].append(name)


def get_arg(space, name):
    global stack
    if name in stack.get(space)[1]:
        return space
    elif space == 'global':
        return 'None'
    else:
        return get_arg(stack.get(space)[0], name)


def get_argf(space, name):
    print(get_arg(space, name))


cmds = {'create': add_space, 'add': add_arg, 'get': get_argf}
in_max = int(input())
for index in range(0, in_max):
    cmd, rspace, arg = input().split()
    cmds.get(cmd)(rspace, arg)