import pygame

pygame.init() # 초기화(필수)

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption('Just Game')

# 이벤트 루프
running = True # 게임이 진행중인지 확인
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트
            running = False # 게임이 진행중이지 않음

# pygame 종료
pygame.quit()