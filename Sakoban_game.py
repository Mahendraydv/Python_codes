import curses

# initialize curses screen
screen = curses.initscr()

# set up screen parameters
curses.noecho()
curses.curs_set(0)
screen.keypad(True)

# create the game board
board = [
    "#####",
    "#   #",
    "#   #",
    "#   #",
    "#   #",
    "#   #",
    "#   #",
    "#   #",
    "#   #",
    "#####"
]

# create the player
player = {
    "x": 1,
    "y": 1
}

# create the box
box = {
    "x": 3,
    "y": 3
}

# game loop
while True:
    # draw the board
    for y, row in enumerate(board):
        for x, char in enumerate(row):
            if x == player["x"] and y == player["y"]:
                screen.addstr(y, x, "@")
            elif x == box["x"] and y == box["y"]:
                screen.addstr(y, x, "$")
            else:
                screen.addstr(y, x, char)
    
    # get user input
    key = screen.getch()
    
    # move player
    if key == curses.KEY_UP:
        if board[player["y"]-1][player["x"]] != "#":
            player["y"] -= 1
    elif key == curses.KEY_DOWN:
        if board[player["y"]+1][player["x"]] != "#":
            player["y"] += 1
    elif key == curses.KEY_LEFT:
        if board[player["y"]][player["x"]-1] != "#":
            player["x"] -= 1
    elif key == curses.KEY_RIGHT:
        if board[player["y"]][player["x"]+1] != "#":
            player["x"] += 1
    
    # move box
    if player["x"] == box["x"] and player["y"] == box["y"]:
        if key == curses.KEY_UP:
            if board[box["y"]-1][box["x"]] != "#":
                box["y"] -= 1
        elif key == curses.KEY_DOWN:
            if board[box["y"]+1][box["x"]] != "#":
                box["y"] += 1
        elif key == curses.KEY_LEFT:
            if board[box["y"]][box["x"]-1] != "#":
                box["x"] -= 1
        elif key == curses.KEY_RIGHT:
            if board[box["y"]][box["x"]+1] != "#":
                box["x"] += 1
    
    # check for win condition
    if box["x"] == 7 and box["y"] == 8:
        break

# end curses screen
curses.endwin()
print("You won!")