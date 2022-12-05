from board import Board
from solver import dfs_solve, greedy_solve, a_star_solve
import pygame

SIZE = 3
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Button:
    def __init__(self, color, x, y, width, height, command, font, text=''):
        self.command = command
        self.bg = pygame.Rect(x, y, width, height)
        self.buttonText = font.render(text, True, (0, 0, 0))
        self.board = None
        self.color = color
        self.is_clicked = False

    def assing_board(self, board):
        self.board = board

    def render(self, display):
        self.update()
        pygame.draw.rect(display, self.color, self.bg)
        display.blit(self.buttonText, self.bg)

    def update(self):
        mouse_pos = pygame.mouse.get_pos()

        if pygame.mouse.get_pressed(num_buttons=3)[0] and self.is_clicked:
            return

        if not pygame.mouse.get_pressed(num_buttons=3)[0]:
            self.is_clicked = False
        else:
            self.is_clicked = True

        if pygame.mouse.get_pressed(num_buttons=3)[0] and self.bg.collidepoint(
                mouse_pos) and not self.board.solve_running:
            self.board.solve_running = True
            self.command(self.board)
            self.board.solve_running = False


def reset_board(board):
    board.reset_board()


def random_field(board):
    board.random_field_generation()


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
dfs_button = Button((253, 0, 6), 510, 10, 80, 80, dfs_solve, pygame.font.SysFont("Verdana", 32), "DFS")
greedy_button = Button((255, 219, 0), 510, 110, 80, 80, greedy_solve, pygame.font.SysFont("Verdana", 22), "Greedy")
a_star_button = Button((180, 242, 0), 510, 210, 80, 80, a_star_solve, pygame.font.SysFont("Verdana", 40), " A*")
reset_button = Button((0, 153, 153), 610, 110, 180, 80, reset_board, pygame.font.SysFont("Verdana", 32), "    Reset")
random_field = Button((0, 153, 153), 610, 210, 180, 80, random_field, pygame.font.SysFont("Verdana", 32), "   Random")
buttons = [dfs_button, greedy_button, a_star_button, reset_button, random_field]
board = Board(SIZE, screen, buttons)

screen.fill((40, 40, 40))
pygame.display.set_caption("Puzzle")
if __name__ == '__main__':

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a and not board.solved:
                    a_star_solve(board)
                if event.key == pygame.K_g and not board.solved:
                    greedy_solve(board)
                if event.key == pygame.K_d and not board.solved:
                    dfs_solve(board)
                if event.key == pygame.K_q:
                    running = False

        board.render_board()
        pygame.display.flip()

    pygame.quit()
