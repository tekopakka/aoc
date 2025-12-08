import sys
sys.path.append("..")
from common import read_file

#Part 1
data = read_file("t.txt")
answer = 0
index_s = -2
SPLITTER = "^"
BEAM = "|"
prev_line = ""
for j in range(len(data)):
    line = data[j]
    if "S" in data[j]: #first line assumption 
        index_s = line.index("S")
        prev_line = line[:index_s] + BEAM + line[index_s+1:]
        continue
    else:
        new_line = line
        for i in range(len(line)):
            if line[i] == SPLITTER:
                if prev_line[i] == BEAM:
                    #SPLIT
                    new_line = new_line[:i-1] + BEAM + SPLITTER + BEAM + new_line[i+2:]
                    answer += 1
            elif line[i] == "." and prev_line[i] == BEAM:
                new_line = new_line[:i] + BEAM + new_line[i+1:]
        prev_line = new_line    
    
print("Part 1 answer is:", answer)

#Part 2
timelines = [0 for _ in data[0]]
num_timelines = 0
for i in range(len(data)):
    line = data[i]
    if "S" in line:
        # Initial timeline 
        timelines[index_s] = 1
        num_timelines += 1
    elif SPLITTER in line:
        for j in range(len(line)):
            if line[j] == SPLITTER and timelines[j] > 0:
                #SPLIT TIMELINE
                timelines[j-1] += timelines[j]
                timelines[j+1] += timelines[j]
                num_timelines += timelines[j]
                timelines[j] = 0
                
print("Part 2 answer is:", num_timelines)