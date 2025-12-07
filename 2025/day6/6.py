import sys
sys.path.append("..")
from common import read_file

#Part 1
data = read_file("t.txt")
temp = data[-1]
temp = temp.replace(" ", "")
assignments = [[] for _ in temp]

i = 0
for line in data:
    line = line.split(" ")
    for item in line:
        if item == "":
            continue
        else:
            assignments[i].append(item)
        i += 1
    i = 0

answer = 0
for assignment in assignments:
    operation = assignment[-1]
    task = 0
    if operation == "*":
        task = 1
    for number in assignment:
        if number in ["+", "*"]:
            break
        if operation == "+":
            task += int(number)
        elif operation == "*":
            task = task*int(number)
        else:
            assert False, "what"
    answer += task
    
print("Part 1 answer is:", answer)

#Part 2
i = len(data[0])-1
numbers = []
answer = 0
while i >= 0:
    number = ""
    j = 0
    while j < len(data)-1:
        if data[j][i] != " ":
            number += data[j][i]
        j += 1
    if number == "":
        i -= 1
        continue
        
    numbers.append(int(number))
    operation = data[len(data)-1][i]
    if operation in ["+", "*"]:
        task = 0
        if operation == "*":
            task = 1
        for num in numbers:
            if operation == "*":
                task *= num
            elif operation == "+":
                task += num
            
        numbers = []
        answer += task
    i -= 1
        
print("Part 2 answer is:", answer)