import tkinter as tk

# Window and its dimensions.
root = tk.Tk()
root.geometry("305x365")

# Class for drawing the window.
class Draw():

    # Class initialization.
    def __init__(self, root, numbers_input):
        self.root = root
        self.grid = []
        self.numbers_input = numbers_input

        # Windows title.
        root.title("Sudoku Solver")

        # Creating empty list (grid).
        for i in range(9):
            self.grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])

        # Drawing the input squares.
        for i in range(9):
            for j in range(9):
                # Chosing the color based on position.
                if (3 <= i <= 5) and (j < 3 or j > 5):
                    color = "grey"
                elif (i < 3 or i > 5) and (3 <= j <= 5):
                    color = "grey"
                else:
                    color = "white"
                # Drawing the input squares.
                self.grid[i][j] = tk.Entry(root, width=2, font=("Arial", 20),
                                           bg=color, borderwidth=1,
                                           textvar=self.numbers_input[i][j],cursor="arrow")
                # Deleting input when input is invalid and user moves mouse.
                self.grid[i][j].bind("<FocusOut>", self.correct_input)
                # Organizing squares into a grid in tkinter
                self.grid[i][j].grid(row=i, column=j)

        # Button for clearing the board.
        clear = tk.Button(root, bg="grey", text="Clear", font=(
            "Arial", 10), fg="black", command=self.clear_board)
        clear.place(x=102, y=330)

        # Button to solve the sudoku.
        solve = tk.Button(root, bg="grey", text="Solve", font=(
            "Arial", 10), fg="black", command=self.solve)
        solve.place(x=162, y=330)

    # Function for correcting the input
    def correct_input(self, event):
        for i in range(9):
            for j in range(9):
                # Deletes the value if the input does not imply to conditions
                if len(self.numbers_input[i][j].get()) > 1:
                    self.numbers_input[i][j].set("")
                if self.numbers_input[i][j].get() not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                    self.numbers_input[i][j].set("")

    # Function to clear the board.
    def clear_board(self):
        for i in range(9):
            for j in range(9):
                self.numbers_input[i][j].set("")

    # Function to solve the sudoku (call the solve Class)
    def solve(self):
        solution = Solve()


# Fill inputed number with zeros.
numbers_input = []
for i in range(9):
    numbers_input.append([0, 0, 0, 0, 0, 0, 0, 0, 0])

# Add input from the user to the list.
for i in range(9):
    for j in range(9):
        numbers_input[i][j] = tk.StringVar(root)


class Solve():
    def __init__(self):
        self.fill_zero()
        self.solve()

    # Input zeros into empty fields
    def fill_zero(self):
        for i in range(9):
            for j in range(9):
                if numbers_input[i][j].get() not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                    numbers_input[i][j].set(0)

    # Return coorindates of empty field.
    def empty(self):
        for i in range(9):
            for j in range(9):
                if numbers_input[i][j].get() == "0":
                    return (i, j)
        # If no empty field is found, nothing is returned.
        return None

    # Check possible numbers in one position.
    def possible(self, number, coor):

        # Check Row.
        for i in range(9):
            if numbers_input[coor[0]][i].get() == str(number) and coor[1] != i:
                return False

        # Check Column.
        for i in range(9):
            if numbers_input[i][coor[1]].get() == str(number) and coor[0] != i:
                return False

        # Check Square.
        box_x = coor[1] // 3
        box_y = coor[0] // 3

        # Check in 3x3 coordinates.
        for i in range(box_y * 3, box_y * 3 + 3):
            for j in range(box_x * 3, box_x * 3 + 3):
                if numbers_input[i][j].get() == str(number) and (i, j) != coor:
                    return False

        return True

    # Function to solve sudoku using backtracking.
    def solve(self):
        empty_field = self.empty()

        # If nothing is empty, end the solving.
        if not empty_field:
            return True
        # Else find the coordinates of the empty field
        else:
            row, col = empty_field

        # If the number is possible, put it in the position.
        for i in range(1, 10):
            if self.possible(i, (row, col)):
                numbers_input[row][col].set(i)

                # End the function if nothing remains empty.
                if self.solve():
                    return True

                # If nothing is possible, go back.
                numbers_input[row][col].set("0")

        return False

# Class initialization.
Draw(root, numbers_input)

# Tkinter ending the program.
tk.mainloop()
