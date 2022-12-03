import numpy as np
from numba import jit

dirs = [UP, DOWN, LEFT, RIGHT] = range(4)

@jit
def merge(a, n):
    points_gained = 0
    for i in range(n):
        for j in range(n-1):
            if a[i][j] == a[i][j + 1] and a[i][j] != 0:
                a[i][j] *= 2
                a[i][j + 1] = 0
                points_gained += a[i][j]
    return (a,points_gained)

@jit
def justify_left(a, out, n):
    for i in range(n):
        c = 0
        for j in range(n):
            if a[i][j] != 0:
                out[i][c] = a[i][j]
                c += 1
    return out

@jit
def get_available_from_zeros(a, n):
    uc, dc, lc, rc = False, False, False, False

    v_saw_0 = [False] * n
    v_saw_1 = [False] * n

    for i in range(n):
        saw_0 = False
        saw_1 = False

        for j in range(n):

            if a[i][j] == 0:
                saw_0 = True
                v_saw_0[j] = True

                if saw_1:
                    rc = True
                if v_saw_1[j]:
                    dc = True

            if a[i][j] > 0:
                saw_1 = True
                v_saw_1[j] = True

                if saw_0:
                    lc = True
                if v_saw_0[j]:
                    uc = True

    return [uc, dc, lc, rc]

class GameBoard:
    def __init__(self, n, score = 0):
        self.n = n
        self.score = score
        self.grid = np.zeros((n, n))#, dtype=np.int_)

    def clone(self):
        grid_copy = GameBoard(self.n,self.score)
        grid_copy.grid = np.copy(self.grid)
        return grid_copy

    def insert_tile(self, pos, value):
        self.grid[pos[0]][pos[1]] = value

    def get_available_cells(self):
        cells = []
        for x in range(self.n):
            for y in range(self.n):
                if self.grid[x][y] == 0:
                    cells.append((x,y))
        return cells

    def get_max_tile(self):
        return np.amax(self.grid)

    def move(self, dir, get_avail_call = False):
        if get_avail_call:
            clone = self.clone()

        z1 = np.zeros((self.n, self.n))#, dtype=np.int_)
        z2 = np.zeros((self.n, self.n))#, dtype=np.int_)

        if dir == UP:
            self.grid = self.grid[:,::-1].T
            self.grid = justify_left(self.grid, z1, self.n)
            mrg = merge(self.grid, self.n)
            self.grid = mrg[0]
            self.score += mrg[1]
            self.grid = justify_left(self.grid, z2, self.n)
            self.grid = self.grid.T[:,::-1]
        if dir == DOWN:
            self.grid = self.grid.T[:,::-1]
            self.grid = justify_left(self.grid, z1, self.n)
            mrg = merge(self.grid, self.n)
            self.grid = mrg[0]
            self.score += mrg[1]
            self.grid = justify_left(self.grid, z2, self.n)
            self.grid = self.grid[:,::-1].T
        if dir == LEFT:
            self.grid = justify_left(self.grid, z1, self.n)
            mrg = merge(self.grid, self.n)
            self.grid = mrg[0]
            self.score += mrg[1]
            self.grid = justify_left(self.grid, z2, self.n)
        if dir == RIGHT:
            self.grid = self.grid[:,::-1]
            self.grid = self.grid[::-1,:]
            self.grid = justify_left(self.grid, z1, self.n)
            mrg = merge(self.grid, self.n)
            self.grid = mrg[0]
            self.score += mrg[1]
            self.grid = justify_left(self.grid, z2, self.n)
            self.grid = self.grid[:,::-1]
            self.grid = self.grid[::-1,:]

        if get_avail_call:
            return not (clone.grid == self.grid).all()
        else:
            return None

    def get_available_moves(self, dirs = dirs):
        available_moves = []
        
        a1 = get_available_from_zeros(self.grid, self.n)

        for x in dirs:
            if not a1[x]:
                board_clone = self.clone()

                if board_clone.move(x, True):
                    available_moves.append(x)

            else:
                available_moves.append(x)

        return available_moves

    def get_cell_value(self, pos):
        return self.grid[pos[0]][pos[1]]
