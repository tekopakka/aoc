import sys
sys.path.append("..")
from common import read_file

data = read_file("t.txt")
answer = 0

#Part 1
for line in data:
    max1 = 0
    index1 = 0
    max2 = 0
    i = 0
    while i < len(line)-1:
        if int(line[i]) > max1:
            index1 = i
            max1 = int(line[i])
            if max1 == 9:
                index1 = i
                break
        i += 1
    index1 += 1
    while index1 < len(line):
        if int(line[index1]) > max2:
            max2 = int(line[index1])
            if max2 == 9:
                index1 += 1
                break
        index1 += 1
    answer += 10*max1+max2
print("Part 1 answer is:", answer)

#Part2
batteries = {
    12:[],11:[],10:[],9:[],8:[],7:[],
    6:[],5:[],4:[],3:[],2:[],1:[]
}
answer = 0
for line in data:
    i = 0
    searching = 12
    temp_i = 0
    while searching > 0:
        max = 0
        while i < len(line)-searching+1:
            if int(line[i]) > max:
                max = int(line[i])
                temp_i = i
            i += 1
        batteries[searching].append(int(line[temp_i]))
        i = temp_i+1
        searching -= 1
i = 0
while i < len(batteries[12]):
    answer += int(batteries[12][i]*pow(10,11)+\
                        batteries[11][i]*pow(10,10)+\
                        batteries[10][i]*pow(10,9)+\
                        batteries[9][i]*pow(10,8)+\
                        batteries[8][i]*pow(10,7)+\
                        batteries[7][i]*pow(10,6)+\
                        batteries[6][i]*pow(10,5)+\
                        batteries[5][i]*pow(10,4)+\
                        batteries[4][i]*pow(10,3)+\
                        batteries[3][i]*pow(10,2)+\
                        batteries[2][i]*pow(10,1)+\
                        batteries[1][i]*pow(10,0))

    i += 1        
print("Part 2 answer is:", answer)