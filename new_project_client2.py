import pygame
from network import Network

pygame.init()

n = Network()
clientNumber = 0

width = 800
height = 500

win = pygame.display.set_mode((width, height))
pygame.display.set_caption('Игрок 2')


# converts recieved data into tuple
# преобразовывает полученную информацию в кортеж
def read_info(s):
    #print(s)
    s = s.split(",")
    return int(s[0]), int(s[1]), (s[2]), (s[3])

# converts data into string (to send it to another server)
# преобразовывает нужную информацию в строку, которую потом отправим на другой сервер
def make_info(tup):
    return str(tup[0]) + "," + str(tup[1]) + "," + str(tup[2]) + "," + str(tup[3])


# рисовалка
# painter class (handle clicks and drawing)
class Drawing(object):
    def __init__(self):
        self.color = (0, 0, 0)
        self.width = 10
        self.height = 10
        self.rad = 3

    def draw(self, win, pos):
        if pos[3] == "b":
            self.color = (0, 0, 0)
        elif pos[3] == "w":
            self.color = (255, 255, 255)
        elif pos[3] == "r":
            self.color = (255, 0, 0)
        elif pos[3] == "g":
            self.color = (0, 255, 0)
        elif pos[3] == "bl":
            self.color = (0, 0, 255)

        pygame.draw.circle(win, self.color, (pos[0], pos[1]), self.rad)
        if self.color == (255, 255, 255):
            pygame.draw.circle(win, self.color, (pos[0], pos[1]), 20)


# drawing buttons
# рисуем кнопки
class Button(object):
    def __init__(self, x, y, width, height, color, color2, outline=0, action=0, text=''):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.color = color
        self.outline = outline
        self.color2 = color2
        self.action = action
        self.text = text

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y,
                                           self.width, self.height), self.outline)
        font = pygame.font.SysFont('comicsans', 30)
        text = font.render(self.text, 1, self.color2)
        win.blit(text, (int(self.x + self.width / 2 - text.get_width() / 2),
                        int(self.y + self.height / 2 - text.get_height() / 2)))


def draw_input_field(win, input_text):
    input_rect = pygame.Rect(0, 400, 800, 120)
    pygame.draw.rect(win, (252, 169, 230), input_rect)
    font = pygame.font.SysFont('comicsans', 25)
    text_surface1 = font.render("Введите ваш ответ:", True, (179, 12, 131))
    text_surface2 = font.render(input_text, True, (179, 12, 131))
    win.blit(text_surface1, (input_rect.x + 10, input_rect.y + 10))
    win.blit(text_surface2, (input_rect.x + 10, input_rect.y + 50))


def drawWin(win):
    input_rect = pygame.Rect(0, 0, 800, 60)
    pygame.draw.rect(win, (252, 169, 230), input_rect)
    font = pygame.font.SysFont('comicsans', 30)
    text_surface = font.render("Вы угадываете", True, (179, 12, 131))
    win.blit(text_surface, (30, 10))

    pygame.draw.rect(win, (252, 169, 230), (700, 60, 100, 340), )
    pygame.draw.rect(win, (252, 169, 230), (0, 60, 100, 340), )
    pygame.draw.rect(win, (247, 15, 181), (100, 60, 600, 340), 3)  # drawing canvas space

    pygame.display.update()


def main():
    run = True
    clock = pygame.time.Clock()
    answer = ""
    input_text = ""

    while run:
        clock.tick(60)

        playerInf = n.send("0,0," + answer + ",b")
        if playerInf != None:
            playerInf = read_info(playerInf)
            if playerInf[3] == "quit":
                run = False
                break
            player1.draw(win, playerInf)

        # handling text input
        # ввод текста
        keys = pygame.key.get_pressed()
        draw_input_field(win, input_text)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                elif event.key == pygame.K_RETURN:
                    answer = input_text
                    input_text = ""
                else:
                    input_text += event.unicode

        drawWin(win)

    pygame.quit()


player1 = Drawing()
win.fill((255, 255, 255))
pos = (0, 0)

if __name__ == "__main__":
    main()
