import sys
sys.path.append("..")
from common import read_file

#Part 1
data = read_file("t.txt")
answer = 0
max_area = 0
for i in range(len(data)):
    j = 0
    data_i = data[i].split(",")
    while j < len(data):
        data_j = data[j].split(",")
        if abs(int(data_i[0])-int(data_j[0]))*abs(int(data_i[1])-int(data_j[1])) > max_area:
            max_area = abs(int(data_i[0])-int(data_j[0])+1)*abs(int(data_i[1])-int(data_j[1])+1)
            print("new max", max_area, data_i, data_j)
        j += 1

print("Part 1 answer is:", max_area)