import time


# mini dunder method exercise

# class Example:
#     def __init__(self, value):
#         self.value = value


#     def __str__(self):
#         return "Example object with value " + str(self.value)

    
# e = Example(42)
# print(e)

# end of dunder method exercise

# board needs to be adjusted and spaced out
# make more individual moves
# place all white pieces on the board
# learn the movement of each piece and then move on to the black pieces

class Board:
    def __init__(self):
        self.board = [["-" for _ in range(8)] for _ in range(8)]
        # place the white pawn on the board
        self.board[6][0] = "WP"

    
    def __str__(self):
        board_string = ""
        for row in self.board:
            board_string += "|".join(row) + "\n"
        return board_string


    def move_white_pawn(self, start, end):
        # start and end are tuples representing coordinates on the board
        start_x, start_y = start
        end_x, end_y = end
        
        # check if the end position is valid for a white pawn move
        if start_x - 1 == end_x and start_y == end_y:
            # move is valid, perform the move
            self.board[start_x][start_y] = "-"
            self.board[end_x][end_y] = "WP"

        else:
            return "Invalid move for WP"
        
        time.sleep(1000)
        return self.__str__()



    def move_white_rook():
        pass




# lets test it out
chess_board = Board()
print(chess_board)
print(chess_board.move_white_pawn((6, 0), (5, 0)))