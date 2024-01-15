import pygame

cells = []
num = 5 

for i in range(num):
    if i == round(num / 2):
        cells.append(1)
    else:
        cells.append(0)

ruleset = format(70, 'b') 
length = len(ruleset)

i = 8 - length
for j in range(i):
    ruleset = "0" + ruleset

rules = {
        "111": int(ruleset[0]),
        "110": int(ruleset[1]), 
        "101": int(ruleset[2]), 
        "100": int(ruleset[3]), 
        "011": int(ruleset[4]), 
        "010": int(ruleset[5]), 
        "001": int(ruleset[6]), 
        "000": int(ruleset[7])
}

def update(cells):
    newCells = []
    for i in range(len(cells)):
        if i == len(cells)-1:
            string = f"{cells[-1]}{cells[0]}{cells[1]}"
        else:
            string = f"{cells[i-1]}{cells[i]}{cells[i+1]}"
        newCells.append(rules[string])
    return newCells


# constants

HEIGHT = 600
WIDTH = 600 
CELLSIZE = WIDTH / num # constant num is bad use  


pygame.init()
screen_size = (WIDTH, HEIGHT)
 
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Wolfram Elementary Autometa")
 
clock = pygame.time.Clock()
 
running = True

y = 0 

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    x = 0
    for i in range(len(cells)):
        if cells[i] == 0:
            pygame.draw.rect(screen, 'black', pygame.Rect(x*CELLSIZE, y*CELLSIZE, CELLSIZE, CELLSIZE))
        elif cells[i] == 1:
            pygame.draw.rect(screen, 'white', pygame.Rect(x*CELLSIZE, y*CELLSIZE, CELLSIZE, CELLSIZE))
        x += 1

    y += 1


    cells = update(cells)
    
    pygame.display.update()

    # how many updates per second
    clock.tick()
 
pygame.quit()
