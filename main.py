from game import *
from physics import *
from ui import *
import time
from math import *
import random


run = True
while run:
    clock.tick(120) 
    
    for event in pygame.event.get():
        if ui_status:
            ui_status, run, active, text1, text2 = enter_names(ui_status, run, active, text1, text2, event)
        else:
            mouse_pos = pygame.mouse.get_pos()

            # Bird selection
            if not Visible and p_1:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    R_B = random.choice(rand_birds_p1) 
                    
                    if 10 < mouse_pos[0] < 70 and 10 < mouse_pos[1] < 70:
                        slin_bird = Bird(name=rand_birds_p1[3], x=slin1_bird_x, y=slin1_bird_y)
                        rand_birds_p1[3] = R_B
                        Visible = True
                        birds_update = True
                    elif 90 < mouse_pos[0] < 150 and 10 < mouse_pos[1] < 70:
                        slin_bird = Bird(name=rand_birds_p1[2], x=slin1_bird_x, y=slin1_bird_y)
                        rand_birds_p1[2] = R_B
                        Visible = True
                        birds_update = True
                    elif 170 < mouse_pos[0] < 230 and 10 < mouse_pos[1] < 70:
                        slin_bird = Bird(name=rand_birds_p1[1], x=slin1_bird_x, y=slin1_bird_y)
                        rand_birds_p1[1] = R_B
                        Visible = True
                        birds_update = True
                    elif 230 < mouse_pos[0] < 310 and 10 < mouse_pos[1] < 70:
                        slin_bird = Bird(name=rand_birds_p1[0], x=slin1_bird_x, y=slin1_bird_y)
                        rand_birds_p1[0] = R_B
                        Visible = True
                        birds_update = True
                        
            if not Visible and p_2:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    R_B = random.choice(rand_birds_p2) 
                    
                    if 1466 < mouse_pos[0] < 1526 and 10 < mouse_pos[1] < 70:
                        slin_bird = Bird(name=rand_birds_p2[0], x=slin2_bird_x, y=slin2_bird_y)
                        rand_birds_p2[0] = R_B
                        Visible = True
                        birds_update = True
                    elif 1386 < mouse_pos[0] < 1446 and 10 < mouse_pos[1] < 70:
                        slin_bird = Bird(name=rand_birds_p2[1], x=slin2_bird_x, y=slin2_bird_y)
                        rand_birds_p2[1] = R_B
                        Visible = True
                        birds_update = True
                    elif 1306 < mouse_pos[0] < 1366 and 10 < mouse_pos[1] < 70:
                        slin_bird = Bird(name=rand_birds_p2[2], x=slin2_bird_x, y=slin2_bird_y)
                        rand_birds_p2[2] = R_B
                        Visible = True
                        birds_update = True
                    elif 1226 < mouse_pos[0] < 1286 and 10 < mouse_pos[1] < 70:
                        slin_bird = Bird(name=rand_birds_p2[3], x=slin2_bird_x, y=slin2_bird_y)
                        rand_birds_p2[3] = R_B
                        Visible = True
                        birds_update = True

            # Handle bird launch
            if Visible and p_1:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        run = False
                if  screen_wid/30 < mouse_pos[0] < screen_wid * 2 / 15 and (7 / 9) * screen_height < mouse_pos[1] < screen_height:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        x_lau_b, y_lau_b = mouse_pos[0], mouse_pos[1]
                        dots_path=True
                    if event.type == pygame.MOUSEBUTTONUP:
                        start_time = time.time()
                        dots_path=False
                        launch_state = True
                        T1 = 0
                        # Handle bird launch
            if Visible and p_2:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        run = False
                if  screen_wid*13/15 < mouse_pos[0] < screen_wid *29/15 and (7 / 9) * screen_height < mouse_pos[1] < screen_height:
                    print("hi")
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        x_lau_b, y_lau_b = mouse_pos[0], mouse_pos[1]
                        dots_path=True
                    if event.type == pygame.MOUSEBUTTONUP:
                        start_time = time.time()
                        dots_path=False
                        launch_state = True
                        T1 = 0
    if dots_path:                    
        Vx, Vy = drag_velocity(x_lau_b, y_lau_b)  # new_bird velocity
        Vix, Viy = Vx, Vy  # initial velocities
    # Update birds only when needed
    if birds_update:
        bird_sprites_p1[0] = Bird(name=rand_birds_p1[3], x=10, y=10)
        bird_sprites_p1[1] = Bird(name=rand_birds_p1[2], x=90, y=10)
        bird_sprites_p1[2] = Bird(name=rand_birds_p1[1], x=170, y=10)
        bird_sprites_p1[3] = Bird(name=rand_birds_p1[0], x=250, y=10)
        bird_sprites_p2[3] = Bird(name=rand_birds_p2[3], x=1226, y=10)
        bird_sprites_p2[2] = Bird(name=rand_birds_p2[2], x=1306, y=10)
        bird_sprites_p2[1] = Bird(name=rand_birds_p2[1], x=1386, y=10)
        bird_sprites_p2[0] = Bird(name=rand_birds_p2[0], x=1466, y=10)
        birds_need_update = False    

                        
    if Visible and launch_state:
        t = time.time() - start_time
        if sqrt(Vx**2 + Vy**2) > sqrt(Vix**2 + Viy**2) * 2 / 3:
            if slin_bird.position[1] > screen_height - 55:
                if Vy > 0:
                    Vy *= -0.8
            if (slin_bird.position[0] <= -(screen_wid / 150) and Vx < 0) or (slin_bird.position[0] >= screen_wid - ((screen_wid / 30) * 4 / 5) and Vx > 0):
                Vx *= -0.8
            # Updating bird position
            slin_bird.position[0], slin_bird.position[1], Vx, Vy, T1 = launch_gravity(Vx, Vy, slin_bird.position[0], slin_bird.position[1], t, T1)
            slin_bird.update()
        else:
            launch_state = False
            Visible = False
            birds_need_update = True  # Need to update birds after visibility changes
            if p_1 :
                p_1=False
                p_2=True
            else:
                p_1=True
                p_2=False
    
    # Pre-render text surfaces
    text_surface1 = font.render(text1, True, (0, 0, 0))
    text_surface2 = font.render(text2, True, (0, 0, 0))
    text_surface3 = font.render(text1, True, (255,255,255))
    text_surface4 = font.render(text2, True, (255,255,255))
    
    # Rendering all stuff
    if ui_status:
        screen.blit(ui_image, (0, 0))  # Blit UI background instead of filling
        screen.blit(text_surface1, (ui_x_p1, ui_y_p1))
        screen.blit(text_surface2, (ui_x_p2, ui_y_p2))
    else:
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        screen.blit(sling, sling_1_pos)
        screen.blit(sling, sling_2_pos)
        screen.blit(text_surface1, (400,10))
        screen.blit(text_surface2, (926, 10))
    
    # Rendering all stuff
    if ui_status:
        screen.blit(ui_image, (0, 0))  # Blit UI background instead of filling
        screen.blit(text_surface1, (ui_x_p1, ui_y_p1))
        screen.blit(text_surface2, (ui_x_p2, ui_y_p2))
    else:
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        screen.blit(sling, sling_1_pos)
        screen.blit(sling, sling_2_pos)
        screen.blit(text_surface3, (400,10))
        screen.blit(text_surface4, (926, 10))
        
        # Draw all bird sprites
        for bird in bird_sprites_p1:
            if bird:
                bird.draw(screen)
        for bird in bird_sprites_p2:
            if bird:
                bird.flip(screen)
                
        if Visible:
            if p_1:
                slin_bird.draw(screen)
            if p_2:
                slin_bird.flip(screen)
                
    if Visible and dots_path:
            draw_dots(screen,slin_bird.center[0],slin_bird.center[1],Vx,Vy,600,10,10)
        
    
    pygame.display.update()

pygame.quit()