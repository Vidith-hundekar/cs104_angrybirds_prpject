from initialization import *
from functions import *
from ui import *
import time
from math import *
import random

# Initialize these important variables
Vx, Vy = 0, 0
Vix, Viy = 0, 0
T1 = 0
Turn=0

run = True
# Initialize slin_bird to None to avoid 'int' object AttributeError
slin_bird = None

while run:
    clock.tick(90) 
    
    for event in pygame.event.get():
        #entering names
        if ui_status:
            ui_status, run, active, Name_active_p_1, Name_active_p_2, text1, text2 , level= enter_names(ui_status, run, active, Name_active_p_1, Name_active_p_2, text1, text2, event , level)
        #selecting_levels_instructions
        elif level:
            mouse_pos = pygame.mouse.get_pos()
            screen.blit(level_bac,(0,0))
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
            if 0<mouse_pos[0]< 300*Nx and 166 *Nx < mouse_pos[1] <300*Ny:
                screen.blit(level_easy,(0,0))
                if event.type == pygame.MOUSEBUTTONDOWN: 
                    level=False
                    box_obj_p1=box_em_obj_p1
                    box_obj_p2=box_em_obj_p2
                    Stage="easy"     
            if 0<mouse_pos[0] <300*Nx and 496*Nx  < mouse_pos[1] <630*Ny:
                screen.blit(level_med,(0,0))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    level=False
                    box_obj_p1=box_em_obj_p1 
                    box_obj_p2=box_em_obj_p2
                    Stage= "medium"     
            if 0<mouse_pos[0] <300*Nx and 815*Nx  < mouse_pos[1] <960*Ny:
                screen.blit(level_cus,(0,0))    
                if event.type == pygame.MOUSEBUTTONDOWN: 
                    level=False
                    Stage = "customized"   
        #battleground       
        else:
            mouse_pos = pygame.mouse.get_pos()
            if not Visible and p_1:
                #selecting from randomised deck_p1
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        run = False
                if event.type == pygame.MOUSEBUTTONDOWN:                 
                    if 10*Nx < mouse_pos[0] < 70*Nx and 10*Ny < mouse_pos[1] < 70*Ny:
                        slin_bird = Bird(name=rand_birds_p1[3], Nx=Nx, Ny=Ny, x=slin1_bird_x, y=slin1_bird_y)
                        rand_birds_p1[3] = gen_ran_bird(rand_birds_p1)
                        Visible = True
                        birds_update = True
                    elif 90*Nx < mouse_pos[0] < 150*Nx and 10*Ny < mouse_pos[1] < 70*Ny:
                        slin_bird = Bird(name=rand_birds_p1[2], Nx=Nx, Ny=Ny, x=slin1_bird_x, y=slin1_bird_y)
                        rand_birds_p1[2] = gen_ran_bird(rand_birds_p1)
                        Visible = True
                        birds_update = True
                    elif 170*Nx < mouse_pos[0] < 230*Nx and 10*Ny < mouse_pos[1] < 70*Ny:
                        slin_bird = Bird(name=rand_birds_p1[1], Nx=Nx, Ny=Ny, x=slin1_bird_x, y=slin1_bird_y)
                        rand_birds_p1[1] = gen_ran_bird(rand_birds_p1)
                        Visible = True
                        birds_update = True
                    elif 230*Nx < mouse_pos[0] < 310*Nx and 10*Ny < mouse_pos[1] < 70*Ny:
                        slin_bird = Bird(name=rand_birds_p1[0], Nx=Nx, Ny=Ny, x=slin1_bird_x, y=slin1_bird_y)
                        rand_birds_p1[0] = gen_ran_bird(rand_birds_p1)
                        Visible = True
                        birds_update = True
             #sselecting thee randomised deck_p2           
            if not Visible and p_2:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 1466*Nx < mouse_pos[0] < 1526*Nx and 10*Ny < mouse_pos[1] < 70*Ny:
                        slin_bird = Bird(name=rand_birds_p2[0], Nx=Nx, Ny=Ny, x=slin2_bird_x, y=slin2_bird_y)
                        rand_birds_p2[0] = gen_ran_bird(rand_birds_p2)
                        Visible = True
                        birds_update = True
                    elif 1386*Nx < mouse_pos[0] < 1446*Nx and 10*Ny < mouse_pos[1] < 70*Ny:
                        slin_bird = Bird(name=rand_birds_p2[1], Nx=Nx, Ny=Ny, x=slin2_bird_x, y=slin2_bird_y)
                        rand_birds_p2[1] = gen_ran_bird(rand_birds_p2)
                        Visible = True
                        birds_update = True
                    elif 1306*Nx < mouse_pos[0] < 1366*Nx and 10*Ny < mouse_pos[1] < 70*Ny:
                        slin_bird = Bird(name=rand_birds_p2[2], Nx=Nx, Ny=Ny, x=slin2_bird_x, y=slin2_bird_y)
                        rand_birds_p2[2] = gen_ran_bird(rand_birds_p2)
                        Visible = True
                        birds_update = True
                    elif 1226*Nx < mouse_pos[0] < 1286*Nx and 10*Ny < mouse_pos[1] < 70*Ny:
                        slin_bird = Bird(name=rand_birds_p2[3], Nx=Nx, Ny=Ny, x=slin2_bird_x, y=slin2_bird_y)
                        rand_birds_p2[3] = gen_ran_bird(rand_birds_p2)
                        Visible = True
                        birds_update = True

            # bird launch
            if Visible and p_1 and slin_bird:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        run = False
                if screen_wid/50 < mouse_pos[0] < screen_wid * 2 / 15 and (7 / 9) * screen_height < mouse_pos[1] < screen_height:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        x_lau_b, y_lau_b = mouse_pos[0], mouse_pos[1]
                        dots_path = True
                    if event.type == pygame.MOUSEBUTTONUP:
                        start_time = time.time()
                        dots_path = False
                        launch_state = True
                        T1 = 0
                        
            if Visible and p_2 and slin_bird:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        run = False
                if screen_wid*13/15 < mouse_pos[0] < screen_wid *29/15 and (7 / 9) * screen_height < mouse_pos[1] < screen_height:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        x_lau_b, y_lau_b = mouse_pos[0], mouse_pos[1]
                        dots_path = True
                    if event.type == pygame.MOUSEBUTTONUP:
                        start_time = time.time()
                        dots_path = False
                        launch_state = True
                        T1 = 0
    if not level:       
        if dots_path and slin_bird:
            #launch _ready
            mouse_pos = pygame.mouse.get_pos()
            #  if mouse is in the boundaries for player 1
            if p_1 and not (screen_wid/50 < mouse_pos[0] < screen_wid * 2 / 15 and (7 / 9) * screen_height < mouse_pos[1] < screen_height):
                dots_path = False
                # Reset bird position 
                slin_bird.position[0], slin_bird.position[1] = slin1_bird_x, slin1_bird_y
                slin_bird.update(Nx, Ny)
            # if mouse is in the boundaries for player 2  
            elif p_2 and not (screen_wid*13/15 < mouse_pos[0] < screen_wid *29/15 and (7 / 9) * screen_height < mouse_pos[1] < screen_height):
                dots_path = False
                # Reset bird position 
                slin_bird.position[0], slin_bird.position[1] = slin2_bird_x, slin2_bird_y
                slin_bird.update(Nx, Ny)
            else:
                Vx, Vy = drag_velocity(x_lau_b, y_lau_b, Nx, Ny)  # new_bird velocity
                Vix, Viy = Vx, Vy  # initial velocities
                slin_bird.position[0], slin_bird.position[1] = mouse_pos[0]-27.5*Nx, mouse_pos[1]-27.5*Ny
                slin_bird.update(Nx, Ny)    
        # Update birds only when needed
        if birds_update:
            bird_sprites_p1[0] = Bird(name=rand_birds_p1[3], Nx=Nx, Ny=Ny, x=10*Nx, y=10*Ny)
            bird_sprites_p1[1] = Bird(name=rand_birds_p1[2], Nx=Nx, Ny=Ny, x=90*Nx, y=10*Ny)
            bird_sprites_p1[2] = Bird(name=rand_birds_p1[1], Nx=Nx, Ny=Ny, x=170*Nx, y=10*Ny)
            bird_sprites_p1[3] = Bird(name=rand_birds_p1[0], Nx=Nx, Ny=Ny, x=250*Nx, y=10*Ny)
            bird_sprites_p2[3] = Bird(name=rand_birds_p2[3], Nx=Nx, Ny=Ny, x=1226*Nx, y=10*Ny)
            bird_sprites_p2[2] = Bird(name=rand_birds_p2[2], Nx=Nx, Ny=Ny, x=1306*Nx, y=10*Ny)
            bird_sprites_p2[1] = Bird(name=rand_birds_p2[1], Nx=Nx, Ny=Ny, x=1386*Nx, y=10*Ny)
            bird_sprites_p2[0] = Bird(name=rand_birds_p2[0], Nx=Nx, Ny=Ny, x=1466*Nx, y=10*Ny)
            birds_update = False    

                            
        if Visible and launch_state and slin_bird:
            t = time.time() - start_time
            # Modified condition to allow both player birds to handle multiple collisions
            # Check if bird should still be active
            if (slin_bird.count < 5 or sqrt(Vx**2 + Vy**2) > sqrt(Vix**2 + Viy**2) * 1 / 3) and slin_bird.count < 6 :
                # collision with ground
                if slin_bird.position[1] > screen_height - 55*Ny:
                    if Vy > 0:
                        Vy *= -0.8
                        slin_bird.count += 1
                if slin_bird.position[1] < 100*Ny:
                    if Vy < 0:
                        Vy *= -0.8
                        slin_bird.count += 1
                
                # Handle left and right screen collision
                if (slin_bird.position[0] <= -(screen_wid / 150) and Vx < 0) or (slin_bird.position[0] >= screen_wid - ((screen_wid / 30) * 4 / 5) and Vx > 0):
                    Vx *= -0.8
                    slin_bird.count += 1
                    
                # Updating bird position
                slin_bird.position[0], slin_bird.position[1], Vx, Vy, T1 = launch_gravity(Vx, Vy, slin_bird.position[0], slin_bird.position[1], t, T1)
                slin_bird.update(Nx, Ny)
                # Update the center of the bird after position update
                slin_bird.center = [slin_bird.position[0]+27.5*Nx, slin_bird.position[1]+27.5*Ny]
            else:
                launch_state = False
                Visible = False
                birds_update = True
                Turn+=1
                if p_1:
                    p_1 = False
                    p_2 = True
                    continue
                else:
                    p_1 = True
                    p_2 = False
                    continue
        
        # render text surfaces
        screen.fill((0, 0, 0))
        if(Stage=="customized"):
            screen.blit(background1, (0, 0))  
        if ( Stage == "easy"):
            screen.blit(background2, (0, 0))
        if ( Stage == "medium"):
            screen.blit(background3, (0, 0))
        text_surface1 = font.render(text1, True, (0, 0, 0))
        text_surface2 = font.render(text2, True, (0, 0, 0))
        text_surface3 = font.render(text1, True, (255,255,255))
        text_surface4 = font.render(text2, True, (255,255,255))
        text_surface5 = small_font.render(text3,True,(255,0,0))
        text_surface6 = smaller_font.render(text4,True,(0,0,255))
        
        # Rendering everything
        if ui_status:
            screen.blit(ui_image, (0, 0))
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
        else:

            screen.blit(sling, sling_1_pos)
            screen.blit(sling, sling_2_pos)
            screen.blit(text_surface3, (360*Nx, 10*Ny))
            screen.blit(text_surface4, (920*Nx, 10*Ny))
            
            # Draw all boxes first
            i = 0
            while i < len(box_obj_p1):
                obj = box_obj_p1[i]
                if obj.health != 0:
                    obj.draw(screen)
                    i += 1  # Only increment index if we didn't remove an object
                else:
                    box_obj_p1.pop(i)  # Remove object and don't increment index

            # For player 2 boxes
            j = 0
            while j < len(box_obj_p2):
                obj = box_obj_p2[j]
                if obj.health != 0:
                    obj.draw(screen)
                    j += 1  # Only increment index if we didn't remove an object
                else:
                    box_obj_p2.pop(j)  # Remove object and don't increment index

            if Visible and slin_bird:
                collision_detected = False  ###Track if collision happens this frame
                
                if p_1:
                    targ=box_obj_p2
                elif p_2:
                    targ=box_obj_p1

                for obj in targ:
                    # Check if this object is on cooldown for collision
                    obj_id = id(obj)  # ID as unique 
                    
                    # Initialize if  doesn't exist
                    if not hasattr(slin_bird, 'object_cooldowns'):
                        slin_bird.object_cooldowns = {}
                    
                    # Skip collision c
                    if obj_id in slin_bird.object_cooldowns and slin_bird.object_cooldowns[obj_id] > 0:
                        slin_bird.object_cooldowns[obj_id] -= 1
                        continue
                        
                    if slin_bird.rect.colliderect(obj) and getattr(slin_bird, 'collision_cooldown', 0) <= 0:
                        print(Vx,Vy)
                        if not collision_detected:
                            slin_bird.count += 1
                            collision_detected = True
                        
                        dx = slin_bird.center[0] - obj.position[0]
                        dy = slin_bird.center[1] - obj.position[1]
                        
                        # Normalize direction vector
                        mag = sqrt(dx*dx + dy*dy)
                        if obj.name in slin_bird.tar:
                            if mag > 0:
                                if abs(dx) > abs(dy):
                                    if destroy(slin_bird, Vx, obj):
                                        Vx*=1/5
                                    else:  
                                        obj.damage(slin_bird.max*abs(Vx)/1600, Nx, Ny)                          
                                        Vx *= -0.7
                                else:
                                    if destroy(slin_bird, Vy, obj):
                                        Vy*=1/5
                                    else:
                                        obj.damage(slin_bird.max*abs(Vy)/1000, Nx, Ny)
                                        Vy *= -0.7
                            else:
                                if not destroy(slin_bird, max(abs(Vx), abs(Vy)), obj):
                                    Vx *= -0.7
                                    Vy *= -0.7
                                    obj.damage(slin_bird.max*abs(Vx)/3200+slin_bird.max*abs(Vy)/2000, Nx, Ny)
                            
                            # Set cooldown 
                            slin_bird.object_cooldowns[obj_id] = 15
                            
                            if destroy(slin_bird, max(abs(Vx), abs(Vy)), obj):
                                continue  # Skip to next obstacle if this one was destroyed
                            else:
                                break  # Stop checking 
                        else:
                            if mag > 0:  
                                if abs(dx) > abs(dy):
                                    if destroy(slin_bird, Vx, obj):
                                        Vx*=1/5
                                    else:  
                                        obj.damage(slin_bird.nor*abs(Vx)/1600, Nx, Ny)                          
                                        Vx *= -0.7
                                else:
                                    if destroy(slin_bird, Vy, obj):
                                        Vy*=1/5
                                        pass
                                    else:
                                        obj.damage(slin_bird.nor*abs(Vy)/1000, Nx, Ny)
                                        Vy *= -0.7
                            else:
                                if not destroy(slin_bird, max(abs(Vx), abs(Vy)), obj):
                                    Vx *= -0.7
                                    Vy *= -0.7
                                    obj.damage(slin_bird.nor*abs(Vx)/3200+slin_bird.nor*abs(Vy)/2000, Nx, Ny)
                            
                            # Set cooldown 
                            slin_bird.object_cooldowns[obj_id] = 15
                            
                            if destroy(slin_bird, max(abs(Vx), abs(Vy)), obj):
                                continue  # Skip to next obstacle if this one was destroyed
                            else:
                                break  # Stop checking
                    # Global collision cooldown (still useful to keep)
                    slin_bird.collision_cooldown = max(0, getattr(slin_bird, 'collision_cooldown', 0) - 1)
            
            # Draw all bird sprites
            for bird in bird_sprites_p1:
                if bird:
                    bird.draw(screen)
            for bird in bird_sprites_p2:
                if bird:
                    bird.flip(screen)
                    
            # Draw the active bird
            if Visible and slin_bird:
                if p_1:
                    slin_bird.draw(screen)
                if p_2:
                    slin_bird.flip(screen)
                    
            # Draw trajectory dots
            if dots_path and slin_bird:
                if(Stage=="easy"):
                    draw_dots(screen, slin_bird.center[0], slin_bird.center[1], Vx, Vy, 600, 10, 5,1.5)
                if(Stage=="medium"):
                    draw_dots(screen, slin_bird.center[0], slin_bird.center[1], Vx, Vy, 600, 3, 5,0.5)
                if(Stage=="customized"):
                    draw_dots(screen, slin_bird.center[0], slin_bird.center[1], Vx, Vy, 600, 3, 5,0.5)
        if Stage == "medium":
            for box in box_obj_p1:
                # Add vertical oscillation effect
                if not hasattr(box, 'osc'):
                    box.osc = random.uniform(0, 6.28)  # Random phase
                    box.speed = random.uniform(0.1, 0.15)  # Random speed
                box.osc += box.speed
                Amp = sin(box.osc) * 2  
                new_y = box.position[1] + Amp
                box.position[1] = max(370*Ny, min(650*Ny, new_y))
                
                box.update(Nx, Ny)
                
            for box in box_obj_p2:
                # Add vertical oscillation effect
                if not hasattr(box, 'osc'):
                    box.osc = random.uniform(0, 6.28)  # Random phase 
                    box.speed = random.uniform(0.1, 0.15)  # Random speed
                box.osc += box.speed
                Amp = sin(box.osc) * 2  
                new_y = box.position[1] + Amp
                box.position[1] = max(370*Ny, min(650*Ny, new_y))  
                
                box.update(Nx, Ny)
        if Turn%2 != 0:
            if win(text1,text2,box_obj_p1,box_obj_p2) != "goingon":
                screen.blit(background4,(0,0))
                text_surface_e = font_e.render(win(text2,text1,box_obj_p1,box_obj_p2), True, (120,120,120))
                screen.blit(text_surface_e,(650*Nx,800*Ny))
                
    pygame.display.update()

pygame.quit()