import tkinter as tk

def main():
    screen_width = 400
    screen_height = 400

    window = tk.Tk()
    window.title("Sudoku Solver")
    canvas = tk.Canvas(width=screen_width, height=screen_height)
    canvas.pack()

    canvas.create_text(200, 25, text="Enter numbers and press Submit")

    black = (0,0,0)

    x = 87.5
    for i in range(9):
        y = 50
        for j in range(9):
            entry = tk.Entry()
            canvas.create_window(x, y, anchor="nw", window=entry, height=20, width=20)
            y += 25
        x += 25

    y = 47
    for i in range(10):
        if i % 3 == 0 or i == 0:
            width = 5
        else:
            width = 2
        canvas.create_line(82, y, 312, y, width=width)
        y += 25

    x = 84
    for i in range(10):
        if i % 3 == 0 or i == 0:
            width = 5
        else:
            width = 2
        canvas.create_line(x, 45, x, 275, width=width)
        x += 25

    tk.mainloop()

main()