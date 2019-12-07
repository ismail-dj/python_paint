import pygame


class Brush:
    def paint(self, screen, color, x, y):
        pygame.draw.rect(screen, color, pygame.Rect(x, y, 5, 5))


class Colors:
    def __init__(self, screen, color, x, y):
        self.color = color
        self.x = x
        self.y = y
        pygame.draw.rect(screen, color, pygame.Rect(x, y, 50, 20))
        self.rect = None
        self.collidebox()

    def collidebox(self):
        self.rect = pygame.Rect(self.x, self.y, 50, 20)


class App:
    def __init__(self):
        pygame.init()
        pygame.font.init()

        self.screen = pygame.display.set_mode((500, 520))

        self.COLORS = {0: (255, 0, 0),
                       1: (255, 140, 0),
                       2: (255, 255, 0),
                       3: (0, 255, 0),
                       4: (0, 0, 255),
                       5: (128, 0, 128),
                       6: (0, 0, 0),
                       7: (255, 255, 255)}
        self.clock = pygame.time.Clock()
        self.myfont = pygame.font.SysFont('Arial', 13)
        self.mytext = self.myfont.render("Press ENTER to SAVE", False, (0,0,0))

    def main(self):
        done = False
        brush = Brush()
        mybrush = False
        mycolor = 0
        colornum = 0
        left = 1
        right = 3
        picnum = 0
        self.screen.fill(self.COLORS.get(7))
        self.red = Colors(self.screen, self.COLORS.get(0), 0, 500)
        self.orange = Colors(self.screen, self.COLORS.get(1), 50, 500)
        self.yellow = Colors(self.screen, self.COLORS.get(2), 100, 500)
        self.green = Colors(self.screen, self.COLORS.get(3), 150, 500)
        self.blue = Colors(self.screen, self.COLORS.get(4), 200, 500)
        self.purple = Colors(self.screen, self.COLORS.get(5), 250, 500)
        self.black = Colors(self.screen, self.COLORS.get(6), 300, 500)
        self.white = Colors(self.screen, self.COLORS.get(7), 350, 500)
        self.buttons = [self.red, self.orange, self.yellow, self.green, self.blue, self.purple, self.black, self.white]
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == left:
                    mybrush = True
                elif event.type == pygame.MOUSEBUTTONUP:
                    mybrush = False
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == right:
                    colornum += 1
                    if colornum == 8:
                        colornum = 0
                    mycolor = self.COLORS.get(colornum)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        rect = pygame.Rect(0, 0, 500, 500)
                        sub = self.screen.subsurface(rect)
                        pygame.image.save(sub, "paintpictures/mypicture%s.jpg" % picnum)
                        print("SAVED")
                        picnum += 1
            mouse_pos = pygame.mouse.get_pos()

            pygame.draw.rect(self.screen, self.COLORS.get(6), (350, 500, 50, 19), 2)

            if mybrush and mouse_pos[1] <= 490:
                brush.paint(self.screen, mycolor, event.pos[0],
                            event.pos[1])

            for b in self.buttons:
                if b.rect.collidepoint(mouse_pos):
                    mycolor = b.color

            self.screen.blit(self.mytext, (415,505))
            pygame.display.flip()

            self.clock.tick(60)


app = App()
app.main()
