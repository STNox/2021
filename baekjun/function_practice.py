# def solve(a):
#     add = sum(a)
#     return add

# num = [n for n in range(1, 10001)]
# def selfnum(num):
#     has_consts = []
#     for i in range(len(num)):
#         under_10000 = True
#         mom_num = num[i]
#         while under_10000:
#             units = list(map(int, [k for k in str(mom_num)]))
#             child_num = mom_num + sum(units)
#             if child_num <= 10000:
#                 has_consts.append(child_num)
#                 mom_num = child_num
#             else:
#                 under_10000 = False
#     has_consts = list(set(has_consts))
#     selfnumber = num
#     for j in range(len(has_consts)):
#         selfnumber.remove(has_consts[j])
    
#     for sn in selfnumber:
#         print(sn)

# selfnum(num)

n = int(input())
if n < 100:
    hansu = n
else:
    hansu = 99
    nums = [num for num in range(100, n + 1)]
    for nm in nums:
        units = list(map(int, [i for i in str(nm)]))
        if units[2] - units[1] == units[1] - units[0]:
            hansu += 1
print(hansu)
        