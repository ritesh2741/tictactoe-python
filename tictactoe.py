#!/usr/bin/python
import random
import pdb


winning_combination = [[0,1,2],[0,3,6],[3,4,5],[1,4,7],[6,7,8],[2,5,8],[0,4,8],[2,4,6]]
corners = [0,2,6,8]
sides = [1,3,5,7]
middle = 4

def printboard(game):
	if game == '3':
		print '',0, '|', 1, '|',2,'|',3
		print '---------------'
		print '',4, '|', 5, '|',6,'|',7
		print '---------------'
		print '',8, '|', 9, '|',10,'|',11
		print '---------------'
		print '',12,'|', 13,'|',14,'|',15
	else :
		print '',0, '|', 1, '|',2
		print '-----------'
		print '',3, '|', 4, '|',5
		print '-----------'
		print '',6, '|', 7, '|',8

def welcome_screen():
	print("\n ***************************************************************** \n")
	print(" 	              LETS PLAY TIC TAC TOE ")
	print("\n ***************************************************************** \n")
	print("\n			SELECT A GAME")
	print("\n 		    --------------------\n")
	print("			1 : User vs. Computer\n")
	print("			2 : User vs. User\n")
	print("			3 : 4 x 4 Grid \n")
	print("			4 : Exit \n")
	print("\n ***************************************************************** \n")

def initialize3x3():
	return	[' ', ' ', ' ',
			 ' ', ' ', ' ',
			 ' ', ' ', ' ']

def checkline(char, spot1, spot2, spot3):
	if board33[spot1] == char and board33[spot2] == char and board33[spot3] == char :
		return True

def checkAll(char):
	if checkline(char,0,1,2):
		return True
	if checkline(char,0,3,6):
		return True
	if checkline(char,3,4,5):
		return True
	if checkline(char,1,4,7):
		return True
	if checkline(char,6,7,8):
		return True
	if checkline(char,2,5,8):
		return True
	if checkline(char,0,4,8):
		return True
	if checkline(char,2,4,6):
		return True

def print_3x3_board(board33):
	print '',board33[0], '|', board33[1], '|',board33[2]
	print '-----------'
	print '',board33[3], '|', board33[4], '|',board33[5]
	print '-----------'
	print '',board33[6], '|', board33[7], '|',board33[8]

def clear():
	print ('\n'*50)
	print "\t\t\t =================================="
	print "	\t\t\t\tTIC TAC TOE"
	print "\t\t\t =================================\n\n\n"

def checkfordraw():
	for i in range(0,9):
		if board33[i] == ' ':
			return True

def playagain():
	again = raw_input("Do you Want to play again ? (Y/N)   ")
	if (again == 'Y' or again == 'y' or again =='yes'):
		return True
	else:
		return False

def is_space_free(index):
	"checks for free space of the board"
	return board33[index] == ' '

def choose_random_move(move_list):
	possible_winning_moves = []
	for index in move_list:
		if is_space_free(index):
			possible_winning_moves.append(index)
			if len(possible_winning_moves) != 0:
				return random.choice(possible_winning_moves)
			else:
				return None

def logic():
# Check if Computer can win
	for i in range(0,9):
		if is_space_free(i):
			board33[i]='O'
			if checkAll('O') == True:
				board33[i] = ' '
				return i
			else:
				board33[i] = ' '
# Check if player is going to win
	for i in range(0,9):
		if is_space_free(i):
			board33[i]='X'
			if checkAll('X') == True:
				board33[i] = ' '
				return i
			else:
				board33[i] = ' '

	move = choose_random_move(corners)
	if move != None:
		return move

	# If the middle is free, take it
	if board33[middle] == ' ':
		return middle;

	# else, take one free space on the sides
	return choose_random_move(sides)

def beginner_moves():
	while True:
		print_3x3_board(board33)
		ip = int(raw_input("\nSelect a spot: "))
		if board33[ip] != 'X' and board33[ip] != 'O':
			board33[ip] = 'X'

			if checkAll('X') == True:
				print_3x3_board(board33)
				print"\t\t YOU WIN ! ! ! ! !"
				if playagain() == True:
					return;
				else:
					print "\n\n\t\tTHANK YOU FOR PLAYING\n\n"
					exit()

			while True:
				while True:
					random.seed()
					pc = random.randint(0,8)
					if board33[pc] != 'O' and board33[pc] != 'X' :
						board33[pc]= 'O'
						break;
				if checkAll('O') == True:
					print_3x3_board(board33)
					print"\n \n \t\t COMPUTER WINS ! ! ! ! ! \n \n"
					if playagain() == True:
						return;
					else:
						print "\n\n\t\tTHANK YOU FOR PLAYING\n\n"
						exit()
				break;
		else:
				print '\n\n\tThis spot is already taken \n \n'

		if checkfordraw() != True:
			print_3x3_board(board33)
			print ("\n\n\tGAME DRAW\n\n")
			if playagain() == True:
				return;
			else:
				print "\n\n\t\tTHANK YOU FOR PLAYING\n\n"
				exit()

def beginner(choice):
	if choice == 'B' or choice == 'b':
		print "\n\n \tCOMPUTER GOES FIRST\n\n"
		board33 = initialize3x3()
		pc_move = choose_random_move(corners)
		board33[pc_move] = 'O'
		beginner_moves(board33)
	else:
		print "\n\n \t USER GOES FIRST\n\n"
		board33 = initialize3x3()
		beginner_moves()

def expert_moves():
	while True:
		print_3x3_board(board33)
		ip = int(raw_input("\nSelect a spot: "))
		if board33[ip] != 'X' and board33[ip] != 'O':
			board33[ip] = 'X'

			if checkAll('X') == True:
				print_3x3_board(board33)
				print"\t\t YOU WIN ! ! ! !\n\n"
				return;

			while True:
				pc = logic()
				if board33[pc] != 'O' and board33[pc] != 'X' :
					board33[pc]= 'O'
					if checkAll('O') == True:
						print_3x3_board(board33)
						print"\n \n \t\t COMPUTER WINS ! ! ! ! ! \n \n"
						if playagain():
							return;
						else:
							print "\n\n\t\tTHANK YOU FOR PLAYING\n\n"
							exit()
				break;
		else:
			print '\n\n\t\n\n\tThis spot is already taken \n \n'
		if checkfordraw() != True:
			print_3x3_board(board33)
			print ("\n\n\tGAME DRAW\n\n")
			if playagain() == True:
				return;
			else:
				print "\n\n\t\tTHANK YOU FOR PLAYING\n\n"
				exit()

def expert(choice):
	initialize3x3()
	if choice == 'B' or choice == 'b':
		print "\n\n \tCOMPUTER GOES FIRST\n\n"
		pc_move = choose_random_move(corners)
		board33[pc_move] = 'O'
		expert_moves()
	else:
		print "\n\n \tUSER GOES FIRST\n\n"
		expert_moves()

def uservspc():
	printboard('1')
	board33 = initialize3x3()
	while True:
		clear()
		print "\t\t\t\tUser vs. Computer \n "
		print "\t\t\t\tDifficulty Level \n"
		print ("\n 1: Beginner \n")
		print (" 2: Expert \n")
		game = raw_input(' Please Select Difficulty Level:  ')
		clear()
		printboard('1')
		print ("\t\t Who goes First ?")
		print ("\n\n\t A. User ")
		print ("\n\tB. Computer")
		choice = raw_input("\t\t Please Enter Your Choice(A/B) ?   ")
		if game == '1' :
			if choice == 'A' or choice == 'a' or choice == 'B' or choice == 'b' :
				beginner(choice)
			else :
				print ("Invalid Choice")
		elif game == '2' :
			if choice == 'A' or choice == 'a' or choice == 'B' or choice == 'b' :
				expert(choice)
			else :
				print ("Invalid Choice")
		else :
			clear()
			print (" Invalid Choice.")

def uservsuser():
	printboard('2')
	while True:
		print "\n\nPlayer 1 Turn\n\n"
		print_3x3_board(board33)
		ip = int(raw_input("\nSelect a spot: "))
		if board33[ip] != 'X' and board33[ip] != 'O':
			board33[ip] = 'X'
			if checkAll('X') == True:
				print_3x3_board(board33)
				print"\t\t 1st Player Wins ! ! ! ! !"
				if playagain() == True:
					return;
				else:
					print "\n\n\t\tTHANK YOU FOR PLAYING\n\n"
					exit()
			else:
				while True:
					print_3x3_board(board33)
					print "\n\nPlayer 2 Turn\n\n"
					print_3x3_board(board33)
					ip2 = int(raw_input("\nSelect a spot: "))
					if board33[ip2] != 'X' and board33[ip2] != 'O':
						board33[ip2] = 'O'
						if checkAll('O') == True:
							print_3x3_board(board33)
							print"\t\t 2nd Player Wins ! ! ! ! !"
							if playagain() == True:
								return;
							else:
								print "\n\n\t\tTHANK YOU FOR PLAYING\n\n"
								exit()
						break;
					else:
						print '\n\n\tThis spot is already taken \n \n'

		else:
			print '\n\n\tThis spot is already taken \n \n'

		if checkfordraw() != True:
			print_3x3_board(board33)
			print ("\n\n\tGAME DRAW\n\n")
			if playagain() == True:
				return;
			else:
				print "\n\n\t\tTHANK YOU FOR PLAYING\n\n"
				exit()


# 4 x 4  TIC TAC TOE

winning_combination4x4=[[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15],[0,4,8,12],[1,5,9,13],[2,6,10,14],[3,7,11,
15],[0,5,10,15],[3,6,9,12]]
corners4x4 = [0,3,12,15]
sides4x4 = [1,2,4,7,8,11,13,14]
middle4x4 = [5,6,9,10]

def initialize4x4():
	return	[' ', ' ', ' ', ' ',
			 ' ', ' ', ' ', ' ',
			 ' ', ' ', ' ', ' ',
		 	' ', ' ', ' ', ' ']

def print_4x4_board(board44):
	print '',board44[0], '|', board44[1], '|',board44[2],'|',board44[3]
	print '---------------'
	print '',board44[4], '|', board44[5], '|',board44[6],'|',board44[7]
	print '---------------'
	print '',board44[8], '|', board44[9], '|',board44[10],'|',board44[11]
	print '---------------'
	print '',board44[12],'|', board44[13],'|',board44[14],'|',board44[15]

def checkline4x4(char,spot1,spot2,spot3,spot4):
	if board44[spot1] == char and board44[spot2] == char and board44[spot3] == char and board44[spot4] == char:
			return True

def checkAll4x4(char):
	if checkline4x4(char,0,1,2,3):
		return True
	if checkline4x4(char,4,5,6,7):
		return True
	if checkline4x4(char,8,9,10,11):
		return True
	if checkline4x4(char,0,5,10,15):
		return True
	if checkline4x4(char,0,4,8,12):
		return True
	if checkline4x4(char,1,5,9,13):
		return True
	if checkline4x4(char,2,6,10,14):
		return True
	if checkline4x4(char,3,7,11,15):
		return True
	if checkline4x4(char,0,5,10,15):
		return True
	if checkline4x4(char,3,6,9,12):
		return True

def checkfordraw4x4():
	for i in range(0,16):
		if board44[i] == ' ':
			return True

def is_space_free4x4(index):
	"checks for free space of the board"
	# print "SPACE %s is taken" % index
	return board44[index] == ' '

def choose_random_move4x4(move_list):
	possible_winning_moves = []
	for index in move_list:
		if is_space_free4x4(index):
			possible_winning_moves.append(index)
			if len(possible_winning_moves) != 0:
				return random.choice(possible_winning_moves)
			else:
				return None

def logic4x4():
# Check if Computer can win
	for i in range(0,16):
		if is_space_free4x4(i):
			board44[i]='O'
			if checkAll4x4('O') == True:
				board44[i] = ' '
				return i
			else:
				board44[i] = ' '

# Check if player is going to win
	for i in range(0,16):
		if is_space_free4x4(i):
			board44[i]='X'
			if checkAll4x4('X') == True:
				board44[i] = ' '
				return i
			else:
				board44[i] = ' '

	move = choose_random_move4x4(corners4x4)
	if move != None:
		return move
	else:
		move = choose_random_move4x4(middle4x4)
		if move != None:
			return move
	# else, take one free space on the sides
	return choose_random_move4x4(sides4x4)

def fourxfour():
	clear()
	printboard('3')
	while True:
		print ('\n\n')
		print_4x4_board(board44)
		ip = int(raw_input("\nSelect a spot: "))
		if board44[ip] != 'X' and board44[ip] != 'O':
			board44[ip] = 'X'

			if checkAll4x4('X') == True:
				print_4x4_board(board44)
				print"\t\t YOU WIN ! ! ! ! !"
				return;

			while True:
				pc = logic4x4()
				if board44[pc] != 'O' and board44[pc] != 'X' :
					board44[pc]= 'O'
					if checkAll4x4('O') == True:
						print_4x4_board(board44)
						print"\n \n \t\t COMPUTER WINS ! ! ! ! ! \n \n"
						if playagain():
							return;
						else:
							print "\n\n\t\tTHANK YOU FOR PLAYING\n\n"
							exit()
				break;
		else:
			print '\n\n\t\n\n\tThis spot is already taken \n \n'
		if checkfordraw4x4() != True:
			print_4x4_board(board44)
			print ("\n\n\tGAME DRAW\n\n")
			if playagain() == True:
				return;
			else:
				print "\n\n\t\tTHANK YOU FOR PLAYING\n\n"
				exit()

while True:
	welcome_screen()
	option = raw_input('Please Enter the Game You want to play:  ')
	if option == '1':
		board33 = initialize3x3()
		uservspc()
	elif option == '2':
		board33 = initialize3x3()
		uservsuser()
	elif option == '3':
		board44 = initialize4x4()
		fourxfour()
	elif option == '4':
		print(" Thank You for Trying the game. Come back Soon ! ! ")
		exit()
	else:
		print( "\n\n Invalid Option Please Try again \n\n")

