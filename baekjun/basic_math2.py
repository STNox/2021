# n = int(input())
# nums = [number for number in map(int, input().split())]
# prime_nums = []
# for num in nums:
#     divisor = []
#     for i in range(1, num + 1):
#         if num % i == 0:
#             divisor.append(i)
#     if len(divisor) == 2:
#         prime_nums.append(num)
# print(len(prime_nums))

# m = int(input())
# n = int(input())
# nums = [number for number in range(m, n + 1)]
# prime_nums = []
# for num in nums:
#     divisor = 1
#     while divisor <= num:
#         divisor += 1
#         if num % divisor == 0 and divisor < num:
#             break
#         elif divisor == num:
#             prime_nums.append(num)
#             break
# if len(prime_nums) == 0:
#     print(-1)
# else:
#     print(sum(prime_nums))
#     print(min(prime_nums))

# n = int(input())
# if n != 1:
#     prime_factor = []
#     for i in range(2, n + 1):
#         while n % i == 0:
#             if n % i == 0:
#                 prime_factor.append(i)
#                 n = n // i
#     for pf in prime_factor:
#         print(pf)

# m, n = map(int, input().split())
# sieve = [1] * (n + 1)
# multiple = int(n ** 0.5)
# for i in range(2, multiple + 1):
#     if sieve[i] == 1:
#         for j in range(i * 2,  n + 1, i):
#             sieve[j] = 0
# sieve[1] = 0
# prime_nums = [i for i in range(m, n + 1) if sieve[i] == 1]
# for pn in prime_nums:
#     print(pn)

# while True:
#     n = int(input())
#     if n == 0:
#         break
#     sieve = [1] * (n * 2 + 1)
#     m = int((n * 2) ** 0.5)
#     for i in range(2, m + 1):
#         if sieve[i] == 1:
#             for j in range(i * 2, n * 2 + 1, i):
#                 sieve[j] = 0
#     sieve[1] = 0
#     prime_nums = [i for i in range(n + 1, n * 2 + 1) if sieve[i] == 1]
#     print(len(prime_nums))

# sieve = [1] * 10001
# m = int(10001 ** 0.5)
# for i in range(2, m + 1):
#     if sieve[i] == 1:
#         for j in range(i * 2, 10001, i):
#             sieve[j] = 0

# t = int(input())
# for _ in range(t):
#     n = int(input())
#     a = n // 2
#     b = a
#     for _ in range(10000):
#         if sieve[a] == 1 and sieve[b] == 1:
#             print(a, b)
#             break
#         a -= 1
#         b += 1

# x, y, w, h = map(int, input().split())
# left = x
# right = w - x
# up = h - y
# down = y

# print(min(left, right, up, down))

# ax, ay = map(int, input().split())
# bx, by = map(int, input().split())
# cx, cy = map(int, input().split())
# nx = ny = 0
# xys = [[ax, bx, cx, nx], [ay, by, cy, ny]]
# for i in range(2):
#     if xys[i][0] - xys[i][1] == 0:
#         xys[i][3] += xys[i][2]
#     else:
#         if xys[i][1] - xys[i][2] == 0:
#             xys[i][3] += xys[i][0]
#         else:
#             xys[i][3] += xys[i][1]
# print(xys[0][3], xys[1][3])

# while True:
#     a, b, c = map(int, input().split())
#     if a + b + c > 0:
#         legs = [a, b, c]
#         hypo = max(a, b, c)
#         legs.remove(hypo)
#         if hypo ** 2 == legs[0] ** 2 + legs[1] ** 2:
#             print('right')
#         else:
#             print('wrong')
#     else:
#         break

# import math
# r = int(input())
# pi = math.pi
# euclid = pi * (r ** 2)
# taxi = 2 * (r ** 2)
# print(euclid)
# print(taxi)

t = int(input())
for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    dist = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    if x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)
    elif x1 == x2 and y1 == y2 and r1 != r2:
        print(0)
    elif x1 != x2 or y1 != y2:
        if (r1 > dist + r2) or (r2 > dist + r1):
            print(0)
        elif (r1 == dist + r2) or (r2 == dist + r1):
            print(1)
        else:
            if r1 + r2 > dist:
                print(2)
            elif r1 + r2 == dist:
                print(1)
            else:
                print(0)