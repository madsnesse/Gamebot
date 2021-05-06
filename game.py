from othello import Othello

class Game():

    def __init__(self, game="othello", pone='X', ptwo='O'):
        if game == "othello":
            self.game = Othello(p1=pone, p2=ptwo)
        self.emojis = ['0️⃣','1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣','7️⃣', '8️⃣','9️⃣','🈹','🆖','🆒','🅾️','🅿️','🈂️','🈷️','🈯','🈹','🈁']

    def get_possible(self):
        return self.game.get_possible()

    def board_to_string(self):
        
        output = "```\n"
        pi = 0
        possible = self.get_possible()
        for row in range(len(self.game.board.grid)):
            for col in range(len(self.game.board.grid)):
                if self.game.board.get((row,col)) == None:
                    if (row,col) in possible:
                        output += self.get_emoji(pi)
                        pi += 1
                    else:
                        output+='⬜'  
                elif self.game.get_symbol(self.game.board.get((row,col))) == 'O':
                    output+='🔵'
                elif self.game.get_symbol(self.game.board.get((row,col))) == 'X':
                    output+='🔴'
            output+='\n'        
        output += str(self.game.players[self.game.currentplayer]) + "'s move"
        output += self.game.get_score()
        output += "```"
    
        
        return output
    
    def get_move(self, emoji):
        for i in range(len(self.emojis)):
            if emoji == self.emojis[i]:
                return self.get_possible()[i]

    def get_emoji(self, i):
        return self.emojis[i]

    def makemove(self, emoji):
        if emoji == '⏭️':
            if self.game.currentplayer == 1:
                self.game.currentplayer = 0
            else:
                self.game.currentplayer += 1
        else:
            move = self.get_move(emoji)
            self.game.place(move[0], move[1])

    def is_game_over(self):
        if self.game.get_possible() == 0:
            self.game.change_player()
            isOver = self.game.get_possible() == 0
            self.game.change_player()
            return isOver
    
    def get_winner(self):
        p1Score =  self.game.score[self.game.players[self.game.currentplayer]]
        self.game.change_player()
        p2Score =  self.game.score[self.game.players[self.game.currentplayer]]
        self.game.change_player()
        if p1Score > p2Score:
            return self.game.players[self.game.currentplayer]
        else:
            self.game.change_player()
            return self.game.players[self.game.currentplayer]
