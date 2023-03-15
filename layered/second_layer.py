from cubert import cubert

# global color variables
w = 0
o = 1
g = 2
r = 3
b = 4
y = 5

# global edge variables
og = ["o", "g"]
gr = ["g", "r"]
rb = ["r", "b"]
bo = ["b", "o"]

def update_top(self):
    e0 = [self.cube[y*9+3],self.cube[o*9+7]]
    e1 = [self.cube[y*9+1],self.cube[g*9+7]]
    e2 = [self.cube[y*9+5],self.cube[r*9+7]]
    e3 = [self.cube[y*9+7],self.cube[b*9+7]]
    top = [e0,e1,e2,e3]
    return top

def update_mid(self):
    e4 = [self.cube[o*9+5],self.cube[g*9+3]]
    e5 = [self.cube[g*9+5],self.cube[r*9+3]]
    e6 = [self.cube[r*9+5],self.cube[b*9+3]]
    e7 = [self.cube[b*9+5],self.cube[o*9+3]]
    mid = [e4,e5,e6,e7]
    return mid

def second_layer(self):
    # solve this layer one edge piece at a time

    edges = [og, gr, rb, bo]
    centers = ["o","g","r","b"]
    top = update_top(self)
    mid = update_mid(self)

    # go through each edge and solve
    for i in range(len(edges)):
        moves=""

        # check if edge is already correct
        if edges[i] == mid[i]:
            continue

        # get edge out of mid if trapped there
        while set(edges[i]) in [set(mid[j]) for j in range(4)]:
            if set(edges[i]) == set(mid[0]):
                moves+="yoy'o'y'g'yg"
            elif set(edges[i]) == set(mid[1]):
                moves+="ygy'g'y'r'yr"
            elif set(edges[i]) == set(mid[2]):
                moves+="yry'r'y'b'yb"
            elif set(edges[i]) == set(mid[3]):
                moves+="yby'b'y'o'yo"
            cubert.run_moves(self, moves)
            moves=""
            top = update_top(self)
            mid = update_mid(self)


        # match edge to proper center piece
        match1 = (top[i][1] == centers[i]) and (top[i][0] == edges[i][1])
        match2 = (top[i][1] == centers[(i+1)%4]) and \
                 (top[i][0] == edges[i][0])
        
        # make sure correct edge matched middle piece
        while not(match1 or match2):
            cubert.run_moves(self,"y")
            top = update_top(self)
            mid = update_mid(self)
            match1 = (top[i][1] == centers[i]) and (top[i][0] == edges[i][1])
            match2 = (top[i][1] == centers[(i+1)%4]) and (top[i][0] == edges[i][0])
            if match1 or match2:
                break

        # moving left
        if match1:
            if i == 0:
                moves+="y'g'ygyoy'o'"
            elif i == 1:
                moves+="y'r'yrygy'g'"
            elif i == 2:
                moves+="y'b'ybyry'r'"
            elif i == 3:
                moves+="y'o'yoyby'b'"
        # moving right
        elif match2:
            if i == 0:
                moves+="y2oy'o'y'g'yg"
            elif i == 1:
                moves+="y2gy'g'y'r'yr"
            elif i == 2:
                moves+="y2ry'r'y'b'yb"
            elif i == 3:
                moves+="y2by'b'y'o'yo"
        cubert.run_moves(self, moves)
        moves=""
        top = update_top(self)
        mid = update_mid(self)

    return
