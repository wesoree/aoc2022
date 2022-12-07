from functools import cached_property
from itertools import chain




class File:
    def __init__(self, name, size, parent):
        self.name = name
        self.size = size
        self.parent = parent
    
class Directory:
    def __init__(self, name, parent = None, children = None):
        self.name = name
        self.parent = parent
        self.children = children or []
    
    @cached_property
    def size(self):
        return sum(c.size for c in self.children)

def build_file_tree(commands):
    root = Directory(name='root')
    current_directory = root
    for line in commands:
        if line.startswith('$'):
            prompt, command, *target = line.split()
            if command == 'cd':
                if target == ['..']:
                    current_directory = current_directory.parent
                else:
                    current_directory = next(filter(lambda c: c.name == target[0], current_directory.children))
        else:
            p1, p2 = line.split()
            if p1 == 'dir':
                item = Directory(name=p2, parent=current_directory)
            else:
                item = File(name=p2, size=int(p1), parent=current_directory)
            if item.name not in {c.name for c in current_directory.children}:
                current_directory.children.append(item)
    return root

def find_items(node, comparason):
    dirs = [c for c in node.children if isinstance(c,Directory)]
    node = [node] if comparason(node.size) else []
    return node + list(chain.from_iterable(map(lambda c: find_items(c, comparason), dirs)))

def sol1(input_string):
    root = build_file_tree(input_string.splitlines()[1:])

    return print(sum(i.size for i in find_items(root, comparason=lambda n: n<=100000)))

def sol2(input_string):
    root = build_file_tree(input_string.splitlines()[1:])

    free_space = 70000000 - root.size
    need_to_free = 30000000 - free_space

    return print(min(find_items(root, lambda n: n>= need_to_free), key=lambda x: x.size).size)
if __name__ == '__main__':
    with open('day7input.txt') as f:
        f = f.read()
    sol1(f)
    sol2(f)