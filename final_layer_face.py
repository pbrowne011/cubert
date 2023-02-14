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

def final_layer_face(self):
    # create a yellow face on the cube

    # Step 1: create a yellow cross
    edges = get_edges(self)
    corners = get_corners(self)
    
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
            print(corners)
            print(c)
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
            print(s)
            cubert.print_cube(self)
            moves+=s+"y"+s+"'y"+s+"y2"+s+"'"
            cubert.run_moves(self, moves)
            moves=""
            corners = get_corners(self)
            c=0
            for i in range(len(corners)):
                if corners[i][0] == "y":
                    c+=1
            cubert.print_cube(self)

    return

    



