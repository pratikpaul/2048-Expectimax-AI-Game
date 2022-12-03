**README**

**Game 2048**

Italian web developer Gabriele Cirulli created the single-player sliding tile puzzle video game 2048, which was made available on GitHub. The goal of the game is to assemble numbered tiles on a grid to make a tile with the number 2048, although players can keep playing the game after achieving the objective to create tiles with higher numbers.

**Expectimax**

The game theory algorithm Expectimax is used to maximize the expected utility. In this game, we implement depth limited search where the expectation and maximization alternate turns. It assesses all potential tile values and tile locations for the upcoming generations in anticipation and optimizes based on weights that correspond to the likelihood of each possibility (10% for 4 and 90% for 2). In maximizing, it evaluates every move and chooses the one with the highest score. The tree search stops as soon as the predeﬁned depth limit, or highly unlike board state is reached.

**Setup**

Use the following code to install all packages:

**pip install -r requirements.txt**

**Execution Steps**

1. Run the game by executing the below command:

**Python main\_cli.py**

1. Enter the board size – which will create the NxN board.
2. Enter the target tile – The game will end once the target tile is reached
3. Select the Gameplay mode:

1. Human Player: Press 0 (One can manually choose an action: Up, Down, Left, Right or q to exit the game)
2. Baseline AI: Press 1 (Uniformly random actions are selected.)
3. Tree-Based AI: Press 2 (choose the best optimal action to increase the score.)

**Evaluation of Scores**

Evaluations of the final score for baseline AI and Tree-based AI and representation using histogram

**Steps:**

1. Run the following command:

**python evaluation.py**

1. Enter the board size for evaluation.
2. Enter the target game tile.
3. Enter the number of iterations you want to execute.

![plot](./blob/main/AIscores.png)
