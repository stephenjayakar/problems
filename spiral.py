WIDTH = 10
HEIGHT = 15

# next rotate translation
rotation = {(1, 0): (0, 1),
            (0, 1): (-1, 0),
            (-1, 0): (0, -1),
            (0, -1): (1, 0)}

# checks if x and y are in bounds for the array
def in_bounds(arr, x, y):
    return y < len(arr) and x < len(arr[0]) and x >= 0 and y >= 0

# returns the next change of x and y
def rotate(dx, dy):
    return rotation[(dx, dy)]

# seeding the matrix
arr = []
count = 1
for i in range(WIDTH):
    arr.append([0] * HEIGHT)
    for j in range(HEIGHT):
        arr[i][j] = count
        count += 1

# printing the original matrix        
for row in arr:
    print(row)

# creating the visited matrix    
visited = []
for i in range(WIDTH):
    visited.append([False] * HEIGHT)


# x, y indexes
ix = 0
iy = 0
# change of indexes
dx = 1
dy = 0

# while the element to the right is not visited
while not visited[iy][ix]:
    while in_bounds(arr, ix, iy) and not visited[iy][ix]:
        # print("INDEX X: {}, INDEX Y: {}".format(ix, iy))
        print(arr[iy][ix])
        visited[iy][ix] = True
        ix += dx
        iy += dy
    # accounting for the edge case of going out of bounds
    ix -= dx
    iy -= dy
    dx, dy = rotate(dx, dy)
    ix += dx
    iy += dy
