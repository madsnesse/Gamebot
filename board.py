class Board():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = []
        for i in range(height):
            row = []
            for j in range(width):
                row.append(None)

            self.grid.append(row)

    def setPos(self, pos, player):
        if pos[0] >= self.width or pos[0] < 0 or pos[1] >= self.height or pos[1] < 0:
            raise Exception("out of bounds")
        self.grid[pos[0]][pos[1]] = player

    
    def get(self, pos):
        return self.grid[pos[0]][pos[1]]

    def out_of_bounds(self,pos):
        return pos[0] >= self.width or pos[0] < 0 or pos[1] >= self.height or pos[1] < 0

    def __str__(self):
        output = ""
        for row in self.grid:
            for col in row:
                if col == None:
                    output += " "
                else:
                    output += col
            output += "\n"
        return output