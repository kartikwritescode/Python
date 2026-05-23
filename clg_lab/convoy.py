import os, time, random

ROWS = 20
COLS = 40
DELAY = 1   # seconds

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def random_grid():
    return [[1 if random.random() < 0.25 else 0 for _ in range(COLS)]
            for _ in range(ROWS)]

def neighbors(g, r, c):
    dirs = [(-1,-1),(-1,0),(-1,1),
            (0,-1),(0,1),
            (1,-1),(1,0),(1,1)]
    s = 0
    for dr, dc in dirs:
        s += g[(r+dr)%ROWS][(c+dc)%COLS]
    return s

def step(g):
    ng = [[0]*COLS for _ in range(ROWS)]
    for r in range(ROWS):
        for c in range(COLS):
            n = neighbors(g,r,c)
            if g[r][c] == 1:
                ng[r][c] = 1 if n in (2,3) else 0
            else:
                ng[r][c] = 1 if n == 3 else 0
    return ng

def draw(g):
    for row in g:
        print("".join("O" if x else "." for x in row))

g = random_grid()

while True:
    clear()
    draw(g)
    g = step(g)
    time.sleep(DELAY)
