import pygame
from game import *

def enter_names(ui_status, run, active,A_p1,A_p2, text1, text2,event):
    screen.blit(ui_image, (0, 0))  # Render the background
    mouse_pos = pygame.mouse.get_pos()
    
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            run = False
    # if event.type == pygame.MOUSEBUTTONUP:
    #     print(pygame.mouse.get_pos())

    # Activate input on mouse click
    if event.type == pygame.MOUSEBUTTONDOWN:
        if (0.208 * screen_wid < mouse_pos[0] < 0.435 * screen_wid and 0.140 * screen_height < mouse_pos[1] < 0.279 * screen_height):
            active = "p_1"
            A_p1=True
            pygame.key.start_text_input()
        elif (0.578 * screen_wid < mouse_pos[0] < 0.804 * screen_wid and 0.140 * screen_height < mouse_pos[1] < 0.279 * screen_height):
            active = "p_2"
            A_p2=True
            pygame.key.start_text_input() 
        elif(0.423*screen_wid < mouse_pos[0] < 0.599*screen_wid and 0.601*screen_height < mouse_pos[1] < 0.740*screen_height):
            ui_status=False

    # Handle text input for Player 1
    if active == "p_1":
        if event.type == pygame.TEXTINPUT:
            if len(text1) < 10:
                text1 += event.text
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                text1 = text1[:-1]
            elif event.key == pygame.K_RETURN:
                active = None
                pygame.key.stop_text_input()

    # Handle text input for Player 2
    if active == "p_2":
        if event.type == pygame.TEXTINPUT:
            print(len(text2))
            if len(text2) < 10:
                text2 += event.text 
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                text2 = text2[:-1] 
            elif event.key == pygame.K_RETURN:
                active = None
                pygame.key.stop_text_input()

    return ui_status, run, active,A_p1,A_p2, text1, text2
