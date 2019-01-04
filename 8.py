data = list(map(int, open('8.txt').read().split()))
i = 0

def next_value():
    global i, data
    i += 1
    return data[i-1]

def read_tree():
    next_child, next_metadata = next_value(), next_value()
    children = []
    metadata = []
    if next_child > 0:
        for i in range(next_child):
            children.append(read_tree())
    for i in range(next_metadata):
        metadata.append(next_value())
    return (children, metadata)

def sum_metadata(data):
    children, metadata = data
    total = 0
    for d in metadata:
        total += d
    for c in children:
        total += sum_metadata(c)
    return total

def value_metadata(data):
    children, metadata = data
    value = 0
    if not children:
        value += sum(metadata)
    else:
        for m in metadata:
            if m-1 >= len(children):
                continue
            value += value_metadata(children[m-1])
    return value

tree = read_tree()
print(sum_metadata(tree))
print(value_metadata(tree))
