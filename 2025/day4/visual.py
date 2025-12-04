import pygame
import random
import time

import sys
sys.path.append("..")
from common import read_file

data = read_file("t.txt")
i = 0
while i < len(data):
    data[i] = "."+data[i]+"."
    i += 1

data = ["."*(len(data[0]))]+data+["."*(len(data[0]))]

# --- Config ---
W = len(data[0])              # Grid lenght
H = len(data)                 # Grid height 
NODE_SIZE = 5        # Node is 2x2 pixels
EMPTY_COLOR = (0, 0, 0)          # Black
FILLED_COLOR = (200, 200, 200)   # Light gray

# Window size
WIDTH = W * NODE_SIZE
HEIGHT = H * NODE_SIZE

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paper block organizer")

def is_paper_accessible(i, j):
    spot = data[i-1][j-1]+data[i-1][j]+data[i-1][j+1]+\
            data[i][j-1]+data[i][j+1]+\
            data[i+1][j-1]+data[i+1][j]+data[i+1][j+1]
    if spot.count("@") < 4:
        return True
    else:
        return False

done = False
running = True
remove_paper = []
paper_rolls_accessable = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == "@":
                if is_paper_accessible(i, j):
                    paper_rolls_accessable += 1
                    remove_paper.append([i, j])
    for paper in remove_paper:
        data[paper[0]] = data[paper[0]][:paper[1]] + "." + data[paper[0]][paper[1]+1:]
    if paper_rolls_accessable == 0:
        done = True
    paper_rolls_accessable = 0

    # Draw the grid
    for y in range(H):
        for x in range(W):
            color = FILLED_COLOR if data[y][x] == "@" else EMPTY_COLOR
            rect = pygame.Rect(x * NODE_SIZE, y * NODE_SIZE, NODE_SIZE, NODE_SIZE)
            pygame.draw.rect(screen, color, rect)

    pygame.display.flip()
    time.sleep(0.2)

    if done:
        time.sleep(5)
        running = False

pygame.quit()