from game import *

def drag_velocity(x_lau_b, y_lau_b):
    global V_factor
    mouse_pos = pygame.mouse.get_pos()
    x_lau_a = mouse_pos[0]
    y_lau_a = mouse_pos[1]
    del_x = x_lau_b - x_lau_a
    del_y = y_lau_b - y_lau_a
    Vx = del_x * V_factor
    Vy = del_y * V_factor 
    return Vx, Vy

def launch_gravity(Vx, Vy, red_x, red_y, t, T1):
    A = 600
    del_t = t - T1
    rel_x = Vx * del_t
    rel_y = Vy * del_t
    red_x += rel_x
    red_y += rel_y
    Vy += A * del_t
    T1 = t
    return red_x, red_y, Vx, Vy, T1

def draw_dots(screen, proj_x, proj_y, Vx, Vy, A, num, dot_size):
    dot_list = []
    for i in range(1, num+1):
        t = (1.5/num) * i
        dot = [None, None]
        dot[0] = proj_x + Vx * t  # Start from bird position
        dot[1] = proj_y + Vy * t + 0.5 * A * t * t  # Correct physics formula
        dot_list.append(dot)
    
    for dots in dot_list:
        # Don't add proj_x/y again since we already included it in the calculation
        pygame.draw.circle(screen, (255, 255, 255), (int(dots[0]), int(dots[1])), dot_size)
    
def gen_ran_bird(rand_birds):
    bird_types = ["RED", "CHUCKS", "BOMB", "BLUE"]
    # Start with one of each bird type
    for bird in rand_birds:
        if rand_birds.count(bird) >= 2:
            name=bird
            return random.choice( [b for b in bird_types if b != bird])
    return random.choice(bird_types)