import sys
sys.path.append("..")
from common import read_file

data = read_file("t.txt")
data = data[0].split(",")
goofys = []

for item in data:
    temp = item.split("-")
    start = int(temp[0])
    end = int(temp[1])
    while start <= end:
        str_start = str(start)
        p1, p2 = str_start[:int((len(str_start)/2))], str_start[int((len(str_start)/2)):]
        if p1 == p2:
            goofys.append(int(str_start))
        start += 1

result = 0
for goof in goofys:
    result += goof
print("Part 1 answer is:", result)

##Part 2
goofys = []

for item in data:
    temp = item.split("-")
    start = int(temp[0])
    end = int(temp[1])
    while start <= end:
        str_start = str(start)
        i = 1
        while i <= int(len(str_start)/2):
            n = 0
            chunks = [str_start[n:n+i] for n in range(0, len(str_start), i)]
            if len(set(chunks)) == 1:
                goofys.append(start)
                break
            i += 1
        start += 1
            
result = 0
for goof in goofys:
    result += goof
print("Part 2 answer is:", result)