import pygame
import random




class snake:

    class node:

        prev_x = 0
        prev_y = 0

        def __init__(self, x, y, next=None):
            self.x = x
            self.y = y
            self.next = next

    head = None
    tail = None

    snake_color = 255,0,0
    snake_width = 10
    snake_height = 10

    def isEmpty(self):
        return self.tail == None

    def addToTail(self, x, y):
        if self.isEmpty():
            self.tail = self.node(x, y)
            self.head = self.tail
        else:
            self.tail.next = self.node(x, y)
            self.tail = self.tail.next

    def __init__(self, x, y):
        self.addToTail(x, y)

class food:
    food_colour = 0,255,0
    food_width = 10
    food_height = 10

    def __init__(self):
        self.x = random.randint(0,game.width-1)
        self.x = self.x - (self.x % food.food_width)
        self.y = random.randint(0, game.height-1)
        self.y = self.y - (self.y % food.food_height)
        
class game:

    size = width, height = 800,400

    def __init__(self):
        pygame.init()

        #Simple game properties
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
                if event.type == pygame.QUIT:
                    run = False

            #Draw background
            screen.fill(background_colour)
            
            #Keys pressed events
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

             

                 
            #Player movement
            if pressed == pygame.K_a:
                aux = player.head #Pointer for linked list
                aux.prev_x = aux.x
                aux.prev_y = aux.y
                while(aux != None):
                    if aux.next != None:
                        aux.next.x = aux.prev_x
                        aux.next.y = aux.prev_y
                        aux.next.prev_x = aux.next.x
                        aux.next.prev_y = aux.next.y
                    aux = aux.next    
                player.head.x = player.head.x - player.snake_width
            if pressed == pygame.K_d:
                aux = player.head #Pointer for linked list
                aux.prev_x = aux.x
                aux.prev_y = aux.y
                while(aux != None):
                    if aux.next != None:
                        aux.next.x = aux.prev_x
                        aux.next.y = aux.prev_y
                        aux.next.prev_x = aux.next.x
                        aux.next.prev_y = aux.next.y
                    aux = aux.next
                player.head.x = player.head.x + player.snake_width
            if pressed == pygame.K_w:
                aux = player.head #Pointer for linked list
                aux.prev_x = aux.x
                aux.prev_y = aux.y
                while(aux != None):
                    if aux.next != None:
                        aux.next.x = aux.prev_x
                        aux.next.y = aux.prev_y
                        aux.next.prev_x = aux.next.x
                        aux.next.prev_y = aux.next.y
                    aux = aux.next
                player.head.y = player.head.y - player.snake_height
            if pressed == pygame.K_s:
                aux = player.head #Pointer for linked list
                aux.prev_x = aux.x
                aux.prev_y = aux.y
                while(aux != None):
                    if aux.next != None:
                        aux.next.x = aux.prev_x
                        aux.next.y = aux.prev_y
                        aux.next.prev_x = aux.next.x
                        aux.next.prev_y = aux.next.y
                    aux = aux.next
                player.head.y = player.head.y + player.snake_height
            
            if player.head.x == apple.x and player.head.y == apple.y:
                player.addToTail(player.tail.x, player.tail.y)
                apple = food()

            aux = player.head
            count = 0
            while(aux != None):
                count = count + 1
                print("This is " + str(count) + " and its x pos is: " + str(aux.x))
                aux = aux.next
            #print(count)    
            
            #draw food
            pygame.draw.rect(screen, apple.food_colour, (apple.x, apple.y, apple.food_width, apple.food_height))

            aux = player.head #Pointer for linked list
            while(aux != None):
                pygame.draw.rect(screen, player.snake_color, (aux.x, aux.y, player.snake_width, player.snake_height))
                aux = aux.next

            pygame.display.flip() 


if __name__ == "__main__":
    game()