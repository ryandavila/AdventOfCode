from collections import Counter

codes = [line.rstrip('\n') for line in open('2.in')]

#part (a)
letter_counts = []

for c in codes:
    letter_counts.append(Counter(list(c)).most_common(2))

twos = 0
threes = 0

for lc in letter_counts:
    if any(map(lambda t: t[1] == 2, lc)):
        twos += 1
    if any(map(lambda t: t[1] == 3, lc)):
        threes += 1

print(twos*threes)

#part (b)
def countDiff(str1, str2):
    count = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            count += 1
    return count

ans1 = 0
ans2 = 0
for i in range(len(codes)):
    j = i+1
    for j in range(len(codes)):
        baseString = codes[i]
        testString = codes[j]
        if (countDiff(baseString, testString) == 1):
            ans1 = testString
            ans2 = baseString   #assigns twice

index = 0
for i in range(len(ans1)):
    if ans1[i] != ans2[i]:
        index = i

answer = ans1[:index]+ans1[index+1:]
print(answer)
