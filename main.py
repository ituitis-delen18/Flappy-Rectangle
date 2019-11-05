"""
    Emirhan Delen
    Flappy Bird:Made with python/pygame
    Made for only improving myself on python/pygame
"""

import pygame,sys,random

pygame.init()

window_size = (800,600)
gameScreen = pygame.display.set_mode(window_size)

pygame.display.set_caption("Flappy Bird")

font = pygame.font.Font(pygame.font.get_default_font(), 23)

FPS = pygame.time.Clock()


highScores = []
f = open("high_scores.txt")
for i in range(0,5):
    highScores.append(int(f.readline()))
f.close()

class Block(object):
    def __init__(self,y1):
        self.y1 = y1
        self.x = 800
        self.width = 80
        self.speed = 5

def quiting():
    quit_text = font.render(" Thanks for playing my game :) ",True , (0,0,0))
    quit_rect = quit_text.get_rect()
    quit_rect.center = (400,300)
    gameScreen.fill((255,255,255))
    gameScreen.blit(quit_text, quit_rect)
    pygame.display.update()
    pygame.time.delay(2500)
    sys.exit()

def yuksekSkorlar():
    firstRankImg = pygame.image.load("challenger.png") # 46x53
    secondRankImg = pygame.image.load("grandmaster.png")
    thirdRankImg = pygame.image.load("diamond.png")
    fourthRankImg = pygame.image.load("gold.png")
    fifthRankImg = pygame.image.load("bronze.png")

    birinci = font.render("{}".format(highScores[0]), True, (0,0,0))
    ikinci = font.render("{}".format(highScores[1]), True, (0, 0, 0))
    ucuncu = font.render("{}".format(highScores[2]), True, (0, 0, 0))
    dorduncu = font.render("{}".format(highScores[3]), True, (0, 0, 0))
    besinci = font.render("{}".format(highScores[4]), True, (0, 0, 0))

    mainMenu_text = font.render("Back to Main Menu" ,True, (0,0,0))
    main_rect = pygame.Rect(window_size[0]/2 - 107 , 450 , 124 , 24)
    print(main_rect)
    while True:
        gameScreen.fill((255,255,255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = event.pos
                if main_rect.collidepoint(x,y):
                    mainMenu()
        gameScreen.blit(firstRankImg, (175,15 + 100))
        gameScreen.blit(secondRankImg, (175, 75 + 100))
        gameScreen.blit(thirdRankImg, (175, 135 + 100))
        gameScreen.blit(fourthRankImg, (175, 195 + 100))
        gameScreen.blit(fifthRankImg, (175, 255 + 100))
        gameScreen.blit(birinci ,(190 + 46 , 115 + 12))
        gameScreen.blit(ikinci ,(190 + 46, 75 + 100 + 12))
        gameScreen.blit(ucuncu ,(190 + 46, 135 + 100 + 12))
        gameScreen.blit(dorduncu ,(190 + 46, 195 + 100 + 12))
        gameScreen.blit(besinci ,(190 + 46, 255 + 100 + 12))

        gameScreen.blit(mainMenu_text, main_rect)
        pygame.display.update()

def gameOver(score):
    isItHighscore = []
    gecici_highscore = []
    for i in highScores:
        gecici_highscore.append(i)
    print(gecici_highscore)

    for i in highScores:
        if score > i:
            isItHighscore.append(1)
        else :
            isItHighscore.append(0)
    toplam = 0
    for i in isItHighscore:
        toplam += i
    if toplam == 0:
        print("6.")
    if toplam == 1:
        print("5.")
        highScores[0] = gecici_highscore[0]
        highScores[1] = gecici_highscore[1]
        highScores[2] = gecici_highscore[2]
        highScores[3] = gecici_highscore[3]
        highScores[4] = score

    if toplam == 2:
        print("4.")
        highScores[0] = gecici_highscore[0]
        highScores[1] = gecici_highscore[1]
        highScores[2] = gecici_highscore[2]
        highScores[3] = score
        highScores[4] = gecici_highscore[3]

    if toplam == 3:
        print("3.")
        highScores[0] = gecici_highscore[0]
        highScores[1] = gecici_highscore[1]
        highScores[2] = score
        highScores[3] = gecici_highscore[2]
        highScores[4] = gecici_highscore[3]

    if toplam == 4:
        print("2.")
        highScores[0] = gecici_highscore[0]
        highScores[1] = score
        highScores[2] = gecici_highscore[1]
        highScores[3] = gecici_highscore[2]
        highScores[4] = gecici_highscore[3]
    if toplam == 5:
        print("1.")
        highScores[0] = score
        highScores[1] = gecici_highscore[0]
        highScores[2] = gecici_highscore[1]
        highScores[3] = gecici_highscore[2]
        highScores[4] = gecici_highscore[3]
    f = open("high_scores.txt", "w")
    for i in highScores:
        f.write("{}\n".format(i))
    f.close()
    game_over = font.render("Game Over!", True, (0, 0, 0))
    yourScore = font.render("Your Score: {}".format(score), True, (0, 0, 0))
    yourScore_rect = yourScore.get_rect()
    print(yourScore_rect)
    yourScore_rect.center = (window_size[0]/2 , window_size[1]/2)
    gameOver_rect = pygame.Rect(window_size[0]/2 - 134/2, window_size[1]/2 - 68 , 135 , 24) # 0 0 135 24
    gameScreen.fill((255, 255, 255))
    gameScreen.blit(game_over, gameOver_rect)
    gameScreen.blit(yourScore, yourScore_rect)
    pygame.display.update()
    pygame.time.delay(3000)
    mainMenu()

def gameLoop():
    blocks = []
    # width = 45 , height = 80
    myChar_x = 50
    myChar_y = 220
    y_speed = -7
    score = 0
    initial_time = pygame.time.get_ticks()
    tester = 0
    while True:
        FPS.tick(30)
        now = pygame.time.get_ticks()
        seconds = int((now - initial_time)/1000)
        gameScreen.fill((255,255,255))
        y_speed -= 2
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if seconds % 2 == 0 and tester < seconds:
                tester = seconds
                x = random.randint(50,350)
                blocks.append(Block(x))
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                y_speed = 15

        myChar_y -= y_speed
        if myChar_y < 0:
            myChar_y = 0
        if myChar_y > 520:
            myChar_y = 520
        myChar_rect = pygame.Rect(myChar_x, myChar_y, 45, 80)

        for block in blocks:
            block.x -= block.speed
            if block.x < 0 - block.width:
                blocks.pop(blocks.index(block))
            ust_block = pygame.Rect(block.x, 0, 80, block.y1)
            alt_block = pygame.Rect(block.x, block.y1 + 200, 80, 450 - block.y1)
            pygame.draw.rect(gameScreen, (255,255,0), ust_block, 0)
            pygame.draw.rect(gameScreen, (255, 255, 0), alt_block, 0)
            if ust_block.colliderect(myChar_rect):
                gameOver(score)
            elif alt_block.colliderect(myChar_rect):
                gameOver(score)
            elif block.x +80 == myChar_x:
                score += 1

        score_Text = font.render("Your Score: {}".format(score), True, (0, 0, 0))
        pygame.draw.rect(gameScreen, (255,0,0), myChar_rect)
        gameScreen.blit(score_Text, (15, 15))
        pygame.display.update()

def mainMenu():
    play_text = font.render("Play", True, (0, 0, 0))
    play_rect = pygame.Rect(window_size[0]/2 - 24, 150, 48, 24)

    high_scores = font.render("High Scores", True, (0, 0, 0))
    high_scores_rect = pygame.Rect(window_size[0]/2 - 134/2, 200, 134, 25)

    quit_text = font.render("Quit", True, (0, 0, 0))
    quit_rect = pygame.Rect(window_size[0]/2 - 24, 250, 49, 24)

    while True:
        FPS.tick(30)
        gameScreen.fill((255,255,255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                x,y = event.pos
                if play_rect.collidepoint(x,y):
                    print("xd")
                    gameLoop()
                elif high_scores_rect.collidepoint(x,y):
                    print("haha")
                    yuksekSkorlar()
                elif quit_rect.collidepoint(x,y):
                    print("r u kidding?")
                    quiting()

        gameScreen.blit(play_text, play_rect)
        gameScreen.blit(high_scores, high_scores_rect)
        gameScreen.blit(quit_text, quit_rect)
        pygame.display.update()

mainMenu()
