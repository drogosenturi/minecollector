import random
import os
import getch

# Function to build the grid. Takes x and y which define the area
#   Coordinates are produced, X represents cursor
#   o represents safety, *'s represent mines
#   It is then saved to variable grid
def makegrid(x, y):
    coordinates = []
    grid= ''
    for i in range(0, x):
        for u in range(0,y):
            set = i,u
            coordinates.append(set)
    for t in coordinates:
        if t[1] == (y-1):
            grid = grid + "\n\n"
        elif t == (x-1, y-2):
            grid = grid + "X"
        elif random.randint(0,10) < 3:
            grid = grid + "*    "
        else:
            grid = grid + "o    "
        pass
    return grid

# Function to move X (up left down right) based on user input (WASD). In each direction, list is reordered to place "X"
# in the spot that there was previously a mine or an 'o'
def move(x):
    user = getch.getch()
    pos = x.index('X')
    if user == "w":
        grid = x.replace(x[pos],'o')
        if (pos - 51) > 0:
            grid = grid[:pos - 52] + 'X' + grid[pos - 51:] # move up line
        else:
            grid = grid[:pos - 48] + 'X' + grid[pos - 47:] # wrap to bottom
    if user == "a":
        grid = x.replace(x[pos], 'o')
        if pos % 52 == 0:
            grid = grid[:pos + 45] + 'X' + grid[pos + 46:] # move left along line
        else:
            grid = grid[:pos - 5] + 'X' + grid[pos - 4:] # wrap to right
    if user == "d":
        grid = x.replace(x[pos], 'o')
        if pos in list(range(45,2000,52)): 
            grid = grid[:pos - 45] + 'X' + grid[pos - 44:] # move right along line
        else:
            grid = grid[:pos + 5] + 'X' + grid[pos + 6:] # wrap to the left edge
    if user == "s":
        grid = x.replace(x[pos],'o')
        if pos in list(range(520,570,5)):
            grid = grid[:pos - 520] + 'X' + grid[pos - 519:] # move down along line
        else:
            grid = grid[:pos + 52] + 'X' + grid[pos + 53:] # wrap to the top edge
    return grid, pos


os.system('clear' if os.name == 'posix' else 'cls')
grid = makegrid(11,11)
mines = grid.count("*")
steps = 0
steplimit = 60
print("\033[31;1mMINE COLLECTOR\033[0m") # red bold
print(f"\033[90;3mCollect all of the mines (*) within {steplimit} steps\033[0m") # light black italic
print("Use WASD to navigate. Start navigating to begin.")
print(grid)
print("mine count: ", mines)
print("steps: ", steps)
while mines != 0 and steps != steplimit:
    grid, pos = move(grid)
    mines = grid.count("*")
    steps = steps + 1
    os.system('clear' if os.name == 'posix' else 'cls')
    print("\033[31;1mMINE COLLECTOR\033[0m") # red bold
    print(f"\033[90;3mCollect all of the mines (*) within {steplimit} steps\033[0m\n") #dark black italic and newline
    print(grid)
#    print("\npos: ",pos) # string position for testing
    print("mine count: ", mines)
    print("steps: ", steps)
if mines == 0:
    print("\033[38;5;207;48;5;8;1;5m                Great job!                  \033[0m") #gray background pink blinky bold
else:
    print("\033[91;1;5mFAILURE. . .\033[0m") #red bold blinky