from game import *

def drag_velocity(x_lau_b, y_lau_b, Nx, Ny):
    global V_factor
    mouse_pos = pygame.mouse.get_pos()
    x_lau_a = mouse_pos[0]
    y_lau_a = mouse_pos[1]
    del_x = x_lau_b - x_lau_a
    del_y = y_lau_b - y_lau_a
    
    # Limit maximum velocity for better playability
    # Scale maximum magnitude based on screen size
    magnitude = (del_x**2 + del_y**2)**0.5
    max_magnitude = 80*((Nx+Ny)/2)  # Scale the maximum magnitude with screen size
    
    if magnitude > max_magnitude:
        scale_factor = max_magnitude / magnitude
        del_x *= scale_factor
        del_y *= scale_factor
    
    # Scale velocity based on screen size
    Vx = del_x * V_factor
    Vy = del_y * V_factor
    return Vx, Vy

def launch_gravity(Vx, Vy, red_x, red_y, t, T1):
    # Scale gravity based on global scaling factors to maintain consistent physics
    A = 600  # Base gravity acceleration
    del_t = t - T1
    
    # Limit the time step to prevent physics issues
    if del_t > 0.1:
        del_t = 0.1
    
    # Calculate position change
    rel_x = Vx * del_t
    rel_y = Vy * del_t
    
    # Update position
    red_x += rel_x
    red_y += rel_y
    
    # Update velocity (only vertical affected by gravity)
    Vy += A * del_t
    
    # Update time
    T1 = t
    
    return red_x, red_y, Vx, Vy, T1

def draw_dots(screen, proj_x, proj_y, Vx, Vy, A, num, dot_size):
    dot_list = []
    
    # Calculate and store trajectory points
    for i in range(1, num+1):
        t = (1.5/num) * i
        dot = [None, None]
        dot[0] = proj_x + Vx * t
        dot[1] = proj_y + Vy * t + 0.5 * A * t * t
        dot_list.append(dot)
    
    # Draw trajectory dots
    for dots in dot_list:
        # Only draw points that are on screen
        if 0 <= dots[0] <= screen.get_width() and 0 <= dots[1] <= screen.get_height():
            pygame.draw.circle(screen, (255, 255, 255), (int(dots[0]), int(dots[1])), dot_size)
    
def gen_ran_bird(rand_birds):
    bird_types = ["RED", "CHUCKS", "BOMB", "BLUE"]
    
    # Count bird occurrences
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
        
    