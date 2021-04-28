from random import *
from time import *


class TicTacToe:
    def __init__(self):
        print("Welcome to the Game of TIC-TAC-TOE")
        print("Do you want to: ")
        print("1: play against Computer")
        print("2: play against Another Player")
        print("3: Quit")
        TicTacToe.choice = input("Type 1, 2, or 3: ")
        while TicTacToe.choice not in ['1', '2', '3']:
            TicTacToe.choice = input("Please type 1,2 or 3 as your Choice: ")
        if TicTacToe.choice == "1":
            print("You are playing against a robot. Good Luck!")
            TicTacToe.GameType = "S"
        elif TicTacToe.choice == "2":
            print("You can play against your new enemy!")
            TicTacToe.GameType = "M"
        else:
            print("Are you chickening out?")
            TicTacToe.GameType = ""
            return

        Board()
        TicTacToe.letter = choice(['X', 'O'])
        TicTacToe.Round()

        if TicTacToe.GameWon == True:
            print(TicTacToe.WinningType, "Wins!")
        else:
            print("Draw!")

        playAgain = input("Do you want to play again? Yes or No: ")
        if playAgain in ['Yes', 'y', 'Y', 'yes']:
            TicTacToe()

    def Round():
        TicTacToe.GameWon = False
        while not TicTacToe.GameWon:
            TicTacToe.Move()
            TicTacToe.CheckWin()
            TicTacToe.ChangeType()

            if TicTacToe.GameType == "S" and TicTacToe.GameWon == False:
                print(TicTacToe.letter + "'s Go...")
                sleep(1)
                Player.GetPlayerChoice()
                TicTacToe.CheckWin()
                TicTacToe.ChangeType()

    def Move():
        TicTacToe.VerifyPosition()
        Board.drawBoard()

    def ChangeType():
        if TicTacToe.letter == 'X':
            TicTacToe.letter = 'O'
        else:
            TicTacToe.letter = 'X'

    def VerifyPosition():
        Valid = False
        print(TicTacToe.letter + "'s Go...")
        while not Valid:
            Position = input("Please type where you wish to place: ")
            while Position.isdigit() == False or int(Position) > 9 or int(Position) <= 0:
                Position = input("Please type a valid integer between 1 and 9: ")
            TicTacToe.Position = int(Position)
            if Board.cells[TicTacToe.Position - 1] == 'X' or Board.cells[TicTacToe.Position - 1] == 'O':
                Valid = False
                print("That is an invalid square, please try again ")
            else:
                Valid = True
        Board.cells[TicTacToe.Position - 1] = TicTacToe.letter

    def CheckWin():
        if ((Board.cells[0] == TicTacToe.letter) and (Board.cells[1] == TicTacToe.letter) and (
                Board.cells[2] == TicTacToe.letter)) or (
                (Board.cells[3] == TicTacToe.letter) and (Board.cells[4] == TicTacToe.letter) and (
                Board.cells[5] == TicTacToe.letter)) or (
                (Board.cells[6] == TicTacToe.letter) and (Board.cells[7] == TicTacToe.letter) and (
                Board.cells[8] == TicTacToe.letter)) or (
                # Row Check^^^^^^^
                (Board.cells[0] == TicTacToe.letter) and (Board.cells[3] == TicTacToe.letter) and (
                Board.cells[6] == TicTacToe.letter)) or (
                (Board.cells[1] == TicTacToe.letter) and (Board.cells[4] == TicTacToe.letter) and (
                Board.cells[7] == TicTacToe.letter)) or (
                (Board.cells[2] == TicTacToe.letter) and (Board.cells[5] == TicTacToe.letter) and (
                Board.cells[8] == TicTacToe.letter)) or (
                # Column Check^^^^
                (Board.cells[0] == TicTacToe.letter) and (Board.cells[4] == TicTacToe.letter) and (
                Board.cells[8] == TicTacToe.letter)) or (
                (Board.cells[2] == TicTacToe.letter) and (Board.cells[4] == TicTacToe.letter) and (
                Board.cells[6] == TicTacToe.letter)):
            # Diagonal Check^^
            TicTacToe.WinningType = TicTacToe.letter
            TicTacToe.GameWon = True
        if TicTacToe.GameWon != True:  # if no one wins (potentially on the last go...)
            DrawCheck = 0
            for i in range(0, 9):  # checks the number of spaces left in the board out of 9 squares, 0-8
                if Board.cells[i] == ' ':
                    DrawCheck = DrawCheck + 1
            if DrawCheck == 0:  # if there are no squares...
                TicTacToe.GameWon = 'Draw'


class Player:
    def GetPlayerChoice():
        Player.FindEmptySpaces()
        Player.PlayerMove()
        Board.drawBoard()  #

    def FindEmptySpaces():
        Player.EmptySpaces = []
        for i in range(0, 9):  #
            if Board.cells[i] == ' ':  #
                Player.EmptySpaces.append(i)  #

    def PlayerMove():
        Player.Change = False
        OriginalType = TicTacToe.letter  #
        for j in range(0, 2):  #
            for i in range(0, len(Player.EmptySpaces)):  #
                if not Player.Change:  #
                    Player.CheckPlayerWin((Player.EmptySpaces[i]))  #
                if Player.Change:  # If there is a change...
                    Board.cells[Player.EmptySpaces[i]] = OriginalType  #
                    TicTacToe.letter = OriginalType
                    return
            TicTacToe.ChangeType()  #
        TicTacToe.letter = OriginalType
        Board.cells[choice(Player.EmptySpaces)] = OriginalType  #

    def CheckPlayerWin(SpaceToCheck):
        if (SpaceToCheck in [6, 3, 0] and Board.cells[SpaceToCheck + 1] == TicTacToe.letter and Board.cells[
            SpaceToCheck + 2] == TicTacToe.letter) or (  #
                SpaceToCheck in [7, 4, 1] and Board.cells[SpaceToCheck + 1] == TicTacToe.letter and Board.cells[
            SpaceToCheck - 1] == TicTacToe.letter) or (  #
                SpaceToCheck in [8, 5, 2] and Board.cells[SpaceToCheck - 1] == TicTacToe.letter and Board.cells[
            SpaceToCheck - 2] == TicTacToe.letter) or (  #
                SpaceToCheck in [6, 7, 8] and Board.cells[SpaceToCheck - 3] == TicTacToe.letter and Board.cells[
            SpaceToCheck - 6] == TicTacToe.letter) or (  #
                SpaceToCheck in [5, 4, 3] and Board.cells[SpaceToCheck - 3] == TicTacToe.letter and Board.cells[
            SpaceToCheck + 3] == TicTacToe.letter) or (  #
                SpaceToCheck in [2, 1, 0] and Board.cells[SpaceToCheck + 3] == TicTacToe.letter and Board.cells[
            SpaceToCheck + 6] == TicTacToe.letter) or (  #
                SpaceToCheck == 0 and Board.cells[SpaceToCheck + 4] == TicTacToe.letter and Board.cells[
            SpaceToCheck + 8] == TicTacToe.letter) or (  #
                SpaceToCheck == 2 and Board.cells[SpaceToCheck + 2] == TicTacToe.letter and Board.cells[
            SpaceToCheck + 4] == TicTacToe.letter) or (  #
                SpaceToCheck == 6 and Board.cells[SpaceToCheck - 2] == TicTacToe.letter and Board.cells[
            SpaceToCheck - 4] == TicTacToe.letter) or (  #
                SpaceToCheck == 8 and Board.cells[SpaceToCheck - 4] == TicTacToe.letter and Board.cells[
            SpaceToCheck - 8] == TicTacToe.letter) or (  #
                SpaceToCheck == 4 and ((Board.cells[SpaceToCheck + 2] == TicTacToe.letter and Board.cells[
            SpaceToCheck - 2] == TicTacToe.letter) or (  #
                                               Board.cells[SpaceToCheck + 4] == TicTacToe.letter and Board.cells[
                                           SpaceToCheck - 4] == TicTacToe.letter))):  #
            Player.Change = True


class Board:
    def __init__(self):
        Board.cells = [' ', ' ', ' ',
                       ' ', ' ', ' ',
                       ' ', ' ', ' ']
        Board.drawBoard()

    def drawBoard():
        print('   |   |')
        print(' ' + Board.cells[6] + ' | ' + Board.cells[7] + ' | ' + Board.cells[8])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + Board.cells[3] + ' | ' + Board.cells[4] + ' | ' + Board.cells[5])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + Board.cells[0] + ' | ' + Board.cells[1] + ' | ' + Board.cells[2])
        print('   |   |')


TicTacToe()
