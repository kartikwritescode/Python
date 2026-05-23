import os , time , random
rows = 50
cols = 50
delay = 1


def clear():
    os.system('cls' if os.name=='nt' else 'clear')


def random_grid():
    return [[1 if random.random()<0.25 else 0 for _ in range(cols)]for _ in range(rows)]

def neighbours(g,r,c):
    dirs = [(-1,-1),(-1,0),(-1,1),
            (0,-1),(0,1),
            (1,-1),(1,0),(1,1)]
    
    s=0
    for dr,dc in dirs:
        s+=g[(r+dr)%rows][(c+dc)%cols]
    return s

def step(g):
    ng=[[0]*cols for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            n=neighbours(g,r,c)
            if g[r][c]==1:
                ng[r][c]=1 if n in (2,3) else 0
            else:
                ng[r][c]=1 if n==3 else 0
    return ng

def draw(g):
    for row in g:
        print("".join("0" if x else "." for x in row))


g = random_grid()

while True:
    clear()
    draw(g)
    g=step(g)
    time.sleep(delay)

