import pygame

pygame.init() # 초기화(필수)

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption('Just Game')

# 배경 이미지 불러오기
background = pygame.image.load('C:/Users/caush/Desktop/C/python/pygame_basic/background.png')

# 스프라이트(캐릭터) 불러오기
character = pygame.image.load('C:/Users/caush/Desktop/C/python/pygame_basic/character.png')
character_size = character.get_rect().size # 이미지의 크기
character_width = character_size[0] # 캐릭터 가로 크기
character_height = character_size[1] # 캐릭터 세로 크기
character_x_pos = screen_width / 2 - character_width / 2 # 화면 가로의 중앙에 위치
character_y_pos = screen_height - character_height # 화면 세로의 가장 아래에 위치

# 이벤트 루프
running = True # 게임이 진행중인지 확인
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트
            running = False # 게임이 진행중이지 않음
    
    screen.blit(background, (0, 0)) # 배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos))
    pygame.display.update() # 게임 화면 다시 그리기(필수)

# pygame 종료
pygame.quit()