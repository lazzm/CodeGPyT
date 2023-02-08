import tkinter as tk
import random

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Bouncing Square")
        self.geometry("500x300")
        self.resizable(False, False)
        self.canvas = tk.Canvas(self, width=500, height=300, bg="black")
        self.canvas.pack()
        self.square = self.canvas.create_rectangle(0, 0, 50, 50, fill="blue")
        self.x = 0
        self.y = 0
        self.dx = 1
        self.dy = 1
        self.colors = ["blue", "red", "green", "yellow", "white"]
        self.after(10, self.update)

    def update(self):
        self.x += self.dx
        self.y += self.dy
        if self.x < 0 or self.x > 450:
            self.dx *= -1
            self.canvas.itemconfig(self.square, fill=random.choice(self.colors))
        if self.y < 0 or self.y > 250:
            self.dy *= -1
            self.canvas.itemconfig(self.square, fill=random.choice(self.colors))
        self.canvas.move(self.square, self.dx, self.dy)
        self.after(10, self.update)

if __name__ == "__main__":
    app = App()
    app.mainloop()
