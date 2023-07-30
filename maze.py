from turtle import *
from tkinter import *
import turtle


def draw_maze_line(turtle, room_size, go_right, pen_up, segments):
    """ Draw a line in a maze in segments.

        The parameter room_size is the width of a square room
        in the maze in pixels. """

    # Skip to next line over
    turtle.up()
    if go_right:
        turtle.right(90)
        turtle.forward(1*room_size)
        turtle.right(90)
    else:
        turtle.left(90)
        turtle.forward(1*room_size)
        turtle.left(90)        
    turtle.down()

    # Draw the line in segments
    for s in segments:
        if pen_up:
            turtle.up()
        turtle.forward(s*room_size)
        if pen_up:
            turtle.down()
        pen_up = not(pen_up)


def draw_hampton_court_maze(tracer_on, colour, room_size,
                            line_width, start_x, start_y):
    """ Draws a stylised version of the Hampton Court Maze """

    # create a turtle for drawing the maze
    turtle1 = Turtle()
    turtle1.hideturtle()
    turtle1.name = 'Hampton Court Maze Drawing Turtle'

    turtle1.reset()
    turtle1.speed('fastest')
    tracer(tracer_on)
    
    turtle1.color(colour)
    turtle1.width(line_width)

    # Start at bottom right, one row down pointing to the right (east)
    turtle1.up()
    turtle1.goto(start_x,start_y)
    turtle1.down()
    
    # Draw horizontal lines in zig zag fashion, first right to left,
    # then left to right, and so on
    draw_maze_line(turtle1, room_size, 0, 0, [9, 0, 9])
    draw_maze_line(turtle1, room_size, 1, 1, [1, 18])
    draw_maze_line(turtle1, room_size, 0, 1, [1, 8, 2, 6])
    draw_maze_line(turtle1, room_size, 1, 1, [3, 3, 3, 2, 2, 2])
    draw_maze_line(turtle1, room_size, 0, 1, [5, 2, 1, 3, 4, 0, 2])
    draw_maze_line(turtle1, room_size, 1, 0, [0, 18])
    draw_maze_line(turtle1, room_size, 0, 0, [0, 17, 0])
    draw_maze_line(turtle1, room_size, 1, 1, [5, 6, 6, 0])
    draw_maze_line(turtle1, room_size, 0, 1, [2, 2, 1, 3, 2, 3, 3])
    draw_maze_line(turtle1, room_size, 1, 0, [3, 2, 4, 2, 4, 1])
    draw_maze_line(turtle1, room_size, 0, 0, [4, 2, 3, 1, 2, 2, 3, 1])
    draw_maze_line(turtle1, room_size, 1, 0, [19, 1])

    # Now at top right one column outside maze, re-orient pointing up (north)
    turtle1.left(90)

    # Draw Vertical lines in zig zag fashion, first top to bottom,
    # then bottom to top, and so on
    draw_maze_line(turtle1, room_size, 0, 0, [11])
    draw_maze_line(turtle1, room_size, 1, 1, [2, 3, 2, 3])
    draw_maze_line(turtle1, room_size, 0, 1, [1, 1, 1, 4])
    draw_maze_line(turtle1, room_size, 1, 1, [1, 4])
    draw_maze_line(turtle1, room_size, 0, 1, [6, 0])
    draw_maze_line(turtle1, room_size, 1, 1, [1, 0, 8])
    draw_maze_line(turtle1, room_size, 0, 0, [0, 8, 0])
    draw_maze_line(turtle1, room_size, 1, 1, [1, 3, 3, 0])
    draw_maze_line(turtle1, room_size, 0, 1, [8])
    draw_maze_line(turtle1, room_size, 1, 0, [0, 7])
    draw_maze_line(turtle1, room_size, 0, 0, [0, 8, 0])
    draw_maze_line(turtle1, room_size, 1, 1, [2, 0, 8, 0])
    draw_maze_line(turtle1, room_size, 0, 1, [7])
    draw_maze_line(turtle1, room_size, 1, 0, [3, 1, 0, 3])
    draw_maze_line(turtle1, room_size, 0, 0, [0, 3, 0, 6])
    draw_maze_line(turtle1, room_size, 1, 0, [0, 6])
    draw_maze_line(turtle1, room_size, 0, 0, [5, 1])
    draw_maze_line(turtle1, room_size, 1, 0, [1, 1, 0, 3, 2, 1])
    draw_maze_line(turtle1, room_size, 0, 0, [4, 2, 3, 1])
    draw_maze_line(turtle1, room_size, 1, 0, [11])
    
    
    Ernest = turtle
    Ernest.width(4)
    Ernest.speed(0)
    Ernest.color("red")
    Ernest.penup()
    Ernest.goto(10, -60)  #(190, -140)
    Ernest.pendown()
    Ernest.left(90)
    #Ernest.fd(10)    #(190,-130)
    Ernest.left(90)
    #Ernest.fd(360)   #(-170, -130)
    Ernest.right(90)
    #Ernest.fd(200)   #(-170, 70)
    Ernest.right(90)
    #Ernest.fd(360)   #(190, 70)
    Ernest.right(90)
    #Ernest.fd(180)    #(190, -110)
    Ernest.right(90)
    #Ernest.fd(340)    #(-150, -110)
    Ernest.right(90)
    #Ernest.fd(160)    #(-150, 50)
    Ernest.right(90)
    #Ernest.fd(320)     #(170, 50)
    Ernest.right(90)
    #Ernest.fd(140)    #(170, -90)
    Ernest.right(90)
    #Ernest.fd(300)    #(-130, -90)
    Ernest.right(90)  
    #Ernest.fd(120)  #(-130, 30)
    Ernest.right(90)
    #Ernest.fd(280)   #(150, 30)
    Ernest.right(90)
    #Ernest.fd(100)   #(150, -70)
    Ernest.right(90)
    #Ernest.fd(140)   #(10, -70)
    Ernest.right(90)
    #Ernest.fd(10)    #(10, -60)
    update()


    
draw_hampton_court_maze(1, "blue", 20, 4, 180, -160)  

  
