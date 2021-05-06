import discord
from game import Game

client = discord.Client()
TOKEN = ""
with open("token.txt", "r") as f:
    TOKEN = f.read()
CURRENT_GAME = None
BOARD_MESSAGE = None

async def update_board():
    global BOARD_MESSAGE
    global CURRENT_GAME
    
    board = CURRENT_GAME.board_to_string()
    await BOARD_MESSAGE.edit(content=board)
    await BOARD_MESSAGE.clear_reactions()
    possible = CURRENT_GAME.get_possible()
    for i in range(len(possible)):
        await BOARD_MESSAGE.add_reaction(CURRENT_GAME.get_emoji(i))
    if len(possible) == 0:
        await BOARD_MESSAGE.add_reaction('⏭️')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))




@client.event
async def on_message(message):
    global CURRENT_GAME
    global BOARD_MESSAGE
    
    if message.author == client.user:
        return
    if message.content.startswith("%newgame"):
        if BOARD_MESSAGE != None:
            BOARD_MESSAGE.delete()
        player1 = message.author.name
        m = message.mentions
        if len(m) != 1:
            return
        player2 = m[0]
        print(player1)
        print(player2)
        CURRENT_GAME = Game(game="othello",pone=player1,ptwo=player2.name)
        BOARD_MESSAGE = await message.channel.send(CURRENT_GAME.board_to_string())
        await update_board()

    # if message.content[:8] == "makemove":
        # (row,col) = message.content[8:].strip().split(" ")
        # print((row,col))
        # #CURRENT_GAME.place(int(row), int(col))
        # possible = CURRENT_GAME.get_possible()
        # board = CURRENT_GAME.board_to_string()
        # await BOARD_MESSAGE.edit(content=board)
        # await BOARD_MESSAGE.clear_reactions()
        # for i in range(len(possible)):
        #     await BOARD_MESSAGE.add_reaction(get_emoji(i))
        # await message.delete()
        
@client.event
async def on_reaction_add(reaction, user):
    global BOARD_MESSAGE
    global CURRENT_GAME
    if CURRENT_GAME.is_game_over():
        await BOARD_MESSAGE.channel.send("Game over... " + CURRENT_GAME.get_winner() + " won!")
        CURRENT_GAME = None
        BOARD_MESSAGE = None
    if CURRENT_GAME != None and BOARD_MESSAGE != None:
        message = reaction.message
        if message == BOARD_MESSAGE:
            if user == client.user:
                return
            if user.name != CURRENT_GAME.game.get_current_player():
                return
            CURRENT_GAME.makemove(reaction.emoji)
            if not CURRENT_GAME.is_game_over():
                await update_board()
            else:
                await BOARD_MESSAGE.channel.send("Game over... " + CURRENT_GAME.get_winner() + " won!")
                CURRENT_GAME = None
                BOARD_MESSAGE = None
            


client.run(TOKEN)