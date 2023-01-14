from Board import*
        
        
class Piece(object):

    def __init__(self, name, colour, hasMoved = False, x = None, y = None):
        self.name = name
        self.colour = colour
        self.x = x
        self.y = y
        self.hasMoved = hasMoved
        
        #self.selectedPieceCoods = False
        
    def setCoords(self, board):
        for row, lists in enumerate(board.squares):
            for col, element in enumerate(lists):
                if element != None and element is self:
                    self.x = row
                    self.y = col
    
class Pawn(Piece):
    def __init__(self, colour):
        super(Pawn, self).__init__('pawn', colour)
        
    def possibleMoves(self, board):
        moveList = []
        moves = []
        
        if self.colour == "white":
            moves.append((-1,0))
            
            if not self.hasMoved:
                moves.append((-2,0))
                
        if self.colour == "black":
            moves.append((1,0))
            
            if not self.hasMoved:
                moves.append((2, 0))
                    
        for move in moves:
            newPosition = (self.x + move[0], self.y + move[1])
            if newPosition[1] < 8 and newPosition[1] >= 0:
                moveList.append(newPosition)
        return moveList
    
    def getMoves(self, board):
        moveList = []
        
        for destination in self.possibleMoves(board):
            if board.squares[destination[0]][destination[1]] != None:
                break
            else:
                moveList.append(destination)

        if self.colour == 'white':
            if self.x - 1 >=0 and self.y + 1 < 8:
                destination = board.squares[self.x-1][self.y+1]
                if destination != None:
                    if destination.colour != self.colour:
                        moveList.append((self.x-1, self.y+1))
                        
            if self.x - 1 >= 0 and self.y - 1>=0:
                destination = board.squares[self.x-1][self.y-1]
                if destination != None:
                    if destination.colour != self.colour:
                        moveList.append((self.x-1, self.y-1))
                        
        if self.colour == 'black':
            if self.x + 1 < 8 and self.y + 1 < 8:
                destination = board.squares[self.x+1][self.y+1]
                if destination != None:
                    if destination.colour != self.colour:
                        moveList.append((self.x+1, self.y+1))
                        
            if self.x + 1 < 8 and self.y - 1>=0:
                destination = board.squares[self.x+1][self.y-1]
                if destination != None:
                    if destination.colour != self.colour:
                        moveList.append((self.x+1, self.y-1))
                        
        return moveList
                
    

class Knight(Piece):
     def __init__(self, colour):
        super(Knight, self).__init__('knight', colour)
        
class Bishop(Piece):
     
     def __init__(self, colour):
        super(Bishop, self).__init__('bishop', colour)
        
class Rook(Piece):
    def __init__(self, colour):
        super(Rook, self).__init__('rook', colour)
        
class Queen(Piece):
    
    def __init__(self, colour):
        super(Queen, self).__init__('queen', colour)
        
class King(Piece):
    def __init__(self, colour):
        super(King, self).__init__('king', colour)
        self.inCheck = False
        self.firstMove = True
