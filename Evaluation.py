from board import Board
from ai_expectimax import AI_expectimax
from ai_expectimax_neural_network import AI_expectimax_neural_network
#from human import Human
from baseline_ai import Baseline
from random import randint
import matplotlib.pyplot as plt


dirs = {
    0: "UP",
    1: "DOWN",
    2: "LEFT",
    3: "RIGHT"
}


class Evaluation:
        
    def __init__(self, n, tgt):
        self.board_size = n
        self.target_score = tgt
        self.board = Board(self.board_size)
        #self.human = Human()
        self.baseline_ai = Baseline()
        self.ainn = AI_expectimax_neural_network()
        self.ai = AI_expectimax()

        self.init_game()
        
        print("Select the Number of executions:")
        
        inpt = abs(int(input()))
        
        self.evaluate(inpt,self.board_size)
        self.over = False
    
    def evaluate(self,inpt,board_size):
        baseline_score=[]
        baseline_node_count=[]
        tree_score=[]
        tree_node_count=[]
        tree_NN_score=[]
        tree_NN_node_count=[]
        for i in range(inpt):
            score,node=self.run_game(1)
            baseline_score.append(score)
            baseline_node_count.append(node)
            self.board = Board(board_size)
        
        self.board = Board(board_size)
        for i in range(inpt):
            print(i)
            score,node=self.run_game(2)
            tree_score.append(score)
            tree_node_count.append(node)
            self.board = Board(board_size)

        self.board = Board(board_size)
        for i in range(inpt):
            print(i)
            score,node=self.run_game(3)
            tree_NN_score.append(score)
            tree_NN_node_count.append(node)
            self.board = Board(board_size)

        print('baseline_score: '+str(baseline_score))
        print('tree_score: '+str(tree_score))
        print('tree_NN_score: '+str(tree_NN_score))


        fig,ax=plt.subplots()
        plt.hist(baseline_score,align='mid',bins=50)
        plt.xlabel('Scores')
        plt.ylabel('counts')
        plt.title('baseline AI performance')
        props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
        text='board size='+str(board_size)+' tile size='+str(target_tile)
        ax.text(0.05, 0.95,text,transform=ax.transAxes, fontsize=14,verticalalignment='top',bbox=props)
        plt.savefig("%dx%d-baseline AI performance (Scores vs Counts)" % (board_size, board_size))
        plt.clf()

        fig, ax=plt.subplots()
        plt.hist(tree_score,align='mid',bins=50)
        plt.xlabel('Scores')
        plt.ylabel('counts')
        plt.title('Tree based AI performance')
        props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
        text='board size='+str(board_size)+' tile size='+str(target_tile)
        ax.text(0.05, 0.95,text,transform=ax.transAxes, fontsize=14,verticalalignment='top',bbox=props)
        plt.savefig("%dx%d-Tree based AI performance (Scores vs Counts)" % (board_size, board_size))
        plt.clf()

        fig, ax=plt.subplots()
        plt.hist(tree_NN_score,align='mid',bins=50)
        plt.xlabel('Scores')
        plt.ylabel('counts')
        plt.title('Tree+NN AI performance')
        props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
        text='board size='+str(board_size)+' tile size='+str(target_tile)
        ax.text(0.05, 0.95,text,transform=ax.transAxes, fontsize=14,verticalalignment='top',bbox=props)
        plt.savefig("%dx%d-Tree+NN AI performance (Scores vs Counts)" % (board_size, board_size))
        plt.clf()

        fig,ax=plt.subplots()
        plt.hist(baseline_node_count,align='mid',bins=100)
        plt.xlabel('Nodes')
        plt.ylabel('counts')
        plt.title('baseline AI performance')
        props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
        text='board size='+str(board_size)+' tile size='+str(target_tile)
        ax.text(0.05, 0.95,text,transform=ax.transAxes, fontsize=14,verticalalignment='top',bbox=props)
        plt.savefig("%dx%d-Tree+NN AI performance (Nodes vs Counts)" % (board_size, board_size))
        plt.clf()

        fig, ax=plt.subplots()
        plt.hist(tree_node_count,align='mid',bins=100)
        plt.xlabel('Nodes')
        plt.ylabel('counts')
        plt.title('Tree based AI performance')
        props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
        text='board size='+str(board_size)+' tile size='+str(target_tile)
        ax.text(0.05, 0.95,text,transform=ax.transAxes, fontsize=14,verticalalignment='top',bbox=props)
        plt.savefig("%dx%d-Tree based AI performance (Nodes vs Counts)" % (board_size, board_size))
        plt.clf()

        fig, ax=plt.subplots()
        plt.hist(tree_NN_node_count,align='mid',bins=100)
        plt.xlabel('Nodes')
        plt.ylabel('counts')
        plt.title('Tree+NN AI performance')
        props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
        text='board size='+str(board_size)+' tile size='+str(target_tile)
        ax.text(0.05, 0.95,text,transform=ax.transAxes, fontsize=14,verticalalignment='top',bbox=props)
        plt.savefig("%dx%d-Tree+NN AI performance (Nodes vs Counts)" % (board_size, board_size))
        plt.clf()

    def init_game(self):
        self.insert_random_tile()
        self.insert_random_tile()


    def run_game(self,inpt):
        node=0
        while True:
            if inpt == 1:
                move = self.baseline_ai.move()
            elif inpt == 2:
                move = self.ai.get_move(self.board)
            elif inpt == 3:
                move = self.ainn.get_move(self.board)
            node=node+1
            self.board.move(move)
            #print("Computer's Turn")
            self.insert_random_tile()

            if(self.board.get_max_tile() >= self.target_score):   
                return self.board.score, node
            
            if len(self.board.get_available_moves()) == 0:
                return self.board.score, node

    def print_board(self):
        print("Score: " + str(int(self.board.score)))
        for i in range(self.board_size):
            for j in range(self.board_size):
                print("%6d  " % self.board.grid[i][j], end="")
            print("")
        print("")

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

if __name__ == '__main__':
    print("\nThe size you provide will be converted into a MxM board")
    print("Please enter the board size : ")
    board_size = input()
    print("Enter the target tile you wanna reach to")
    target_tile = input()
    evaluation = Evaluation(int(board_size), int(target_tile))
