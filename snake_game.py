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
        print(self.count)
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
        self.x = random.randint(0,game.width-1)
        self.x = self.x - (self.x % food.food_width)
        self.y = random.randint(0, game.height-1)
        self.y = self.y - (self.y % food.food_height)

class game:

    #game properties.
    size = width, height = 800, 400

    def __init__(self):
        pygame.init() #get neccessary modules.

        #pygame properties
        pygame.display.set_caption("snake")
        background_colour = 0,0,0
        clock = pygame.time.Clock()
        screen = pygame.display.set_mode(game.size)

        #Create snake and food
        player = snake(game.width/2, game.height/2)
        pressed = None #Nothing is pressed at the beginning
        apple = food()

        run = True
        while run:
            clock.tick(15)
            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    run = False

            #Draw background
            screen.fill(background_colour)

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

            #Apple with apple -> add a new add to the single linked list and respawn food.
            if(player.tail.x == apple.x and player.tail.y == apple.y):
                player.addToHead(player.head.x, player.head.y)
                apple = food()

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

            #Player movement
            if(pressed == pygame.K_a):
                player.tail.x = player.tail.x - player.snake_width
            if(pressed == pygame.K_d):
                player.tail.x = player.tail.x + player.snake_width
            if(pressed == pygame.K_w):
                player.tail.y = player.tail.y - player.snake_height
            if(pressed == pygame.K_s):
                player.tail.y = player.tail.y + player.snake_height

            #Game boarder controls
            if(player.tail.x < 0):
                player.tail.x = player.tail.x + game.width
            if(player.tail.x > game.width):
                player.tail.x = -player.tail.x
            if(player.tail.y > game.height):
                player.tail.y = -player.tail.y
            if(player.tail.y < 0):
                player.tail.y = player.tail.y + game.height

            #draw food
            pygame.draw.rect(screen, apple.food_colour, (apple.x, apple.y, apple.food_width, apple.food_height))

            #draw snake and all tail segments
            aux = player.head
            while(aux is not None):
                pygame.draw.rect(screen, player.snake_color, (aux.x, aux.y, player.snake_width, player.snake_height))
                aux = aux.next

            #Update is faster than flip(). Doesnt redraw the entire screen.
            pygame.display.update()


if __name__ == "__main__":
    game()