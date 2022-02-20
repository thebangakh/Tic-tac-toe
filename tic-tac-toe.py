game = [[2, 2, 2],
		[0, 2, 1],
		[2, 1, 2],]

	
def win(current_game):
	#horizontally	
	for row in game:
		print(row)
		if row.count(row[0]) == len(row) and row[0] != 0:
			print(f"Player {row[0]} is the winner Horizontally!!!")			


# diagonally	
	diags = []
	for col, row in enumerate(reversed(range(len(game)))):
		diags.append(game[col][row])
	if diags.count(diags[0]) == len(diags) and diags[0] != 0:
			print(f"Player {diags[0]} is the Winner Diagonally")

	diags = []
	for ix in range (len(game)):
		diags.append(game[ix][ix])
	if diags.count(diags[0]) == len(diags) and diags[0] != 0:
			print(f"Player {diags[0]} is the Winner Diagonally")

	#vertically		
	for col in range(len(game)):
		check = []
		for row in game:
			check.append(row[col])
		if check.count(check[0]) == len(check) and check[0] != 0:
			print(f"Player {check[0]} is the Winner Vertically")

def game_board(game_map, player=0, row=0, column=0, just_display=False):
	try:
		print('   0  1  2')
		if not just_display:
			game_map[row][column] = player
		for count, row in enumerate(game):    #enumerate is grabing an index number i.e. 0 plus the index value which is the whole row
			print(count, row)
		return game_map	
	except IndexError as e:
		print("Something went wrong!!!", e)	

	except Exception as e:
		print('Something went very wrong' )	

play = True
players = [1, 2]
while play:
	game = [[0, 0, 0],
			[0, 0, 0],
			[0, 0, 0]]  
	game_won = False
	while not game_won:	
		current_player = 1
		column_choice = int(input("What column do you want to play? (0,1,2)"))
		row_choice = int(input("What row do you want to play? (0,1,2)"))
		game = game_board(game, current_player, row_choice, column_choice)

# game = game_board(game, just_display=True)
# game = game_board(game_board, player=1, row=3, column=1) 