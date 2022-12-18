import math
import time
import numpy as np
import torch as tr
from torch.nn import Sequential, Linear, Flatten

UP, DOWN, LEFT, RIGHT = range(4)

# #4
# Generate NN module
# return type: torch.nn.Module
class AI_expectimax_neural_network:
    def getNet(self, board_size):
        return Sequential(
            Flatten(),
            Linear(in_features=board_size*board_size,out_features=board_size),
            Linear(in_features=board_size,out_features=1)
        )

    def nn_utility(self, board):
        # NN instance
        net = self.getNet(board.n)
        net.load_state_dict(tr.load("model%d.pth" % board.n))

        # Predicted NN factor
        return net(tr.tensor([board.grid.flatten()]).float())[0]

    def getUtility(self, board):
        utility = 0
        empty_count = 0

        # Sum non 0 tile values, times factor
        # factor = log2(tile)
        # Count num of zero tiles
        for i in range(board.grid.shape[0]):
            for j in range(board.grid.shape[1]):
                if board.grid[i][j] != 0:
                    utility += board.grid[i][j] * math.log(board.grid[i][j], 2)
                else:
                    empty_count += 1

        # More zero tiles = higher utility
        utility += empty_count * board.n
        # Add NN factor
        utility += self.nn_utility(board)

        return utility

    def get_move(self, board):
        best_move, _ = self.maximize(board)
        return best_move

    def eval_board(self, board, n_empty): 
        grid = board.grid

        utility = 0
        smoothness = 0

        big_t = np.sum(np.power(grid, 2))
        s_grid = np.sqrt(grid)
        smoothness -= np.sum(np.abs(s_grid[::,0] - s_grid[::,1]))
        smoothness -= np.sum(np.abs(s_grid[::,1] - s_grid[::,2]))
        smoothness -= np.sum(np.abs(s_grid[::,2] - s_grid[::,3]))
        smoothness -= np.sum(np.abs(s_grid[0,::] - s_grid[1,::]))
        smoothness -= np.sum(np.abs(s_grid[1,::] - s_grid[2,::]))
        smoothness -= np.sum(np.abs(s_grid[2,::] - s_grid[3,::]))
        
        empty_w = 100000
        smoothness_w = 3

        empty_u = n_empty * empty_w
        smooth_u = smoothness ** smoothness_w
        # big_t_u = big_t

        utility += self.getUtility(board)
        utility += empty_u
        utility += smooth_u

        return (utility, empty_u, smooth_u, big_t)

    def maximize(self, board, depth = 0):
        moves = board.get_available_moves()
        moves_boards = []

        for m in moves:
            m_board = board.clone()
            m_board.move(m)
            moves_boards.append((m, m_board))

        max_utility = (float('-inf'),0,0,0)
        best_direction = None

        for mb in moves_boards:
            utility = self.chance(mb[1], depth + 1)

            if utility[0] >= max_utility[0]:
                max_utility = utility
                best_direction = mb[0]

        return best_direction, max_utility

    def chance(self, board, depth = 0):
        empty_cells = board.get_available_cells()
        n_empty = len(empty_cells)

        #if n_empty >= 7 and depth >= 5:
        #    return self.eval_board(board, n_empty)

        if n_empty >= 6 and depth >= 3:
            return self.eval_board(board, n_empty)

        if n_empty >= 0 and depth >= 5:
            return self.eval_board(board, n_empty)

        if n_empty == 0:
            _, utility = self.maximize(board, depth + 1)
            return utility

        possible_tiles = []

        chance_2 = (.9 * (1 / n_empty))
        chance_4 = (.1 * (1 / n_empty))
        
        for empty_cell in empty_cells:
            possible_tiles.append((empty_cell, 2, chance_2))
            possible_tiles.append((empty_cell, 4, chance_4))

        utility_sum = [0, 0, 0, 0]

        for t in possible_tiles:
            t_board = board.clone()
            t_board.insert_tile(t[0], t[1])
            _, utility = self.maximize(t_board, depth + 1)

            for i in range(4):
                utility_sum[i] += utility[i] * t[2]

        return tuple(utility_sum)
