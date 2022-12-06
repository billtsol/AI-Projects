# Sudoku Solving With Backtracking
import pygame
import functions as f

pygame.init()
s = [[2, 0, 0, 0, 0, 7, 5, 0, 0],
     [0, 6, 5, 0, 1, 0, 0, 0, 4],
     [7, 0, 0, 0, 5, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 6, 9, 0, 3],
     [6, 0, 0, 0, 0, 0, 0, 7, 8],
     [0, 7, 4, 0, 0, 1, 0, 0, 0],
     [0, 0, 0, 4, 0, 0, 0, 0, 1],
     [4, 3, 7, 0, 0, 0, 0, 9, 5],
     [9, 0, 2, 5, 3, 8, 0, 0, 0]]

sol = [[2, 4, 3, 6, 8, 7, 5, 1, 9],
       [8, 6, 5, 9, 1, 3, 7, 2, 4],
       [7, 9, 1, 2, 5, 4, 3, 8, 6],
       [1, 5, 8, 7, 2, 6, 9, 4, 3],
       [6, 2, 9, 3, 4, 5, 1, 7, 8],
       [3, 7, 4, 8, 9, 1, 6, 5, 2],
       [5, 8, 6, 4, 7, 9, 2, 3, 1],
       [4, 3, 7, 1, 6, 2, 8, 9, 5],
       [9, 1, 2, 5, 3, 8, 4, 6, 7]]
pygame.init()
controlTable = []
inGameTable = []
running = True

screen = pygame.display.set_mode([580, 510])

clickedButton = -1

f.createBoard(controlTable, inGameTable, s)


while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with black
    screen.fill((0, 0, 0))

    f.drawingTheBoard(screen, controlTable, inGameTable)

    controlTableHoverEffect = False
    inGameTableHoverEffect = False
    # Draw the board
    for i in range(9):
        if controlTable[i].isHover():
            controlTableHoverEffect = True

        if controlTable[i].isClicked():
            if clickedButton != -1:
                controlTable[clickedButton].clicked = False
                clickedButton = -1

            controlTable[i].clicked = True
            clickedButton = i

        if controlTable[i].clicked:
            controlTable[i].backgroumdColor = (5, 190, 220)
        else:
            controlTable[i].backgroumdColor = (255, 255, 255)

    if clickedButton != -1:
        for i in range(81):
            if (inGameTable[i].isHover()):
                inGameTableHoverEffect = True
            if inGameTable[i].isClicked() and inGameTable[i].squareNumber == 0:
                if controlTable[clickedButton].squareNumber == sol[inGameTable[i].row][inGameTable[i]
                                                                                       .column]:
                    s[inGameTable[i].row][inGameTable[i]
                                          .column] = controlTable[clickedButton].squareNumber
                    inGameTable[i].squareNumber = controlTable[clickedButton].squareNumber

    if controlTableHoverEffect or inGameTableHoverEffect:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
    else:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
