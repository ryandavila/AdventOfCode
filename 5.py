polymer = ''.join([line.rstrip('\n') for line in open('5.txt')])

#part a
stack = []
alphabet = 'abcdefghijklmnopqrstuvwxyz'
alpha = {}
for a in alphabet:
    alpha[a.upper()] = a.lower()
    alpha[a.lower()] = a.upper()

for c in polymer:
    if stack and alpha[stack[-1]] == c:
        stack = stack[:-1]
    else:
        stack.append(c)
print(len(stack))

#part b
length = 100000
for a in alphabet:
    new_polymer = polymer.replace(a, '').replace(a.upper(), '')
    stack = []
    for c in new_polymer:
        if stack and alpha[stack[-1]] == c:
            stack.pop()
        else:
            stack.append(c)
    length = min(length, len(stack))
print(length)
