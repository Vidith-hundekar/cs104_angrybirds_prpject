from initialization import *

def drag_velocity(x_lau_b, y_lau_b, Nx, Ny):
    global V_factor
    mouse_pos = pygame.mouse.get_pos()
    x_lau_a = mouse_pos[0]
    y_lau_a = mouse_pos[1]
    del_x = x_lau_b - x_lau_a
    del_y = y_lau_b - y_lau_a
    
    # Limit maximum velocity 
    magnitude = (del_x**2 + del_y**2)**0.5
    max_magnitude = 80*((Nx+Ny)/2)
    if magnitude > max_magnitude:
        scale_factor = max_magnitude / magnitude
        del_x *= scale_factor
        del_y *= scale_factor
    # Scale velocity based on screen size
    Vx = del_x * V_factor
    Vy = del_y * V_factor
    return Vx, Vy

def launch_gravity(Vx, Vy, red_x, red_y, t, T1):
    A = 600  # Base gravity acceleration
    del_t = t - T1
    if del_t > 0.1:
        del_t = 0.1
    rel_x = Vx * del_t
    rel_y = Vy * del_t
    red_x += rel_x
    red_y += rel_y
    Vy += A * del_t
    T1 = t
    return red_x, red_y, Vx, Vy, T1

def draw_dots(screen, proj_x, proj_y, Vx, Vy, A, num, dot_size,a):
    dot_list = []
    
    # Calculate and store trajectory points
    for i in range(1, num+1):
        t = (a/num) * i
        dot = [None, None]
        dot[0] = proj_x + Vx * t
        dot[1] = proj_y + Vy * t + 0.5 * A * t * t
        dot_list.append(dot)
    for dots in dot_list:
        if 0 <= dots[0] <= screen.get_width() and 0 <= dots[1] <= screen.get_height():
            pygame.draw.circle(screen, (255, 255, 255), (int(dots[0]), int(dots[1])), dot_size)
    
def gen_ran_bird(rand_birds):
    bird_types = ["RED", "CHUCKS", "BOMB", "BLUE"]
    bird_counts = {}
    for bird in bird_types:
        bird_counts[bird] = rand_birds.count(bird)
    
    # Find birds that are less frequent
    min_count = min(bird_counts.values())
    options = [bird for bird in bird_types if bird_counts[bird] == min_count]
    # Choose one of the less frequent birds
    if options:
        return random.choice(options)
    else:
        return random.choice(bird_types)
    
def destroy(Bird,V,block):
    if(block.name in Bird.tar):
        if(block.health <= abs(Bird.max*V/1600)):
            block.health=0
            return True
    else:
        if(block.health <= Bird.nor*V/1600):
            block.health=0
            return True
    return False
        
def win(text1, text2, list1, list2):
    if not list1 and not list2: 
        return "draw"
    elif list1 and not list2: 
        return text2 + " is winner"
    elif not list1 and list2:  
        return text1 + " is winner"
    else:                        
        return "goingon" 