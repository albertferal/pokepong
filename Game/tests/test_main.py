def test_pygame_initialization():
    import pygame
    pygame.init()
    assert pygame.display.get_init() == True
