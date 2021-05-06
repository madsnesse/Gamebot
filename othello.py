from board import Board
from directions import EIGHT_DIRECTIONS

class Othello():
    def __init__(self, p1=None, p2=None, players=[None,None]):
        if players == [None,None]:
            self.players = [p1,p2]
        else:
            self.players = players
        self.score = {p1:2,p2:2}
        self.currentplayer = 0
        self.board = Board(8,8)
        self.board.setPos((4,3),p1)
        self.board.setPos((3,3),p2)
        self.board.setPos((4,4),p2)
        self.board.setPos((3,4),p1)

    def place(self, row, col):
        if self.can_place(row,col):
            dictionary = dict(zip(EIGHT_DIRECTIONS, self.get_consecutive((row,col))))
            self.score[self.get_other_player()] -= sum(dictionary.values())
            self.score[self.get_current_player()] += sum(dictionary.values())+1
            for dir in dictionary:
                self.flip_in_dir((row,col),dir,dictionary[dir])
        if self.currentplayer == 1:
            self.currentplayer = 0
        else:
            self.currentplayer += 1

    def can_place(self,row,col):
        for i in self.get_consecutive((row,col)):
            if i > 0:
                return True
        return False

    def get_consecutive(self, pos):
        consec = []
        for dir in EIGHT_DIRECTIONS:
            consec.append(self.go_in_direction(pos,dir))
        return consec

    def flip_in_dir(self, pos, dir, i):
        current = (pos[0] + dir[0], pos[1] + dir[1])
        for j in range(i):
            self.board.setPos(current, self.players[self.currentplayer])
            current = (current[0] + dir[0], current[1] + dir[1])
        
        self.board.setPos(pos, self.players[self.currentplayer])

    def go_in_direction(self,pos, direction):
        current = (pos[0]+direction[0], pos[1]+direction[1])
        i = 0
        while not self.board.out_of_bounds(current) and self.board.get(current) != None and self.get_symbol(self.board.get(current)) != self.get_symbol(self.players[self.currentplayer]):
            
            if self.board.out_of_bounds(current) or self.board.get(current) == None:
                return 0
            i+=1
            current = (current[0]+direction[0], current[1]+direction[1])
        if self.board.out_of_bounds(current) or self.board.get(current) == None:
            return 0
        return i

    def get_possible(self):
        possible = []
        for row in range(len(self.board.grid)):
            for col in range(len(self.board.grid)):
                if self.board.get((row,col)) is None and self.can_place(row, col):
                    possible.append((row,col))
        return possible
    
    def get_symbol(self, player):
        if player == self.players[0]:
            return 'X'
        elif player == self.players[1]:
            return 'O'

    def get_current_player(self):
        return self.players[self.currentplayer]

    def get_other_player(self):
        return self.players[self.currentplayer-1] if self.currentplayer == 1 else self.players[1]

    def get_score(self):
        return str(self.score)

    def change_player(self):
        if self.currentplayer == 0:
            self.currentplayer = 1
        else:
            self.currentplayer = 0