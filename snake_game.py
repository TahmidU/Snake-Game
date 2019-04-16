import pygame
import random

class snake:

    class node:

        def __init__(self, x, y, next=None):
            self.x = x
            self.y = y
            self.next = next

    head = None

    snake_color = 255,0,0
    snake_width = 10
    snake_height = 10

    def isEmpty(self):
        return self.head == None

    def addToHead(self, x, y, next):
        if self.isEmpty():
            print("Is Empty")
            self.head = self.node(x, y)
        else:
            print("Not Empty")
            self.head = self.node(x, y, next)

    def __init__(self, x, y):
        self.addToHead(x, y, None)

class food:
    food_colour = 0,255,0
    food_width = 10
    food_height = 10

    def __init__(self):
        self.x = (random.randint(1,160)*self.food_width)%799   
        self.y = (random.randint(1, 80)*self.food_height)%399

if __name__ == "__main__":
    pygame.init()

    pygame.display.set_caption("snake")
    size = width, height = 800, 400
    screen = pygame.display.set_mode(size)

    background_colour = 0,0,0

    player = snake(width/2, height/2)
    pressed = None

    apple = food()

    run = True
    while run:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        screen.fill(background_colour)
        pygame.draw.rect(screen, apple.food_colour, (apple.x, apple.y, apple.food_width, apple.food_height))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            if pressed != pygame.K_d:
                pressed = pygame.K_a
        if keys[pygame.K_d]:
            if pressed != pygame.K_a:
                pressed = pygame.K_d
        if keys[pygame.K_w]:
            if pressed != pygame.K_s:
                pressed = pygame.K_w
            pressed = pygame.K_w
        if keys[pygame.K_s]:
            if pressed != pygame.K_w:
                pressed = pygame.K_s

        aux = player.head
        while(aux != None):
            if pressed == pygame.K_a:
                aux.x = aux.x - player.snake_width
            if pressed == pygame.K_d:
                aux.x = aux.x + player.snake_width
            if pressed == pygame.K_w:
                aux.y = aux.y - player.snake_height
            if pressed == pygame.K_s:
                aux.y = aux.y + player.snake_height
            pygame.draw.rect(screen, player.snake_color, (aux.x, aux.y, player.snake_width, player.snake_height))    
            aux = aux.next    
        
        
        pygame.display.flip()
        

    pygame.quit()    