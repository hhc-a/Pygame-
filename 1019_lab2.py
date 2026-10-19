import pygame, sys
pygame.init()
screen = pygame.display.set_mode((600, 600))
font = pygame.font.SysFont("Arial", 28, bold=True)
user_input = "" #儲存玩家⽬前鍵⼊的英⽂字⺟
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        #監聽鍵盤按下事件 (KEYDOWN)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                user_input = user_input[:-1] #按退格鍵刪除最後⼀個字
            elif event.key == pygame.K_RETURN:
                print(f"[按下 Enter 送出測試答案]: {user_input}")
            else:
                #限制英⽂字⺟並轉⼤寫
                if len(user_input) < 10 and event.unicode.isalpha():
                    user_input += event.unicode.upper()
    screen.fill((245, 240, 230))
    #即時繪製⽬前打字的字串
    input_surface = font.render(f"Input: {user_input}", True, (233, 91, 67))
    screen.blit(input_surface, (50, 200))
    pygame.display.flip()