import pygame, sys

def get_mock_level_packet():
    return {
        "level": 1,
        # 10x10 遮罩陣列: 0 =隱藏背景格, 1 =玩家可填字空⽩格, 2 =預設顯⽰且不能更動
        "grid_mask": [
        [2, 1, 1, 1, 1, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ] + [[0]*10 for _ in range(6)],
        # 10x10 答案⼆維清單 (List of Lists): 存放關卡預設⽂字與標準解答
        "solution_grid": [
        ["C", "L", "O", "U", "D", "", "", "", "", ""],
        ["O", "", "", "", "", "", "", "", "", ""],
        ["D", "", "", "", "", "", "", "", "", ""],
        ["E", "", "", "", "", "", "", "", "", ""]
        ] + [[""]*10 for _ in range(6)]
    }

packet = get_mock_level_packet()
print(f"位置 (0,0) 的 Mask 碼: {packet['grid_mask'][0][0]}") #印出 2
print(f"位置 (0,0) 的預設顯⽰⽂字: {packet['solution_grid'][0][0]}") #印出

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Step 3 - draw.rect 基礎語法")
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((245, 240, 230))

    for j in range(10):
        for i in range(10):
            if packet['grid_mask'][i][j]==0:
                continue
            pygame.draw.rect(screen, (183, 212, 135), (50+i*50, 50+50*j, 40, 40))
            pygame.draw.rect(screen, (20, 43, 64), (50+i*50, 50+50*j, 40, 40), 2)

    pygame.display.flip()