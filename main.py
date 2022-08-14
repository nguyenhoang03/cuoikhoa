import pygame,sys, time,random
difficulty=10

width=720
height=480

pygame.init()
pygame.display.set.caption('snake game')
game_window= pygame.display.set_mode((width,height))

black= pygame.Color(0,0,0)
white=pygame.Color(255,255,255)
red= pygame.Color(255,0,0)
green= pygame.Color(0,255,0)
blue=pygame.Color(0,0,255)
fps_controller=pygame.time.Clock()
def get_random_coordinate(position,size=10):
    return random.randrange(1,(position//size))*size
class Snake():
    def __init__(self,size=10):
        global width,height
        self.size=size
        self.head= list()
        self.head.append(get_random_coordinate(width,size))
        self.head.append(get_random_coordinate(height,size))
        self.body=list()
        self.body.append(self.head)
    def newhead(self,direction):
        if direction=='UP':
            self.head[1]-=self.size
        if direction=='DOWN':
            self.head[1]+=self.size
        if direction=='LEFT':
            self.head[0]-=self.size
        if direction=='RIGHT':
            self.head[0]+=self.size
        self.body.insert(0, list(self.head))
    def movetail(self):
        self.body.pop()
        def print_snake(self,snake_color,screen_color):
            global game_window
            game_window.fill(screen_color)
            for pos in self.body:
                pygame.draw.rect(game_window,snake_color,pygame.Rect(pos[0],pos[1],self.size))
    def check_touching_itself(self):
            for pos in self.body[1:]:
                if self.head[0]==pos[0] and self.head[1]==pos[1]:
                    return True
            return False
direction= 'RIGHT'
changeto=direction
snake_size=20
the_snake=Snake(snake_size)
score=0
exist_food= False
food_pos=[None,None]
def create_food(size, food_color):
    global game_window, exis_food,food_pos,width,height
    if not exist_food:
        food_pos= [get_random_coordinate(width,size),get_random_coordinate,height,size]
    exist_food=True
    pygame.draw.rect(game_window,food_color,pygame.Rect(food_color,pygame.rect(food_pos[0],food_pos[1])))
def gameover():
    my_font=pygame.font.SysFont('concolas',90)
    gameover_surface=my_font.render('you DIED LOSER',True,red)
    game_window.fill(black)
    game_window.blit(gameover_surface,(width/4,height/4))
    show_score(0,red,'consolas',20)
def show_score(choice,color,font,size):
    score_font=pygame.font.Sysfont(font,size)
    score_surface=score_font.render('score: '+str(score),True,color)
    score_rect=(None,None)
    if choice==1:
        score_rect=(width/10,15)
    else:
        score_rect=(width/2,height/1,25)
        game_window.blit(score_surface,score_rect)
def mainloop():
    global the_snake,direction,changeto,exist_food,score
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP or event.key==ord('w'):
                    changeto='UP'
                if event.key==pygame.K_DOWN or event.key==ord('s'):
                    changeto='DOWN'
                if event.key==pygame.K_LEFT or event.key==ord('a'):
                    changeto='LEFT'
                if event.key==pygame.K_RIGHT or event.key==ord('d'):
                    changeto='RIGHT'
                if event.key==ptgame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))
        the_snake.print_snake(green,black)
        if changeto=='UP' and direction !='DOWN':
            direction='UP'
        if changeto=='DOWN'and direction !='UP':
            direction='DOWN'
        if changeto=='LEFT'and direction !='LEFT':
            direction='LEFT'
        if changeto=='RIGHT'and direction !='RIGHT':
            direction='RIGHT'
        the_snake.new_head(direction)
        create_food(snake_size,red)
        if the_snake.head[0]==food_pos[0] and the_snake.head[1]==food_pos[1]:
            score+=1
            exist_food= False
        else:
            the_snake.move_tall()
        show_score(1,white,'consolas',20)
        if the_snake.check_touching_edge():
            gameover()
        if the_snake.check_touching_itself():
            gameover()
        pygame.display.update()
        fps_controller.trick(difficulty)
mainloop()
        