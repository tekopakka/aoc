import pygame
import sys
import time
sys.path.append("..")
from common import read_file

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# --- CONFIG ---
speed = 20

font = pygame.font.SysFont(None, 50)

# --- UTILITY: move a point towards another point ---
def move_towards(pos, target, speed):
    x, y = pos
    tx, ty = target
    dx, dy = tx - x, ty - y
    dist = (dx*dx + dy*dy) ** 0.5

    if dist <= speed:
        return target
    return (x + dx/dist * speed, y + dy/dist * speed)

# --- MAIN LOOP ---
state = "next_item"    # states: center_hold → leaving → next_item  (eventually ---> done)
start_time = time.time()

# Starting text position will be set when each string appears
pos = None

data = read_file("test.txt")
data = data[0].split(",")
numbers = []
index = 0
answer_value = 0
item = 0
goofy = False

for foo in data:
    temp = foo.split("-")
    start = int(temp[0])
    end = int(temp[1])
    while start <= end:
        numbers.append(start)
        start += 1

while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(("white"))

    answer_str = font.render(str(answer_value), True, (0,0,0))
    screen.blit(answer_str, (100, 500))

    if state != "done":
        # Generate center position for the first frame of each item
        if state == "center_hold" and pos is None:
            rendered_small = font.render(str(item), True, (255,255,255))
            rect_small = rendered_small.get_rect(center=(400, 300))
            pos = rect_small.topleft
            start_time = time.time()

        # CENTER HOLD FOR 1 SECONDS WITH FONT CHANGE
        if state == "center_hold":
            # During hold: switch fonts over time or instantly (your choice)
            elapsed = time.time() - start_time
            
            if elapsed < 1 and goofy:
                rendered = font.render(str(item), True, font_color)
            elif elapsed > 1 and not goofy:
                rendered = font.render(str(item), True, font_color)
                state = "next_item"
                index += 1
            elif goofy:
                # After 1 seconds → begin leaving
                state = "leaving"
                target = (100, 500)
                continue
                
            screen.blit(rendered, pos)

        # LEAVING CENTER → CORNER
        elif state == "leaving":
            rendered = font.render(str(item), True, font_color)
            pos = move_towards(pos, target, speed)
            screen.blit(rendered, pos)

            # If reached corner, go to next item
            if pos == target:
                state = "next_item"
                index += 1
                print(index)
                if goofy:
                    answer_value += item
            

        # SETUP NEXT ITEM
        elif state == "next_item":
            goofy = False
            try:
                item = numbers[index]
            except:
                state = "done"
            i = 1
            str_start = str(item)
            font_color = (216, 20, 184)
            while i <= int(len(str_start)/2):
                n = 0
                chunks = [str_start[n:n+i] for n in range(0, len(str_start), i)]
                if len(set(chunks)) == 1:
                    goofy = True
                    font_color = (12, 200, 2)
                    break
                i += 1
            pos = None
            state = "center_hold"
            continue

    else:
        # Finished all items
        rendered = font.render("DONE", True, (0,255,0))
        screen.blit(rendered, (250, 250))

    pygame.display.flip()
    clock.tick(60)