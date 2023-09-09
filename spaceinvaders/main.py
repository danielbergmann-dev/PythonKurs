import pygame


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Space Invaders")
        self.clock = pygame.time.Clock()
        self.running = True
        self.background_img = pygame.image.load("img/stars.png")

        while self.running:
            self.clock.tick(60)
            self.screen.fill((0, 0, 255))
            self.screen.blit(self.background_img, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            pygame.display.update()


if __name__ == "__main__":
    game = Game()
