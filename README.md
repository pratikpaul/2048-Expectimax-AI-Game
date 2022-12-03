                                                          **README**
Setup
1.	Download the project from Github
Git clone 
2.	Use the following code to install all packages:
            	pip install -r requirements.txt

Execution Steps
1.	Run the game by executing the below command:
Python main_cli.py
2.	Enter the board size – which will create the NxN board.
3.	Enter the target tile – The game will end once the target tile is reached
4.	Select the Gameplay mode:
a.	Human Player: Press 0 (One can manually choose an action: Up, Down, Left, Right or q to exit the game)
b.	Baseline AI: Press 1 (Uniformly random actions are selected.)
c.	Tree-Based AI: Press 2 (choose the best optimal action to increase the score.)
Evaluation of Scores
Evaluations of the final score for baseline AI and Tree-based AI and representation using histogram
Steps:
1.	Run the following command:
python evaluation.py
2.	Enter the board size for evaluation.
3.	Enter the target game tile.
4.	Enter the number of iterations you want to execute.
Expectimax
The game theory algorithm Expectimax is used to maximize the expected utility. In this game, we implement depth limited search where the expectation and maximization alternate turns. It assesses all potential tile values and tile locations for the upcoming generations in anticipation and optimizes based on weights that correspond to the likelihood of each possibility (10% for 4 and 90% for 2). In maximizing, it evaluates every move and chooses the one with the highest score. The tree search stops as soon as the predeﬁned depth limit, or highly unlike board state is reached.





![image](https://user-images.githubusercontent.com/25953840/205424444-75c85369-cfa3-4158-98a0-f68d87c5b86d.png)

