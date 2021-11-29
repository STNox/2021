# while True:
#     a, b = map(int, input().split())
#     if a == 0 and b == 0:
#         break
#     else:
#         print(a + b)

# while True:
#     try:
#         a, b = map(int, input().split())
#         print(a + b)
#     except:
#         break
# a와 b가 입력되지 않았을 때 예외 처리를 위해 try-except 사용

n = int(input())
cycle = True
cycle_count = 0
num = n
while cycle:
    units = num % 10
    if num >= 0 and num < 10:
        tens = 0
    else:
        tens = num // 10
    new_num = units * 10 + ((units + tens) % 10)
    cycle_count += 1
    if new_num == n:
        cycle = False
        print(cycle_count)
    else:
        num = new_num
