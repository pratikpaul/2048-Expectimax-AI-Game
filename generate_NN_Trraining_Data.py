import torch as tr
import numpy as np
import pickle as pk
import math
from board import Board
from ai_expectimax import AI_expectimax
from random import randint, seed


# Class to train data
class NN_train_data:
    def __init__(self, boardsize, targetScore):
        self.board_size = boardsize
        self.board = Board(self.board_size)
        self.ai = AI_expectimax()
        self.inputs = []
        self.outputs = []
        self.target_score = targetScore

        self.init_game()

    def encode(self):
        print(self.board.grid)
        return tr.from_numpy(self.board.grid.copy()).float()
    
    def getUtility(self):
        utility = 0
        empty_count = 0

        # Sum non 0 tile values, times factor
        # factor = log2(tile)
        # Count num of zero tiles
        for i in range(self.board.grid.shape[0]):
            for j in range(self.board.grid.shape[1]):
                if self.board.grid[i][j] != 0:
                    utility += self.board.grid[i][j] * math.log(self.board.grid[i][j], 2)
                else:
                    empty_count += 1

        # More zero tiles = higher utility
        utility += empty_count * 5

        return utility
    
    def init_game(self):
        self.insert_random_tile()
        self.insert_random_tile()

    def insert_random_tile(self):
        if randint(0,99) < 100 * 0.9:
            value = 2
        else:
            value = 4

        cells = self.board.get_available_cells()
        pos = cells[randint(0, len(cells) - 1)] if cells else None

        if pos is None:
            return None
        else:
            self.board.insert_tile(pos, value)
            return pos

    def run_game(self):
        while True:
            print(self.board.grid)
            move = self.ai.get_move(self.board)
            print("AI's Turn:", end="")
            self.board.move(move)
            #print_board()
            #print("Computer's Turn")
            self.insert_random_tile()
            self.print_board()
            self.inputs.append(self.encode())
            self.outputs.append(tr.tensor([self.getUtility()]))
            
            if(self.board.get_max_tile() >= self.target_score):
                print("You Win.. You have reached the target score of " + str(self.target_score))
                print("Your final score is : " + str(int(self.board.score)))
                break
            
            if len(self.board.get_available_moves()) == 0:
                print("GAME OVER (max tile): " + str(self.board.get_max_tile()) + " Total score : " + str(int(self.board.score)))
                break
        self.inputs = tr.stack(self.inputs)
        self.outputs = tr.stack(self.outputs)

    def print_board(self):
        print("Score: " + str(int(self.board.score)))
        for i in range(self.board_size):
            for j in range(self.board_size):
                print("%6d  " % self.board.grid[i][j], end="")
            print("")
        print("")

# #3
# Generate training data file
# Call get_batch function, save training data as a ".pkl" file
if __name__ == "__main__":
    for board_size in [4,6,8]:
        nn_data = NN_train_data(board_size, 4096)
        print("Working on data%d.pkl..." % board_size)
        num_games = 50
        print("Checkpoint 1")
        nn_data.run_game()
        print(nn_data.inputs)
        with open("data%d.pkl" % board_size, "wb") as f: pk.dump((nn_data.inputs, nn_data.outputs), f)
        print("data%d.pkl generated" % board_size)