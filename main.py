import pygame
from logger import log_state, log_event
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, SHOT_COOLDOWN_TIMER
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys
from shot import Shot

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))



def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        for astro in asteroids:
            if player1.collides_with(astro):
                log_event("player hit")
                print("Game Over!")
                sys.exit()
            for shot in shots:
                if shot.collides_with(astro):
                    log_event("asteroid hit")
                    astro.split()
                    shot.kill()
                
            
        clk_obj = pygame.time.Clock()
        dt = 0
        log_state()
        screen.fill('black')
        
        #player1.draw(screen)
        for item in drawable:
            item.draw(screen)

        pygame.display.flip()
        dt = clk_obj.tick(60) / 1000.0
        #player1.update(dt)
        updatable.update(dt)
        player1.shot_cooldown -= dt
        #print(dt)


if __name__ == "__main__":
    main()
