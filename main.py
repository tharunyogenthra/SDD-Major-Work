# add failsafe
# edit difficulties (MAJOR PROBLEM)
# add cross platform
import random
import PySimpleGUI as sg
from random import sample
import pprint
import turtle
import math
import os
from guiapplication import base, times, difficulty, mode
from datetime import datetime


# initial set up

t = turtle.Turtle()
t.speed(0)
WIDTH, HEIGHT = 1100, 1100
ts = turtle.Screen()
ts.setup(WIDTH, HEIGHT)
ts.title("Sudoku Machine 3000")
rows, column, sizeMultiplier = 0, 0, 40
style = ('Times New Roman', sizeMultiplier // 2, 'normal')


def gotoCoords(x, y):
    t.penup()
    t.goto(columns * sizeMultiplier / -2 + sizeMultiplier * x,
           rows * sizeMultiplier / -2 + sizeMultiplier * y)
    t.pendown()


def makeBorders():
    t.penup()
    t.goto(columns*sizeMultiplier/-2, rows*sizeMultiplier/-2)
    t.pendown()
    t.pensize(5)
    for _ in range(2):
        t.fd(sizeMultiplier*columns)
        t.left(90)
        t.fd(sizeMultiplier*rows)
        t.left(90)
    t.pensize(1)


def drawGrid(grid, colour):
    t.hideturtle()
    t.pencolor("black")
    t.penup()

    global rows
    global columns
    rows = len(grid)
    columns = len(grid[0])

    makeBorders()
    subSquareLength = int(math.sqrt(rows))
    for i in range(rows + 1):
        if i % subSquareLength == 0:
            t.pensize(5)
        else:
            t.pensize(1)
        t.penup()
        t.goto(columns * sizeMultiplier / -2, (rows * sizeMultiplier / -2) + sizeMultiplier * i)                        # Change so code can work for windows
        t.pendown()
        t.fd(sizeMultiplier * rows)
    t.setheading(90)

    for i in range(columns + 1):
        if i % subSquareLength == 0:
            t.pensize(5)
        else:
            t.pensize(1)
        t.penup()
        t.goto(columns * sizeMultiplier / -2 + sizeMultiplier * i, (rows * sizeMultiplier / -2))
        t.pendown()
        t.fd(sizeMultiplier * columns)
    t.setheading(0)
    t.pencolor(colour)
    for rowNo in range(rows):
        for columnNo in range(columns):
            gotoCoords(columnNo + 0.5, rows - rowNo - 1)
            t.write(grid[rowNo][columnNo], font=style, align="center")


if __name__ == "__main__":

    base = int(base)
    times = int(str(times))
    mode = str(mode)
    print(
        f"You picked {base ** 2}x{base ** 2} Sudokus /"
        f" You picked {times} batches /"
        f" You picked {difficulty.upper()} sudokus")
    print("Starting program...")
    for j in range(times):

        now = datetime.now()
        dt_string = now.strftime("(%d.%m) [%H:%M:%S]")

        if (os.path.exists(f"/Users/tharun/Desktop/SDD MAJOR WORK2/Sudokus")) == True:
            pass
        else:
            directory = "Sudokus"
            parent_dir = "/Users/tharun/Desktop/SDD MAJOR WORK2"
            path = os.path.join(parent_dir, directory)
            os.makedirs(path)

        side = base ** 2
        lst = list()
        counter = 0
        if difficulty.lower() == "e":
            limit = (side ** 2)/4 * 3/2
        if difficulty.lower() == "m":             # side ==4
            limit = (side ** 2)/4 * 3/1.5
        if difficulty.lower() == "h":
            limit = (side ** 2)/4 * 3

        def pattern(r, c):
            return (base * (r % base) + r // base + c) % side                                                           # 1

        def shuffle(s):
            return sample(s, len(s))                                                                                    # 2

        # cite this
        rBase = range(base)
        rows = []
        cols = []
        board = []

        for g in shuffle(rBase):
            for r in shuffle(rBase):
                rows.append(g*base + r)                                                                                 # no idea what the fuck it means

        for g in shuffle(rBase):
            for c in shuffle(rBase):
                cols.append(g*base + c)

        nums = shuffle(range(1, base**2+1))                                                                             # 5

        board = [[nums[pattern(r, c)] for c in cols] for r in rows]                                                     # 6

        drawGrid(board, "red")
        gotoCoords(base, -1)
        t.write("Solution", font=style, align="center")

        if (os.path.exists("/Users/tharun/Desktop/SDD MAJOR WORK2/Sudokus/Answers")) == True:
            pass
        else:
            directory = "Answers"
            parent_dir = "/Users/tharun/Desktop/SDD MAJOR WORK2/Sudokus"
            path = os.path.join(parent_dir, directory)
            os.makedirs(path)

        ts.getcanvas().postscript(file="/Users/tharun/Desktop/SDD MAJOR WORK2/Sudokus/Answers/"
                                       + "[" + str(difficulty.upper()) + "]" + "-" + "{" + str(base ** 2) + "x"
                                       + str(base**2) + "}" + "_" + dt_string + ".ps")

        turtle.clearscreen()

        for x in board:
            lst += x

        while counter < limit:                      # max things that can be removed from a sudoku
            i = random.randint(0, base**4-1)
            if lst[i] == 0:
                continue
            else:
                lst[i] = 0
            counter += 1

        for i in range(len(lst)):   # making so zeros dont appear on sudoku and replace them with nothing
            if lst[i] == 0:
                lst[i] = ''
                continue

        grid = [lst[i:i + (base ** 2)] for i in range(0, len(lst), (base ** 2))]                                        # 7
        pprint.pprint(board)
        pprint.pprint(grid)
        print("\n")

        drawGrid(grid, "black")  # writing solveable on the bottom of maze
        gotoCoords(base, -1)
        t.write("Solveable", font=style, align="center")
        ts = turtle.Screen()

        if (os.path.exists("/Users/tharun/Desktop/SDD MAJOR WORK2/Sudokus/BlankSudoku/")) == True:
            pass
        else:
            directory = "BlankSudoku"
            parent_dir = f"/Users/tharun/Desktop/SDD MAJOR WORK2/Sudokus"
            path = os.path.join(parent_dir, directory)
            os.makedirs(path)

        ts.getcanvas().postscript(file=f"/Users/tharun/Desktop/SDD MAJOR WORK2/Sudokus/BlankSudoku/" +
                                       "[" + str(difficulty.upper()) + "]" + "-" + "{" + str(base ** 2) +
                                       "x" + str(base ** 2) + "}" + "_" + dt_string + ".ps")

        if mode == "inst save":
            sg.theme("Reddit")
            layout = [
                [sg.Text('Do you want to save this sudoku?', font=("Arial", 14))],
                [sg.Radio('Save', "Radiobtns", default=False, size=(10, 1), k='-R1-', font=("Arial", 14)),
                 sg.Radio('Discard', "Radiobtns", default=True, size=(10, 1), k='-R2-', font=("Arial", 14))],
                [sg.Button('Submit', key="-SUBMIT-", font=("Arial", 14))],
            ]

            window = sg.Window('Decider', layout, auto_size_text=True, location=(635, 600), element_justification="c")

            while True:
                event, values = window.read()
                if event == sg.WIN_CLOSED:
                    break

                if event == "-SUBMIT-":
                    a, b = values["-R1-"], values["-R2-"]
                    if a == True:
                        saveVar = "y"
                        window.close()
                    if b == True:
                        saveVar = "n"
                        window.close()

            if saveVar == "n":
                print("Sudoku discarded")
                if os.path.exists("/Users/tharun/Desktop/SDD MAJOR WORK2/Sudokus/Answers/"
                                  + "[" + str(difficulty.upper()) + "]" + "-" + "{" + str(base ** 2)
                                  + "x" + str(base ** 2) + "}" + "_" + dt_string + ".ps"):

                    os.remove("/Users/tharun/Desktop/SDD MAJOR WORK2/Sudokus/Answers/"
                              + "[" + str(difficulty.upper()) + "]" + "-" + "{" + str(base ** 2)
                              + "x" + str(base ** 2) + "}" + "_" + dt_string + ".ps")

                if os.path.exists("/Users/tharun/Desktop/SDD MAJOR WORK2/Sudokus/BlankSudoku/"
                                  + "[" + str(difficulty.upper()) + "]" + "-" + "{" + str(base ** 2)
                                  + "x" + str(base ** 2) + "}" + "_" + dt_string + ".ps"):
                    os.remove("/Users/tharun/Desktop/SDD MAJOR WORK2/Sudokus/BlankSudoku/"
                              + "[" + str(difficulty.upper()) + "]" + "-" + "{" + str(base ** 2)
                              + "x" + str(base ** 2) + "}" + "_" + dt_string + ".ps")

            if saveVar.lower() == "y":
                print("Sudoku saved")

        img_folder_path = '/Users/tharun/Desktop/SDD MAJOR WORK2/Sudokus/Answers'
        dirListing = os.listdir(img_folder_path)

        turtle.clearscreen()

    print("\n\nYou have " + str((len(dirListing))) + " sudoku(s)")
    print("Ending program...")
