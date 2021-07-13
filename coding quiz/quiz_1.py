names = ['승우아빠', '장삐쭈', '새덕후', '우마']

for youtuber in names:
    filename = f'{youtuber}.txt'
    content = "안녕하세요?\t" f'{youtuber}'"님.\n\n" "(주)녹스출판 편집자 녹스입니다.\n현재 저희 출판사는 파이썬에 관한 주제로 책 출간을 기획 중입니다.\n" f'{youtuber}'"님의 유튜브 영상을 보고 연락을 드리게 되었습니다.\n자세한 내용은 첨부드리는ㅇ 제안서를 확인 부탁드리며, 긍정적인 회신 기다리겠습니다.\n\n좋은 하루 보내세요^^\n감사합니다.\n\n- 녹스 드림" 
        
    with open(filename, 'w', encoding='utf8') as file:
        file.write(content)


# 답안
# names = ['승우아빠', '장삐쭈', '새덕후', '우마']
# 1)
# for name in names:
#   with open('{}.txt'.format(name), 'w', encoding='utf8') as email_file:
#       email_file.write(f'''
# 안녕하세요? {name}님. ~   
#       ''')
# 2)
# for name in names:
#   with open('{}.txt'.format(name), 'w', encoding='utf8') as email_file:
#       contents = (f'안녕하세요? {name}님.\n\n'
#           '(주)녹스출판 편집자 녹스입니다.\n'~)      
#       email_file.write(contents)