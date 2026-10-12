import pygame, sys
pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Step 2 - ⽂字渲染")

font_title = pygame.font.SysFont("Arial", 32, bold=True)
font_hint = pygame.font.SysFont("SimHei", 20) 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((245, 240, 230))

    title_surface = font_title.render("Wordle Puzzle Game", True, (233, 91,20))
    screen.blit(title_surface, (50, 30)) 

    hint_surface = font_hint.render("提示：與 Google 雲端服務有關的單字", True,(20, 43, 64))
    screen.blit(hint_surface, (50, 80))

    bottom_surface=font_hint.render("按下[ESC]鍵退出遊戲",False,(154,130,149),(0,0,0))
    screen.blit(bottom_surface,(50,530))

    pygame.display.flip()