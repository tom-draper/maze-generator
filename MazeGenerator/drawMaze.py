import turtle

class DrawMaze():
    
    def __init__(self, size):
        self.wn = turtle.Screen()
        self.pen = turtle.Turtle()
        
        self.wn_width = 1000
        self.wn_height = 1000
        
        self.startX = -((self.wn_width-100)/2)
        self.startY = (self.wn_height-100)/2
        
        self.cellLength = ((self.wn_width-100)/size)
        
        self.drawInitialGrid(size)
        
    def drawInitialGrid(self, size):
        
        self.wn.title("Maze")
        self.wn.bgcolor("white")
        
        self.wn.setup(self.wn_width, self.wn_height)
        
        # Set up drawing tool
        self.pen.color("black")
        self.pen.hideturtle()
        self.pen.speed(0)
        self.pen.pensize(3)
        turtle.tracer(False)
        
        # Draw horizontal lines
        for count in range(size + 1):
            self.pen.up()
            self.pen.goto(self.startX, self.startY - (count * self.cellLength))
            self.pen.down()
            forward = size * self.cellLength
            self.pen.forward(forward)
            
        self.pen._rotate(270)
            
        # Draw vertical lines
        for count in range(size + 1):
            self.pen.up()
            self.pen.goto(self.startX + (count * self.cellLength), self.startY )
            self.pen.down()
            forward = size * self.cellLength
            self.pen.forward(forward)
        
        turtle.update()
        
    def removeEdge(self, X1, Y1, X2, Y2):
        self.pen = turtle.Turtle()
        self.pen.color("white")
        
        print('\n')
        print(str(X1))
        print(str(Y1))
        print(str(X2))
        print(str(Y2))
        
        self.pen.up()
        self.pen.goto(X1, Y1)
        self.pen.down()
        self.pen.goto(X2, Y2)
        
        turtle.update()
        
    def createExit(self, vertex, size, edge):
        # Get location vertex by length along edge either right or down 
            # (depending on edge)
        if edge == 't':
            location = vertex
            X1 = self.startX + location * self.cellLength
            X2 = X1 + self.cellLength
            y = self.startY
            self.removeEdge(X1, y, X2, y)
        elif edge == 'b':
            location = vertex - (size*(size-1))
            X1 = self.startX + location * self.cellLength
            X2 = X1 + self.cellLength
            y = self.startY + (self.cellLength * (size + 1))
            self.removeEdge(X1, y, X2, y)
        elif edge == 'l':
            location = vertex / size
            x = self.startX
            Y1 = self.startY + (location * self.cellLength)
            Y2 = Y1 + self.cellLength
            self.removeEdge(x, Y1, x, Y2)
        elif edge == 'r':
            location = (vertex - (size - 1)) / size
            x = self.startX + (self.cellLength * (size + 1))
            Y1 = self.startY + (location * self.cellLength)
            Y2 = Y1 + self.cellLength
            self.removeEdge(x, Y1, x, Y2)
        
            