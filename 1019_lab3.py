import pygame, sys

def get_mock_level_packet():
    return {
        "level": 1,
        # 10x10
        #遮罩陣列: 0 =隱藏背景格, 1 =玩家可填字空⽩格, 2 =預設顯⽰且不能更動
        "grid_mask": [
        [2, 1, 1, 1, 2, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 1, 1, 1, 1, 2, 0],
        [2, 0, 0, 0, 2, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ] + [[0]*10 for _ in range(6)],
        # 10x10
        "solution_grid": [
        ["C", "L", "O", "U", "D", "", "", "", "", ""],
        ["O", "", "", "", "O", "C", "E", "A", "N", ""],
        ["D", "", "", "", "G", "L", "O", "W", "R", "Y"],
        ["E", "", "", "", "", "", "", "", "", ""]
        ] + [[""]*10 for _ in range(6)]
    }
packet = get_mock_level_packet()

inputData = [["" for i in range(10)] for j in range(10)]

pygame.init()
screen = pygame.display.set_mode((600, 800))
pygame.display.set_caption("Step 3 - draw.rect 基礎語法")
font_title = pygame.font.SysFont("Arial", 32, bold=True)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            x,y = pygame.mouse.get_pos()
            if (x - 50) % 50 > 40 or (y - 50) % 50 > 40:
                print('hi')
                continue
            x_idx = (x-50)//50
            y_idx = (y-250)//50
            if x_idx > 9 or y_idx > 9 or x_idx < 0 or y_idx < 0:
                continue
            print(y_idx , x_idx)
            inputData[y_idx][x_idx] = 1

    screen.fill((245, 240, 240))
    # 1.
    for i in range(10):
        for j in range(10):#i => 0~9
            if packet['grid_mask'][i][j] == 0:
                continue
            if inputData[i][j] == 1:
                pygame.draw.rect(screen, (125, 220, 175), (50+j*50, 250+50*i, 40, 40))
            else:
                pygame.draw.rect(screen, (238, 234, 241), (50+j*50, 250+50*i, 40, 40))
            pygame.draw.rect(screen, (20, 43, 64), (50+j*50, 250+50*i, 40, 40), 2)
           
            if packet['grid_mask'][i][j] == 2:
                t = font_title.render(packet['solution_grid'][i][j] , True , "black")
                screen.blit(t , (50+j*50+10, 250+50*i+1) )

    pygame.display.flip()