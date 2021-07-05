import pygame
import random
###################################################################################################
# 기본적인 초기 설정

pygame.init() # 초기화(필수)

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption('Quiz')

# FPS
clock = pygame.time.Clock()
###################################################################################################

# 1. 사용자 게임 초기화 (배경, 게임 이미지, 좌표, 속도 폰트 등)

# 배경 이미지 불러오기
background = pygame.image.load('C:/Users/caush/Desktop/C/python/2021Python/pygame_basic/background.png')

# 스프라이트(캐릭터) 불러오기
character = pygame.image.load('C:/Users/caush/Desktop/C/python/2021Python/pygame_basic/character.png')
character_size = character.get_rect().size # 이미지의 크기
character_width = character_size[0] # 캐릭터 가로 크기
character_height = character_size[1] # 캐릭터 세로 크기
character_x_pos = screen_width / 2 - character_width / 2 # 화면 가로의 중앙에 위치
character_y_pos = screen_height - character_height # 화면 세로의 가장 아래에 위치

# 이동할 좌표
to_x = 0
to_ey = 0.7

# 이동 속도
character_speed = 0.6

# 상대 캐릭터
enemy = pygame.image.load('C:/Users/caush/Desktop/C/python/2021Python/pygame_basic/enemy.png')
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = random.randint(0, screen_width - enemy_width)
enemy_y_pos = 0

# 폰트 정의
game_font = pygame.font.Font(None, 40) # 폰트 객체 생성(폰트, 크기)


# 시작 시간 정보
start_ticks = pygame.time.get_ticks() # 시작 tick을 받기

# 이벤트 루프
running = True # 게임이 진행중인지 확인
while running:
    dt = clock.tick(30) # 게임 화면의 FPS

# 2. 이벤트 처리 (키보드, 마우스 등)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트
            running = False # 게임이 진행중이지 않음

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            
# 3. 게임 캐릭터 위치 정의
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            
    character_x_pos += to_x * dt
    enemy_y_pos += to_ey * dt

    # 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    
    if enemy_x_pos < 0:
        enemy_x_pos = 0
    elif enemy_x_pos > screen_width - enemy_width:
        enemy_x_pos = screen_width - enemy_width
    
    if enemy_y_pos > screen_height:
        enemy_x_pos = random.randint(0, screen_width)
        enemy_y_pos = 0
    

# 4. 충돌 처리
    # 충돌 처리를 위한 rect 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # 충돌 체크
    if character_rect.colliderect(enemy_rect):
        print("충돌")
        running = False

# 5. 화면에 그리기
    screen.blit(background, (0, 0)) # 배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 그리기
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos)) # 상대 캐릭터 그리기
    
        

    # 타이머
    # 경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 # 경과 시간을 초 단위로 표시

    timer = game_font.render(str(int(elapsed_time)), True, (255, 255, 255)) # 출력할 글자, 안티앨리어싱, 색깔
    screen.blit(timer, (10, 10))

    pygame.display.update() # 게임 화면 다시 그리기(필수)

# 종료 전 대기
pygame.time.delay(2000)

# pygame 종료
pygame.quit()