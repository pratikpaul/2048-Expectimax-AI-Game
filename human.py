import readchar
import numpy as np

class Human:
        
    def move(self):
        while(1):
            k=readchar.readkey()
            if k!='':break
        if k=='\x1b[A' or k=='\x00H':
            return np.random.choice([0,1],p=[0.9,0.1])
        elif k=='\x1b[B' or k=='\x00P':
            return np.random.choice([1,2],p=[0.9,0.1])
        elif k=='\x1b[D' or k=='\x00K':
            return np.random.choice([2,3],p=[0.9,0.1])
        elif k=='\x1b[C' or k=='\x00M':
            return np.random.choice([3,0],p=[0.9,0.1])
        elif k == 'q':
            exit()
        else:
            return self.move()
        