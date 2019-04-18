grid = [[]]
r = 0 #row
# move right
grid[r].append(1)
grid[r].append(2)

#move down off grid
r += 1
grid.append([3])

#move left
grid[r].insert(0,4)
grid[r].insert(0,5)

#move up on grid
r -= 1
grid[r].insert(0,6)

#move up off grid
grid.insert(0,[7])

# move right
grid[r].append(8)
grid[r].append(9)
grid[r].append(10)

#move down on grid
r += 1
grid[r].append(11)
r += 1
grid[r].append(12)

def place_right(grid, r, n):
    grid[r].append(n)


for i in range(len(grid)):
    print(grid[i])