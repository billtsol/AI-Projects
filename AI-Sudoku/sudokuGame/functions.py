import classes as c
import pygame


def createBoard(controlTable, inGameTable, gameBoard):

    space = 0
    for i in range(9):
        if (i == 3 or i == 6):
            space += 5
        controlTable.append(c.gameSquare(i+1, 5, 5 + (i * 55) + space))

    space2 = 0
    for y in range(1, 10):
        space = 0
        if y == 4 or y == 7:
            space2 += 5
        for x in range(1, 10):
            if x == 4 or x == 7:
                space += 5
            inGameTable.append(c.gameSquare(
                gameBoard[y-1][x-1], 75 + ((x - 1) * 55) + space,  5 + ((y - 1) * 55) + space2, y-1, x-1))


def drawingTheBoard(screen, controlTable, inGameTable):
    for i in range(9):
        controlTable[i].drawRect(screen)

        font = pygame.font.SysFont('timesnewroman',  40)

        text = font.render(str(controlTable[i].squareNumber), True, (0, 0, 0))

        textRect = text.get_rect()

        textRect.center = (25 + controlTable[i].x, 25 + controlTable[i].y)

        screen.blit(text, textRect)

    for i in range(81):
        inGameTable[i].drawRect(screen)
        if (inGameTable[i].squareNumber != 0):
            font = pygame.font.SysFont('timesnewroman',  40)

            text = font.render(
                str(inGameTable[i].squareNumber), True, (0, 0, 0))

            textRect = text.get_rect()

            textRect.center = (25 + inGameTable[i].x, 25 + inGameTable[i].y)

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
    # if solved:
    #     for line in sudoku_puzzle:
    #         print(*line)
    return solved
