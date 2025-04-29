from game import *
from physics import *
from ui import *
import time
from math import *
import random

# Initialize these important variables
Vx, Vy = 0, 0
Vix, Viy = 0, 0
T1 = 0

run = True
while run:
    clock.tick(90) 
    
    for event in pygame.event.get():
        if ui_status:
            ui_status, run, active,Name_active_p_1,Name_active_p_2, text1, text2 = enter_names(ui_status, run, active,Name_active_p_1,Name_active_p_2, text1, text2, event)
        else:
            mouse_pos = pygame.mouse.get_pos()
            if not Visible and p_1:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        run = False
                if event.type == pygame.MOUSEBUTTONDOWN:                 
                    if 10*Nx < mouse_pos[0] < 70*Nx and 10*Ny < mouse_pos[1] < 70*Ny:
                        slin_bird = Bird(name=rand_birds_p1[3], x=slin1_bird_x, y=slin1_bird_y)
                        rand_birds_p1[3] = gen_ran_bird(rand_birds_p1)
                        Visible = True
                        birds_update = True
                    elif 90*Nx < mouse_pos[0] < 150*Nx and 10*Ny < mouse_pos[1] < 70*Ny:
                        slin_bird = Bird(name=rand_birds_p1[2], x=slin1_bird_x, y=slin1_bird_y)
                        rand_birds_p1[2] = gen_ran_bird(rand_birds_p1)
                        Visible = True
                        birds_update = True
                    elif 170*Nx < mouse_pos[0] < 230*Nx and 10*Ny < mouse_pos[1] < 70*Ny:
                        slin_bird = Bird(name=rand_birds_p1[1], x=slin1_bird_x, y=slin1_bird_y)
                        rand_birds_p1[1] = gen_ran_bird(rand_birds_p1)
                        Visible = True
                        birds_update = True
                    elif 230*Nx < mouse_pos[0] < 310*Nx and 10*Ny < mouse_pos[1] < 70*Ny:
                        slin_bird = Bird(name=rand_birds_p1[0], x=slin1_bird_x, y=slin1_bird_y)
                        rand_birds_p1[0] = gen_ran_bird(rand_birds_p1)
                        Visible = True
                        birds_update = True
                        
            if not Visible and p_2:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    R_B = random.choice(rand_birds_p2) 
                    
                    if 1466*Nx < mouse_pos[0] < 1526*Nx and 10*Ny < mouse_pos[1] < 70*Ny:
                        slin_bird = Bird(name=rand_birds_p2[0], x=slin2_bird_x, y=slin2_bird_y)
                        rand_birds_p2[0] = gen_ran_bird(rand_birds_p2)
                        Visible = True
                        birds_update = True
                    elif 1386*Nx < mouse_pos[0] < 1446*Nx and 10*Ny < mouse_pos[1] < 70*Ny:
                        slin_bird = Bird(name=rand_birds_p2[1], x=slin2_bird_x, y=slin2_bird_y)
                        rand_birds_p2[1] = gen_ran_bird(rand_birds_p2)
                        Visible = True
                        birds_update = True
                    elif 1306*Nx < mouse_pos[0] < 1366*Nx and 10*Ny < mouse_pos[1] < 70*Ny:
                        slin_bird = Bird(name=rand_birds_p2[2], x=slin2_bird_x, y=slin2_bird_y)
                        rand_birds_p2[2] = gen_ran_bird(rand_birds_p2)
                        Visible = True
                        birds_update = True
                    elif 1226*Nx < mouse_pos[0] < 1286*Nx and 10*Ny < mouse_pos[1] < 70*Ny:
                        slin_bird = Bird(name=rand_birds_p2[3], x=slin2_bird_x, y=slin2_bird_y)
                        rand_birds_p2[3] = gen_ran_bird(rand_birds_p2)
                        Visible = True
                        birds_update = True

            # Handle bird launch
            if Visible and p_1:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        run = False
                if  screen_wid/50 < mouse_pos[0] < screen_wid * 2 / 15 and (7 / 9) * screen_height < mouse_pos[1] < screen_height:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        x_lau_b, y_lau_b = mouse_pos[0], mouse_pos[1]
                        dots_path=True
                    if event.type == pygame.MOUSEBUTTONUP:
                        start_time = time.time()
                        dots_path=False
                        launch_state = True
                        T1 = 0
                        
            if Visible and p_2:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        run = False
                if  screen_wid*13/15 < mouse_pos[0] < screen_wid *29/15 and (7 / 9) * screen_height < mouse_pos[1] < screen_height:
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
        slin_bird.position[0],slin_bird.position[1]=mouse_pos[0]-27.5,mouse_pos[1]-27.5
        slin_bird.update()
        
    # Update birds only when needed
    if birds_update:
        bird_sprites_p1[0] = Bird(name=rand_birds_p1[3], x=10*Nx, y=10*Ny)
        bird_sprites_p1[1] = Bird(name=rand_birds_p1[2], x=90*Nx, y=10*Ny)
        bird_sprites_p1[2] = Bird(name=rand_birds_p1[1], x=170*Nx, y=10*Ny)
        bird_sprites_p1[3] = Bird(name=rand_birds_p1[0], x=250*Nx, y=10*Ny)
        bird_sprites_p2[3] = Bird(name=rand_birds_p2[3], x=1226*Nx, y=10*Ny)
        bird_sprites_p2[2] = Bird(name=rand_birds_p2[2], x=1306*Nx, y=10*Ny)
        bird_sprites_p2[1] = Bird(name=rand_birds_p2[1], x=1386*Nx, y=10*Ny)
        bird_sprites_p2[0] = Bird(name=rand_birds_p2[0], x=1466*Nx, y=10*Ny)
        birds_update = False    

                        
    if Visible and launch_state:
        t = time.time() - start_time
        if (slin_bird.count <3 or sqrt(Vx**2 + Vy**2) > sqrt(Vix**2 + Viy**2) * 1 / 2) and slin_bird.count < 6:
            if slin_bird.position[1] > screen_height - 55*Ny:
                if Vy > 0:
                    Vy *= -0.8
                    slin_bird.count+=1
            if (slin_bird.position[0] <= -(screen_wid / 150) and Vx < 0) or (slin_bird.position[0] >= screen_wid - ((screen_wid / 30) * 4 / 5) and Vx > 0):
                Vx *= -0.8
                slin_bird.count+=1
            # Updating bird position
            slin_bird.position[0], slin_bird.position[1], Vx, Vy, T1 = launch_gravity(Vx, Vy, slin_bird.position[0], slin_bird.position[1], t, T1)
            slin_bird.update()
        else:
            launch_state = False
            Visible = False
            birds_update = True  # Need to update birds after visibility changes
            if p_1:
                p_1 = False
                p_2 = True
            else:
                slin_bird=0
                p_1 = True
                p_2 = False
    
    # Pre-render text surfaces
    text_surface1 = font.render(text1, True, (0, 0, 0))
    text_surface2 = font.render(text2, True, (0, 0, 0))
    text_surface3 = font.render(text1, True, (255,255,255))
    text_surface4 = font.render(text2, True, (255,255,255))
    text_surface5 = small_font.render(text3,True,(255,0,0))
    text_surface6 = smaller_font.render(text4,True,(0,0,255))
    # Rendering everything - FIXED: removed duplicate rendering code
    if ui_status:
        screen.blit(ui_image, (0, 0))  # Blit UI background instead of filling
        if not Name_active_p_1:
            screen.blit(text_surface5,(na_x_p1,na_y_p1))   
            screen.blit(text_surface6,(ma_x_p1,ma_y_p1)) 
        else:
            screen.blit(text_surface1, (ui_x_p1, ui_y_p1))
        if not Name_active_p_2:
            screen.blit(text_surface5,(na_x_p2,na_y_p2))
            screen.blit(text_surface6,(ma_x_p2 ,ma_y_p2)) 
        else: 
            screen.blit(text_surface2, (ui_x_p2, ui_y_p2))
        if sound:
            screen.blit(sound_on,(748*Nx,0))
    else:
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        screen.blit(sling, sling_1_pos)
        screen.blit(sling, sling_2_pos)
        screen.blit(text_surface3, (360*Nx, 10*Ny))
        screen.blit(text_surface4, (920*Nx, 10*Ny))
        if Visible:
            if p_1:
                for obj in box_obj_p2:
                    print(slin_bird.position[0]-obj.position[0])
                    if(sqrt((slin_bird.position[0]-obj.position[0])**2 + (slin_bird.position[1]-obj.position[1])**2) < 62.5 ):
                        collision_rect = obj.rect.inflate(-10,-10)
                        if collision_rect.colliderect(slin_bird.rect):
                            collide_list=[obj.position[0],obj.position[1]]
                            iscol=True
                            slin_bird.count+=1
            if p_2:
                for obj in box_obj_p1:
                    if(sqrt((slin_bird.position[0]-obj.position[0])**2 + (slin_bird.position[1]-obj.position[1])**2) < 62.5 ):
                        collision_rect = obj.rect.inflate(-10, -10)
                        if collision_rect.colliderect(slin_bird.rect):
                            collide_list=[obj.position[0],obj.position[1]]
                            iscol=True
                            slin_bird.count+=1
        if iscol:
            if( abs((slin_bird.position[1]-collide_list[1])/(slin_bird.position[0]-collide_list[0]))<1):
                Vx=Vx*-0.8
                iscol=False
                
            
        for obj in box_obj_p1:
            obj.draw(screen)
        for obj in box_obj_p2:
            obj.draw(screen)     
        
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
                
        # Draw trajectory dots
        if dots_path:
            draw_dots(screen, slin_bird.center[0], slin_bird.center[1], Vx, Vy, 600, 10, 5)
    
    pygame.display.update()

pygame.quit()