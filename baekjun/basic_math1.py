# a, b, c = map(int, input().split())
# if b > c or b == c:
#     x = -1
# else:
#     x = a / (c - b) + 1
# print(int(x))

# n = int(input())
# test = 0
# group = 0
# while True:
#     test += 6 * group + 1
#     if n <= test:
#         break
#     else:
#         test -= 1
#         group += 1
# print(group + 1)

# x = int(input())
# group = 1
# while True:
#     test = int(group * (group + 1) / 2)
#     if x <= test:
#         break
#     else:
#         group += 1
# diff = test - x
# if group % 2 == 0:
#     row, col = group, 1
#     col += diff
#     row -= diff
# else:
#     row, col = 1, group
#     col -= diff
#     row += diff
# print(f'{row}/{col}')

# import math
# a, b, v = map(int, input().split())
# days = math.ceil((v - b) / (a - b))
# print(days)

# t = int(input())
# for _ in range(t):
#     h, w, n = map(int, input().split())
#     if n % h == 0:
#         room_floor = h
#         room_num = n // h
#     else:
#         room_floor = n % h
#         room_num = n // h + 1
#     room_fl = str(room_floor)
#     if room_num < 10:
#         room_nm = '0' + str(room_num)
#     else:
#         room_nm = str(room_num)
#     print(f'{room_fl}{room_nm}')
    
# t = int(input())
# for _ in range(t):
#     k = int(input())
#     n = int(input())
#     zero_fl = [residents + 1 for residents in range(n)]
#     apt_dict = {}
#     apt_dict[0] = zero_fl
#     for i in range(k):
#         lower_fl = apt_dict[i][:n]
#         apt_dict[i + 1] = [sum(lower_fl[:i + 1]) for i in range(n)]
#     print(apt_dict[k][n - 1])
    
# n = int(input())
# bag_1 = 0
# combi = []
# while True:
#     bag_2 = int((n - 3 * bag_1) / 5)
#     total = bag_1 * 3 + bag_2 * 5
#     if total == n:
#         if bag_2 < 0:
#             break
#         else:
#             combi.append(bag_1 + bag_2)
#             bag_1 += 1
#     else:
#         bag_1 += 1
# if len(combi) < 1:
#     print(-1)
# else:
#     print(min(combi))

# a, b = map(int, input().split())
# print(a + b)

# [1] 1, 1
# [1, 1] 2, 2
# [1, 1, 1] 3
# [1, 2, 1] 4, 3
# [1, 2, 1, 1] 5
# [1, 2, 2, 1] 6, 4
# [1, 2, 2, 1, 1] 7
# [1, 2, 2, 2, 1] 8
# [1, 2, 3, 2, 1] 9, 5
# [1, 2, 3, 2, 1, 1] 10
# [1, 2, 3, 2, 2, 1] 11
# [1, 2, 3, 3, 2, 1] 12, 6
# [1, 2, 3, 3, 2, 1, 1] 13
# [1, 2, 3, 3, 2, 2, 1] 14
# [1, 2, 3, 3, 3, 2, 1] 15
# [1, 2, 3, 4, 3, 2, 1] 16, 7
# [1, 2, 3, 4, 3, 2, 1, 1] 17
# [1, 2, 3, 4, 4, 3, 2, 1] 20, 8
# [1, 2, 3, 4, 4, 3, 2, 1, 1] 21
# [1, 2, 3, 4, 5, 4, 3, 2, 1] 25, 9
t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    dist = y - x
    k = 1
    while True:
        sqr = k * k
        if sqr >= dist:
            if k * (k - 1) >= dist:
                operation_time = 2 * k - 2
            else:
                operation_time = 2 * k - 1
            break
        else:
            k += 1
    print(operation_time)