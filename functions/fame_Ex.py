import pgzrun
HEIGHT=600
WIDTH=800
p=Actor('ironman.png',(100,100))
c=Actor('cookie.png',(30,80))

def draw():
    screen.fill('white')
    p.draw()
    c.draw()
    print('drawing')

def update():
    p.x -= 3
    p.angle = -10
    if p.x < 0:  # player moving from left side
        p.x=WIDTH
    print(p.x, p.y)
pgzrun.go()  