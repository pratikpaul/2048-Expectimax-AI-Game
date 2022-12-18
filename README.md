**README**

===========================================================================================================================================================
===========================================================================================================================================================

**Game 2048**

Italian web developer Gabriele Cirulli created the single-player sliding tile puzzle video game 2048, which was made available on GitHub. The goal of the 
game is to assemble numbered tiles on a grid to make a tile with the number 2048, although players can keep playing the game after achieving the objective 
to create tiles with higher numbers.

**Expectimax**

To implement this game, we are using the Expectimax algorithm. Expectimax is used for the tree search AI because, in any 2-player game, the "opponent" 
performs random actions and is not an actual adversarial player. Since there is an element of chance in each turn of the 2048 game that the agent must 
analyze and account for before taking action, Expectimax was the most appropriate algorithm to use. After each turn, the agent will compete against the 
randomness of the location, where new tiles will automatically spawn. In this game, we implement limited depth search where the expectation and 
maximization alternate turns. In anticipation, it assesses all potential tile values and locations for the upcoming generations. In maximizing, it 
evaluates every move and chooses the one with the highest score. The tree search stops as soon as the predeﬁned depth limit, or highly unlike board state, 
is reached. The game uses a depth limit without an evaluation function as a form of pruning to limit the search tree size.

**Neural Network**
We designed an AI that chooses the subsequent move using Expectimax tree search and a neural network to enhance tree search. The following is how we built 
a neural network on Expectimax tree search technique: Our Expectimax tree search uses a utility8 function to compute the projected utility and maximum 
utility at each level. The decision tree search path is influenced by the utility calculation's result.
The current state of the 2048 game board was used as input for the training data for our neural network. An integer number close to the future game board 
state's utility should result from an Expectimax tree search with sufficient depth. We play the 2048 game with the Expectimax tree search AI and map the 
game's current state to the usefulness of the AI's subsequent move to accomplish this. All the game data for each of our three board sizes—4x4, 6x6, and 
8x8—was recorded for 100 games and stored in three distinct files. 

**Setup**

Use the following code to install all packages:

**pip install -r requirements.txt**

**Execution Steps**

1. Run the game by executing the below command:

**python main.py**

1. Enter the board size – which will create the NxN board.
2. Enter the target tile – The game will end once the target tile is reached
3. Select the Gameplay mode:

4. Human Player: Press 0 (One can manually choose an action: Up, Down, Left, Right or q to exit the game)
5. Baseline AI: Press 1 (Uniformly random actions are selected.)
6. Expectimax AI: Press 2 (choose the best optimal action to increase the score.)
7. Expectimax AI + Neural Network: Press 3 (choose the best optimal action using tree based AI and Neural Netwrok to increase the score)


**Step before running Expectimax + Neural Network choice**
1. Train the data using generate_NN_Trraining_Data.py
2. Build a model using generate_model.py
3. Run main_cli.py and choose option 3 to run Tree AI + Neural Network


**Evaluation of Scores**

Evaluations of the final score for baseline AI and Tree-based AI and representation using histogram

**Steps:**

1. Run the following command:

**python evaluation.py**

1. Enter the board size for evaluation.
2. Enter the target game tile.
3. Enter the number of iterations you want to execute.

Sample Output: Baseline Ai v/s Tree Based AI
 
![image](https://user-images.githubusercontent.com/25953840/208282201-cb228454-d7b3-4dea-88fc-83de00742bc9.png)
