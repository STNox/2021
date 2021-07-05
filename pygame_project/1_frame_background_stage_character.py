import pygame
import os
###################################################################################################
# 기본적인 초기 설정

pygame.init() # 초기화(필수)

# 화면 크기 설정
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption('Pang')

clock = pygame.time.Clock()

# 사용자 게임 초기화 (배경, 게임 이미지, 좌표, 속도 폰트 등)
current_path = os.path.dirname(__file__) # 현재 파일 위치 반환
image_path = os.path.join(current_path, 'images') # images 폴더 위치 반환

# 배경 만들기
background = pygame.image.load(os.path.join(image_path, 'background.png'))

# 스테이지 만들기
stage = pygame.image.load(os.path.join(image_path, 'stage.png'))
stage_size = stage.get_rect().size
stage_height = stage_size[1] # 스테이지 높이 위에 캐릭터를 두기 위함

# 캐릭터 만들기
character = pygame.image.load(os.path.join(image_path, 'character.png'))
character_size = character.get_rect().size # 이미지의 크기
character_width = character_size[0] # 캐릭터 가로 크기
character_height = character_size[1] # 캐릭터 세로 크기
character_x_pos = screen_width / 2 - character_width / 2 # 화면 가로의 중앙에 위치
character_y_pos = screen_height - character_height - stage_height # 스테이지 위에 위치

running = True
while running:
    dt = clock.tick(30)

# 화면에 그리기
    screen.blit(background, (0, 0)) # 배경 그리기
    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 그리기

    
    pygame.display.update() # 게임 화면 다시 그리기(필수)

# 종료 전 대기
pygame.time.delay(2000)

# pygame 종료
pygame.quit()