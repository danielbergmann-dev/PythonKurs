import pygame


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Space Invaders")
        self.clock = pygame.time.Clock()
        self.running = True
        self.spaceship = Spaceship(self, 370, 515)
        self.background_img = pygame.image.load("img/stars.png")

        while self.running:
            self.clock.tick(60)
            self.screen.fill((0, 0, 255))
            self.screen.blit(self.background_img, (0, 0))
            self.spaceship.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.spaceship.move(-15)
                    if event.key == pygame.K_RIGHT:
                        self.spaceship.move(15)

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.spaceship.move(15)
                    if event.key == pygame.K_RIGHT:
                        self.spaceship.move(-15)


            pygame.display.update()

class Spaceship:
    def __init__(self, game, x, y):
        self.game = game
        self.x = x
        self.y = y
        self.spaceship_img = pygame.image.load("img/spaceship.png")
        self.change_x = 0
    def move(self, speed):
        self.change_x += speed

    def update(self):
        self.x += self.change_x
        print(self.x)
        self.game.screen.blit(self.spaceship_img, (self.x, self.y))


if __name__ == "__main__":
    game = Game()
