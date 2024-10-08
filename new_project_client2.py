# import library
import pygame
import random
from network import Network

n = Network()

clientNumber = 0

pygame.init()

# Setting window size
win_x = 500
win_y = 500

win = pygame.display.set_mode((win_x, win_y))
pygame.display.set_caption('Игрок 2')

def read_position(s):
    #print(s)
    s = s.split(",")
    return int(s[0]), int(s[1])

def make_position(tup):
    return str(tup[0]) + "," + str(tup[1])

# Class for drawing
class drawing(object):

    def __init__(self):
        '''constructor'''
        self.color = (0, 0, 0)
        self.width = 10
        self.height = 10
        self.rad = 6
        self.tick = 0
        self.time = 0
        self.play = False

    # Drawing Function
    def draw(self, win, pos):
        #print(pos[0], pos[1])
        #n.send(make_position((pos[0], pos[1])))
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
        pygame.draw.rect(win, (255, 255, 255), (410, 446, 80, 35))
        # pygame.draw.rect(win, (255, 255, 255), (410, 308, 80, 35))
        win.blit(text, (int(self.x +self.width / 2 - text.get_width( ) /2),
                        int(self.y +self.height / 2 - text.get_height( ) /2)))


def drawHeader(win):
    # Drawing header space
    pygame.draw.rect(win, (175, 171, 171), (0, 0, 500, 25))
    pygame.draw.rect(win, (0, 0, 0), (0, 0, 400, 25), 2)
    pygame.draw.rect(win, (0, 0, 0), (400, 0, 100, 25), 2)

    # Printing header
    font = pygame.font.SysFont('comicsans', 30)

    canvasText = font.render('Canvas', 1, (0, 0, 0))
    win.blit(canvasText, (int(200 - canvasText.get_width() / 2),
                          int(26 / 2 - canvasText.get_height() / 2) + 2))



def draw(win):

    pygame.draw.rect(win, (0, 0, 0), (400, 0, 100, 500),
                     2)  # Drawing button space
    pygame.draw.rect(win, (255, 255, 255), (400, 0, 100, 500) ,)
    #pygame.draw.rect(win, (0, 0, 0), (0, 0, 400, 500),
                     #2)  # Drawing canvas space
    drawHeader(win)

    for button in Buttons_color:
        button.draw(win)

    for button in Buttons_other:
        button.draw(win)

    pygame.display.update()



def main():
    run = True
    clock = pygame.time.Clock()

    input_text = ""


    while run:
        print(1)
        clock.tick(60)

        p2Pos = n.send("0,0")
        if p2Pos != None:
            p2Pos = read_position(p2Pos)
            print(p2Pos)
            #pygame.draw.circle(win, player1.color, (pos[0], pos[1]), player1.rad)
            player1.draw(win, p2Pos)


        keys = pygame.key.get_pressed()
        draw_input_field(win, input_text)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                run = False
            input_text = handle_input(event, input_text)



        draw(win)

        if 0 < player1.tick < 40:
            player1.tick += 1
        else:
            player1.tick = 0

        if 0 < player1.time < 4001:
            player1.time += 1
        elif 4000 < player1.time < 4004:
            gameOver()
            player1.time = 4009
        else:
            player1.time = 0
            player1.play = False

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
    input_rect = pygame.Rect(100, 450, 300, 40)
    pygame.draw.rect(win, (255, 255, 255), input_rect, 2)
    font = pygame.font.SysFont('comicsans', 30)
    text_surface = font.render(input_text, True, (0, 0, 0))
    win.blit(text_surface, (input_rect.x + 43, input_rect.y + 10))

# Функция для обработки ввода с клавиатуры
def handle_input(event, input_text):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_BACKSPACE:
            input_text = input_text[:-1]
        elif event.key == pygame.K_RETURN:
            # Отправка текста на сервер
            n.send(input_text)
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


blackButton = button(407, 168, 1, 1, (0, 0, 0), (0, 0, 0))


# Defining other buttons
clrButton = button(407, 214, 1, 1, (201, 201, 201), (0, 0, 0), 0, 1, '')


playButton = button(407, 352, 1, 1, (201, 201, 201), (0, 0, 0), 0, 5, '')
stopButton = button(407, 398, 1, 1, (201, 201, 201), (0, 0, 0), 0, 6, '')
timeDisplay = button(407, 444, 86, 40, (0, 0, 0), (0, 0, 0), 1, 7, 'Time')

Buttons_color = [blackButton]
Buttons_other = [clrButton, playButton, stopButton, timeDisplay]

if __name__ == "__main__":
    main()

list = pygame.font.get_fonts()
print(list)
