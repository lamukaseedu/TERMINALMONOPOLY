# monopoly notes
"""
turn based game, goal is to make money from other players while not going bankrupt
each turn player rolls 2 die, move around board clockwise
start on go (BR), 200 collected for passing
land on property, able to buy it if you can afford it
land on others' property, pay defined rent amount
rent can be increased by buying houses
utility/railroad: fixed rent, increases depending on other owned utility/railroad (seperate)
roll doubles, roll again, if 3 in a row go to jail tile, done collect money
jail: cant leave until you roll doubles or 3 turns
community chest/chance: given a card that may or may not benefit/move player
"""

# board info
"""
notes:
blue is comm chest
orange is chance
dark grey are railroads
SOMETHING are utilities
BR is go
BL is jail
TL is free parking
TR is go to jail
the color of the bottom right of a tile corresponds to player color
the  number of green voxels following that correspond to number of other util/railroads owned or number of houses
players represented by a colored tile with circle   '
"""

#notes for implementation
"""
- must be skipable
- possibly add additional argument for starting game without getting tutorial screen/question
- info section on different screens, enter to continue to next section screen
"""


import screenspace as ss
from style import COLORS
import style

cols = ss.WIDTH
rows = ss.HEIGHT
graphics = style.get_graphics()

def print_tutorial_screen(cols:int, rows:int, title:str, obj_list:list[dict]) -> None:
    """
    Parameters:
    cols (int): number of columns in the terminal
    rows (int): number of rows in the terminal
    title (str): text to go inline with the screen border
    obj_list (list[dict]): a list of dictionary objects with all text to render to the screen
        "col" (int): x position of the object
        "row" (int): y position of the object
        "num_lines" (int): the number of rows that the object takes up
        "text" (str): the text to render to the screen 

    Renders a tutorial screen to the terminal with a title and a list of objects to render to the screen.
        Currently, can only be the light gray color. (support for custom coloring may be added later)

    Returns:
    None
    """
    screen_content = []

    title_padding = cols//2 - len(title)//2 - 1

    if (len(obj_list) > 0):
        pass
    
    screen_content.append(COLORS.LIGHTGRAY+'╔' + ('═' * title_padding) + " " + title + " " + ('═' * (title_padding - (len(title)%2 == 1) * 1)) + '╗' + "   ")

    #split all text objects into a list of lines
    for obj in obj_list:
        temp = obj["text"].split("\n")
        obj["text"] = temp

    for y in range(1, rows):
        screen_content.insert(y, "") #initializes index
        screen_content[y] = screen_content[y] + COLORS.LIGHTGRAY + "║ "

        for obj in obj_list:
            if obj["row"] <= y and y <= obj["row"] + obj["num_lines"]:
                screen_content[y] = screen_content[y] + (" " * (obj["col"] + len(COLORS.LIGHTGRAY) - len(screen_content[y])))
                screen_content[y] = screen_content[y] + obj["text"][y - obj["row"]]

        #fill in remaining empty space
        screen_content[y] = screen_content[y] + (" " * (cols + len(COLORS.LIGHTGRAY) - len(screen_content[y]))) + " ║"

    #print bottom border with title
    screen_content.append(COLORS.LIGHTGRAY+'╚' + ('═' * title_padding) + " " + title + " " + ('═' * (title_padding - (len(title)%2 == 1) * 1)) + '╝' + "   ")

    print("\033[1A" * (rows + 4), end='\r') #reset cursor to top left
    for row in screen_content:
        print(row)

    input("Press Enter to continue...")


print_tutorial_screen(cols, rows, "Terminal Monopoly 1", [
    {"col": 3, "row": 2, "num_lines": 0, "text":"Welcome to:"},
    {"col": 10, "row": 5, "num_lines": 17, "text":graphics["logo"]}
])

# Fills the rest of the terminal
print(' ' * ss.WIDTH, end='\r')

