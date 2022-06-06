import sys
import PySimpleGUI as sg
import webbrowser
import os

"""
Potential Themes:

DarkTeal
DarkGrey2
DarkBlue2
"""

theme = "DarkGrey2"
sg.theme(theme)
font = ("Arial", 14)

layout = [
    # 4 9 16 25
    [sg.Text('What size do you want 4x4(2), 9x9(3)?', font=font)],
    [sg.Slider(orientation='h',tick_interval=1, font=font, key='-SIZE-', range=(2, 5))],
    [sg.HorizontalSeparator()],
    [sg.Text('How many batches do you want?', font=font)],

    [sg.Spin([i for i in range(1, 101)], font=font, initial_value=1, key="-INPUT-",
             size=(5, 2)), sg.Text('No. of Sudokus (1-100)', font=font)],

    [sg.HorizontalSeparator()],
    [sg.Text('What difficulty do you want?', font=font)],

    [sg.Radio('Easy', "Radiobtns", default=True, size=(9, 1), k='-R1-', font=font),
     sg.Radio('Medium', "Radiobtns", default=True, size=(9, 1), k='-R2-', font=font),
     sg.Radio('Hard', "Radiobtns", default=True, size=(9, 1), k='-R3-', font=font)],

    [sg.HorizontalSeparator()],
    [sg.Text('What mode do you want?', font=font)],

    [sg.Radio('Normal', "Radiobtns_1", default=False, size=(10, 1), k='-R4-', font=font),
     sg.Radio('Manual Save', "Radiobtns_1", default=True, size=(13, 1), k='-R5-', font=font)],

    [sg.HorizontalSeparator()],

    [sg.Button('Submit', key="-SUBMIT-", font=font, size=(9, 1)),
     sg.Button('Exit', key="-EXIT-", font=font, size=(9, 1))],

    [sg.HorizontalSeparator()],

    [sg.Button('Open Dir', key="-OPEN-", font=font, size=(9, 1)),
     sg.Button('Help', key="-HELP-", font=font, size=(9, 1))],


]

window = sg.Window('SUDOKU MAKER 3000 V2', layout, grab_anywhere=True,
                   element_justification="c", resizable=True)


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == "-OPEN-":
        if os.path.exists("/Users/tharun/Desktop/SDD MAJOR WORK2/Sudokus"):
            webbrowser.open("file:///Users/tharun/Desktop/SDD MAJOR WORK2/Sudokus")
        else:
            sg.Popup("Directory has not been made yet."
                     "\nDirectory will be automatically made and local stored into this folder.",
                     font=font, keep_on_top=True)

    if event == "-HELP-":
        sg.Popup(f"--/GUIDE\-- By Tharun Yogenthra\n\n--INTRODUCTION--\n"
                 
                 f"In this small guide I will be going over the most important features of this program. "
                 f"In short this program generates sudokus of certain variables (will be explained later in further detail) and saves them in a local folder. "
                 f"This window is moveable so adjust to what feels the best for you. "
                 
                 f"\n\n--SIZE (input = slider)--\n"
                 
                 f"The slider is there to let you input a size for your sudoku. "
                 f"For example if you want a 4x4 sudoku you put 2 on the slider, 9x9 you put 3 and so on. "
                 
                 f"\n\n--BATCHES (input = spin)--\n"
                 
                 f"Batches refers to how many times you want to program to loop to produce new sudokus. "
                 f"In this input field a user can either use the arrows to go higher or lower or manually type in how many sudokus they want. "
                 f"The max times the code can repeat itself is 100 times due to performance problems. "
                 
                 f"\n\n--Difficulty (input = radio buttons)--\n"
                 
                 f"The options for difficulty determine how many numbers (in the sudoku cells) will get removed from a sudoku. "
                 f"This value is of course scalable to the size of the sudoku. "
                 
                 f"\n\n--Mode(input = radio buttons)--\n"
                 
                 f"As you know these sudokus are saved to a local folder and also not all sudokus are made equally. "
                 f"Normal mode is pretty self explanatory as the code just loops without any interruptions or user prompts which will be ideal is bulk making many sudokus. "
                 f"Manual mode is where after every sudoku is generated there will be a popup will prompts the user if they want to delete of save that certain sudoku. "
                 
                 f"\n\n--Remaining 4 buttons on the bottom (input = buttons)--\n"
                 
                 f"Submit - is what you use after inputting all necessary information and will start the program. "
                 f"Exit - is pretty self explanatory. "
                 f"Open dir - is a button that open the local saved sudoku directory so the user can view/edit the sudokus. "
                 f"Help - I am hoping you know what this means. If not how did you get here???"

                 , font=font, grab_anywhere=True, keep_on_top=True, line_width=100)


    if event == "-SUBMIT-":
        base, times, c, d, e, f, g = int(values["-SIZE-"]), values["-INPUT-"], \
                                     values["-R1-"], values["-R2-"],\
                                  values["-R3-"], values["-R4-"], values["-R5-"]
        # c,d,e,f,g are all radio button variables

        if str(times).isdigit() is True:
            # Exception handling for negative numbers as they use "-" which is a char and also letters
            if int(times) == 0 or int(times) > 100:  # Exception handling for float numbers and values < 0 and > 100
                sg.popup("Input can not be < 1 or > 100.\nPlease enter a valid number", font=font, title="Invalid Input")
                continue
        else:
            sg.popup("Input can not have characters e.g.[. , - , abcedfg].\nPlease enter a valid number", font=font, title="Invalid Input")
            continue

        if c == True:
            difficulty = "E"

        if d == True:
            difficulty = "M"

        if e == True:
            difficulty = "H"

        if f == True:
            mode = "normal"
            sg.Popup(f"You picked base = {base**2}\nYou picked times = {times}\nYou picked {difficulty} difficulty\n"
                     f"You picked {mode} mode"
                     , keep_on_top=True, font=font, title="Inputs STDOUT")
            window.close()

        if g == True:
            mode = "inst save"
            sg.Popup(f"You picked base = {base}\nYou picked times = {times}\nYou picked {difficulty} difficulty\n"
                     f"You picked {mode} mode"
                     , keep_on_top=True, font=font, title="Inputs STDOUT")
            window.close()

    if event == "-EXIT-":
        sg.Popup("Thank you for using this Generator\n\n-From Tharun Yogenthra", font=font, title="Bye Bye")
        sys.exit()

