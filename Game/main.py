import pygame
import sys

# Inicializamos Pygame
pygame.init()
#pygame.mixer.init()  # Inicializa el módulo de sonido
#goal_sound = pygame.mixer.Sound('assets\pokegol.mp3') 
#hit_sound = pygame.mixer.Sound("assets\pokehit.mp3")

# Definimos algunas constantes
WIDTH, HEIGHT = 800, 600
BALL_RADIUS = 15
PADDLE_WIDTH, PADDLE_HEIGHT = 15, 130
FPS = 60

# Definimos colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (28, 5, 171)
RED = (209, 17, 26)

# Creamos la pantalla
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Inicializamos las posiciones
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_speed_x = 3
ball_speed_y = 3

left_paddle_y = (HEIGHT - PADDLE_HEIGHT) // 2
right_paddle_y = (HEIGHT - PADDLE_HEIGHT) // 2

# Creamos los relojes para controlar el tiempo
clock = pygame.time.Clock()

# Función para manejar los eventos del juego
def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

ball_image = pygame.image.load("Game\PKBALL.png").convert_alpha()  # Reemplaza 'nombre_de_la_imagen.png' con tu nombre de archivo
ball_image = pygame.transform.scale(ball_image, (BALL_RADIUS * 3, BALL_RADIUS * 3))  # Cambiar el tamaño de la imagen
ball_image.set_colorkey((255, 255, 255))

background_image = pygame.image.load("Game\SCREENIMG2.png").convert()
ball_angle = 0  # Ángulo inicial de rotación


J1_score = 0
J2_score = 0

# Bucle principal del juego
while True:
    
    handle_events()
    # Movimiento de las paletas
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and left_paddle_y > 10:
        left_paddle_y -= 8
    if keys[pygame.K_s] and left_paddle_y < HEIGHT - PADDLE_HEIGHT -10:
        left_paddle_y += 8
    if keys[pygame.K_UP] and right_paddle_y > 10:
        right_paddle_y -= 8
    if keys[pygame.K_DOWN] and right_paddle_y < HEIGHT - PADDLE_HEIGHT -10:
        right_paddle_y += 8


    # Movimiento de la pelota
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Colisiones con las paletas
    if ball_x - BALL_RADIUS*2 < PADDLE_WIDTH and left_paddle_y < ball_y < left_paddle_y + PADDLE_HEIGHT:
            #hit_sound.play()
            ball_speed_x = -ball_speed_x
            ball_speed_y +=0.6
            ball_speed_x +=0.3
    elif ball_x + BALL_RADIUS*2 > WIDTH - PADDLE_WIDTH and right_paddle_y < ball_y < right_paddle_y + PADDLE_HEIGHT:
            #hit_sound.play()
            ball_speed_x = -ball_speed_x
            ball_speed_x -=0.6
            ball_speed_y -=0.3

    # Colisiones con las paredes superior e inferior
    if ball_y - BALL_RADIUS < 0 or ball_y + BALL_RADIUS > HEIGHT:
        ball_speed_y = -ball_speed_y
        
    #Colisiones con las paredes izq y der
    if ball_x + 30 < 0:
        ball_x = WIDTH // 2
        ball_y = HEIGHT // 2
        #goal_sound.play()
        ball_speed_x = 2
        ball_speed_y = 2
        J2_score +=1
    
     #Colisiones con las paredes izq y der
    if ball_x - 30 > WIDTH:
        ball_x = WIDTH // 2
        ball_y = HEIGHT // 2
        #goal_sound.play()
        ball_speed_x = -2
        ball_speed_y = -2
        J1_score +=1
        

    # Dibujamos en la pantalla
    screen.fill(BLACK)
    screen.blit(background_image, (60, 200))
    
    # Dibujar los marcadores en la pantalla
    font = pygame.font.Font(None, 36)
    left_score_text = font.render(f"RED: {J1_score}", True, WHITE)
    right_score_text = font.render(f"BLUE: {J2_score}", True, WHITE)
    screen.blit(left_score_text, (50, 50))
    screen.blit(right_score_text, (WIDTH - 160, 50))

    # Rotar la imagen de la pelota
    ball_rotated = pygame.transform.rotate(ball_image, ball_angle)
    ball_rotated.set_colorkey((255,255,255))
    ball_rect = ball_rotated.get_rect(center=(ball_x, ball_y))

    # Actualizar el ángulo para la próxima iteración (ajusta la velocidad de rotación según tu preferencia)
    ball_angle += 10  # Puedes cambiar el valor para ajustar la velocidad de giro
    # Dibujar la imagen rotada en la pantalla
    screen.blit(ball_rotated, ball_rect)

    #pygame.draw.circle(screen, WHITE, (ball_x, ball_y), BALL_RADIUS)
    pygame.draw.rect(screen, RED, (PADDLE_WIDTH, left_paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(screen, BLUE, (WIDTH - 2 * PADDLE_WIDTH, right_paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    

    # Actualizamos la pantalla
    pygame.display.flip()

    # Controlamos la velocidad de la pantalla
    clock.tick(FPS)
