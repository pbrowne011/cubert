import numpy as np
from cubert import cubert

# global color variables
w = 0
o = 1
g = 2
r = 3
b = 4
y = 5

def check_top(self):
    top_loc = [[9*y+1, 9*g+7], [9*y+3, 9*o+7], [9*y+5, 9*r+7], [9*y+7, 9*b+7]]
    top = [False] * 4
    for i in range(len(top_loc)):
        for j in range(len(top_loc[0])):
            if self.cube[top_loc[i][j]] == 'w':
                top[i] = True
    return top

def check_mid(self):
    mid_loc = [[o*9+5, g*9+3], [g*9+5, r*9+3], [r*9+5, b*9+3], [b*9+5, o*9+3]]
    mid = [False] * 4
    for i in range(len(mid_loc)):
        for j in range(len(mid_loc[0])):
            if self.cube[mid_loc[i][j]] == 'w':
                mid[i] = True
    return mid

def check_bot(self):
    bot_loc = [[w*9+3, o*9+1],[w*9+7, g*9+1],[w*9+5, r*9+1],[w*9+1, b*9+1]]
    bot = [False] * 4
    for i in range(len(bot_loc)):
        for j in range(len(bot_loc[0])):
            if self.cube[bot_loc[i][j]] == 'w':
                bot[i] = True
    return bot




def cross(self):
    # method to solve white cross on top

    # first, make a daisy

    # Step 1: check pieces on top, middle, and bottom to see what's where
    top = check_top(self)
    mid = check_mid(self)
    bot = check_bot(self)
    
    # Step 2: bring the middle pieces to the yellow layer

    moves = ""
    while mid != [False] * 4:
        for i in range(len(mid)):
            if mid[i]:
                if i == 0:
                    f = top[0]
                    s = top[1]
                    if f and s:
                        moves+= "y'g'"
                    elif f:
                        moves+= "o"
                    else:
                        moves+= "g'"
                elif i == 1:
                    f = top[2]
                    s = top[0]
                    if f and s:
                        moves+= "y'r'"
                    elif f:
                        moves+= "g"
                    else:
                        moves+= "r'"
                elif i == 2:
                    f = top[3]
                    s = top[2]
                    if f and s:
                        moves+= "y'b'"
                    elif f:
                        moves+= "r"
                    else:
                        moves+= "b'"
                elif i == 3:
                    f = top[1]
                    s = top[3]
                    if f and s:
                        moves+= "y'o'"
                    elif f:
                        moves+= "b"
                    else:
                        moves+= "o'"
                cubert.run_moves(self, moves)
                moves = ""
                top = check_top(self)
                mid = check_mid(self)
    
    top = check_top(self)
    mid = check_mid(self)
    bot = check_bot(self)

    # Step 3: deal with bottom

    while bot != [False] * 4:
        for i in range(len(bot)):
            if bot[i]:
                if i == 0:
                    if top[1]:
                        moves += "w'"
                    else:
                        moves += "o2"
                elif i == 1:
                    if top[0]:
                        moves += "w'"
                    else:
                        moves += "g2"
                elif i == 2:
                    if top[2]:
                        moves += "w'"
                    else:
                        moves += "r2"
                elif i == 3:
                    if top[3]:
                        moves += "w'"
                    else:
                        moves += "b2"
                cubert.run_moves(self, moves)
                moves= ""
                bot = check_bot(self)
                top = check_top(self)

    top = check_top(self)
    mid = check_mid(self)
    bot = check_bot(self)

    # Step 4: flip necessary tiles

    next=["g'yr'", "o'yg'", "r'yb'", "b'yo'"]
    daisy=[self.cube[y*9+1], self.cube[y*9+3], \
           self.cube[y*9+5], self.cube[y*9+7]]

    while daisy != ["w"]*4:
        if self.cube[y*9+1] != "w":
            cubert.run_moves(self, next[0])
        if self.cube[y*9+3] != "w":
            cubert.run_moves(self, next[1])
        if self.cube[y*9+5] != "w":
            cubert.run_moves(self, next[2])
        if self.cube[y*9+7] != "w":
            cubert.run_moves(self, next[3])
        daisy=[self.cube[y*9+1], self.cube[y*9+3], \
               self.cube[y*9+5], self.cube[y*9+7]]
    
    # Step 5: complete the white cross

    cross=[self.cube[w*9+1], self.cube[w*9+3], \
           self.cube[w*9+5], self.cube[w*9+7]]
    while cross != ["w"]*4:
        if daisy[0] == "w" and self.cube[g*9+7] == "g":
            moves += "g2"
        elif daisy[1] == "w" and self.cube[o*9+7] == "o":
            moves += "o2"
        elif daisy[2] == "w" and self.cube[r*9+7] == "r":
            moves += "r2"
        elif daisy[3] == "w" and self.cube[b*9+7] == "b":
            moves += "b2"
        else:
            moves += "y"
        cubert.run_moves(self, moves)
        moves=""
        cross=[self.cube[w*9+1], self.cube[w*9+3], \
            self.cube[w*9+5], self.cube[w*9+7]]
        daisy=[self.cube[y*9+1], self.cube[y*9+3], \
            self.cube[y*9+5], self.cube[y*9+7]]
        


    print("\ncube after cross")
    cubert.print_cube(self)
    return