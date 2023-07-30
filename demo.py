from pyamaze import maze,COLOR,agent
m=maze(16,24)
#m.CreateMaze(loadMaze="hampton_court_maze.csv")
#m.CreateMaze(loadMaze="hampton.csv")
m.CreateMaze(theme=COLOR.light, saveMaze=True)
a=agent(m,footprints=True)

m.run()