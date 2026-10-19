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
x_idx = -1
y_idx = -1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            x,y = pygame.mouse.get_pos()
            if (x - 50) % 50 > 40 or (y - 50) % 50 > 40:
                x_idx = -1
                y_idx = -1
                continue
            x_idx = (x-50)//50
            y_idx = (y-250)//50
            if x_idx > 9 or y_idx > 9 or x_idx < 0 or y_idx < 0:
                x_idx = -1
                y_idx = -1
                continue
        if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE and x_idx != -1 and y_idx != -1:
                        inputData[y_idx][x_idx]  = ""
                        #按退格鍵刪除最後⼀個字
                    else:
                        #限制英⽂字⺟並轉⼤寫
                        if event.unicode.isalpha():
                            inputData[y_idx][x_idx] = event.unicode.upper()

    screen.fill((245, 240, 240))
    # 1.
    for i in range(10):
        for j in range(10):#i => 0~9
            if packet['grid_mask'][i][j] == 0:
                continue
            pygame.draw.rect(screen, (238, 234, 241), (50+j*50, 250+50*i, 40, 40))
            if i == y_idx and j == x_idx:
                pygame.draw.rect(screen, "#A08801" , (50+j*50, 250+50*i, 40, 40), 2)    
            else:
                pygame.draw.rect(screen, (20, 43, 64), (50+j*50, 250+50*i, 40, 40), 2)
           
            if packet['grid_mask'][i][j] == 2:
                t = font_title.render(packet['solution_grid'][i][j] , True , "black")
                screen.blit(t , (50+j*50+10, 250+50*i+1) )
            elif inputData[i][j] != "":
                t = font_title.render(inputData[i][j] , True , "black")
                screen.blit(t , (50+j*50+10, 250+50*i+1) )

    pygame.display.flip()