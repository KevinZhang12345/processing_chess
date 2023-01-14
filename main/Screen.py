from GAME_CONSTANTS import*

from Piece import*


class render():
    def __init__(self):
        pass
        
    def displayBackground(self):
        background(39,37,34)
        
class renderGameSrcreen(render):
    def displayText(self):
        aLpha = "abcdefgh"
        for col, label in enumerate(aLpha):
            if col % 2 != 0:
                fill(234,235,200)
            else:
                fill(119,154,88)
            textSize(Height* 30/800)
            text(8 - (col), 0,col*squareSize + squareSize /4)
            if col % 2 != 0:
                fill(119,154,88)
            else:
                fill(234,235,200)
            text(label, col*squareSize + squareSize/1.3, Height-7)
    
    def displayBoard(self):
        fill(68,64,62)
        for row in range(ROWS):
            for col in range(COLS):
                if (row + col) % 2 == 0:
                    fill(234,235,200)
                else:
                    fill(119,154,88)
                noStroke()
                rect(col * squareSize, row*squareSize,squareSize,squareSize, 
                     15 if col == 0 and row == 0  else 0,15 if col == 7 and row == 0  else 0,
                     15 if col == 7 and row == 7  else 0,15 if col == 0 and row == 7  else 0)
                
    def displayPieces(self, board, pieceImages, pieceNames):
        imageMode(CENTER)
        for row in range(ROWS):
            for col in range(COLS):
                loadedPiece = board.squares[row][col]
                if isinstance(loadedPiece, Piece):
                    name = loadedPiece.name
                    x = col * squareSize + squareSize//2
                    y = row*squareSize + squareSize//2
                    if loadedPiece.colour == "black":
                        image(pieceImages[0][pieceNames.index(name)],x,y)
                    else:
                        image(pieceImages[1][pieceNames.index(name)],x,y)
