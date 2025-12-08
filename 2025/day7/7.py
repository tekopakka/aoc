import sys
sys.path.append("..")
from common import read_file

#Part 1
data = read_file("test.txt")
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
timelines = []
num_timelines = 0
for i in range(len(data)):
    remove_timelines = []
    new_timelines = []
    line = data[i]
    if "S" in line:
        # Initial timeline 
        timelines.append([index_s])
        num_timelines += 1
    elif SPLITTER in line:
        splitters = line.count(SPLITTER)
        j = 0
        index = 0
        while j < splitters:
            index = line.index(SPLITTER, index)
            for timeline in timelines:
                if timeline[-1] == index:
                    #SPLIT TIMELINE
                    remove_timelines.append(timeline)
                    new_timelines.append(timeline + [index-1])
                    new_timelines.append(timeline + [index+1])
                    num_timelines += 1
            index += 1
            j += 1
    for rem in remove_timelines:
        timelines.remove(rem)
    for add in new_timelines:
        timelines.append(add)
    print(len(timelines))

print("Part 2 answer is:", num_timelines)