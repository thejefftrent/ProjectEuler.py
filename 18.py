

tri = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

tri = tri.split("\n")
for i in range(len(tri)):
    tri[i] = tri[i].split(" ")
    for j in range(len(tri[i])):
        tri[i][j] = int(tri[i][j])

#pathing down the triangle works by moving to the same index down the line or 1 larger i.e. [4][2] can move to [5][2] or [5][3] nowhere else

#yolo
from random import random
def max_path_sum(tri):
    sum = 0
    pos = 0 #index of col
    for i in range(len(tri)):
        #print(str(tri[i][pos]), i, pos)
        sum += tri[i][pos]
        if i < len(tri) -1:
            if random() * 2 > 1:
                pos += 1
    return sum


best_sum = 0 
while True:
    sum = max_path_sum(tri)
    if sum > best_sum:
        print(str(sum))
        best_sum = sum