#importing Constants
from GAME_CONSTANTS import*

#importing Classes
from Board import*
from Piece import*
from Screen import*


#importing functions
from chessSetup import*
from mouseFunctions import*

pieceNames = ["pawn","knight","bishop","rook","queen","king"]

b = Board()

game = renderGameSrcreen()


def setup():  
     
    global pieceImages
    
    size(Width,Height)
    background(39,37,34)
    
    b.boardSetup()
    pieceImages = pieceSetup()
    print(b.squares[6][0].possibleMoves(b))

    b.squares[6][0].move(b, (5,0))
    print(b.squares[5][0].possibleMoves(b))
    b.squares[5][0].move(b, (4,0))

def draw():
    game.displayBoard() 
    game.displayText()
    game.displayPieces(b, pieceImages, pieceNames)
    
def mousePressed():
    pass
        
def mouseDragged():
    pass
    
def mouseReleased():
    mx = getClickPos()[0]
    my = getClickPos()[1]
    
    if b.selectedPiece == None:
        b.selectedPiece = b.squares[checkSquare(mx, my)[0]] [checkSquare(mx, my)[1]]
    else:
        b.selectedPiece.move(b, checkSquare(mx, my))
        b.selectedPiece = None
    
