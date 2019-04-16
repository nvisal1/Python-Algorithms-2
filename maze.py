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