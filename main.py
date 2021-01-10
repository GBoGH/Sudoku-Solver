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
                self.grid[i][j] = tk.Entry(root,
                                           width=2,
                                           font=("Arial", 20),
                                           bg=color,
                                           borderwidth=1,
                                           textvar=self.numbers_input[i][j], cursor="arrow")
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
        solution = Solve()


numbers_input = []
for i in range(9):
    numbers_input.append([0, 0, 0, 0, 0, 0, 0, 0, 0])

for i in range(9):
    for j in range(9):
        numbers_input[i][j] = tk.StringVar(root)


class Solve():
    def __init__(self):
        self.fill_zero()
        self.solve()

    def fill_zero(self):
        for i in range(9):
            for j in range(9):
                if numbers_input[i][j].get() not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                    numbers_input[i][j].set(0)

    def empty(self):
        for i in range(9):
            for j in range(9):
                if numbers_input[i][j].get() == "0":
                    return (i, j)
        return None

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

        for i in range(box_y * 3, box_y * 3 + 3):
            for j in range(box_x * 3, box_x * 3 + 3):
                if numbers_input[i][j].get() == str(number) and (i, j) != coor:
                    return False

        return True

    def solve(self):
        empty_field = self.empty()

        if not empty_field:
            return True
        else:
            row, col = empty_field

        for i in range(1, 10):
            if self.possible(i, (row, col)):
                numbers_input[row][col].set(i)

                if self.solve():
                    return True

                numbers_input[row][col].set("0")

        return False


Draw(root, numbers_input)

tk.mainloop()
