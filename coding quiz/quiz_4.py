class Word:
    def __init__(self, new_word, ex1, ex2, answer):
        self.new_word = new_word
        self.ex1 = ex1
        self.ex2 = ex2
        self.answer = answer
    
    def show_question(self):
        print(f'"{self.new_word}"의 뜻은?')
        print(f'1. {self.ex1}')
        print(f'2. {self.ex2}')

    def check_answer(self, script):
        if script == self.answer:
            print('정답입니다.')
        else:
            print('틀렸습니다.')

word = Word('애빼시', '애교 빼면 시체', '애들은 빼빼로 시시해', 1)
word.show_question()
word.check_answer(int(input('=> ')))
    

