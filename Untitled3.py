
# coding: utf-8

# In[ ]:


#Tic Tac Toe game created in python

#Import
import os
import time
import random

#Define the board
board = ["", " ", " ", " ", " ", " ", " ", " ", " ", " "]

#Welcome message to the players
print("Welcome to the Tic Tac Toe Game!")
print("Choose who is player one and player two") #choosing player 1 and 2

#Define the print_board function 
def print_board():
	print("   |   |   ")
	print(" "+board[1]+" | "+board[2]+" | "+board[3]+"  ")
	print("   |   |   ")
	print("---|---|---")
	print("   |   |   ")
	print(" "+board[4]+" | "+board[5]+" | "+board[6]+"  ")
	print("   |   |   ")
	print("---|---|---")
	print("   |   |   ")
	print(" "+board[7]+" | "+board[8]+" | "+board[9]+"  ")
	print("   |   |   ")
	
while True:
	os.system("clear")
	print_board()
	
	#Get Player X Input
	choice = input("Please choose an empty space for X. ")
	choice = int(choice)
	
	#Check to see if the space is empty first
	if board[choice] == " ":
		board[choice] = "X"
	else:
		print("Sorry, that space is not empty!")
		time.sleep(1)
		
	#Check for X win
	if (board[1] == "X" and board[2] == "X" and board[3] == "X") or 		(board[4] == "X" and board[5] == "X" and board[6] == "X") or 		(board[7] == "X" and board[8] == "X" and board[9] == "X") or 		(board[1] == "X" and board[4] == "X" and board[7] == "X") or 		(board[2] == "X" and board[5] == "X" and board[8] == "X") or 		(board[3] == "X" and board[6] == "X" and board[9] == "X") or 		(board[1] == "X" and board[5] == "X" and board[9] == "X") or 		(board[3] == "X" and board[5] == "X" and board[7] == "X"):
		os.system("clear")
		print_board()
		print("Congratulations player 1, you have won")
		break
		
	os.system("clear")
	print_board()
	
	#Check for a tie (is the board full)
	isFull = True
	if " " in board:
		isFull = False
	
	#If no one has won a message is outputted
	if isFull == True:
		print("Tie!")
		break
	
	#Get Player O Input
	choice = input("Please choose an empty space for O")
	choice = int(choice)
	
	#Check to see if the space is empty first
	if board[choice] == " ":
		board[choice] = "O"
	else:
		print("Sorry, that space is not empty!")
		time.sleep(1)
		
	#Check if player 2 wins
	if (board[1] == "O" and board[2] == "O" and board[3] == "O") or 		(board[4] == "O" and board[5] == "O" and board[6] == "O") or 		(board[7] == "O" and board[8] == "O" and board[9] == "O") or 		(board[1] == "O" and board[4] == "O" and board[7] == "O") or 		(board[2] == "O" and board[5] == "O" and board[8] == "O") or 		(board[3] == "O" and board[6] == "O" and board[9] == "O") or 		(board[1] == "O" and board[5] == "O" and board[9] == "O") or 		(board[3] == "O" and board[5] == "O" and board[7] == "O"):
		os.system("clear")
		print_board()
		print("Congratulations player 2, you have won")
		break
		
	#Check if the board is full
	isFull = True
	if " " in board:
		isFull = False
	
	#If they have tied
	if isFull == True:
		print("Tie!")#outputted the 
		break
	
	
	

