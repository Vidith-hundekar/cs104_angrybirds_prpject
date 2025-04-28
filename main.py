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
            print(text1)
        else:
            mouse_pos = pygame.mouse.get_pos()

            # Bird selection
            if not Visible:
                R_B = random.choice(rand_birds_p1)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 10 < mouse_pos[0] < 70 and 10 < mouse_pos[1] < 70:
                        slin_bird = Bird(name=rand_birds_p1[3], x=slin_bird_x, y=slin_bird_y)
                        rand_birds_p1[3] = R_B
                        Visible = True
                    elif 90 < mouse_pos[0] < 150 and 10 < mouse_pos[1] < 70:
                        slin_bird = Bird(name=rand_birds_p1[2], x=slin_bird_x, y=slin_bird_y)
                        rand_birds_p1[2] = R_B
                        Visible = True
                    elif 170 < mouse_pos[0] < 230 and 10 < mouse_pos[1] < 70:
                        slin_bird = Bird(name=rand_birds_p1[1], x=slin_bird_x, y=slin_bird_y)
                        rand_birds_p1[1] = R_B
                        Visible = True
                    elif 230 < mouse_pos[0] < 310 and 10 < mouse_pos[1] < 70:
                        slin_bird = Bird(name=rand_birds_p1[0], x=slin_bird_x, y=slin_bird_y)
                        rand_birds_p1[0] = R_B
                        Visible = True

            # Handle bird launch
            if Visible:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        run = False
                if mouse_pos[0] > screen_wid / 30 and mouse_pos[0] < screen_wid * 2 / 15 and mouse_pos[1] > (7 / 9) * screen_height and mouse_pos[1] < screen_height:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        x_lau_b, y_lau_b = mouse_pos[0], mouse_pos[1]
                    if event.type == pygame.MOUSEBUTTONUP:
                        start_time = time.time()
                        launch_state = True
                        T1 = 0
                        Vx, Vy = drag_velocity(x_lau_b, y_lau_b)  # new_bird velocity
                        Vix, Viy = Vx, Vy  # initial velocities
                        
                        
    if Visible:
        if launch_state:
            t = time.time() - start_time
            print(t)
            if sqrt(Vx**2 + Vy**2) > sqrt(Vix**2 + Viy**2) * 2 / 3:
                if slin_bird.position[1] > screen_height - 55:
                    if Vy > 0:
                        Vy *= -0.8
                if (slin_bird.position[0] <= -(screen_wid / 150) and Vx < 0) or \
                    (slin_bird.position[0] >= screen_wid - ((screen_wid / 30) * 4 / 5) and Vx > 0):
                    Vx *= -0.8
                # Updating bird position
                slin_bird.position[0], slin_bird.position[1], Vx, Vy, T1 = launch_gravity(
                    Vx, Vy, slin_bird.position[0], slin_bird.position[1], t, T1
                )
                slin_bird.update()
                print(t)
            else:
                launch_state = False
                Visible = False

    B0 = Bird(name=rand_birds_p1[3], x=10, y=10)
    B1 = Bird(name=rand_birds_p1[2], x=90, y=10)
    B2 = Bird(name=rand_birds_p1[1], x=170, y=10)
    B3 = Bird(name=rand_birds_p1[0], x=250, y=10)
    
    text_surface1 = font.render(text1, True, (0, 0, 0))
    text_surface2 = font.render(text2, True, (0, 0, 0))
    
    # Rendering all stuff
    if ui_status:
        screen.blit(text_surface2, (ui_x_p2, ui_y_p2))
        screen.blit(text_surface1, (ui_x_p1, ui_y_p1))
    else:
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        screen.blit(sling, sling_1_pos)
        screen.blit(sling, sling_2_pos)
        B0.draw(screen)
        B1.draw(screen)
        B2.draw(screen)
        B3.draw(screen)
        if Visible:
            slin_bird.draw(screen)

    pygame.display.update()

pygame.quit()
