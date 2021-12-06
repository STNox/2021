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

t = int(input())
for _ in range(t):
    n = int(input())
    sieve = [1] * (n + 1)
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == 1:
            for j in range(i * 2, n + 1, i):
                sieve[j] = 0
    prime_nums = [i for i in range(2, n + 1) if sieve[i] == 1]
    goldbach = []
    for i in range(int(len(prime_nums) / 2) + 1):
        a = n - prime_nums[i]
        if a in prime_nums:
            goldbach.append(a)
    less_diff = sorted([min(goldbach), n - min(goldbach)])
    print(less_diff[0], less_diff[1])
        