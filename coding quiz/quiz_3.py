seats = [f'A{n}' for n in range(1, 21)]
for i in range(0, 20, 2):
    print(seats[i], end=' ')

# 답안1
# for i in range(1, 21):
#    if i % 2 == 1:
#       print('A' + str(i), end=' ')

# 답안2
# for i in range(1, 21)[::2]:
#   print('A' + str(i), end=' ')