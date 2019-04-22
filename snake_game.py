import random
import pygame


class snake:

    class node:

        def __init__(self, x, y, next=None):
            self.x = x
            self.y = y
            self.next = next

    #Linked list
    head = None
    tail = None

    #Snake properties.
    snake_color = 255,0,0
    snake_width = 10
    snake_height = 10

    def isEmpty(self):
        return self.tail == None

    def addToTail(self, x, y):
        if(self.isEmpty()):
            self.tail = self.node(x, y)
            self.head = self.tail
        else:
            self.tail.next = self.node(x, y)
            self.tail = self.tail.next

    def addToHead(self, x, y):
        if(self.isEmpty()):
            self.head = self.node(x,y)
            self.tail = self.head
        else:
            self.head = self.node(x,y,self.head)

    #Count number of nodes in the linked list.
    def countNodes(self):
        self.count = 0
        self.aux = self.head
        while(self.aux is not None):
            self.count = self.count + 1
            self.aux = self.aux.next
        return self.count

    def __init__(self, x, y):
        #Snake head is the tail in the linked link. This is so that the tail effect is possible (with .next).
        self.addToTail(x, y)

class food:

    #Food properties
    food_colour = 0,255,0
    food_width = 10
    food_height = 10

    def __init__(self):
        self.spawn()

    def spawn(self):
        self.x = random.randint(0,game.width-1)
        self.x = self.x - (self.x % food.food_width)
        self.y = random.randint(0, game.height-1)
        self.y = self.y - (self.y % food.food_height)

class game:

    #Game properties.
    size = width, height = 800, 400
    screen = pygame.display.set_mode(size)

    #States
    RUNNING, OVER = 0,1
    state = RUNNING

    def display_msg(self, text, text_size, text_color, x, y):
            self.font = pygame.font.SysFont(None, text_size)
            self.text = self.font.render(text, True, text_color)
            self.textRect = self.text.get_rect()
            self.textRect.center = (x, y)
            game.screen.blit(self.text, self.textRect)

    def __init__(self):
        pygame.init() #get neccessary modules.

        #pygame properties
        pygame.display.set_caption("snake")
        background_colour = 0,0,0
        clock = pygame.time.Clock()

        #Create snake and food
        player = snake(game.width/2, game.height/2)
        pressed = None #Nothing is pressed at the beginning
        apple = food()

        if game.state == game.RUNNING:
            run = True
            while run:
                clock.tick(24)
                for event in pygame.event.get():
                    if(event.type == pygame.QUIT):
                        run = False

                #Draw background
                game.screen.fill(background_colour)

                #Game Over
                aux = player.head
                while(aux.next is not None):
                    if(player.tail.x == aux.x and player.tail.y == aux.y):
                        game.state = game.OVER
                        run = False
                    aux = aux.next

                #Snake eats apple -> add a new add to the single linked list and respawn food.
                if(player.tail.x == apple.x and player.tail.y == apple.y):
                    player.addToHead(player.head.x, player.head.y)
                    apple.spawn()

                #1st segment of tail follows the head of the snake.
                if (player.head is not None):
                    player.head.x = player.tail.x
                    player.head.y = player.tail.y

                #All other segments of tail follow the first segment of the tail. ^
                aux = player.head
                while(aux.next is not None):
                    aux.x = aux.next.x
                    aux.y = aux.next.y
                    aux = aux.next

                #Keys pressed events
                keys = pygame.key.get_pressed()
                if(keys[pygame.K_a]):
                    if(pressed != pygame.K_d):
                        pressed = pygame.K_a
                if(keys[pygame.K_d]):
                    if(pressed != pygame.K_a):
                        pressed = pygame.K_d
                if(keys[pygame.K_w]):
                    if(pressed != pygame.K_s):
                        pressed = pygame.K_w
                if(keys[pygame.K_s]):
                    if(pressed != pygame.K_w):
                        pressed = pygame.K_s

                #Player movement
                if(pressed == pygame.K_a):
                    player.tail.x = player.tail.x - player.snake_width
                if(pressed == pygame.K_d):
                    player.tail.x = player.tail.x + player.snake_width
                if(pressed == pygame.K_w):
                    player.tail.y = player.tail.y - player.snake_height
                if(pressed == pygame.K_s):
                    player.tail.y = player.tail.y + player.snake_height

                #Game border controls
                if(player.tail.x < 0):
                    player.tail.x = player.tail.x + game.width
                if(player.tail.x > game.width-1):
                    player.tail.x = -player.tail.x
                if(player.tail.y > game.height-1):
                    player.tail.y = -player.tail.y
                if(player.tail.y < 0):
                    player.tail.y = player.tail.y + game.height

                #Draw food
                pygame.draw.rect(game.screen, apple.food_colour, (apple.x, apple.y, apple.food_width, apple.food_height))

                #Draw snake and all tail segments
                aux = player.head
                while(aux is not None):
                    pygame.draw.rect(game.screen, player.snake_color, (aux.x, aux.y, player.snake_width, player.snake_height))
                    aux = aux.next

                #Update is faster than flip(). Doesnt redraw the entire screen.
                pygame.display.update()

        if game.state == game.OVER:
                self.display_msg("GAME OVER", 155, (255,255,255), self.width/2, self.height/2)
                continue_font = 30
                self.display_msg("press any key to continue...", continue_font, (255,255,255), self.width/2, (self.height/2)+(continue_font*2))
                pygame.display.update()
                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            return


if __name__ == "__main__":
    game()