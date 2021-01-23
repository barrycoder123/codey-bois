#Ibrahima Barry
from tkinter import *
import random
   
####################################
# customize these functions
####################################
def checking_changes_for_git():
    pass

def hard_press():
    pass

def init(data):
    # load data.xyz as appropriate data.rows, data.cols, data.cellSize, and data.margin
    data.board = []
    data.rows = 15
    data.cols = 10
    data.cellsize = 20
    data.margin = 25
    data.emptyColor = "blue"
    data.fallingPiece = None  
    data.fallingPieceColor = None
    data.fallingPieceRow = None
    data.fallingPieceCol = None
    data.score = 0
    data.isGameOver = False # false for now until it becomes relevant
    '''
    data.newRow = None
    data.newCol = None
    data.newCenterRow = None
    ''' 
    for row in range(data.rows):
        data.board.append([])
        for col in range(data.cols):
            data.board[row].append(data.emptyColor)
  #
    # Seven "standard" pieces (tetrominoes)

    iPiece = [
        [  True,  True,  True,  True ]
    ]

    jPiece = [
        [  True, False, False ],
        [  True,  True,  True ]
    ]

    lPiece = [
        [ False, False,  True ],
        [  True,  True,  True ]
    ]

    oPiece = [
        [  True,  True ],
        [  True,  True ]
    ]

    sPiece = [
        [ False,  True,  True ],
        [  True,  True, False ]
    ]

    tPiece = [
        [ False,  True, False ],
        [  True,  True,  True ]
    ]

    zPiece = [
        [  True,  True, False ],
        [ False,  True,  True ]
    ]
    data.tetrisPieces = [ iPiece, jPiece, lPiece, oPiece, sPiece, tPiece, zPiece ]
    data.tetrisPieceColors = [ "red", "yellow", "magenta", "pink", "cyan", "green", "orange" ]
    # selecting falling pieces
    newFallingPiece(data)
   # print(data.board)
        

def mousePressed(event, data):
    # use event.x and event.y
    pass

def keyPressed(event, data):
    # use event.char and event.keysym
    # first make sure gameOver is false so you can do all this so you'll use elif
    if(data.isGameOver == False):
        if event.keysym == "w":
            rotateFallingPiece(data)
            
        elif event.keysym == "s":
            moveFallingPiece( data, 1, 0)
            
        elif event.keysym == "a":
            moveFallingPiece( data, 0, -1)
            
        elif event.keysym == "d":
            moveFallingPiece( data, 0, 1)
            
    # but now how do you restart the game
    if event.char == "r":
        init(data)
        
def timerFired(data):
    # a way to check gameOver
    if (data.isGameOver == False):
        result = moveFallingPiece(data, +1, 0)
    # if moveFallingPiece returns false(you cant move it) that means the piece has reached the bottom so call the new falling piece. Use any move dire
        if result == False:
            placeFallingPiece(data)
            newFallingPiece(data)
        # if you place a piece and right away its not legal then gameOver == true
            if fallingPieceIsLegal(Canvas, data) == False:
                data.isGameOver = True
def redrawAll(canvas, data):
    # draw in canvas
    canvas.create_rectangle(0, 0, 250, 350, fill = "orange")
    drawBoard(canvas, data)
    drawFallingPiece(canvas, data)
    # draw the score
    canvas.create_text(data.width/2, 15, font = "Arial 10 bold", text = "Score: " + str(data.score))
    # instructions for when gameOver is true
    if (data.isGameOver == True):
        canvas.create_rectangle(0,0,data.width, data.height, fill="yellow", width = 0)
        canvas.create_text(data.width/2, data.height/2, font = "Arial 35 bold", text = "LOSER")
        canvas.create_text(data.width/2, data.height/2 + 35, font = "Arial 10 bold", text = "\"r\" to restart")
def drawBoard(canvas, data):
    for r in range(len(data.board)):
        for c in range(len(data.board[0])):
            drawCell(canvas, data, r, c, data.board[r][c])
       
    
def drawCell( canvas, data, row, col, color):
    x = col * data.cellsize + data.margin
    y = row * data.cellsize + data.margin
    canvas.create_rectangle( x, y, x + data.cellsize, y + data.cellsize,
    fill = color, width  = 3.7)
def newFallingPiece(data):
    # postion it in the middle
    randomIndex = random.randint(0, len(data.tetrisPieces) - 1)
    data.fallingPiece =  data.tetrisPieces[randomIndex]
    data.fallingPieceColor = data.tetrisPieceColors[randomIndex]
    data.fallingPieceRow = 0 
    data.fallingPieceCol = data.cols//2 - len(data.fallingPiece[0])//2
    
    removeFullRows(data)
    
def drawFallingPiece( canvas, data):
    # itreate through each cell in falling piece
    for row in range(len(data.fallingPiece)):
        for col in range(len(data.fallingPiece[row])):
            if data.fallingPiece[row][col]:
                drawCell(canvas, data, data.fallingPieceRow + row , data.fallingPieceCol + col, data.fallingPieceColor )
                
def fallingPieceIsLegal(Canvas, data):

    for row in range(len(data.fallingPiece)):
        for col in range(len(data.fallingPiece[0])):
            if data.fallingPiece[row][col]:
                if (data.fallingPieceRow + row >= data.rows) or (data.fallingPieceRow + row < 0)  or (data.fallingPieceCol+ col >= data.cols) or (data.fallingPieceCol + col< 0):
                        return False
                        
    for row in range(len(data.fallingPiece)):
        for col in range(len(data.fallingPiece[0])):
            if data.fallingPiece[row][col] == True:
                if data.board[data.fallingPieceRow + row][data.fallingPieceCol + col] != "blue":
                    return False                    
    return True
    
def moveFallingPiece( data, drow, dcol ):

    boi = False
    data.fallingPieceCol += dcol
    data.fallingPieceRow +=drow
    
    
    for row in range(len(data.fallingPiece)):
        for col in range(len(data.fallingPiece[0])):
            if fallingPieceIsLegal(Canvas, data) == False:
                boi = True
                
    if boi == True:
        data.fallingPieceCol -= dcol
        data.fallingPieceRow -= drow
        return False
        
    return True

def rotateFallingPiece(data):
    lstrot= []
    lstrot2 = []
    # step 1
    oldfallingPieceRow = data.fallingPieceRow
    oldfallingPieceCol = data.fallingPieceCol
    oldfallingPiece = data.fallingPiece
    newNumRows = len(data.fallingPiece[0])
    newNumCols = len(data.fallingPiece)
    # step 4 
    for i in range(newNumRows):
        lstrot.append([])
        for c in range(newNumCols):
            lstrot[i].append(None)
            # step 5 
    print(lstrot)
    
    for i in range(newNumCols):
        for j in range(newNumRows):
            lstrot2.append(data.fallingPiece[i][j])
    print(lstrot2)

    if (newNumRows == newNumCols) or (newNumRows == 1 and newNumCols == 4) or (newNumRows == 4 and newNumCols == 1):
        for row in range(len(lstrot)):
            for col in range(len(lstrot[0])):
                lstrot[row][col] = True
                data.fallingPiece = lstrot
                
    if (newNumRows == 3) and (newNumCols == 2):
        lstrot[0][0] = lstrot2[2]
        lstrot[0][1] = lstrot2[5]
        lstrot[1][0] = lstrot2[1]
        lstrot[1][1] = lstrot2[4]
        lstrot[2][0] = lstrot2[0]
        lstrot[2][1] = lstrot2[3]
        data.fallingPiece = lstrot
        
    if (newNumRows == 2) and (newNumCols == 3):
        lstrot[0][0] = lstrot2[1]
        lstrot[0][1] = lstrot2[3]
        lstrot[0][2] = lstrot2[5]
        lstrot[1][0] = lstrot2[0]
        lstrot[1][1] = lstrot2[2]
        lstrot[1][2] = lstrot2[4]
        data.fallingPiece = lstrot
        
        # step 6
    data.fallingPieceCol = oldfallingPieceCol + newNumRows//2 - len(oldfallingPiece)//2
    data.fallingPieceRow = oldfallingPieceRow + newNumCols//2 - len(oldfallingPiece[0])//2
        # step 7 
        
    if fallingPieceIsLegal(Canvas, data) == False:
        data.fallingPiece = oldfallingPiece
        data.fallingPieceRow = oldfallingPieceRow
        data.fallingPieceCol = oldfallingPieceCol
def placeFallingPiece(data):
    # place the pieces by using a similar method to draw falling piece but instead of drawing a cell, load the cell using fallingPieceColor. Youre making the colors corresponding to the piece part of the board
    for row in range(len(data.fallingPiece)):
        for col in range(len(data.fallingPiece[row])):
            if data.fallingPiece[row][col]:
                 data.board[data.fallingPieceRow + row][data.fallingPieceCol+ col] = data.fallingPieceColor

def removeFullRows(data):
    # keep track of the number of full rows this how we will keep score
    myRow = 0
    myBool =  False
    # copy over non full rows
    copier  = []
    # add empty color row to replace once full 
    newRow =  data.board[0].copy()
    newBoard = data.board.copy()
    # if the row isnt blue or data.empty color add my row + 1
    for row in range(len(newBoard)):
        if (data.emptyColor in newBoard[row]) == False:
            newBoard[row] = []
            myRow +=1
            
    while (myBool == False):
        while(copier in newBoard):
            newBoard.remove(copier)
        myBool = True
        
    if myRow > 0:
        for i in range(myRow):
            newBoard = [newRow] + newBoard
            
    data.score += myRow**2
    
    if myRow > 0:
        data.board = newBoard.copy()
      
####################################
# use the run function as-is
# set up functions so that it actually runs
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 700 # milliseconds
    root = Tk()
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

def playTetris(rows=15, cols=10, cellSize=20, margin=25):
    # fill in code here!
    run(250, 350)

playTetris()
