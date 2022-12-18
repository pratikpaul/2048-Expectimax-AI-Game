import random
import math
import numpy as np
import torch as tr
import pickle as pk
import matplotlib.pyplot as pt
from torch.nn import Sequential, Linear, Flatten

def getNet(board_size):
    return Sequential(
        Flatten(),
        Linear(in_features=board_size*board_size,out_features=board_size),
        Linear(in_features=board_size,out_features=1)
    )


if __name__ == "__main__":
    for board_size in [4,6,8]:
        # NN instance
        net = getNet(board_size)

        # Load training data
        with open("data%d.pkl" % board_size,"rb") as f: (x, y_targ) = pk.load(f)

        # Prepare training data
        train_loss = []
        shuffle = np.random.permutation(range(len(x)))
        train = shuffle[:-10]

        # Gradient descent
        optimizer = tr.optim.Adam(net.parameters())

        ## DIANA ZHENG OPTIMIZER
        # optimizer = tr.optim.AdamW(net.parameters())

        ## KEVIN KHA OPTIMIZER
        # optimizer = tr.optim.Adamax(net.parameters())
        for epoch in range(1000):
            optimizer.zero_grad()
            y_train = net(x[train])
            e_train = tr.sum((y_train - y_targ[train])**2)
            e_train.backward()
            optimizer.step()
            train_loss.append(e_train.item() / (len(shuffle)-10))

        # Save trained data
        tr.save(net.state_dict(), "model%d.pth" % board_size)
        print(len(net.state_dict()))
        pt.plot(train_loss,'b-', color="green")
        pt.legend(["Training"], loc='upper right')
        pt.xlabel("Iteration", color="blue")
        pt.ylabel("Average Loss", color="blue")
        pt.title("Iteration vs. Average Loss - %dx%d game size" % (board_size, board_size), color="blue")
        pt.savefig("%dx%d-NN_Expectimax" % (board_size, board_size))
        pt.clf()
        print("Figure saved")
        
        # Plot actual output vs. target loss
        pt.plot(y_train.detach().numpy(), y_targ[train].detach().numpy(),'bo', color="green")
        pt.legend(["Training"], loc='upper right')
        pt.xlabel("Actual o/p", color="blue")
        pt.ylabel("Target o/p", color="blue")
        pt.title("Actual output vs. Target output - %dx%d game size" % (board_size, board_size), color="blue")
        pt.savefig("%dx%d-NN_Expectimax" % (board_size, board_size))
        pt.clf()
        print("Figure saved")