# Sudoku Solving With Backtracking
from time import sleep
import pygame
import numpy as np


def drawingTheBoard(screen, sudoku_puzzle):
    space = 0
    for i in range(9):
        if (i == 3 or i == 6):
            space += 5

        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(
            5, 5 + (i * 55) + space, 50, 50))

        font = pygame.font.SysFont('timesnewroman',  40)

        text = font.render(str(i+1), True, (0, 0, 0))

        textRect = text.get_rect()

        textRect.center = (25 + 5, 25 + 5 + (i * 55) + space)

        screen.blit(text, textRect)

    space2 = 0

    for y in range(1, 10):
        space = 0
        if y == 4 or y == 7:
            space2 += 5
        for x in range(1, 10):
            if x == 4 or x == 7:
                space += 5
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(
                75 + ((x - 1) * 55) + space, 5 + ((y - 1) * 55) + space2, 50, 50))

            if (sudoku_puzzle[y-1][x-1] != 0):
                font = pygame.font.SysFont('timesnewroman',  40)

                text = font.render(
                    str(sudoku_puzzle[y-1][x-1]), True, (0, 0, 0))

                textRect = text.get_rect()

                textRect.center = (
                    25 + 75 + ((x - 1) * 55) + space, 25 + 5 + ((y - 1) * 55) + space2)

                screen.blit(text, textRect)


def checkPuzzle(sudoku_puzzle):
    checkRow = all([all([x in sudoku_puzzle[nrow, :]
                   for x in range(1, 10)]) for nrow in range(9)])
    checkCol = all([all([x in sudoku_puzzle[:, ncol]
                   for x in range(1, 10)]) for ncol in range(9)])

    checkUpperLeft = all([x in sudoku_puzzle[0:3, 0:3] for x in range(1, 10)])
    checkUpperMid = all([x in sudoku_puzzle[0:3, 3:6] for x in range(1, 10)])
    checkUpperRight = all([x in sudoku_puzzle[0:3, 6:9] for x in range(1, 10)])

    checkMidLeft = all([x in sudoku_puzzle[3:6, 0:3] for x in range(1, 10)])
    checkMidMid = all([x in sudoku_puzzle[3:6, 3:6] for x in range(1, 10)])
    checkMidRight = all([x in sudoku_puzzle[3:6, 6:9] for x in range(1, 10)])

    checkLowerLeft = all([x in sudoku_puzzle[6:9, 0:3] for x in range(1, 10)])
    checkLowerMid = all([x in sudoku_puzzle[6:9, 3:6] for x in range(1, 10)])
    checkLowerRight = all([x in sudoku_puzzle[6:9, 6:9] for x in range(1, 10)])

    solved = all([checkRow, checkCol, checkUpperLeft, checkUpperMid, checkUpperRight,
                  checkMidLeft, checkMidMid, checkMidRight, checkLowerLeft, checkLowerMid, checkLowerRight])
    return solved


def determineValues(sudoku_puzzle):
    puzzle_values = list()
    for r in range(9):
        for c in range(9):
            if sudoku_puzzle[r, c] == 0:
                cell_values = np.array(range(1, 10))
                cell_values = np.setdiff1d(
                    cell_values, sudoku_puzzle[r, :][np.where(sudoku_puzzle[r, :] != 0)]).tolist()
                cell_values = np.setdiff1d(
                    cell_values, sudoku_puzzle[:, c][np.where(sudoku_puzzle[:, c] != 0)]).tolist()
            else:
                cell_values = [sudoku_puzzle[r, c]]
            puzzle_values.append(cell_values)
    return puzzle_values


def checkGrids(r, c, sudoku_puzzle, n):
    if r < 3:
        if c < 3:
            subgrid = n in sudoku_puzzle[0:3, 0:3]
        elif c < 6:
            subgrid = n in sudoku_puzzle[0:3, 3:6]
        else:
            subgrid = n in sudoku_puzzle[0:3, 6:9]
    elif r < 6:
        if c < 3:
            subgrid = n in sudoku_puzzle[3:6, 0:3]
        elif c < 6:
            subgrid = n in sudoku_puzzle[3:6, 3:6]
        else:
            subgrid = n in sudoku_puzzle[3:6, 6:9]
    else:
        if c < 3:
            subgrid = n in sudoku_puzzle[6:9, 0:3]
        elif c < 6:
            subgrid = n in sudoku_puzzle[6:9, 3:6]
        else:
            subgrid = n in sudoku_puzzle[6:9, 6:9]
    return subgrid


s = [[0, 0, 8, 0, 0, 0, 4, 0, 0],
     [0, 0, 0, 4, 6, 0, 4, 9, 0],
     [0, 9, 0, 0, 1, 5, 0, 7, 0],
     [9, 8, 1, 7, 4, 0, 2, 0, 5],
     [0, 0, 3, 0, 0, 0, 1, 0, 6],
     [4, 6, 0, 3, 2, 1, 9, 0, 7],
     [8, 0, 7, 0, 3, 4, 0, 0, 0],
     [5, 4, 0, 0, 0, 0, 7, 0, 0],
     [0, 0, 0, 5, 0, 0, 0, 1, 0]]

controlTable = []
inGameTable = []
running = True
arr = np.array(s)
puzzle_values = determineValues(arr)
sudoku_puzzle = arr
count = 0
solution = False
rows = np.array(np.where(sudoku_puzzle == 0))[0]
cols = np.array(np.where(sudoku_puzzle == 0))[1]
dic = dict(zip(list(range(len(rows))), np.zeros(len(rows), dtype=int).tolist()))


pygame.init()
screen = pygame.display.set_mode([580, 510])

f = 1
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with black
    screen.fill((0, 0, 0))

    if f == 1:
        f = 2
        drawingTheBoard(screen, sudoku_puzzle.tolist())
        pygame.display.flip()
        sleep(5)
    else:
        if solution == False:
            if count >= len(rows):
                solution = checkPuzzle(sudoku_puzzle)
            else:
                r = rows[count]
                c = cols[count]
                len_num = len(np.array(puzzle_values).reshape(9, 9)[r, c])
                num = dic[count]
                while num < len_num:
                    cell = np.array(puzzle_values).reshape(9, 9)[r, c][num]
                    checkRow = cell in sudoku_puzzle[r, :]
                    if checkRow:
                        num += 1
                        continue
                    checkCol = cell in sudoku_puzzle[:, c]
                    if checkCol:
                        num += 1
                        continue
                    checkGrid = checkGrids(r, c, sudoku_puzzle, cell)
                    if checkGrid:
                        num += 1
                        continue
                    dic[count] = num
                    count += 1
                    sudoku_puzzle[r, c] = cell
                    break
                else:
                    sudoku_puzzle[r, c] = 0
                    dic[count] = 0
                    count -= 1

    drawingTheBoard(screen, sudoku_puzzle.tolist())

    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
