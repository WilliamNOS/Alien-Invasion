import pygame

class AlienBoss: 
    """A class to manage Alien Boss"""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect
        self.image = pygame.image.load('image/alienboss.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Drawn the ship at its current location"""
        self.screen.blit(self.image, self.rect)
