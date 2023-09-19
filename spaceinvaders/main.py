import pygame
import random
import math

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Space Invaders")
        self.clock = pygame.time.Clock()
        self.initialize_game()
        self.game_loop()

    def initialize_game(self):
        self.running = True
        self.spaceship = Spaceship(self, 370, 515)
        self.score = 0
        self.background_img = pygame.image.load("img/stars.png")
        self.enemies = []
        for i in range(12):
            self.enemies.append(
                Enemy(self, random.randint(0, 736), random.randint(50, 150))
            )

    def restart_game(self):
        self.initialize_game()

    def game_loop(self):
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
                    if event.key == pygame.K_SPACE:
                        self.spaceship.fire_bullet()
                    if event.key == pygame.K_r:
                        self.restart_game()

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        self.spaceship.change_x = 0

            if len(self.spaceship.bullets) > 0:
                for bullet in self.spaceship.bullets:
                    if bullet.is_fired:
                        bullet.update()
                    else:
                        self.spaceship.bullets.remove(bullet)

            for enemy in self.enemies:
                enemy.update()
                enemy.check_collision()
                if random.random() < 0.01:  # 1% Chance pro Frame, dass ein Feind schießt
                    enemy.fire_bullet()

                if enemy.y >= 440:
                    for i in self.enemies:
                        i.y = 2000
                    self.print_game_over()
                    break

                for bullet in enemy.bullets:
                    bullet.update()
                    distance = math.sqrt(
                        math.pow(self.spaceship.x - bullet.x, 2) + math.pow(self.spaceship.y - bullet.y, 2)
                    )
                    if distance < 35:
                        for i in self.enemies:
                            i.y = 2000
                        self.print_game_over()
                        break

            self.print_score()
            pygame.display.update()

    def print_game_over(self):
        go_font = pygame.font.Font("freesansbold.ttf", 64)
        go_text = go_font.render("GAME OVER", True, (255, 255, 255))
        self.screen.blit(go_text, (200, 250))

        restart_font = pygame.font.Font("freesansbold.ttf", 32)
        restart_text = restart_font.render("Press 'R' to Restart", True, (255, 255, 255))
        self.screen.blit(restart_text, (230, 350))


    def print_score(self):
        score_font = pygame.font.Font("freesansbold.ttf", 32)
        score_text = score_font.render("Score: " + str(self.score), True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))

class Spaceship:
    def __init__(self, game, x, y):
        self.game = game
        self.x = x
        self.y = y
        self.spaceship_img = pygame.image.load("img/spaceship.png")
        self.change_x = 0
        self.bullets = []

    def fire_bullet(self):
        self.bullets.append(Bullet(self.game, self.x, self.y))
        self.bullets[len(self.bullets) - 1].fire()

    def move(self, speed):
        self.change_x += speed

    def update(self):
        self.x += self.change_x
        if self.x <= 0:
            self.x = 0
        elif self.x >= 736:
            self.x = 736
        self.game.screen.blit(self.spaceship_img, (self.x, self.y))


class Bullet:
    def __init__(self, game, x, y):
        self.game = game
        self.x = x
        self.y = y
        self.bullet_img = pygame.image.load("img/bullet.png")
        self.bullet_speed = 10

    def fire(self):
        self.is_fired = True

    def update(self):
        self.y -= self.bullet_speed
        if self.y <= 0:
            self.is_fired = False

        self.game.screen.blit(self.bullet_img, (self.x, self.y))


class EnemyBullet(Bullet):
    def __init__(self, game, x, y):
        super().__init__(game, x, y)
        self.bullet_speed = -5  # Negative Geschwindigkeit, um nach unten zu schießen


class Enemy:
    def __init__(self, game, x, y):
        self.game = game
        self.x = x
        self.y = y
        self.change_x = 5
        self.change_y = 60
        self.enemy_img = pygame.image.load("img/enemy.png")
        self.enemy_speed = 10
        self.bullets = []

    def fire_bullet(self):
        self.bullets.append(EnemyBullet(self.game, self.x, self.y))
        self.bullets[len(self.bullets) - 1].fire()

    def check_collision(self):
        for bullet in self.game.spaceship.bullets:
            distance = math.sqrt(
                math.pow(self.x - bullet.x, 2) + math.pow(self.y - bullet.y, 2)
            )
            if distance < 35:
                bullet.is_fired = False
                self.game.score += 1
                self.x = random.randint(0, 736)
                self.y = random.randint(50, 150)

    def update(self):
        self.x += self.change_x
        if self.x >= 736:
            self.change_x = -5
            self.y += self.change_y
        elif self.x < 0:
            self.change_x = 5
            self.y += self.change_y

        self.game.screen.blit(self.enemy_img, (self.x, self.y))


if __name__ == "__main__":
    game = Game()
