import pygame
from objects import Spaceship, Planet


pygame.init()

WIDTH, HEIGHT = 800, 800  # Setting the window's parameters

window = pygame.display.set_mode((HEIGHT, WIDTH))  # Instantiate the window
pygame.display.set_caption('Gravitational Slingshot Effect') # Set the window title

PLANET_MASS: int = 100
SHIP_MASS: int = 5
G: int = 5   # Gravity index; The higher it gets, the more attraction we get
FPS: int = 60  # speed of the animation
PLANET_SIZE: int = 50  # radius of the planet
OBJ_SIZE: int = 5
VEL_SCALE: int = 100

BG = pygame.transform.scale(pygame.image.load('./images/background.jpg'), (WIDTH, HEIGHT))  # load the background file
# and scale it
# Same for Jupiter image:
PLANET = pygame.transform.scale(pygame.image.load('./images/jupiter.png'), (PLANET_SIZE * 2, PLANET_SIZE * 2))


# Define colors:
WHITE: tuple = (255, 255, 255)
RED: tuple = (255, 0, 0)
BLUE: tuple = (0, 0, 255)


def create_ship(win, location, mouse, ship_mass, size, color, vel_scale):
    temp_x, temp_y = location
    m_x, m_y = mouse
    vel_x = (m_x - temp_x) / vel_scale
    vel_y = (m_y - temp_y) / vel_scale
    return Spaceship(temp_x, temp_y, vel_x, vel_y, ship_mass, win, size, color, G)


def main():
    running: bool = True
    clock = pygame.time.Clock()
    planet = Planet(WIDTH / 2, HEIGHT / 2, PLANET_MASS, window, PLANET, PLANET_SIZE)
    objects: list = []
    temp_obj_pos = None  # temporarily placed object, not launched yet

    while running:
        clock.tick(FPS)
        mouse_pos = pygame.mouse.get_pos()  # get the current cursor position in (x, y) tuple
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running: bool = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if temp_obj_pos:
                    obj = create_ship(window, temp_obj_pos, mouse_pos, SHIP_MASS, OBJ_SIZE, RED, FPS)
                    objects.append(obj)
                    temp_obj_pos = None
                else:
                    temp_obj_pos = mouse_pos
        window.blit(BG, (0, 0))  # Place the image, starting from the left top corner (X=0, Y=0 in left top corner)
        if temp_obj_pos:
            pygame.draw.line(window, WHITE, temp_obj_pos, mouse_pos, 2)  # draw the white direction line starting
            # from circle to mouse cursor
            pygame.draw.circle(window, RED, temp_obj_pos, OBJ_SIZE)  # draw the position with circle
        for obj in objects:
            # Check if object is out of the screen. If so, delete from objects list in order to clear memory
            if obj.x > WIDTH or obj.x < 0:
                objects.remove(obj)
            if obj.y > HEIGHT or obj.y < 0:
                objects.remove(obj)
            # Check if the ship hit the planet. If so, remove it from objects list:
            planet_collision: bool = (obj.x < planet.x + PLANET_SIZE and obj.x > planet.x - PLANET_SIZE) and \
                                     (obj.y < planet.y + PLANET_SIZE and obj.y > planet.y - PLANET_SIZE)
            if planet_collision:
                objects.remove(obj)
            obj.move(planet)
            obj.draw()

        planet.draw()  # place the planet object / image
        pygame.display.update()
    pygame.quit()


if __name__ == '__main__':
    main()
