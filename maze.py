"""
Name: Nicholas Visalli 
Assignment number: 2
Purpose: Solve a maze using stacks
"""

"""Determine if there is a path to the left of current position in maze
:param maze: 2D array that represents maze structure
:type maze: 2D array
:param row: number of current row in maze
:type row: number
:param column: number of current column in maze
:type column: number
:param usedPaths: array of coordinates that have already been visited
:type usedPaths: array
:returns: None 
:rtype: None
"""
def checkLeft(maze, row, column, usedPaths):
    if column == 0:
        return '1'
    if str(row) + ' ' + str(column-1) in usedPaths:
        return '1'
    else:
        return maze[row][0][column-1]

"""Determine if there is a path to the right of current position in maze
:param maze: 2D array that represents maze structure
:type maze: 2D array
:param row: number of current row in maze
:type row: number
:param column: number of current column in maze
:type column: number
:param usedPaths: array of coordinates that have already been visited
:type usedPaths: array
:returns: None 
:rtype: None
"""
def checkRight(maze, row, column, usedPaths):
    if column == 19: 
        return '1'
    if str(row) + ' ' + str(column+1) in usedPaths:
        return '1'
    else:
        return maze[row][0][column+1]

"""Determine if there is a path above current position in maze
:param maze: 2D array that represents maze structure
:type maze: 2D array
:param row: number of current row in maze
:type row: number
:param column: number of current column in maze
:type column: number
:param usedPaths: array of coordinates that have already been visited
:type usedPaths: array
:returns: None 
:rtype: None
"""
def checkUp(maze, row, column, usedPaths):
    if row == 0:
        return '1'
    if str(row-1) + ' ' + str(column) in usedPaths:
        return '1'
    else:
        return maze[row-1][0][column]

"""Determine if there is a path below current position in maze
:param maze: 2D array that represents maze structure
:type maze: 2D array
:param row: number of current row in maze
:type row: number
:param column: number of current column in maze
:type column: number
:param usedPaths: array of coordinates that have already been visited
:type usedPaths: array
:returns: None 
:rtype: None
"""
def checkDown(maze, row, column, usedPaths):
    if row == 19:
        return '1'
    if str(row+1) + ' ' + str(column) in usedPaths:
        return '1'
    else:
        return maze[row+1][0][column]

"""Prints out resulting maze (finished or not)
:param maze: 2D array that represents maze structure
:type maze: 2D array
:param exitRoute: array that contains coordinates of escape route
:type exitRoute: array
:param startingPoint: a pair of coordinates that represent the starting point in the maze
:type stringPoint: string
:param completed: boolean that determines if user was able to complete the maze or not
:type completed: boolean
:returns: None
:rtype: None
"""
def displayCompletedMaze(maze, exitRoute, startingPoint, completed):
    print('     0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19')
    for x in range(len(maze)): 
        if x < 10:
            print str(x) + ':  ',
        else:
            print str(x) + ': ',
        for i in range(len(maze[x][0])):
            if str(x) + ' ' + str(i) in exitRoute:
                if str(x) + ' ' + str(i) == startingPoint: 
                    print'S  ',
                elif maze[x][0][i] == 'E':
                    print'E  ',
                else: 
                    print'+  ',
            else: 
                print maze[x][0][i] + '  ',
        print('\n')
    if completed:
        print("I am free!")
    else:
        print("Help, I am trapped")


"""Initializes the maze structure and required metadata
:returns: None 
:rtype: None
"""
def main():
    exitRoute = []
    usedPaths = []
    ins = open( "maze.txt", "r" )
    maze = [[n for n in line.split()] for line in ins]
    startingPoint = raw_input("Please enter the starting point (ie 0 1 where 0 is the row and 1 is the column): ")
    type(startingPoint)
    exitRoute.append(startingPoint)
    usedPaths.append(startingPoint)
    solveMaze(maze, exitRoute, usedPaths, startingPoint)

"""Orchestrates the process of solving the maze
:param maze: 2D array that represents maze structure
:type maze: 2D array
:param exitRoute: array that contains coordinates of escape route
:type exitRoute: array
:param usedPaths: array of coordinates that have already been visited
:type usedPaths: array
:param startingPoint: a pair of coordinates that represent the starting point in the maze
:type stringPoint: string
:returns: None
:rtype: None
"""
def solveMaze(maze, exitRoute, usedPaths, startingPoint):
    row = int(exitRoute[-1].split(' ')[0])
    column = int(exitRoute[-1].split(' ')[1])
    while maze[row][0][column] != 'E':
        completed = False
        paths = {}
        paths['right'] = checkRight(maze, row, column, usedPaths)
        paths['left'] = checkLeft(maze, row, column, usedPaths)
        paths['up'] = checkUp(maze, row, column, usedPaths)
        paths['down'] = checkDown(maze, row, column, usedPaths)

        if paths['up'] == '0' or paths['up'] == 'E':
            exitRoute.append(str(row-1) + ' ' + str(column))
            usedPaths.append(str(row-1) + ' ' + str(column))
            row = int(exitRoute[-1].split(' ')[0])
            column = int(exitRoute[-1].split(' ')[1])
            if paths['up'] == 'E':
                completed = True
        elif paths['left'] == '0' or paths['left'] == 'E':
            exitRoute.append(str(row) + ' ' + str(column-1))
            usedPaths.append(str(row) + ' ' + str(column-1))
            row = int(exitRoute[-1].split(' ')[0])
            column = int(exitRoute[-1].split(' ')[1])
            if paths['left'] == 'E':
                completed = True
        elif paths['right'] == '0' or paths['right'] == 'E':
            exitRoute.append(str(row) + ' ' + str(column+1))
            usedPaths.append(str(row) + ' ' + str(column+1))
            row = int(exitRoute[-1].split(' ')[0])
            column = int(exitRoute[-1].split(' ')[1])
            if paths['right'] == 'E':
                completed = True
        elif paths['down'] == '0' or paths['down'] == 'E':
            exitRoute.append(str(row+1) + ' ' + str(column))
            usedPaths.append(str(row+1) + ' ' + str(column))
            row = int(exitRoute[-1].split(' ')[0])
            column = int(exitRoute[-1].split(' ')[1])
            if paths['down'] == 'E':
                completed = True
        else:
            if (exitRoute[-1] != startingPoint):
                exitRoute.pop()
                row = int(exitRoute[-1].split(' ')[0])
                column = int(exitRoute[-1].split(' ')[1])
            else: 
                break;

    displayCompletedMaze(maze, exitRoute, startingPoint, completed)
        
if __name__== "__main__":
    main()