# n = int(input())
# for i in range(1, 10):
#     mul = n * i
#     print(f'{n} * {i} = {mul}')

# t = int(input())
# for i in range(t):
#     a, b = map(int, input().split())
#     print(a + b)

# n = int(input())
# s = 0
# for i in range(1, n + 1):
#     s += i
# print(s)

# import sys
# t = int(input())
# for i in range(t):
#     a, b = map(int, sys.stdin.readline().rstrip().split())
#     print(a + b)
# 여러 줄을 입력할 경우 input()보다 sys.stdin.readline()을 쓰는 것이 빠르다.
# sys.stdin.readline()은 개행문자까지 입력 받기 때문에 .rstrip()을 사용한다.

# n = int(input())
# for i in range(n):
#     print(i + 1)

# n = int(input())
# for i in range(n):
#     m = n - i
#     print(m)

# t = int(input())
# for i in range(1, t + 1):
#     a, b = map(int, input().split())
#     s = a + b
#     print(f'Case #{i}: {s}')

# t = int(input())
# for i in range(1, t + 1):
#     a, b = map(int, input().split())
#     s = a + b
#     print(f'Case #{i}: {a} + {b} = {s}')

# n = int(input())
# for i in range(1, n + 1):
#     star = '*' * i
#     print(star)

# n = int(input())
# for i in range(1, n + 1):
#     star = ' ' * (n - i) + '*' * i
#     print(star)

n, x = map(int, input().split())
lst = input().split()
result = []
for i in range(n):
    if int(lst[i]) < x:
        result.append(lst[i])
print(' '.join(result))