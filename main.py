import pygame






class Board:
    def __init__(self, size, ceil_size):
        self.board = []
        self.x, self.y = size
        self.w, self.h = ceil_size
        self.n = self.x // self.w
        self.k = self.y // self.h
        self.broad = [[0] * self.n for i in range(self.k)]


    def update(self):
        x, y = 0, 0
        for i in range(self.k):
            for j in range(self.n):
                pygame.draw.rect(screen, (255, 0, 0), (x, y, self.w, self.h), 1)
                if self.broad[i][j] == 1:
                    pygame.draw.circle(screen, (255, 0, 0), (x + self.w // 2, y + self.h // 2), self.w // 2, 2)
                elif self.broad[i][j] == 2:
                    pygame.draw.line(screen, (255, 0, 0), [x, y], [self.w + x, self.h + y], 2)
                    pygame.draw.line(screen, (255, 0, 0), [self.w + x, y], [x, self.h + y], 2)

                x += self.w
            x = 0
            y += self.h


    def fill_ceil(self, i, j,button):
        if self.broad[i][j] == 0:
            if button == 1:
                self.broad[i][j] = 1
            else:
                self.broad[i][j] = 2


















pygame.init()
screen = pygame.display.set_mode((800, 600))
main_bord = Board((400, 400), (30, 30))
running = True
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            j = x // main_bord.w
            i = y // main_bord.h
            main_bord.fill_ceil(i, j,event.button)

    main_bord.update()
    pygame.display.flip()
pygame.quit()
