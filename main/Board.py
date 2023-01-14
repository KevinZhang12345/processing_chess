from Piece import*

class Board:
    def __init__(self):
        
        self.squares = [[None,None,None,None,None,None,None,None] for col in range(8)]
        
        self.selectedPiece = None
                        
    def addAllPieces(self, colour):
        rowPawn, rowOtherpiece = (6,7) if colour == 'white' else (1,0)
        
        for col in range(8):
            self.squares[rowPawn][col] = Pawn(colour)
        
        self.squares[rowOtherpiece][1] =  Knight(colour)
        self.squares[rowOtherpiece][6] =  Knight(colour)
        
        self.squares[rowOtherpiece][0] =  Rook(colour)
        self.squares[rowOtherpiece][7] =  Rook(colour)
        
        
        self.squares[rowOtherpiece][2] =  Bishop(colour)
        self.squares[rowOtherpiece][5] =  Bishop(colour)
        
        
        self.squares[rowOtherpiece][3] =  Queen(colour)
        
        self.squares[rowOtherpiece][4] =  King(colour)
        
    def setAllCoords(self):
        for i in range(len(self.squares)):
            for p in self.squares[i]:
                if isinstance(p, Piece):
                    p.setCoords(self)
                    
    def boardSetup(self):
        self.addAllPieces("white")
        self.addAllPieces("black")
        self.setAllCoords()
                    
    
                    
                    
