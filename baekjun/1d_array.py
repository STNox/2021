# n = int(input())
# lst = input().split()
# minVal = int(lst[0])
# maxVal = int(lst[0])
# for i in range(n):
#     if minVal > int(lst[i]):
#         minVal = int(lst[i])
# for i in range(n):
#     if maxVal < int(lst[i]):
#         maxVal = int(lst[i])
# print(minVal, maxVal)

# n_list = [input() for _ in range(9)]
# maxVal = int(n_list[0])
# for i in range(len(n_list)):
#     if maxVal < int(n_list[i]):
#         maxVal = int(n_list[i])

# validx = n_list.index(str(maxVal)) + 1
# print(maxVal)
# print(validx)

# a = int(input())
# b = int(input())
# c = int(input())
# mul = a * b * c
# digits = []
# for m in str(mul):
#     digits.append(m)
# for i in range(10):
#     digi_count = digits.count(str(i))
#     print(digi_count)

# n_list = [int(input()) for _ in range(10)]
# remains = []
# for i in range(len(n_list)):
#     remains.append(n_list[i] % 42)
# remains_set = set(remains)
# print(len(remains_set))

# n = int(input())
# scores = input().split()
# n_scores = []
# for s in scores:
#     n_scores.append(int(s))
# max_score = max(n_scores)
# fake_scores = []
# for i in range(len(n_scores)):
#     fake_scores.append(n_scores[i] / max_score * 100)
# avg_score = sum(fake_scores) / n
# print(avg_score)

# t = int(input())
# for _ in range(t):
#     oxes = input()
#     oes = oxes.split('X')
#     while '' in oes:
#         oes.remove('')
#     points = 0
#     for o in oes:
#         points += len(o) * (len(o) + 1) / 2
#     print(int(points))

c = int(input())
for _ in range(c):
    scores = list(map(int, input().split()))
    std_count = scores[0]
    avg_score = (sum(scores) - std_count) / std_count
    pass_member = []
    for i in range(1, std_count + 1):
        if scores[i] > avg_score:
            pass_member.append(scores[i])
    pass_perc = '{:.3f}%'.format(len(pass_member) / std_count * 100)
    print(pass_perc)