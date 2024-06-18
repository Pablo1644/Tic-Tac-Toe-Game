import pygame
import sys

# Initialize Pygame
pygame.init()

# VARIABLES
height = 600
width = 600
sqr_size = height / 3
lin_width = 1
line_color = "black"

screen = pygame.display.set_mode((height, width))
pygame.display.set_caption('Kółko i krzyżyk')
board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


def check_win(sign):
    if board[0][0] == board[0][1] == board[0][2] == sign:
        print(f'{sign} wins')
        return True
    elif board[1][0] == board[1][1] == board[1][2] == sign:
        print(f'{sign} wins')
        return True
    elif board[2][0] == board[2][1] == board[0][2] == sign:
        print(f'{sign} wins')
        return True
    elif board[0][0] == board[1][1] == board[2][2] == sign:
        print(f'{sign} wins')
        return True
    elif board[0][2] == board[1][1] == board[2][0] == sign:
        print(f'{sign} wins')
        return True
    elif board[0][0] == board[1][0] == board[2][0] == sign:
        print(f'{sign} wins')
        return True
    elif board[0][1] == board[1][1] == board[2][1] == sign:
        print(f'{sign} wins')
        return True
    elif board[0][2] == board[1][1] == board[2][0] == sign:
        print(f'{sign} wins')
        return True
    elif board[0][2] == board[1][2] == board[2][2] == sign:
        print(f'{sign} wins')
        return True


# Functions
def draw_board():
    pygame.draw.line(screen, line_color, (0, sqr_size), (width, sqr_size), lin_width)
    pygame.draw.line(screen, line_color, (0, 2 * sqr_size), (width, 2 * sqr_size), lin_width)
    pygame.draw.line(screen, line_color, (sqr_size, 0), (sqr_size, height), lin_width)
    pygame.draw.line(screen, line_color, (2 * sqr_size, 0), (2 * sqr_size, height), lin_width)


def find_square_clicked(x1: int, y1: int) -> list[int]:
    return [int(x1 // sqr_size), int(y1 // sqr_size)]


# Main loop
screen.fill((200, 100, 0))
draw_board()

running = True
move_of_circle = True
move_of_cross = False
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            circle_X = find_square_clicked(x, y)[0] * sqr_size + sqr_size / 2
            circle_Y = find_square_clicked(x, y)[1] * sqr_size + sqr_size / 2
            cross_X: int = int(find_square_clicked(x, y)[0])
            cross_Y: int = int(find_square_clicked(x, y)[1])
            if move_of_circle and board[cross_X][cross_Y] == 0:
                pygame.draw.circle(screen, (100,100,111), (circle_X, circle_Y), sqr_size / 2)
                move_of_circle = False
                move_of_cross = True
                board[int(cross_X)][int(cross_Y)] = "circle"
            elif move_of_cross and board[cross_X][cross_Y] == 0:
                pygame.draw.line(screen, "white", (cross_X * sqr_size, cross_Y * sqr_size),
                                 (cross_X * sqr_size + sqr_size, cross_Y * sqr_size + sqr_size), lin_width)
                pygame.draw.line(screen, "white", (cross_X * sqr_size, cross_Y * sqr_size + sqr_size),
                                 (cross_X * sqr_size + sqr_size, cross_Y * sqr_size), lin_width)
                move_of_circle = True
                move_of_cross = False
                board[int(cross_X)][int(cross_Y)] = "cross"
    if check_win('circle') or check_win('cross'):
        running = False
    if 0 not in board[0] and 0 not in board[1] and 0 not in board[2]:
        running = False

    # Update the display
    pygame.display.flip()
print("END OF GAME")
# Quit Pygame
pygame.quit()
sys.exit()
