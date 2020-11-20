#--------------------------------------------------------------------------------------------
# IMPORT STATEMENTS
#--------------------------------------------------------------------------------------------
import math
import pygame
import random

#--------------------------------------------------------------------------------------------
# GLOBAL VARIABLES
#--------------------------------------------------------------------------------------------
# Change this variable to set the size of the grid
n = 20
# Screen Resolution
WIDTH = 800
HEIGHT = 800
# Width of 1 cell in the maze grid
w = WIDTH/n

# Frames per second for pygame
FPS = 30 

# Colors
WHITE = [255,255,255]
BLACK = [0,0,0]
BLUE = [2,5,64]
GREEN = [124, 252, 0]

# Determines the number of rows and columns in the grid
cols = int(math.floor(WIDTH/w))
rows = int(math.floor(HEIGHT/w))

# Arrays
grid = []
stack = []

# Variable to track when the maze is done
mazeComplete = False

#--------------------------------------------------------------------------------------------
# CELL CLASS
#--------------------------------------------------------------------------------------------
class Cell:
    def __init__(self, i,j):
        # i.e the x coordinate
        self.i = i
        # i.e the y coordinate
        self.j = j
        # Boolean value to represent if there is a wall. True = wall.  [Top, Right, Bottom, Left]
        self.walls = [True, True, True, True]
        # Variable to track if the cell was visited True = Visited
        self.visited = False

#--------------------------------------------------------------------------------------------
# FUNCTIONS - in alphabetical order
#--------------------------------------------------------------------------------------------
def checkNeighbours(cell):
    neighbours = []
    
    i = cell.i
    j = cell.j

    # Finds the data for the cells surrounding the current cell
    top = grid[index(i,j-1)]
    right = grid[index(i+1,j)]
    bottom = grid[index(i,j+1)]
    left = grid[index(i-1,j)]    

    # Adds the neighbours to the neighbours array if they have not been visited and that the index is valid
    if top.visited == False and index(i,j-1) >0:
        neighbours.append(top)
    if right.visited == False and index(i+1,j) >0:
        neighbours.append(right)
    if bottom.visited == False and index(i,j+1) >0:
        neighbours.append(bottom)
    if left.visited == False and index(i-1,j) >0:
        neighbours.append(left)

    # Randomly chooses a cell connected to the current cell
    if len(neighbours)>0:
        randomNum = random.randrange(0,len(neighbours))
        return neighbours[randomNum]
    else:
        return None
    

def createGrid(grid):
    for cell in grid:
        
        x = cell.i*w
        y = cell.j*w
        # Draws the top wall
        if cell.walls[0] == True:
            pygame.draw.line(screen, WHITE, [x, y],[x+w,y],1)
        else:
            pygame.draw.line(screen, BLUE, [x, y],[x+w,y],1)
        # Draws the right wall
        if cell.walls[1] == True:
            pygame.draw.line(screen, WHITE, [x+w, y],[x+w,y+w],1)
        else:
            pygame.draw.line(screen, BLUE, [x+w, y],[x+w,y+w],1)
        # Draws the bottom wall
        if cell.walls[2] == True:
            pygame.draw.line(screen, WHITE, [x, y+w],[x+w,y+w],1)
        else:
            pygame.draw.line(screen, BLUE, [x, y+w],[x+w,y+w],1)
        # Draws the left wall
        if cell.walls[3] == True:
            pygame.draw.line(screen, WHITE, [x, y],[x,y+w],1)
        else:
            pygame.draw.line(screen, BLUE, [x, y],[x,y+w],1)
        
        # Marks a cell as visited
        if cell.visited == True:
            markVisited(cell)

def currentHighlight(cell):
    pygame.draw.rect(screen, GREEN, [(cell.i)*w+1, (cell.j)*w+1, w-1, w-1]) # left top width heigh

def index(i,j):
    # Checks to make sure we are getting a valid index
    if (i<0 or j<0 or i>(cols-1) or j>(cols-1)):
        return -1
    
    # Converts the index of a 2D array into a 1D array
    index = i + j*cols
    return index

def markVisited(cell):
    pygame.draw.rect(screen, BLUE, [(cell.i)*w+1, (cell.j)*w+1, w-1, w-1]) # left top width heigh

def removeWalls(a, b):
    # Calculates the index of the given cells
    indexA = index(a.i, a.j)
    indexB = index(b.i, b.j)
    
    x = a.i - b.i
    if x == 1:
        # Removes the left wall of a
        grid[indexA].walls[3] = False
        # Removes the right wall of b
        grid[indexB].walls[1] = False
    elif x == -1:
        # Removes the right wall of a
        grid[indexA].walls[1] = False
        # Removes the left wall of b
        grid[indexB].walls[3] = False
    
    y = a.j - b.j
    if y == 1:
        # Removes the top wall of a
        grid[indexA].walls[0] = False
        # Removes the bottom wall of b
        grid[indexB].walls[2] = False
    elif y == -1:
        # Removes the bottom wall of a
        grid[indexA].walls[2] = False
        # Removes the top wall of b
        grid[indexB].walls[0] = False

#--------------------------------------------------------------------------------------------
# MAZE GENERATING CODE
#--------------------------------------------------------------------------------------------
# Creates the cell objects
for j in range(rows):
    for i in range(cols):
        cell = Cell(i,j)
        grid.append(cell)

#--------------------------------------------------------------------------------------------
# MAIN PYGAME CODE
#--------------------------------------------------------------------------------------------
# Initializes the pygame modules
pygame.init()
# Initializes the module for sound loading and playback
pygame.mixer.init()
# Creates the visual image surface on the monitor.
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# Adds a title of the display window
pygame.display.set_caption("Grid")
# Creates a clock object to track time
clock = pygame.time.Clock()
# Creates the black background on the screen
screen.fill(BLACK)
# Sets the current cell to the first cell and marks it as visited
current = grid[0]
# Labels the first cell as visited and highlights it in the maze
grid[0].visited = True
# Adds the current cell to the stack
stack.append(current)
pygame.display.update()
   

running = True
while running:
    # Keeps the game running at the right speed
    clock.tick(FPS)  

    # Creates the grid for the maze
    createGrid(grid)

    # Randomly chooses the next cell in the maze
    if mazeComplete == False:
        # Finds a neighbouring cell to go to
        nextCell = checkNeighbours(current)
        # Pushes the current cell to the stack
        if nextCell != None:
            nextCell.visited = True
            grid[index(nextCell.i, nextCell.j)].visited = True
            removeWalls(current,nextCell)
            currentHighlight(current)
            stack.append(current)
            current = nextCell
        elif len(stack) > 0:
            # Pops a cell of the stack and makes it the current cell
            current = stack[len(stack)-1]
            del stack[len(stack)-1]
            currentHighlight(current)
        else:
            mazeComplete = True  
            

    pygame.display.update()

    for event in pygame.event.get():
        # Checks for closing the window
        if event.type == pygame.QUIT:
            running = False