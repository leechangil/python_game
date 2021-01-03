import pygame

pygame.init() #초기화 (반드시 필요)

#화면 크기 설정
screen_width = 480 #가로 크기
screen_height = 640 #세로 크기
screen = pygame.display.set_mode((screen_width,screen_height))

#화면 타이틀 설정
pygame.display.set_caption("Nado Game") #게임이름

#배경 이미지 불러오기
background = pygame.image.load("./background.png")

#캐릭터(스프라이트) 불러오기
character = pygame.image.load("./character.png")
character_size = character.get_rect().size #이미지의 크기를 구해옴
character_width = character_size[0] #캐릭터의 가로 크기
character_height = character_size[1] #캐릭터의 세로 크기
character_x_pos = (screen_width / 2) - (character_width / 2) #화면 가로의 절반 크기에 해당하는 곳에 위치
character_y_pos = screen_height - character_height #화면 세로 크기의 가장아래에 

#이동 할 좌표
to_x = 0
to_y = 0
 

#이벤트루프
running = True #게임이진행중인가?
while running:
    for event in pygame.event.get(): #어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: #창이 닫히는 이벤트가 발생하였느가?
            running = False #게임이 진행중이 아님
        
        if event.type == pygame.KYEDOWN #키가 눌러졌으는 확인
            if event.key == pygame.K_LEFT: #캐릭터를 왼쪽으로
                to_x -= 5
            elif event.key == paygame.K_RIGHT: #캐릭터를 오른쪽으로
                to_x += 5
            elif event.key == pygame.K_UP: #캐릭터를 위로 
                to_y -= 5
            elif event.key == pygame.K_DOWN: #캐릭터를 아래쪽으로 
                to_y += 5
        
        if event.type == pygame.KEYUP: #방향키를 떼면 멈춤
            if event.kye == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            if event.kye == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0


    screen.blit(background,(0,0)) #배경그리기

    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update() #게임화면을 다시 그리기

pygame.quit()
