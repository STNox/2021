import random

vocab = ['green', 'yellow', 'red', 'blue']
num = random.randint(0, len(vocab) - 1)
corr_answer = vocab[num]
question = ''
for i in range(0, len(corr_answer)):
    question += '_ '
print(question)

while '_' in question:
    answer = input('input letter> ')
    if len(answer) > 1:
        print('알파벳 하나만 입력하십시오.')
        

    if answer in corr_answer:
        for idx, spell in enumerate(corr_answer):
            if spell == answer:
                if '_' in question:
                    print('Correct\n')
                quest_list = question.split()
                quest_list[idx] = spell
                question = ' '.join(quest_list)
                print(question)
    else:
        print('Wrong')

print('Success')

# 답안
# from random import *
# words = ['green', 'yellow', 'red', 'blue']
# word = choice(words)
# letters = '' # 사용자로부터 입력받은 문자열
#
# while True:
#   success = True
#   print() # 공백 출력(줄 띄우기)
#   for w in word:
#       if w in letters:
#           print(w, end=' ') # 줄 바꿈 없애기
#       else:
#           print('_', end=' ')
#           success = False
#   print()
#   
#   if success:
#       print('Success')
#       break
#
#   letter = input('input letter> ')
#   if letter not in letters:
#       letters += letter
#
#   if letter in word:
#       print('Correct')
#   else:
#       print('Wrong')