#import re
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

# import re
# word = input().upper()
# word2 = list(word)
# counts = []
# for w in word:
#     count = word.count(w)
#     counts.append(count)
#     word = re.sub(w, '', word)
# max_cnt = max(counts)
# if counts.count(max_cnt) > 1:
#     print('?')
# else:
#     most = word2[counts.index(max_cnt)]
#     print(most)

# s = input()
# count = re.findall('[a-zA-Z]+', s)
# length = len(count)
# print(length)

# import re
# a, b = input().split()
# a = list(a)
# b = list(b)
# a.reverse()
# b.reverse()
# sanggeun_a = int(''.join(a))
# sanggeun_b = int(''.join(b))
# print(max(sanggeun_a, sanggeun_b))

# import re
# dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
# time = 3
# total_time = 0
# word = input()
# idx = []
# for w in word:
#     for d in dial:
#         find_num = re.search(w, d)
#         if find_num:
#             idx.append(dial.index(d))
# for i in idx:
#     total_time += i + time
# print(total_time)

# import re
# cro_alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
# word = input()
# cro_abcs = 0
# for cro in cro_alphabet:
#     cro_check = re.findall(cro, word)
#     cro_abcs += len(cro_check)
#     for cc in cro_check:
#         word = word.replace(cc, ' ')
# space_check = re.findall('[a-z]', word)
# non_cro_abcs = len(space_check)
# print(cro_abcs + non_cro_abcs)

n = int(input())
group_word = 0
for _ in range(n):
    word = input()
    letters = []
    letters.append(word[0])
    for i in range(1, len(word)):
        if word[i] != word[i - 1]:
            letters.append(word[i])
    check = set(letters)
    if len(letters) == len(check):
        group_word += 1
print(group_word)
