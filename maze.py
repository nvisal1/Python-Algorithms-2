def checkLeft(maze, row, column, usedPaths):
    if column == 0:
        return '1'
    if str(row) + ' ' + str(column-1) in usedPaths:
        return '1'
    else:
        return maze[row][0][column-1]
    
def checkRight(maze, row, column, usedPaths):
    if column == 19: 
        return '1'
    if str(row) + ' ' + str(column+1) in usedPaths:
        return '1'
    else:
        return maze[row][0][column+1]

def checkUp(maze, row, column, usedPaths):
    if row == 0:
        return '1'
    if str(row-1) + ' ' + str(column) in usedPaths:
        return '1'
    else:
        return maze[row-1][0][column]

def checkDown(maze, row, column, usedPaths):
    if row == 19:
        return '1'
    if str(row+1) + ' ' + str(column) in usedPaths:
        return '1'
    else:
        return maze[row+1][0][column]
    
def main():
    exitRoute = []
    usedPaths = []
    ins = open( "maze.txt", "r" )
    maze = [[n for n in line.split()] for line in ins]
    for line in maze: 
        print(line)
    startingPoint = raw_input("Please enter the starting point (ie 0 1 where 0 is the row and 1 is the column): ")
    type(startingPoint)
    exitRoute.append(startingPoint)
    usedPaths.append(startingPoint)
    solveMaze(maze, exitRoute, usedPaths, startingPoint)

def solveMaze(maze, exitRoute, usedPaths, startingPoint):
    row = int(exitRoute[-1].split(' ')[0])
    column = int(exitRoute[-1].split(' ')[1])
    while maze[row][0][column] != 'E':
        paths = {}
        paths['right'] = checkRight(maze, row, column, usedPaths)
        paths['left'] = checkLeft(maze, row, column, usedPaths)
        paths['up'] = checkUp(maze, row, column, usedPaths)
        paths['down'] = checkDown(maze, row, column, usedPaths)

        if paths['up'] == '0' or paths['up'] == 'E':
            print('up')
            exitRoute.append(str(row-1) + ' ' + str(column))
            usedPaths.append(str(row-1) + ' ' + str(column))
            row = int(exitRoute[-1].split(' ')[0])
            column = int(exitRoute[-1].split(' ')[1])
        elif paths['left'] == '0' or paths['left'] == 'E':
            print('left')
            exitRoute.append(str(row) + ' ' + str(column-1))
            usedPaths.append(str(row) + ' ' + str(column-1))
            row = int(exitRoute[-1].split(' ')[0])
            column = int(exitRoute[-1].split(' ')[1])
        elif paths['right'] == '0' or paths['right'] == 'E':
            print('right')
            exitRoute.append(str(row) + ' ' + str(column+1))
            usedPaths.append(str(row) + ' ' + str(column+1))
            row = int(exitRoute[-1].split(' ')[0])
            column = int(exitRoute[-1].split(' ')[1])
        elif paths['down'] == '0' or paths['down'] == 'E':
            print('down')
            exitRoute.append(str(row+1) + ' ' + str(column))
            usedPaths.append(str(row+1) + ' ' + str(column))
            row = int(exitRoute[-1].split(' ')[0])
            column = int(exitRoute[-1].split(' ')[1])
        else:
            # if (exitRoute[-1] != startingPoint):
            exitRoute.pop()
            print('pop!')
            row = int(exitRoute[-1].split(' ')[0])
            column = int(exitRoute[-1].split(' ')[1])
        
        print(row, column)
        print(maze[row][0][column])
       
if __name__== "__main__":
    main()