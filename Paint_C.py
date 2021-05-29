#Part C
from graphics import *

class Shape:
    def __init__(self, win):
        self.win = win
        
    def line(self):
        T1 = Text(Point(400, 50), "Line: Enter 2 points")
        T1.setSize(8)
        T1.draw(self.win)
        p1 = self.win.getMouse()
        p1.draw(self.win)
        p2 = self.win.getMouse()
        p2.draw(self.win)
        l = Line(p1, p2)
        l.draw(self.win)
        T1.undraw()
        p1.undraw()
        p2.undraw()
        T2 = Text(Point(400, 50), "Line: Color Line(A-J), u to undo, and q to break")
        T2.setSize(8)
        T2.draw(self.win)
        while True:
            k = self.win.checkKey()
            if k == "q":
                break
            elif k == "u":
                l.undraw()
                break
            elif k:
                ColorO(k, l)
        T2.undraw()
    
    def rectangle(self):
        T1 = Text(Point(400, 50), "Rectangle: Enter 2 points")
        T1.setSize(8)
        T1.draw(self.win)
        p1 = self.win.getMouse()
        p1.draw(self.win)
        p2 = self.win.getMouse()
        p2.draw(self.win)
        r = Rectangle(p1, p2)
        r.draw(self.win)
        T1.undraw()
        p1.undraw()
        p2.undraw()
        T2 = Text(Point(400, 50), "Rectangle: Color Shape(0-9), Color Line(A-J), u to undo, and q to break")
        T2.setSize(8)
        T2.draw(self.win)
        while True:
            k = self.win.checkKey()
            if k == "q":
                break
            elif k == "u":
                r.undraw()
                break
            elif k:
                ColorS(k, r)
                ColorO(k, r)
        T2.undraw()
    

    def circle(self):
        T1 = Text(Point(400, 50), "Circle: Enter point")
        T1.setSize(8)
        T1.draw(self.win)
        p1 = self.win.getMouse()
        c = Circle(p1, 50)
        c.draw(self.win)
        T1.undraw()
        T2 = Text(Point(400, 50), "Circle:Color Shape(0-9), Color Line(A-J), u to undo, and q to break")
        T2.setSize(8)
        T2.draw(self.win)
        while True:
            k = self.win.checkKey()
            if k == "q":
                break
            elif k == "u":
                c.undraw()
            elif k:
                ColorS(k, c)
                ColorO(k, c)
        T2.undraw()
    
    def oval(self):
        T1 = Text(Point(400, 50), "Oval: Enter 2 points")
        T1.setSize(8)
        T1.draw(self.win)
        p1 = self.win.getMouse()
        p2 = self.win.getMouse()
        p1.draw(self.win)
        p2.draw(self.win)
        O = Oval(p1, p2)
        O.draw(self.win)
        T1.undraw()
        p1.undraw()
        p2.undraw()
        T2 = Text(Point(400, 50), "Oval: Color Shape(0-9), Color Line(A-J), u to undo, and q to break")
        T2.setSize(8)
        T2.draw(self.win)
        while True:
            k = self.win.checkKey()
            if k == "q":
                break
            elif k == "u":
                c.undraw()
            elif k:
                ColorS(k, O)
                ColorO(k, O)
        T2.undraw()

    def triangle(self):
        T1 = Text(Point(400, 50), "Triangle: Enter 3 points")
        T1.setSize(8)
        T1.draw(self.win)
        p1 = self.win.getMouse()
        p1.draw(self.win)
        p2 = self.win.getMouse()
        p2.draw(self.win)
        p3 = self.win.getMouse()
        p3.draw(self.win)
        t = Polygon(p1, p2, p3)
        t.draw(self.win)
        T1.undraw()
        p1.undraw()
        p2.undraw()
        p3.undraw()
        T2 = Text(Point(400, 50), "Triangle: Color Shape(0-9), Color Line(A-J), u to undo, and q to break")
        T2.setSize(8)
        T2.draw(self.win)
        while True:
            k = self.win.checkKey()
            if k == "q":
                break
            elif k == "u":
                t.undraw()
            elif k:
                ColorS(k, t)
                ColorO(k, t)
        T2.undraw()

        
    def ColorS(C, win):
        if C == "0":
            win.setFill("white")
        elif C == "1":
            win.setFill("black")
        elif C == "2":
            win.setFill("red")
        elif C == "3":
            win.setFill("blue")
        elif C == "4":
            win.setFill("yellow")
        elif C == "5":
            win.setFill("green")
        elif C == "6":
            win.setFill("orange")
        elif C == "7":
            win.setFill("purple")
        elif C == "8":
            win.setFill("pink")
        elif C == "9":
            win.setFill("gray")

    def ColorO(C, win):
        if C == "A":
            win.setOutline("white")
        elif C == "B":
            win.setOutline("black")
        elif C == "C":
            win.setOutline("red")
        elif C == "D":
            win.setOutline("blue")
        elif C == "E":
            win.setOutline("yellow")
        elif C == "F":
            win.setOutline("green")
        elif C == "G":
            win.setOutline("orange")
        elif C == "H":
            win.setOutline("purple")
        elif C == "I":
            win.setOutline("pink")
        elif C == "J":
            win.setOutline("gray")

def Color(C, win):
    if C == "A":
        win.setBackground("white")
    elif C == "B":
        win.setBackground("black")
    elif C == "C":
        win.setBackground("red")
    elif C == "D":
        win.setBackground("blue")
    elif C == "E":
        win.setBackground("yellow")
    elif C == "F":
        win.setBackground("green")
    elif C == "G":
        win.setBackground("orange")
    elif C == "H":
        win.setBackground("purple")
    elif C == "I":
        win.setBackground("pink")
    elif C == "J":
        win.setBackground("gray")
        
def TextS(pt, win):
    entry = Entry(pt, 10)
    entry.draw(win)
# Go modal: wait until user types Return or Escape Key
    while True:
        key = win.getKey()
        if key == "Return":
            break
# undraw the entry and draw Text
    entry.undraw()
    Text(pt, entry.getText()).draw(win)
    win.checkMouse() 
        
def main():
    win = GraphWin('Paint', 800, 800)
    T1 = Text(Point(400, 25), "keys: l - line, r - rectangle, c - circle, o - oval, t - triangle, q - quit")
    T1.setSize(8)
    T1.draw(win)
    S = Shape(win)
    while True:
            key = win.checkKey() 
            if key == "q": # loop exit 
                break 
            elif key == "l":
                S.line()
            elif key == "r":
                S.rectangle()
            elif key == "c":
                S.circle()
            elif key == "o":
                S.oval()
            elif key == "t" : 
                S.triangle() 
            elif key:
                Color(key, win)
            
            pt = win.checkMouse()
            if pt:
                TextS(pt, win)
    win.close()

if __name__ == '__main__': main()
