import tkinter as tk
from modules import RulerModule


class App:
    def __init__(self, master, width, height):
        self.frame = tk.Frame(master=master, width=width, height=height)
        self.frame.pack()
        self.canvas = tk.Canvas(master=self.frame, width=width,
                                height=height, background="#000000")
        self.canvas.pack()
        self.primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,
                       41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        self.prime_axis = RulerModule(self.primes, "#800080", 5, 15, 20)
        self.from_ = 0
        self.to = 10
        self.right = True
        self.mainloop()

    def mainloop(self):
        if self.right:
            self.from_ += 0.1
            self.to += 0.1
            if self.to > 100:
                self.right = False
        else:
            self.from_ -= 0.1
            self.to -= 0.1
            if self.from_ < 0:
                self.right = True

        self.prime_axis.render_region(
            self.from_, self.to, self.canvas, 960, 540)
        self.canvas.after(100, self.mainloop)


root = tk.Tk()
root.resizable(False, False)
app = App(root, 960, 540)
root.mainloop()
