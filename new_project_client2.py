import pygame
from network import Network

pygame.init()

n = Network()
clientNumber = 0

width = 800
height = 500

win = pygame.display.set_mode((width, height))
pygame.display.set_caption('Игрок 2')

def read_position(s):
    #print(s)
    s = s.split(",")
    return int(s[0]), int(s[1]), (s[2]), (s[3])

def make_position(tup):
    return str(tup[0]) + "," + str(tup[1]) + "," + str(tup[2]) + "," + str(tup[3])

# Class for drawing
class drawing(object):

    def __init__(self):
        '''constructor'''
        self.color = (0, 0, 0)
        self.width = 10
        self.height = 10
        self.rad = 3
        self.tick = 0
        self.time = 0
        self.play = False

    # Drawing Function
    def draw(self, win, pos):
        #print(pos[0], pos[1])
        #n.send(make_position((pos[0], pos[1])))

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


# Class for buttons
class button(object):

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

    # Class for drawing buttons
    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y,
                                           self.width, self.height), self.outline)
        font = pygame.font.SysFont('comicsans', 30)
        text = font.render(self.text, 1, self.color2)
        # pygame.draw.rect(win, (255, 255, 255), (410, 446, 80, 35))
        # pygame.draw.rect(win, (255, 255, 255), (410, 308, 80, 35))
        win.blit(text, (int(self.x + self.width / 2 - text.get_width() / 2),
                        int(self.y + self.height / 2 - text.get_height() / 2)))


def drawHeader(win):
    # Drawing header space
    pygame.draw.rect(win, (175, 171, 171), (0, 0, 500, 40))
    # pygame.draw.rect(win, (0, 0, 0), (0, 0, 400, 25), 2)
    # pygame.draw.rect(win, (0, 0, 0), (-5, -5, 510, 40), 2)

    # Printing header
    font = pygame.font.SysFont('comicsans', 30)

    canvasText = font.render('Холст', 1, (0, 0, 0))
    win.blit(canvasText, (int(200 - canvasText.get_width() / 2),
                          int(26 / 2 - canvasText.get_height() / 2) + 2))


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
            playerInf = read_position(playerInf)
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


'''def game():
    object = ['Casa', 'cachoro', 'caneta', 'bola de futebol', 'caneca', 'Computador',
              'Chocolate', 'Jesus', 'Celular', 'Iphone', 'Teclado(instrumento)', 'teclado(computador)']

    font = pygame.font.SysFont('comicsans', 40)
    font2 = pygame.font.SysFont('comicsans', 25)
    text = font.render('Sua Palavra é: ' +
                       object[random.randint(0, (len(object) - 1))], 1, (255, 0, 0))
    Aviso = font2.render('Somente deve olhar essa tela a pessoa que vai desenhar:', 1,
                         (255, 0, 0))
    Aviso2 = font.render('Agora pode olhar', 1,
                         (255, 0, 0))
    i = 0
    time = 1500
    while i < 1500:
        pygame.time.delay(10)
        i += 1
        icount = int((1500 /100) - (i // 100))
        time = font.render(str(icount), 1, (255, 0, 0))
        win.fill((255, 255, 255))
        if int(icount) > 10:
            win.blit(Aviso, (int(5), int(250 - Aviso.get_height() / 2)))
        elif 5 < int(icount) < 11:
            win.blit(Aviso, (int(5), int(100 - text.get_height() / 2)))
            win.blit(text, (int(250 - text.get_width() / 2),
                            int(250 - text.get_height() / 2)))
        else:
            win.blit(Aviso2, (int(250 - Aviso2.get_width() / 2),
                              int(250 - Aviso2.get_height() / 2)))

        win.blit(time, (int(250 - time.get_width() / 2), 270))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                i = 1001
                pygame.quit()
    win.fill((255, 255, 255))'''

def draw_input_field(win, input_text):
    """
    input_rect = pygame.Rect(100, 450, 300, 40)
    pygame.draw.rect(win, (255, 255, 255), input_rect, 2)
    font = pygame.font.SysFont('comicsans', 30)
    text_surface = font.render(input_text, True, (0, 0, 0))
    win.blit(text_surface, (input_rect.x + 43, input_rect.y + 10))
    """
    input_rect = pygame.Rect(0, 400, 800, 120)
    pygame.draw.rect(win, (252, 169, 230), input_rect)
    font = pygame.font.SysFont('comicsans', 25)
    text_surface1 = font.render("Введите ваш ответ:", True, (179, 12, 131))
    text_surface2 = font.render(input_text, True, (179, 12, 131))
    win.blit(text_surface1, (input_rect.x + 10, input_rect.y + 10))
    win.blit(text_surface2, (input_rect.x + 10, input_rect.y + 50))

# Функция для обработки ввода с клавиатуры
def handle_input(event, input_text):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_BACKSPACE:
            input_text = input_text[:-1]
        elif event.key == pygame.K_RETURN:
            # Отправка текста на сервер
            #n.send(input_text)
            input_text = ""

        else:
            input_text += event.unicode
    return input_text


# Ending Function
def gameOver():
    font = pygame.font.SysFont('comicsans', 40)
    text = font.render('GAME OVER', 1, (255, 0, 0))
    i = 0
    while i < 700:
        pygame.time.delay(10)
        i += 1

        win.fill((255, 255, 255))
        win.blit(text, (int(250 - text.get_width() / 2),
                        250 - text.get_height() / 2))
        pygame.display.update()
        print(7 - (i // 100))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                i = 1001
                pygame.quit()
    win.fill((255, 255, 255))


player1 = drawing()
# Fill colored to our paint
win.fill((255, 255, 255))
pos = (0, 0)

# Defining color buttons


whiteButton = button(720, 70, 60, 60, (255, 255, 255), (255, 255, 255))
blackButton = button(720, 136, 60, 60, (0, 0, 0), (247, 15, 181))
redButton = button(720, 202, 60, 60, (255, 0, 0), (255, 0, 0))
blueButton = button(720, 268, 60, 60, (0, 0, 255), (0, 0, 255))
greenButton = button(720, 334, 60, 60, (0, 255, 0), (0, 255, 0))

# Defining other buttons
Buttons_color = []
#Buttons_other = [clrButton, smallerButton, biggerButton, playButton, stopButton, timeDisplay]
Buttons_other = []

if __name__ == "__main__":
    main()

list = pygame.font.get_fonts()
print(list)
