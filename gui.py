import tkinter as tk

root = tk.Tk()
root.geometry("305x365")


class Draw():

    def __init__(self, root, numbers_input):
        self.root = root
        self.grid = []
        self.numbers_input = numbers_input

        root.title("Sudoku Solver")

        for i in range(9):
            self.grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])

        for i in range(9):
            for j in range(9):
                if (3 <= i <= 5) and (j < 3 or j > 5):
                    color = "grey"
                elif (i < 3 or i > 5) and (3 <= j <= 5):
                    color = "grey"
                else:
                    color = "white"
                self.grid[i][j] = tk.Entry(root, width=2, font=(
                    "Arial", 20), bg=color, borderwidth=1,
                    textvar=self.numbers_input[i][j])
                self.grid[i][j].bind("<FocusOut>", self.correct_input)
                self.grid[i][j].grid(row=i, column=j)

        clear = tk.Button(root, bg="grey", text="Clear", font=(
            "Arial", 10), fg="black", command=self.clear_board)
        clear.place(x=102, y=330)

        solve = tk.Button(root, bg="grey", text="Solve", font=(
            "Arial", 10), fg="black", command=self.solve)
        solve.place(x=162, y=330)

    def correct_input(self, event):
        for i in range(9):
            for j in range(9):
                if len(self.numbers_input[i][j].get()) > 1:
                    self.numbers_input[i][j].set("")
                if self.numbers_input[i][j].get() not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                    self.numbers_input[i][j].set("")

    def clear_board(self):
        for i in range(9):
            for j in range(9):
                self.numbers_input[i][j].set("")

    def solve(self):
        ""


def draw_grid():

    numbers_input = []
    for i in range(9):
        numbers_input.append([0, 0, 0, 0, 0, 0, 0, 0, 0])

    for i in range(9):
        for j in range(9):
            numbers_input[i][j] = tk.StringVar(root)

    Draw(root, numbers_input)
    tk.mainloop()


draw_grid()
