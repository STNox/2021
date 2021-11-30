import re
# x = input()
# number = re.match('[0-9]', x)
# if number:
#     print(chr(x))
# else:
#     print(ord(x))

# n = int(input())
# num = input()
# units = list(map(int, num))
# add = sum(units)
# print(add)

# from string import ascii_lowercase
# alphabets = list(ascii_lowercase)
# abcs = ''.join(alphabets)
# s = input()
# idxs = []
# for i in abcs:
#     m = re.search(i, s)
#     if m:
#         idx = m.start()
#     else:
#         idx = -1
#     idxs.append(str(idx))
# print(' '.join(idxs))

# t = int(input())
# for _ in range(t):
#     r, s = input().split()
#     r = int(r)
#     output = ''
#     for i in s:
#         output += i * r
#     print(output)

import sys
word = sys.stdin.readline().rstrip().upper()
word2 = list(word)
counts = []
for w in word2:
    count = word2.count(w)
    counts.append(count)
    while w in word2:
        word2.remove(w)
max_cnt = max(counts)
if counts.count(max_cnt) == 1:
    print(word[counts.index(max_cnt)])
else:
    print('?')