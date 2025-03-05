import pygame, sys

pygame.init()


def main():
    clock = pygame.time.Clock()
    size = width, height = 800, 800
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Piłka i grawitacja!')

    icon = pygame.image.load('favicon.ico')
    pygame.display.set_icon(icon)

    pygame.mixer.music.load(r'music.mp3')
    pygame.mixer.music.play(-1)

    background = pygame.image.load(r'moon.jpg')
    background = pygame.transform.scale(background, size)

    ball = pygame.image.load('ball.gif')
    ball = pygame.transform.scale(ball, (ball.get_width() // 2, ball.get_height() // 2))

    ballrect = ball.get_rect(center=(width / 2, height / 2))
    velocity = [3, -10]
    acceleration = [0, 0.5]
    energy_loss_factor = 0.9
    rolling_friction = 0.995
    min_velocity_threshold = 0.05
    near_ground_threshold = 10

    while True:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()
        if keys[pygame.K_UP]:
            velocity[1] -= 0.5
        if keys[pygame.K_DOWN]:
            velocity[1] += 0.5
        if keys[pygame.K_LEFT]:
            velocity[0] -= 0.5
        if keys[pygame.K_RIGHT]:
            velocity[0] += 0.5

        velocity[0] += acceleration[0]
        velocity[1] += acceleration[1]

        ballrect = ballrect.move(velocity)

        if ballrect.left < 0 or ballrect.right > width:
            velocity[0] = -velocity[0] * energy_loss_factor  #
        if ballrect.bottom > height - near_ground_threshold:
            if abs(velocity[1]) < min_velocity_threshold:
                velocity[1] = 0
                ballrect.bottom = height
                velocity[0] *= rolling_friction
                if abs(velocity[0]) < min_velocity_threshold:
                    velocity[0] = 0
            else:
                velocity[1] = -velocity[1] * energy_loss_factor
                ballrect.bottom = height
        elif ballrect.top < 0:
            velocity[1] = -velocity[1] * energy_loss_factor

        if ballrect.bottom >= height - near_ground_threshold:
            velocity[0] *= rolling_friction

        screen.blit(background, (0, 0))
        screen.blit(ball, ballrect)
        pygame.display.flip()


if __name__ == '__main__':
    main()
