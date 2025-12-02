import pygame
import math
import sys
import time

WIDTH, HEIGHT = 600, 600
RADIUS = 200
SPIN_SPEED = 360  # degrees per second
FONT_SIZE = 20
INSTRUCTION_FILE = "t.txt"

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dial")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, FONT_SIZE)

center = (WIDTH // 2, HEIGHT // 2)

STEP_DEG = 3.6        # each dial step (100 steps = 360°)
STEP_DELAY = 15       # ms delay between steps (controls speed)
ZERO_PAUSE = 500      # pause when crossing 0°
target_angle = 0.0
current_angle = 180.0
last_angle = 0.0

surf_size = RADIUS * 2 + 50
dial_surface = pygame.Surface((surf_size, surf_size), pygame.SRCALPHA)
dial_center = (surf_size // 2, surf_size // 2)

pygame.draw.circle(dial_surface, (240, 240, 255), dial_center, RADIUS)
pygame.draw.circle(dial_surface, (40, 40, 80), dial_center, RADIUS, 4)

for i in range(100):
    ang = math.radians(i * 3.6 - 90)  # 100 marks => 360/100 = 3.6 degrees
    x1 = dial_center[0] + math.cos(ang) * (RADIUS - 10)
    y1 = dial_center[1] + math.sin(ang) * (RADIUS - 10)
    x2 = dial_center[0] + math.cos(ang) * (RADIUS - 2)
    y2 = dial_center[1] + math.sin(ang) * (RADIUS - 2)
    pygame.draw.line(dial_surface, (0, 0, 0), (x1, y1), (x2, y2), 2)

    if i % 5 == 0:
        tx = dial_center[0] + math.cos(ang) * (RADIUS - 35)
        ty = dial_center[1] + math.sin(ang) * (RADIUS - 35)
        num = font.render(str(i), True, (0, 0, 0))
        rect = num.get_rect(center=(tx, ty))
        dial_surface.blit(num, rect)

def spin(direction, target):
    global target_angle

    if direction == "R":
        target_angle = (target_angle + target) % 360
    elif direction == "L":
        target_angle = (target_angle - target) % 360
    else:
        raise ValueError("Direction must be 'R' or 'L'")


def is_spinning():
    diff = (target_angle - current_angle + 180) % 360 - 180
    return abs(diff) >= STEP_DEG


def update_spin():
    """
    Move current_angle toward target_angle using fixed 3.6° steps.
    """
    global current_angle, last_angle

    # Find difference in the shortest direction
    diff = (target_angle - current_angle + 180) % 360 - 180

    if abs(diff) < STEP_DEG:
        last_angle = current_angle
        return  # close enough — stop

    # Determine direction of step
    if diff > 0:
        next_angle = (current_angle + STEP_DEG) % 360  # CW
    else:
        next_angle = (current_angle - STEP_DEG) % 360  # CCW

    # ------- Check if we crossed zero ------
    a1 = current_angle
    a2 = next_angle

    crossed_zero = (
        (a1 > 300 and a2 < 60) or
        (a1 < 60 and a2 > 300)
    )

    if crossed_zero:
        pygame.time.wait(ZERO_PAUSE)

    # Apply step
    current_angle = next_angle
    last_angle = current_angle

    # Step speed: short delay
    pygame.time.wait(STEP_DELAY)


def wait_until_spin_done():
    while is_spinning():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        update_spin()
        draw()
        pygame.display.flip()


# --------------------------
# DRAW
# --------------------------
def draw():
    screen.fill((30, 30, 40))
    rotated = pygame.transform.rotozoom(dial_surface, -current_angle, 1)
    rrect = rotated.get_rect(center=center)
    screen.blit(rotated, rrect)


# --------------------------
# MAIN LOOP (READS THE FILE)
# --------------------------
def main():
    curr = 50
    clicks = 0
    try:
        with open(INSTRUCTION_FILE, "r") as f:
            instructions = f.readlines()
    except FileNotFoundError:
        print("Missing file:", INSTRUCTION_FILE)
        pygame.quit()
        sys.exit()

    for line in instructions:
        parts = line.strip().split()
        direction = line[0]
        num = int(line[1:])

        clicks += int(abs(num)/100)
        num = abs(num)%100
        if direction == "R":
            curr += num
            if curr > 99:
                clicks += 1
                curr -= 100
            elif curr == 0:
                clicks += 1
        elif direction == "L":
            if curr == 0:
                curr += 100
            curr -= num
            if curr < 0:
                clicks += 1
                curr += 100
            elif curr == 0:
                clicks += 1

        angle_val = float(num*3.6)

        spin(direction, angle_val)
        wait_until_spin_done()

        print(f"Completed: {direction} {angle_val} {num}")
    print(clicks)

    # After finishing all spins, idle loop
    while True:
        dt = clock.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        draw()
        pygame.display.flip()


main()