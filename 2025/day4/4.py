import sys
sys.path.append("..")
from common import read_file

data = read_file("t.txt")
i = 0
while i < len(data):
    data[i] = "."+data[i]+"."
    i += 1

data = ["."*(len(data[0]))]+data+["."*(len(data[0]))]

def is_paper_accessible(i, j):
    spot = data[i-1][j-1]+data[i-1][j]+data[i-1][j+1]+\
            data[i][j-1]+data[i][j+1]+\
            data[i+1][j-1]+data[i+1][j]+data[i+1][j+1]
    if spot.count("@") < 4:
        return True
    else:
        return False

#Part 1
paper_rolls_accessable = 0
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == "@":
            if is_paper_accessible(i, j):
                paper_rolls_accessable += 1

print("Part 1 answer is:", paper_rolls_accessable)

#Part2
paper_rolls_accessable = 0
remove_paper = []
while True:
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == "@":
                if is_paper_accessible(i, j):
                    paper_rolls_accessable += 1
                    remove_paper.append([i, j])
    for paper in remove_paper:
        data[paper[0]] = data[paper[0]][:paper[1]] + "." + data[paper[0]][paper[1]+1:]
    if paper_rolls_accessable == 0:
        break
    paper_rolls_accessable = 0

print("Part 2 answer is:", len(remove_paper))
