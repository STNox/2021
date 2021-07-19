import pygame, os

# 집게 클래스
class Claw(pygame.sprite.Sprite):
    def __init__(self, image, position):
        super().__init__()
        self.image = image
        self.original_image = image
        self.rect  = image.get_rect(center=position)

        self.offset = pygame.math.Vector2(default_offset_x_claw, 0)
        self.position = position

        self.direction = LEFT # 집게의 이동 방향
        self.angle_speed = 2.5 # 집게의 각도 변경 폭(좌우 이동 속도)
        self.angle = 10 # 최초 각도 정의(오른쪽 끝)

    def update(self, to_x):
        if self.direction == LEFT:
            self.angle += self.angle_speed
        elif self.direction == RIGHT:
            self.angle -= self.angle_speed
        
        if self.angle > 170:
            self.angle = 170
            self.set_direction(RIGHT)
        elif self.angle < 10:
            self.angle = 10
            self.set_direction(LEFT)

        self.offset.x += to_x
        self.rotate()

    def rotate(self):
        self.image = pygame.transform.rotozoom(self.original_image, -self.angle, 1) # 회전 대상 이미지, 회전 각도, 이미지 크기
        
        offset_rotated = self.offset.rotate(self.angle)

        self.rect = self.image.get_rect(center=self.position + offset_rotated)

    def set_direction(self, direction):
        self.direction = direction

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        pygame.draw.circle(screen, RED, self.position, 3) # 중심점 표시
        pygame.draw.line(screen, BLACK, self.position, self.rect.center, 5) # 직선 그리기

    def set_init_state(self):
        self.offset.x = default_offset_x_claw
        self.angle = 10
        self.direction = LEFT

# 보석 클래스
class Gemstone(pygame.sprite.Sprite):
    def __init__(self, image, position):
        super().__init__()
        self.image = image
        self.rect = image.get_rect(center=position)

def setup_gemstone():
    # 작은 금
    small_gold = Gemstone(gemstone_images[0], (200, 380)) # 0번째 이미지를 (200, 380) 위치에
    gemstone_group.add(small_gold)
    # 큰 금
    gemstone_group.add(Gemstone(gemstone_images[1], (300, 500)))
    # 돌
    gemstone_group.add(Gemstone(gemstone_images[2], (300, 380)))
    # 다이아몬드
    gemstone_group.add(Gemstone(gemstone_images[3], (900, 420)))

pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Gold Miner')
clock = pygame.time.Clock()

# 게임 관련 변수
default_offset_x_claw = 40 # 중심점으로부터 집게까지의 기본 x 간격
to_x = 0

# 속도 변수
move_speed = 12 # 발사할 때 이동 속도 (x 좌표 기준으로 증가되는 값)
return_speed = 20

# 방향 변수
LEFT = -1 # 왼쪽 방향
STOP = 0 # 위치 고정
RIGHT = 1 # 오른쪽 방향

# 색깔 변수
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# 배경 이미지 불러오기
current_path = os.path.dirname(__file__)
background = pygame.image.load(os.path.join(current_path, 'background.png'))

# 4가지 오브젝트 이미지 불러오기(작은 금, 큰 금, 돌, 다이아몬드)
gemstone_images = [
    pygame.image.load(os.path.join(current_path, 'small_gold.png')),
    pygame.image.load(os.path.join(current_path, 'big_gold.png')),
    pygame.image.load(os.path.join(current_path, 'stone.png')),
    pygame.image.load(os.path.join(current_path, 'diamond.png'))
]

# 보석  그룹
gemstone_group = pygame.sprite.Group()
setup_gemstone() # 게임에 원하는 만큼의 보석을 정의

# 집게
claw_image = pygame.image.load(os.path.join(current_path, 'claw.png'))
claw = Claw(claw_image, (screen_width // 2, 110))

running = True
while running:
    clock.tick(30)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            claw.set_direction(STOP)
            to_x =  move_speed

    if claw.rect.left < 0 or claw.rect.right > screen_width or claw.rect.bottom > screen_height:
        to_x = -return_speed
    
    if claw.offset.x < default_offset_x_claw: # 집게 원위치
        to_x = 0
        claw.set_init_state() # 처음 상태로 초기화

    screen.blit(background, (0, 0))

    gemstone_group.draw(screen) # 그룹 내 모든 스프라이트를 screen에 그림
    claw.update(to_x)
    claw.draw(screen)
    pygame.display.update()

pygame.quit()