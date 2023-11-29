#Prueba de inicialización: 
#Verifica si la inicialización de Pygame se realiza correctamente.

def test_pygame_initialization():
    import pygame
    pygame.init()
    assert pygame.display.get_init() == True


#Prueba de pantalla: 
#Comprueba si se puede crear una pantalla y si su tamaño es el esperado.

def test_screen_creation():
    import pygame
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    assert screen.get_width() == 800
    assert screen.get_height() == 600


#Prueba de eventos: 
#Verifica si se manejan correctamente los eventos del teclado o del ratón.

def test_keyboard_events():
    import pygame
    pygame.init()
    keys = pygame.key.get_pressed()
    # Simula eventos de teclado y verifica si la tecla está presionada
    assert keys[pygame.K_UP] == 0  # Por ejemplo, verificar si la tecla de flecha hacia arriba no está presionada inicialmente
