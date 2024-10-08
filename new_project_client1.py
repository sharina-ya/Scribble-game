import pygame
import random
from network import Network

pygame.init()

# getting words to guess
# получаем слова для угадывания
file = open("слова.txt", "r", encoding="utf-8")
words = [i.rstrip() for i in file.readlines()]
file.close()

n = Network()
clientNumber = 0

width = 800
height = 500

win = pygame.display.set_mode((width, height))
pygame.display.set_caption('Игрок 1')


# converts recieved data into tuple
# преобразовывает полученную информацию в кортеж
def read_info(s):
    print(s)
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
        self.tick = 0
        self.time = 0
        self.play = False

    def draw(self, win, pos):
        #print(pos[0], pos[1], pos[2])
        n.send(make_info((pos[0], pos[1], pos[2], pos[3])))
        pygame.draw.circle(win, self.color, (pos[0], pos[1]), self.rad)
        if self.color == (255, 255, 255):
            pygame.draw.circle(win, self.color, (pos[0], pos[1]), 20)

    def click(self, win, list):
        pos = pygame.mouse.get_pos()

        color = ""
        if self.color == (0, 0, 0):
            color = "b"
        elif self.color == (255, 255, 255):
            color = "w"
        elif self.color == (255, 0, 0):
            color = "r"
        elif self.color == (0, 255, 0):
            color = "g"
        elif self.color == (0, 0, 255):
            color = "bl"

        pos += ("", color,)

        if pygame.mouse.get_pressed() == (1, 0, 0) and pos[0] < 700:
            if pos[1] > 25:
                self.draw(win, pos)
        elif pygame.mouse.get_pressed() == (1, 0, 0):
            for button in list:
                if pos[0] > button.x and pos[0] < button.x + button.width:
                    if pos[1] > button.y and pos[1] < button.y + button.height:
                        self.color = button.color2


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
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), self.outline)
        font = pygame.font.SysFont('comicsans', 30)
        text = font.render(self.text, 1, self.color2)
        win.blit(text, (int(self.x +self.width / 2 - text.get_width( ) /2),
                        int(self.y +self.height / 2 - text.get_height( ) /2)))


def draw_answer_field(win, input_text):
    input_rect = pygame.Rect(0, 400, 800, 120)
    pygame.draw.rect(win, (252, 169, 230), input_rect)
    font = pygame.font.SysFont('comicsans', 25)
    text_surface1 = font.render("Ответ игрока 2:", True, (179, 12, 131))
    text_surface2 = font.render(input_text, True, (179, 12, 131))
    win.blit(text_surface1, (input_rect.x + 10, input_rect.y + 10))
    win.blit(text_surface2, (input_rect.x + 10, input_rect.y + 50))

def draw_word_field(win, input_text):
    input_rect = pygame.Rect(0, 0, 800, 60)
    pygame.draw.rect(win, (252, 169, 230), input_rect)
    font = pygame.font.SysFont('comicsans', 30)
    text_surface = font.render("Ваше слово: " + input_text, True, (179, 12, 131))
    win.blit(text_surface, (30, 10))

def drawWin(win):
    player1.click(win, Buttons_color)

    pygame.draw.rect(win, (252, 169, 230), (700, 60, 100, 340) ,)
    pygame.draw.rect(win, (252, 169, 230), (0, 60, 100, 340), )
    pygame.draw.rect(win, (247, 15, 181), (100, 60, 600, 340),3)  # Drawing canvas space

    for button in Buttons_color:
        button.draw(win)

    pygame.display.update()

def random_word(words):
    return random.choice(words)

def main():
    run = True
    clock = pygame.time.Clock()
    word = random_word(words)


    while run:
        clock.tick(60)
        input_text = read_info(n.send(make_info((pos[0], pos[1], "", "b"))))[2]

        draw_answer_field(win, input_text)
        draw_word_field(win, word)

        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                run = False

        #endig game
        #условия окончания игры
        if word == input_text:
            n.send(make_info((pos[0], pos[1], "", "quit")))
            run = False

        drawWin(win)

    pygame.quit()


player1 = Drawing()
win.fill((255, 255, 255))
pos = (0, 0)

# defining color buttons
whiteButton = Button(720, 70, 60, 60, (255, 255, 255), (255, 255, 255))
blackButton = Button(720, 136, 60, 60, (0, 0, 0), (0, 0, 0))
redButton = Button(720, 202, 60, 60, (255, 0, 0), (255, 0, 0))
blueButton = Button(720, 268, 60, 60, (0, 0, 255), (0, 0, 255))
greenButton = Button(720, 334, 60, 60, (0, 255, 0), (0, 255, 0))

Buttons_color = [blackButton, whiteButton, redButton, blueButton, greenButton]


if __name__ == "__main__":
    main()
