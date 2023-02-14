from cubert import cubert

# global color variables
w = 0
o = 1
g = 2
r = 3
b = 4
y = 5

# global faces list
faces = ["o", "g", "r", "b"]

def get_edges(self):
    edges = [self.cube[y*9+3],self.cube[y*9+1],self.cube[y*9+5],\
             self.cube[y*9+7]]
    return edges

def get_corners(self):
    c0 = [self.cube[y*9+0],self.cube[o*9+8],self.cube[g*9+6]]
    c1 = [self.cube[y*9+2],self.cube[g*9+8],self.cube[r*9+6]]
    c2 = [self.cube[y*9+8],self.cube[r*9+8],self.cube[b*9+6]]
    c3 = [self.cube[y*9+6],self.cube[b*9+8],self.cube[o*9+6]]
    corners = [c0, c1, c2, c3]
    return corners

def final_layer(self):
    # finish final layer of cube

    # Step 1: create a yellow cross
    edges = get_edges(self)
    corners = get_corners(self)
    goal_corners = [["y","o","g"],["y","g","r"],["y","r","b"],["y","b","o"]]
    
    # orient cube properly to form cross
    moves=""
    e = edges.count("y")
    if e == 4:
        pass
    else:
        while e < 4:
            if e >= 2:
                # two options, we need to determine geometric shape
                if edges[0] == edges[2] == "y":
                    f = faces[1]
                    s = faces[0]
                elif edges[1] == edges[3] == "y":
                    f = faces[0]
                    s = faces[3]
                elif edges[0] == edges[1] and edges[1] == "y":
                    f = faces[3]
                    s = faces[2]
                elif edges[1] == edges[2] and edges[2] == "y":
                    f = faces[0]
                    s = faces[3]
                elif edges[2] == edges[3] and edges[3] == "y":
                    f = faces[1]
                    s = faces[0]
                elif edges[3] == edges[0] and edges[0] == "y":
                    f = faces[2]
                    s = faces[1]
            else:
                f = faces[0]
                s = faces[3]
            moves+= f+"y"+s+"y'"+s+"'"+f+"'"
            cubert.run_moves(self, moves)
            moves=""
            edges = get_edges(self)
            e = edges.count("y")
    
    # Step 2: add corners to complete final layer face
    edges = get_edges(self)
    corners = get_corners(self)

    # orient the cube to add corners
    c=0
    for i in range(len(corners)):
        if corners[i][0] == "y":
            c+=1
    if c == 4:
        pass
    else:
        while c < 4:
            # no corners, need left tile
            if c == 0:
                for j in range(len(corners)):
                    if corners[j][2] == "y":
                        s = faces[(j-1)%4]
            elif c == 1:
                for j in range(len(corners)):
                    if corners[j][0] == "y":
                        s = faces[(j-1)%4]
            else:
                for j in range(len(corners)):
                    if corners[j][1] == "y":
                        s = faces[(j-1)%4]
            moves+=s+"y"+s+"'y"+s+"y2"+s+"'"
            cubert.run_moves(self, moves)
            moves=""
            corners = get_corners(self)
            c=0
            for i in range(len(corners)):
                if corners[i][0] == "y":
                    c+=1
    
    edges = get_edges(self)
    corners = get_corners(self)

    # Step 3: solve corners by color
    while corners != goal_corners:
        f='a'
        for k in range(len(corners)):
            for i in range(len(corners)):
                c1_bool = corners[i] == goal_corners[i]
                c2_bool = corners[(i+1)%4] == goal_corners[(i+1)%4]
                if c1_bool and c2_bool:
                    f = faces[(i-1)%4]
                    s = faces[(i+2)%4]
                    u = faces[(i+1)%4]
            if f != "a":
                break
            cubert.run_moves(self, "y")
            corners = get_corners(self)

        if f == 'a':
            f = faces[0]
            s = faces[3]
            u = faces[2]
        moves+=s+"'"+f+s+"'"+u+"2"+s+f+"'"+s+"'"+u+"2"+s+"2"+"y'"
        cubert.run_moves(self, moves)
        moves=""
        edges = get_edges(self)
        corners = get_corners(self)


    # Step 4: solve edges and complete
    while True:
        f="a"
        for i in range(len(faces)):
            if self.cube[(i+1)*9:(i+1)*9+9] == [faces[i]]*9:
                f = faces[(i+2)%4]
                l = faces[(i+3)%4]
                s = faces[(i+1)%4]
                break
        if f == "a":
            f = faces[0]
            l = faces[1]
            s = faces[3]
        moves+=f+"2"+"y"+l+s+"'"+f+"2"+l+"'"+s+"y"+f+"2"
        cubert.run_moves(self, moves)
        if self.cube[o*9+6:o*9+9] == ["o"]*3 and \
            self.cube[r*9+6:r*9+9] == ["r"]*3:
            break
        moves=""
    cubert.print_cube(self)

    return
