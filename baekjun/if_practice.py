# a, b = map(int, input().split())
# if a > b:
#     print('>')
# elif a < b:
#     print('<')
# else:
#     print('==')

# score = int(input())
# if 90 <= score <= 100:
#     print('A')
# elif score >= 80:
#     print('B')
# elif score >= 70:
#     print('C')
# elif score >= 60:
#     print('D')
# else:
#     print('F')

# year = int(input())
# if year % 4 == 0 and ((year % 100 != 0) or (year % 400 == 0)):
#     print('1')
# else:
#     print('0')

# x = int(input())
# y = int(input())
# if x > 0 and y > 0:
#     print('1')
# elif x < 0 and y > 0:
#     print('2')
# elif x < 0 and y < 0:
#     print('3')
# elif x > 0 and y < 0:
#     print('4')

h, m = map(int, input().split())
a_m = m - 45
if a_m < 0:
    a_h = h - 1
    if a_h < 0:
        a_h += 24
    a_m += 60
else:
    a_h = h
print(a_h, a_m)