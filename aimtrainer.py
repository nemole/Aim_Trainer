from graphics import *
import random
from datetime import datetime
from math import sqrt

def make_circle():
    bound1 = random.randint(35,1385)
    bound2 = random.randint(35,745)
    radius = random.randint(10,35)

    circle = Circle(Point(bound1,bound2), radius)
    circle.setFill("red")
    circle.setOutline("red")
    return circle

def get_distance(x1, x2, y1, y2):
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)

def get_score(x):
    return int(10000/15)

def setup_score(window):
    midwidth = window.getWidth()/2
    scoret = Text(Point(midwidth - 8, 30), "SCORE")
    scoret.setTextColor("white")
    scoret.draw(window)
    score = Text(Point(midwidth + 32, 30), "0")
    score.setTextColor("white")
    return score

def update_score(circle, score_num_text):
    number = int(score_num_text.getText())
    score_offset = int(1000/circle.radius)
    number = number + score_offset
    score_num_text.setText(str(number))
    
def main():
    
    random.seed(datetime.now())

    window = GraphWin("Aim Trainer", 1400, 780)
    window.setBackground("black")

    midwidth = window.getHeight()/2

    scoretext = setup_score(window)
    scoretext.draw(window)
    
    while(True):
        
        circle = make_circle()

        circle.draw(window)

        centerx = circle.getCenter().x
        centery = circle.getCenter().y
        
        while True:
            click = window.getMouse()
            if get_distance(click.x, centerx, click.y, centery) <= circle.radius:
                break
        
        update_score(circle, scoretext)
        circle.undraw()

if __name__ == "__main__":
    main()

