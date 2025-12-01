import sys
sys.path.append("..")
import common

data = common.read_file("t.txt")

# Part 1
curr = 50
password = []
for line in data:
    direction = line[0]
    num = int(line[1:])
    if direction == "R":
        num = num%100
        curr += num
        if curr > 99:
            curr -= 100
    elif direction == "L":
        num = abs(num)%100
        curr -= num
        if curr < 0:
            curr += 100
    if curr == 0:
        password.append(curr)
        
print("Part1 answer:", len(password))

#Part2
curr = 50
clicks = 0
for line in data:
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
    print("Clicks", clicks)
    print(curr)
            
print("Part2 answer", clicks)
    
            