#A Tic-Tac-Toe Game!

game = [[0, 0, 0],
 		[0, 0, 0],
 		[0, 0, 0],]

def game_board(player=0, row=0, column=0):
	print("   a  b  c")
	game[row][column] = player
	for count, row in enumerate(game):
		print(count, row)
#Now you've got a function!

game_board(player=1, row=2, column=1)
#game[0][1] = 1
#game_board(1, 2, 0)

'''
def addition (x,y):
	return x+y
z = addition("5","3")
print(z)
'''