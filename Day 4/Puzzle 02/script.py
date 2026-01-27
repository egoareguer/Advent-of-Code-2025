from pathlib import Path
import copy
script_dir = Path(__file__).parent
file_path = script_dir / '../input.txt'

grid=[]
sum_removed_rolls=0

with open(file_path, 'r') as input:
    for line in input: 
        grid.append(line.strip())
grid = [list(row) for row in grid]

width=len(grid[0])
height=len(grid)

check_matrix = [["-1", "-1", "-1"], # -1 means out of bound, @ means occupied, . Means free
                ["-1", grid[0][0], grid[0][1]], 
                ["-1", grid[1][0], grid[1][1]]]

def is_accessible (matrix):
    if matrix[1][1]==".": 
        return (False) # There's no paper roll to access

    sum_occupied_neighbors=-1 # -1 to account for the paper rolls we're checking is accessible or not

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]=="@":
                sum_occupied_neighbors +=1 
 
    if sum_occupied_neighbors < 4:
        return (True)
    else:
        return (False)

def set_matrix(x,y): # !! THIS ASSUMES INNER (NON BORDER) COORDINATES !!
    check_matrix[0][0]=grid[y-1][x-1]
    check_matrix[0][1]=grid[y-1][x]
    check_matrix[0][2]=grid[y-1][x+1]
    check_matrix[1][0]=grid[y][x-1]
    check_matrix[1][1]=grid[y][x]
    check_matrix[1][2]=grid[y][x+1]
    check_matrix[2][0]=grid[y+1][x-1]
    check_matrix[2][1]=grid[y+1][x]
    check_matrix[2][2]=grid[y+1][x+1]

def iterate_grid(grid):
    grid_post_removal=copy.deepcopy(grid)
    sum_removed_rolls = 0
    # The four corners are necessarily accessible IF there is a roll there, since they have at most 3 neighbors
    # Yes, you should not run this each time. Osef.
    if grid[0][0]=="@":
        sum_removed_rolls += 1
        grid_post_removal[0][0]="."
    if grid[0][width-1]=="@":
        sum_removed_rolls += 1
        grid_post_removal[0][width-1]="."
    if grid[height-1][0]=="@":
        sum_removed_rolls += 1
        grid_post_removal[height-1][0]="."
    if grid[height-1][width-1]=="@":
        sum_removed_rolls += 1
        grid_post_removal[height-1][width-1]="."

    # We do the four borders in explicit for loops, and the core last

    # Upper border. That means grid[0][x]
    for x in range (1, width - 1): # Borders include two corners we skip
        check_matrix[0]=[".", ".", "."]
        check_matrix[1][0]=grid[0][x-1]
        check_matrix[1][1]=grid[0][x]
        check_matrix[1][2]=grid[0][x+1] # The (width - 2) range ensures we won't go too far
        check_matrix[2][0]=grid[1][x-1]
        check_matrix[2][1]=grid[1][x]
        check_matrix[2][2]=grid[1][x+1]
        if is_accessible(check_matrix):
            sum_removed_rolls += 1 
            grid_post_removal[0][x]="."

    # Left border. That means grid [y][0]
    for y in range (1, height - 1):
        check_matrix[0][0]="."
        check_matrix[1][0]="."
        check_matrix[2][0]="."
        check_matrix[0][1]=grid[y-1][0]
        check_matrix[0][2]=grid[y-1][1]
        check_matrix[1][1]=grid[y][0]
        check_matrix[1][2]=grid[y][1]
        check_matrix[2][1]=grid[y+1][0]
        check_matrix[2][2]=grid[y+1][1]
        if is_accessible(check_matrix):
            sum_removed_rolls += 1 
            grid_post_removal[y][0]="."

    # Right border. That means grid[y][width-1]
    for y in range (1, height - 1):
        check_matrix[0][0]=grid[y-1][width-2]
        check_matrix[1][0]=grid[y][width-2]
        check_matrix[2][0]=grid[y+1][width-2]
        check_matrix[0][1]=grid[y-1][width-1]
        check_matrix[1][1]=grid[y][width-1]
        check_matrix[2][1]=grid[y+1][width-1]
        check_matrix[0][2]="."
        check_matrix[1][2]="."
        check_matrix[2][2]="."
        if is_accessible(check_matrix):
            sum_removed_rolls += 1 
            grid_post_removal[y][width-1]="."

    # Bottom border. So grid[height-1][x]
    for x in range (1, width - 1):
        check_matrix[0][0]=grid[height-2][x-1]
        check_matrix[0][1]=grid[height-2][x]
        check_matrix[0][2]=grid[height-2][x+1]
        check_matrix[1][0]=grid[height-1][x-1]
        check_matrix[1][1]=grid[height-1][x]
        check_matrix[1][2]=grid[height-1][x+1]
        check_matrix[2][0]="."
        check_matrix[2][1]="."
        check_matrix[2][2]="."
        if is_accessible(check_matrix):
            sum_removed_rolls += 1 
            grid_post_removal[height-1][x]="."

    for y in range (1, height - 1):
        for x in range (1, width - 1):
            set_matrix(x,y)
            if is_accessible(check_matrix):
                sum_removed_rolls += 1
                grid_post_removal[y][x]="."
    return (grid_post_removal, sum_removed_rolls)

while True:
    grid_check, removed_rolls = (iterate_grid(grid))
    sum_removed_rolls += removed_rolls
    if grid_check == grid:
        break
    else:
        grid=grid_check

print(sum_removed_rolls)