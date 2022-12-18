from board import Board
from ai_expectimax import AI_expectimax
from ai_expectimax_neural_network import AI_expectimax_neural_network
from human import Human
from baseline_ai import Baseline
from random import randint, seed


dirs = {
    0: "UP",
    1: "DOWN",
    2: "LEFT",
    3: "RIGHT"
}


class CLIRunner:
        
    def __init__(self, n, tgt):
        self.board_size = n
        self.target_score = tgt
        self.board = Board(self.board_size)
        self.human = Human()
        self.baseline_ai = Baseline()
        self.ainn = AI_expectimax_neural_network()
        self.ai = AI_expectimax()

        self.init_game()
        self.print_board()
        
        print("Select the gameplay mode:")
        print("\tTo play yourself, Press : 0")
        print("\tFor Baseline gameplay, Press : 1")
        print("\tFor Expectimax AI, Press : 2")
        print("\tFor Expectimax AI + Neural Network, Press : 3")
        
        inpt = abs(int(input()))
        while(inpt > 3):
            print("Please select from the available options")
            print("Select the gameplay mode:")
            print("\tTo play yourself, Press : 0")
            print("\tFor Baseline gameplay, Press : 1")
            print("\tFor Expectimax AI, Press : 2")
            print("\tFor Expectimax AI + Neural Network, Press : 3")
            inpt = abs(int(input()))
        
        self.run_game(inpt)

        self.over = False

    def init_game(self):
        self.introduce_random_tile()
        self.introduce_random_tile()


    def run_game(self,inpt):
        while True:
            if inpt == 0:
                move = self.human.move()
            elif inpt == 1:
                move = self.baseline_ai.move()
            elif inpt == 2:
                move = self.ai.get_move(self.board)
            else:
                move = self.ainn.get_move(self.board)
            print("AI's Turn:", end="")
            self.board.move(move)
            print(dirs[move])
            self.print_board()
            #print("Computer's Turn")
            self.introduce_random_tile()
            self.print_board()
            
            if(self.board.get_max_tile() >= self.target_score):
                print("You Win.. You have reached the target score of " + str(self.target_score))
                print("Your final score is : " + str(int(self.board.score)))
                break
            
            if len(self.board.get_available_moves()) == 0:
                print("GAME OVER (max tile): " + str(self.board.get_max_tile()) + " Total score : " + str(int(self.board.score)))
                break

    def print_board(self):
        print("Score: " + str(int(self.board.score)))
        for i in range(self.board_size):
            for j in range(self.board_size):
                print("%6d  " % self.board.grid[i][j], end="")
            print("")
        print("")

    def introduce_random_tile(self):
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
    print("Please enter the board size \n(Board sizes >= 4 is currently supported to get better game Data) : ")
    board_size = input()
    print("Enter the target tile you wanna reach to")
    target_tile = input()
    CLIRunner = CLIRunner(int(board_size), int(target_tile))
