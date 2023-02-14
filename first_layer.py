from cubert import cubert

# global color variables
w = 0
o = 1
g = 2
r = 3
b = 4
y = 5

# global corner variables
og = ["w", "o", "g"]
gr = ["w", "g", "r"]
rb = ["w", "r", "b"]
bo = ["w", "b", "o"]

def update_goals(self):
    c0 = [self.cube[w*9+6],self.cube[o*9+2],self.cube[g*9+0]]
    c1 = [self.cube[w*9+8],self.cube[g*9+2],self.cube[r*9+0]]
    c2 = [self.cube[w*9+2],self.cube[r*9+2],self.cube[b*9+0]]
    c3 = [self.cube[w*9+0],self.cube[b*9+2],self.cube[o*9+0]]
    goals = [c0, c1, c2, c3]
    return goals


def update_bottom(self):
    c4 = [self.cube[y*9+0],self.cube[o*9+8],self.cube[g*9+6]]
    c5 = [self.cube[y*9+2],self.cube[g*9+8],self.cube[r*9+6]]
    c6 = [self.cube[y*9+8],self.cube[r*9+8],self.cube[b*9+6]]
    c7 = [self.cube[y*9+6],self.cube[b*9+8],self.cube[o*9+6]]
    bottom = [c4, c5, c6, c7]
    return bottom


def first_layer(self):
    # method to solve first layer of cube completely

    moves=""
    
    # Solve corners in one go
    corners = [og, gr, rb, bo]
    goals = update_goals(self)
    bottom = update_bottom(self)

    for i in range(len(corners)):
        # check if corner is already correct
        if corners[i] == goals[i]:
            continue

        # get corner out of the wrong spot
        while set(corners[i]) in [set(goals[0]),set(goals[1]),set(goals[2]),set(goals[3])]:
            if set(corners[i]) == set(goals[0]):
                moves+="g'y'g"
            elif set(corners[i]) == set(goals[1]):
                moves+="r'y'r"
            elif set(corners[i]) == set(goals[2]):
                moves+="b'y'b"
            elif set(corners[i]) == set(goals[3]):
                moves+="o'y'o"
            cubert.run_moves(self, moves)
            moves=""
            goals = update_goals(self)
            bottom = update_bottom(self)

        # align corner in the correct spot to perform moves to get to top
        while set(bottom[i]) != set(corners[i]):
            cubert.run_moves(self, "y")
            goals = update_goals(self)
            bottom = update_bottom(self)

        # solve any of three possible orientations
        
        # first orientation: white is facing downwards
        if bottom[i][0] == "w":
            if i == 0:
                moves+="oy'o'y2"
            elif i == 1:
                moves+="gy'g'y2"
            elif i == 2:
                moves+="ry'r'y2"
            elif i == 3:
                moves+="by'b'y2"
            cubert.run_moves(self, moves)
            moves=""
            goals = update_goals(self)
            bottom = update_bottom(self)

        # second orientation: white is on "left" side
        if bottom[i][2] == "w":
            if i == 0:
                moves+="yoy'o'"
            elif i == 1:
                moves+="ygy'g'"
            elif i == 2:
                moves+="yry'r'"
            elif i == 3:
                moves+="yby'b'"
            cubert.run_moves(self, moves)
            moves=""
            goals = update_goals(self)
            bottom = update_bottom(self)

        # third orientation: white is on front side
        if bottom[i][1] == "w":
            if i == 0:
                moves+="y'g'yg"
            elif i == 1:
                moves+="y'r'yr"
            elif i == 2:
                moves+="y'b'yb"
            elif i == 3:
                moves+="y'o'yo"
            cubert.run_moves(self, moves)
            moves=""
            goals = update_goals(self)
            bottom = update_bottom(self)

    return
