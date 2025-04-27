import pygame
from game import *

def enter_names(ui_status, run, active, text1, text2):
    screen.blit(ui_image, (0, 0))  # Render the background
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONUP:
            print(pygame.mouse.get_pos())

        # Activate input on mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:
            if (0.208 * screen_wid < mouse_pos[0] < 0.435 * screen_wid and
                0.140 * screen_height < mouse_pos[1] < 0.279 * screen_height):
                active = "p_1"
                pygame.key.start_text_input()  # Start text input for Player 1
            elif (0.578 * screen_wid < mouse_pos[0] < 0.804 * screen_wid and
                  0.140 * screen_height < mouse_pos[1] < 0.279 * screen_height):
                active = "p_2"
                pygame.key.start_text_input()  # Start text input for Player 2
            elif(0.423*screen_wid < mouse_pos[0] < 0.599*screen_wid and
                 0.601*screen_height < mouse_pos[1] < 0.740*screen_height):
                    ui_status=False

        # Handle text input for Player 1
        if active == "p_1":
            if event.type == pygame.TEXTINPUT:
                text1 += event.text  # Add typed character to text1
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    text1 = text1[:-1]  # Remove last character
                elif event.key == pygame.K_RETURN:
                    active = None  # Stop input
                    pygame.key.stop_text_input()

        # Handle text input for Player 2
        if active == "p_2":
            if event.type == pygame.TEXTINPUT:
                text2 += event.text  # Add typed character to text2
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    text2 = text2[:-1]  # Remove last character
                elif event.key == pygame.K_RETURN:
                    active = None  # Stop input
                    pygame.key.stop_text_input()

    # Render both texts
    text_surface1 = font.render(text1, True, (0, 0, 0))
    screen.blit(text_surface1, (ui_x_p1, ui_y_p1))
    text_surface2 = font.render(text2, True, (0, 0, 0))
    screen.blit(text_surface2, (ui_x_p2, ui_y_p2))

    return ui_status, run, active, text1, text2
