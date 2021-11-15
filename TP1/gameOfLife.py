import pygame
import numpy as np
import os, sys

col_about_to_die = (200, 200, 225)
col_alive = (255, 255, 215)
col_background = (10, 10, 40)
col_grid = (30, 30, 60)
# Main definition - constants
menu_actions = {}
dimx = 85
dimy = 70


def update(surface, cur, sz):
    nxt = np.zeros((cur.shape[0], cur.shape[1]))

    for r, c in np.ndindex(cur.shape):
        num_alive = np.sum(cur[r - 1:r + 2, c - 1:c + 2]) - cur[r, c]

        if cur[r, c] == 1 and num_alive < 2 or num_alive > 3:
            col = col_about_to_die
        elif (cur[r, c] == 1 and 2 <= num_alive <= 3) or (cur[r, c] == 0 and num_alive == 3):
            nxt[r, c] = 1
            col = col_alive

        col = col if cur[r, c] == 1 else col_background
        pygame.draw.rect(surface, col, (c * sz, r * sz, sz - 1, sz - 1))

    return nxt


def main_menu():
    os.system('clear')

    print("Welcome,\n")
    print("Please choose the menu you want to start:")
    print("1. Glider Gun")
    print("2. Random")
    print("3. Diehard")
    print("4. Boat")
    print("5. R pentomino")
    print("6. beacon")
    print("7. acorn")
    print("8. spaceship")
    print("9. Block Switch Engine ")
    print("\n0. Quit")
    choice = input(" >>  ")
    exec_menu(choice)
    return


# Execute menu
def exec_menu(choice):
    os.system('clear')
    ch = choice.lower()
    if ch == '':
        menu_actions['main_menu']()
    else:
        try:
            menu_actions[ch]()
        except KeyError:
            print("Invalid selection, please try again.\n")
            menu_actions['main_menu']()
    return


def glider_gun():
    cells = np.zeros((dimy, dimx))
    glider_gun = np.array(
        [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
         [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

    pos = (10, 19)
    cells[pos[0]:pos[0] + glider_gun.shape[0], pos[1]:pos[1] + glider_gun.shape[1]] = glider_gun
    return cells


def random():
    cells = np.zeros((dimy, dimx))
    pattern = np.random.randint(2, size=(50, 50))
    pos = (10, 19)
    cells[pos[0]:pos[0] + pattern.shape[0], pos[1]:pos[1] + pattern.shape[1]] = pattern
    return cells


def diehard():
    cells = np.zeros((dimy, dimx))
    diehard = np.array([[0, 0, 0, 0, 0, 0, 1, 0],
                        [1, 1, 0, 0, 0, 0, 0, 0],
                        [0, 1, 0, 0, 0, 1, 1, 1]])

    pos = (30, 35)
    cells[pos[0]:pos[0] + diehard.shape[0], pos[1]:pos[1] + diehard.shape[1]] = diehard
    return cells


def boat():
    cells = np.zeros((dimy, dimx))
    boat = np.array([[1, 1, 0],
                     [1, 0, 1],
                     [0, 1, 0]])

    pos = (30, 35)
    cells[pos[0]:pos[0] + boat.shape[0], pos[1]:pos[1] + boat.shape[1]] = boat
    return cells


def r_pentomino():
    cells = np.zeros((dimy, dimx))
    r_pentomino = np.array([[0, 1, 1],
                            [1, 1, 0],
                            [0, 1, 0]])
    pos = (30, 35)
    cells[pos[0]:pos[0] + r_pentomino.shape[0], pos[1]:pos[1] + r_pentomino.shape[1]] = r_pentomino
    return cells


def beacon():
    cells = np.zeros((dimy, dimx))
    beacon = np.array([[0, 0, 1, 1],
                       [0, 0, 1, 1],
                       [1, 1, 0, 0],
                       [1, 1, 0, 0]])
    pos = (30, 35)
    cells[pos[0]:pos[0] + beacon.shape[0], pos[1]:pos[1] + beacon.shape[1]] = beacon
    return cells


def acorn():
    cells = np.zeros((dimy, dimx))
    acorn = np.array([[0, 1, 0, 0, 0, 0, 0],
                      [0, 0, 0, 1, 0, 0, 0],
                      [1, 1, 0, 0, 1, 1, 1]])
    pos = (30, 35)
    cells[pos[0]:pos[0] + acorn.shape[0], pos[1]:pos[1] + acorn.shape[1]] = acorn
    return cells


def spaceship():
    cells = np.zeros((dimy, dimx))
    spaceship = np.array([[0, 0, 1, 1, 0],
                          [1, 1, 0, 1, 1],
                          [1, 1, 1, 1, 0],
                          [0, 1, 1, 0, 0]])
    pos = (30, 2)
    cells[pos[0]:pos[0] + spaceship.shape[0], pos[1]:pos[1] + spaceship.shape[1]] = spaceship
    return cells


def block_switch_engine():
    cells = np.zeros((dimy, dimx))
    block_switch_engine = np.array([[0, 0, 0, 0, 0, 0, 1, 0],
                                    [0, 0, 0, 0, 1, 0, 1, 1],
                                    [0, 0, 0, 0, 1, 0, 1, 0],
                                    [0, 0, 0, 0, 1, 0, 0, 0],
                                    [0, 0, 1, 0, 0, 0, 0, 0],
                                    [1, 0, 1, 0, 0, 0, 0, 0]])
    pos = (30, 35)
    cells[pos[0]:pos[0] + block_switch_engine.shape[0],
    pos[1]:pos[1] + block_switch_engine.shape[1]] = block_switch_engine
    return cells


def init():
    #return diehard()
    #return random()
    #return boat()
    #return r_pentomino()
    #return beacon()
    #return acorn()
    return spaceship()
    #return block_switch_engine()


# Back to main menu
def back():
    menu_actions['main_menu']()


# Exit program
def exit():
    sys.exit()


# =======================
#    MENUS DEFINITIONS
# =======================

# Menu definition
menu_actions = {
    'main_menu': main_menu,
    '1': glider_gun,
    '2': random,
    '3': diehard,
    '4': boat,
    '5': r_pentomino,
    '6': beacon,
    '7': acorn,
    '8': spaceship,
    '9': block_switch_engine,
    '10': back,
    '0': exit,
}


def main(cellsize):
    pygame.init()
    surface = pygame.display.set_mode((dimx * cellsize, dimy * cellsize))
    pygame.display.set_caption("Quentin Pierson Game of Life")

    cells = init()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        surface.fill(col_grid)
        cells = update(surface, cells, cellsize)
        pygame.display.update()


if __name__ == "__main__":
    main(8)
    # main_menu()
