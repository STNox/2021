# n = int(input())
# def facto(n):
#     if n == 1 or n == 0:
#         return 1
#     return n * facto(n - 1)
# print(facto(n))

# n = int(input())
# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     return fibonacci(n - 1) + fibonacci(n - 2)
# print(fibonacci(n))

# n = int(input())
# shape = [[0 for i in range(n)] for i in range(n)]
# def stars(n):
#     global shape
#     if n == 3:
#         shape[0][:] = shape[2][:] = [1] * 3
#         shape[1] = [1, 0, 1]
#         return
#     a = n // 3
#     stars(a)
#     for i in range(3):
#         for j in range(3):
#             if i == 1 and j == 1:
#                 continue
#             for k in range(a):
#                 shape[a * i + k][a * j:a * (j + 1)] = shape[k][:a]
# stars(n)

# for i in shape:
#     for j in i:
#         if j:
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print()

n = int(input())
count = 0
from_to = []
def hanoi(n, from_, to_, via_):
    global count
    global from_to
    if n == 1:
        from_to.append([from_, to_])
        count += 1
    else:
        hanoi(n - 1, from_, via_, to_)
        from_to.append([from_, to_])
        count += 1
        hanoi(n - 1, via_, to_, from_)
hanoi(n, 1, 3, 2)
print(count)
for ft in from_to:
    print(ft[0], ft[1])