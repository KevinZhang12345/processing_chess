def getClickPos():
    return mouseX, mouseY

def checkSquare(r, c, squareSize = 100):
    for i in range(8):
        for j in range(8):
            if r < (i+1) * squareSize and c < (j+1) * squareSize and r > i * squareSize and c > j * squareSize:
                return(j, i)
    print("Position is outside of the grid.")
