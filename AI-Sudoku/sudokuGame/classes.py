import pygame


class gameSquare():
    def __init__(self, squareNumber, x, y, row=-1, column=-1):
        self.squareNumber = squareNumber
        self.x = x
        self.y = y
        self.row = row
        self.column = column
        self.isOnBoard = False
        self.backgroumdColor = (255, 255, 255)
        self.clicked = False
        self.hove = False

    def isHover(self):
        return pygame.Rect(self.x, self.y, 50, 50).collidepoint(pygame.mouse.get_pos())

    def drawRect(self, game_screen):
        pygame.draw.rect(game_screen, self.backgroumdColor,
                         pygame.Rect(self.x, self.y, 50, 50))

    def isClicked(self):
        return pygame.mouse.get_pressed()[0] and self.isHover()
