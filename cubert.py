color = {
"U": "white", "D": "yellow", "L": "orange", "R": "red", "F": "#00aa00", "B": "blue", "X": "darkgray",
"o": "#fdfdc6", "x": "blueviolet", "y": "magenta"
}

cube=['w']*9+['o']*9+['g']*9+['r']*9+['b']*9+['y']*9

def print_cube(cube):
    print(cube)
    
print_cube(cube)

def perm_cycle(cube,a,b,c,d):
    p_a=cube[a[0]*9+a[1]]
    p_b=cube[b[0]*9+b[1]]
    p_c=cube[c[0]*9+c[1]]
    p_d=cube[d[0]*9+d[1]]
    #copy to next location
    cube[a[0]*9+a[1]]=p_a
    cube[b[0]*9+b[1]]=p_b
    cube[c[0]*9+c[1]]=p_c
    cube[d[0]*9+d[1]]=p_d
    