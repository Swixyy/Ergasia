import random
import time


# chess board is 8x8
chess_board = [
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
]

blackQueen = 'BQ'
whiteBishop = 'WB'
whiteRook = 'WR'

# black queen -> forward, backward, 
# white rook and white bishop
player1 = 0
player2 = 0

def less_row_less_column(row,column):
    tempList = []
    while row>0 and column>0:
        row -=1
        column -=1
        tempList.append([row,column])
    return tempList

def less_row_more_column(row,column):
    tempList = []
    while row>0 and column>0:
        row -=1
        column +=1
        tempList.append([row,column])
    return tempList
def more_row_less_column(row,column):
    tempList = []
    while row>0 and column>0:
        row +=1
        column -=1
        tempList.append([row,column])
    return tempList
def more_row_more_column(row,column):
    tempList = []
    while row<7 and column<7:
        row +=1
        column +=1
        tempList.append([row,column])
    return tempList

def diagonal_movement(row,column):
    moves = []
    if row == 0 and column == 0:
        for i in range(1,8):
            moves.append([row,i])
    else:
        moves11 = [moves.append([row-i,column+i]) if column+i <8 and row-i>=0 else None  for i in range(1,row+1)]
        moves22 = [moves.append([row+i,column+i]) if column+i <8 and row+i<8 else None for i in range(1,8-row)]
        moves33 = [moves.append([row+i,column-i]) if column-i >=0 and row+i<8 else None for i in range(1,8-row)]
        moves44 = [moves.append([row-i,column-i]) if column-i >= 0 and row-i>=0 else None for i in range(1,row+1)]
    return moves



def forward_movement(row,column):
    # gia paradeigma ean
    moves = []
    moves11 = [moves.append([row+i,column]) if row+i<8 else None for i in range(1,8-row)]
    moves22 = [moves.append([row-i,column]) if row-i>=0 else None for i in range(1,row+1)]
    moves33 = [moves.append([row,column+i]) if column+i <8 else None for i in range(1,8-column)]
    moves44 = [moves.append([row,column-i]) if column-i >=0 else None for i in range(1,column+1)]
    #print(moves)
    return moves


def placeRandom(board,piece):
    while True:
        pieceRow = random.randint(0,7)
        pieceColumn = random.randint(0,7)
        if(board[pieceRow][pieceColumn] == 0):
            board[pieceRow][pieceColumn] = piece
            break
    return board

def place_pieces(board):
    boardQ = placeRandom(board,blackQueen)
    boardQ = placeRandom(boardQ,whiteBishop)
    boardQ = placeRandom(boardQ,whiteRook)
    #print(boardQ.index(blackQueen))
    #print(boardQ)
    return boardQ

#place_pieces(chess_board)
#diagonal_movement()
#forward_movement(0,0);     


def get_piece_coordinates(board,piece):
    for rowIndex,row in enumerate(board):
        for columnIndex,column in enumerate(row):
            if(column == piece):
                return [rowIndex,columnIndex]
    return []

def unique(list1):
    unique_list = []
    for x in list1:
        if x not in unique_list:
            unique_list.append(x)
    return unique_list

def play_game():
    player1Move = True # has only the queen
    player2Move = False # has bishop and rook
    player1Points = 0
    player2Points = 0
    global player1
    global player2
    player1Status = {blackQueen:'A'}
    player2Status = {whiteBishop:'A',whiteRook:'A'}
    # random place the pieces on the board
    board = place_pieces(chess_board)
    while True:
        if(player1Move):
            player1Move = False
            # player1 has only a queen
            if(player1Status[blackQueen] != 'A'):
                break
            # check if in my diagonal i can kill a bishop or a rook, if i cannot just make a random move!
            else:
                # check ama exw kapoio pioni sta diagonal h sto forward!!!
                if(player2Status[whiteBishop] != 'A' and player2Status[whiteRook] != 'A'):
                    # einai dead ara kane break!!!
                    break
                queen_coordinates = get_piece_coordinates(board,blackQueen)
               
                all_queen_moves = unique(list(forward_movement(queen_coordinates[0],queen_coordinates[1]) + diagonal_movement(queen_coordinates[0],queen_coordinates[1])))
                try:
                    all_queen_moves.remove(queen_coordinates)
                except:
                    pass
                if(player2Status[whiteBishop] == 'A'):
                    whiteBishopCoordinates = get_piece_coordinates(board,whiteBishop)
                    if(whiteBishopCoordinates in all_queen_moves):
                        # replace the 
                        board[whiteBishopCoordinates[0]][whiteBishopCoordinates[1]] = blackQueen
                        board[queen_coordinates[0]][queen_coordinates[1]] = 0
                        player2Status[whiteBishop] = 'D'
                        player1 = player1 + 1
                        continue
                if(player2Status[whiteRook] == 'A'):
                    whiteRookCoordinates = get_piece_coordinates(board,whiteRook)
                    if(whiteRookCoordinates in all_queen_moves):
                        # replace the 
                        board[whiteRookCoordinates[0]][whiteRookCoordinates[1]] = blackQueen
                        board[queen_coordinates[0]][queen_coordinates[1]] = 0
                        player2Status[whiteRook] = 'D'
                        player1 = player1 + 1
                        continue
                # play a move
                # random choose a value from the queen moves and play it!!
                newMoveIndex = random.randint(0,len(all_queen_moves)-1)
                newMove = all_queen_moves[newMoveIndex]
                board[newMove[0]][newMove[1]] = blackQueen
                board[queen_coordinates[0]][queen_coordinates[1]] = 0
        else:
            player1Move = True
            if(player1Status[blackQueen] !='A'):
                break
            # check white rook
            blackQueenCoordinates = get_piece_coordinates(board,blackQueen)
            whiteBishopCord = get_piece_coordinates(board,whiteBishop)
            whiteRookCord = get_piece_coordinates(board,whiteRook)
            if(player2Status[whiteBishop] == 'A'):
                # check if we have the black queen in the square
                whiteBishopMoves = unique(diagonal_movement(whiteBishopCord[0],whiteBishopCord[1]))
                if(blackQueenCoordinates in whiteBishopMoves):
                    board[blackQueenCoordinates[0]][blackQueenCoordinates[1]] = whiteBishop
                    board[whiteBishopCord[0]][whiteBishopCord[1]] = 0
                    player2 = player2 + 1
                    break
            if(player2Status[whiteRook] == 'A'):
                # check if we have the black queen in the square
                whiteRookMoves = unique(forward_movement(whiteRookCord[0],whiteRookCord[1]))
                if(blackQueenCoordinates in whiteRookMoves):
                    board[blackQueenCoordinates[0]][blackQueenCoordinates[1]] = whiteRook
                    board[whiteRookCord[0]][whiteRookCord[1]] = 0
                    player2 = player2 + 1 
                    break
            # alliws diale3e tyxaia to rook h to bishop kai pai3e
            if(player2Status[whiteBishop] == 'A' and player2Status[whiteRook] == 'A'):
                randomPiece = random.randint(0,1)
                if(randomPiece == 0):
                    whiteBishopMoves = unique(diagonal_movement(whiteBishopCord[0],whiteBishopCord[1]))
                    randomBishopIndex = random.randint(0,len(whiteBishopMoves) -1)
                    randomBishopMove = whiteBishopMoves[randomBishopIndex]
                    board[randomBishopMove[0]][randomBishopMove[1]] = whiteBishop
                    board[whiteBishopCord[0]][whiteBishopCord[1]] = 0
                    continue
                else:
                    whiteRookMoves = unique(forward_movement(whiteRookCord[0],whiteRookCord[1]))
                    randomRookIndex = random.randint(0,len(whiteRookMoves) -1)
                    randomRookMove = whiteRookMoves[randomRookIndex]
                    board[randomRookMove[0]][randomRookMove[1]] = whiteRook
                    board[whiteRookCord[0]][whiteRookCord[1]] = 0
                    continue
            elif(player2Status[whiteBishop] == 'A'):
                    whiteBishopMoves = unique(diagonal_movement(whiteBishopCord[0],whiteBishopCord[1]))
                    randomBishopIndex = random.randint(0,len(whiteBishopMoves) -1)
                    randomBishopMove = whiteBishopMoves[randomBishopIndex]
                    board[randomBishopMove[0]][randomBishopMove[1]] = whiteBishop
                    board[whiteBishopCord[0]][whiteBishopCord[1]] = 0
                    continue
            elif(player2Status[whiteRook] == 'A'):
                    whiteRookMoves = unique(forward_movement(whiteRookCord[0],whiteRookCord[1]))
                    randomRookIndex = random.randint(0,len(whiteRookMoves) -1)
                    randomRookMove = whiteRookMoves[randomRookIndex]
                    board[randomRookMove[0]][randomRookMove[1]] = whiteRook
                    board[whiteRookCord[0]][whiteRookCord[1]] = 0
                    continue
            else:
                break



for i in range(0,100):
    print("Game ",i+1)
    play_game()
    print("Player 1 points:",player1)
    print("Player 2 points:",player2)
    print("End of game")
