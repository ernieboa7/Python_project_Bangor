from pyamaze import maze,agent,COLOR,textLabel

def BFS(m,c1,c2):
    '''
    The Breadth First Search Algorith for the Maze
    Parameters
    ----------
    m : instance of the Maze
        Declare the type of maze or a blueprint for the maze object
    Returns
    c1: the goal row index
    c2: the goal colomn index
    -------
    fwdPath
        All path that leads to the goal
    
    Pseudeo Code
    ------------
        Add start cell in both Frontier and Explored
        Repeat untill Goal is reached or Frontier is empty:
            currCell=Frontier.pop(0)
            for each direction(ESNW):
                childCell = Next Possible Cell
                if childCell already in Explored list -> Do nothing
                otherwise -> Append/Push childCell to both Explored & Frontier
    Data Structure
    --------------
        Queue
    '''
    start=(m.rows,m.cols)
    frontier=[start]
    explored=[start]
    bfsPath={}
    while len(frontier)>0:
        currCell=frontier.pop(0)
        if currCell==(c1,c2):
            break
        for d in 'ESNW':
            if m.maze_map[currCell][d]==True:
                if d=='E':
                    childCell=(currCell[0],currCell[1]+1)
                elif d=='W':
                    childCell=(currCell[0],currCell[1]-1)
                elif d=='N':
                    childCell=(currCell[0]-1,currCell[1])
                elif d=='S':
                    childCell=(currCell[0]+1,currCell[1])
                if childCell in explored:
                    continue
                frontier.append(childCell)
                explored.append(childCell)
                bfsPath[childCell]=currCell
    fwdPath={}
    cell=(c1,c2)
    while cell!=start:
        fwdPath[bfsPath[cell]]=cell
        cell=bfsPath[cell]
    return fwdPath


def DFS(m,c1,c2):
    '''
    The Depth First Search Algorith for the Maze
    Parameters
    ----------
    m : instance of the Maze
        Declare the type of maze or a blueprint for the maze object
    Returns
    c1: the goal row index
    c2: the goal colomn index
    -------
    fwdPath
        All path that leads to the goal
    
    Pseudeo Code
    ------------
        Push the start cell in both Frontier and Explored
        Repeat untill Goal is reached or Frontier is empty:
            currCell=Frontier.pop()
            for each direction(ESNW):
                childCell = Next Possible Cell
                if childCell already in Explored list -> Do nothing
                otherwise -> Append/Push childCell to both Explored & Frontier
    Data Structure
    --------------
        Stack
    '''
    start=(m.rows,m.cols)
    explored=[start]
    frontier=[start]
    dfsPath={}
    while len(frontier)>0:
        currCell=frontier.pop()
        if currCell==(c1,c2):
            break
        for d in 'ESNW':
            if m.maze_map[currCell][d]==True:
                if d=='E':
                    childCell=(currCell[0],currCell[1]+1)
                elif d=='W':
                    childCell=(currCell[0],currCell[1]-1)
                elif d=='S':
                    childCell=(currCell[0]+1,currCell[1])
                elif d=='N':
                    childCell=(currCell[0]-1,currCell[1])
                if childCell in explored:
                    continue
                explored.append(childCell)
                frontier.append(childCell)
                dfsPath[childCell]=currCell
    fwdPath={}
    cell=(c1,c2)
    while cell!=start:
        fwdPath[dfsPath[cell]]=cell
        cell=dfsPath[cell]
    return fwdPath


    ##PROGRAM START HERE
if __name__=='__main__':
    
    '''
        1.	The Algorithm to use
            a.	For Breadth First Algorithm – 1
            b.	For Depth First Algorithm – 2
        2.	To declare a path for maze in csv or generate a random maze by declaring the dimension of the maze 
            a.	To declare a path – 1, example maze.csv
            b.	To generate a random maze – 2, example 55 for 5 by 5 maze
        3.	To declare the goal cell for the maze search
            a.	For the goal cell, example 11 for the cell (1,1)

    '''
    print("Welcome to the Maze Search Empire")
    algo = input("Which of the algorithm do you want: Type 1 for BFS and 2 for DFS \n")
    if(algo == '1'):
        mazetype = input("Type 1 to declare path for the maze i.e maze1.csv or Type 2 to create a random maze i.e (5,5) for 5 by 5 maze \n")
        print("READY TO USE BFS ALGORITHM")
        if(mazetype == '1'):
            mazepath = input("please declare maze path i.e maze1.csv \n")
            mazetarget = input("please enter the target cell i.e 34 for cell 3,4 \n")
            r1 =int(mazetarget[0])
            r2 =int(mazetarget[1])
            m=maze()
            m.CreateMaze(r1, r2, loopPercent=100, pattern="h",loadMaze=mazepath, theme=COLOR.light)
            path=BFS(m,r1,r2)

            a=agent(m,footprints=True,filled=True)
            m.tracePath({a:path})
            l=textLabel(m,'BREADTH FIRST ALGORITHM: Length of Shortest Path',len(path)+1)

            m.run()
        elif(mazetype == '2'):
            mazepath = input("please the random maze size i.e 55 for 5 by 5 maze\n")
            rows =int(mazepath[0])
            cols =int(mazepath[1])
            mazetarget = input("please enter the target cell i.e 34 for cell 3,4 \n")
            r1 =int(mazetarget[0])
            r2 =int(mazetarget[1])
            m=maze(rows,cols)
            m.CreateMaze(r1,r2, loopPercent=100, pattern="h", theme=COLOR.light)
            path=BFS(m,r1,r2)

            a=agent(m,footprints=True, filled=True)
            m.tracePath({a:path})
            l=textLabel(m,'BREADTH FIRST ALGORITHM: Length of Shortest Path',len(path)+1)

            m.run()
    elif(algo == '2'):
        mazetype = input("Type 1 to declare path for the maze i.e maze1.csv or Type 2 to create a random maze i.e (5,5) for 5 by 5 maze \n")
        print("READY TO USE DFS ALGORITHM")
        if(mazetype == '1'):
            mazepath = input("please declare maze path i.e maze1.csv \n")
            mazetarget = input("please enter the target cell i.e 34 for cell 3,4 \n")
            r1 =int(mazetarget[0])
            r2 =int(mazetarget[1])
            print(mazepath)
            m=maze()
            m.CreateMaze(r1, r2, loopPercent=100, pattern="h", loadMaze=mazepath, theme=COLOR.light)
            path=DFS(m, r1, r2)

            a=agent(m,footprints=True,filled=True)
            m.tracePath({a:path})
            l=textLabel(m,'DEPTH FIRST ALGORITHM: Length of Shortest Path',len(path)+1)

            m.run()
        elif(mazetype == '2'):
            mazepath = input("please the random maze size i.e 55 for 5 by 5 maze\n")
            rows =int(mazepath[0])
            cols =int(mazepath[1])
            mazetarget = input("please enter the target cell i.e 34 for cell 3,4 \n")
            r1 =int(mazetarget[0])
            r2 =int(mazetarget[1])
            m=maze(rows,cols)
            m.CreateMaze(r1, r2, loopPercent=100, pattern="h", theme=COLOR.light)
            path=DFS(m,r1,r2)

            a=agent(m,footprints=True, filled=True)
            m.tracePath({a:path})
            l=textLabel(m,'DEPTH FIRST ALGORITHM: Length of Shortest Path',len(path)+1)

            m.run()
    else:
        print("You have choose a wrong option, pleas try again....")