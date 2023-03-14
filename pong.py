import pygame
pygame.init()

WIDTH, HEIGHT = 700, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60

WHITE, BLACK = (255, 255, 255), (0,0,0)

PADDLE_WIDTH, PADDLE_HEIGHT = 20, 100

BALL_RADIUS = 7

pygame.display.set_caption("Pong")


class Paddle:
    COLOR = WHITE
    VEL = 4
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def move(self, up =True):
        if up:
            self.y -= self.VEL
        else :
            self.y += self.VEL

               
    def draw(self, win):
        pygame.draw.rect(win, self.COLOR, (self.x, self.y, self.width, self.height))

class Ball:
    MAX_VEL = 5
    COLOR = WHITE
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.x_vel = self.MAX_VEL
        self.y_vel = 0

    def draw(self, win):
        pygame.draw.circle(win, self.COLOR, (self.x, self.y), self.radius)

    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel
         




def draw(win, paddles, ball):
    win.fill(BLACK)
    
    for paddle in paddles:
        paddle.draw(WIN)

    ball.draw(WIN)

    for i in range(10, HEIGHT, HEIGHT//20):
        if i % 2 == 1:
            continue
        pygame.draw.rect(win, WHITE, (WIDTH//2 - 5, i, 10, HEIGHT//20))


    pygame.display.update()

def handle_paddle_movement(keys, left_paddle, right_paddle):
    if keys[pygame.K_w] and (left_paddle.y-left_paddle.VEL)>=0:
        left_paddle.move()
    if keys[pygame.K_s] and (left_paddle.y+left_paddle.VEL+left_paddle.height)<=HEIGHT:
        left_paddle.move(False)
        
    if keys[pygame.K_UP] and (right_paddle.y-right_paddle.VEL)>=0:
        right_paddle.move()
    if keys[pygame.K_DOWN] and (right_paddle.y+right_paddle.VEL+right_paddle.height)<=HEIGHT:
        right_paddle.move(False)
    

def main():
    run = True
    clock = pygame.time.Clock()

    left_paddle = Paddle(10, HEIGHT//2-PADDLE_HEIGHT//2, PADDLE_WIDTH,PADDLE_HEIGHT)
    right_paddle = Paddle(WIDTH-10-PADDLE_WIDTH, HEIGHT//2-PADDLE_HEIGHT//2, PADDLE_WIDTH,PADDLE_HEIGHT)

    ball = Ball(WIDTH//2, HEIGHT//2, BALL_RADIUS)

    while run:
        clock.tick(FPS)
        draw(WIN, [left_paddle, right_paddle], ball)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        keys = pygame.key.get_pressed()
        handle_paddle_movement(keys, left_paddle, right_paddle)
    
        ball.move()
    pygame.quit()

if __name__ == '__main__':
    main()

