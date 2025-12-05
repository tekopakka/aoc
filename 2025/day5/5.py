import sys
sys.path.append("..")
from common import read_file

#Part 1
data = read_file("t.txt")
ranges = []
availabilities = []
first = True
for line in data:
    if len(line) == 0:
        first = False
    elif first:
        ranges.append(line)
    else:
        availabilities.append(line)

answer = 0
for item in availabilities:
    for r in ranges:
        rng = r.split("-")
        if int(item) >= int(rng[0]) and int(item) <= int(rng[1]):
            answer += 1
            break

print("Part 1 answer is:", answer)

#Part 2
range_map = []
for rng in ranges:
    range_map.append(rng)

i = 0
while i < len(range_map):
    tmp = range_map[i].split("-")
    small_i = int(tmp[0])
    big_i = int(tmp[1])
    j = 0
    while j < len(range_map):
        if i != j:
            tmp = range_map[j].split("-")
            small_j = int(tmp[0])            
            big_j = int(tmp[1])
            if (small_i >= small_j and small_i <= big_j) or \
                (big_i >= small_j and big_i <= big_j) or \
                (small_i <= small_j and big_i >= big_j) or \
                (small_j <= small_i and big_j >= big_i):
                smallest = min(small_i, small_j)
                largest = max(big_i, big_j)

                range_map.remove(f"{small_i}-{big_i}")
                range_map.remove(f"{small_j}-{big_j}")
                
                range_map.append(f"{smallest}-{largest}")
                i = 0
                j = 0
                break
        j += 1
    i += 1

answer = 0
for r in range_map:
    tmp = r.split("-")
    answer += (int(tmp[1])-int(tmp[0])+1)

print("Part 2 answer is:", answer)