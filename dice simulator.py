import random
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class DiceRoller(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.parent.title('Dice Roller')
        self.parent.geometry('400x300')
        self.parent.resizable(False, False)
        self.create_widgets()

    def create_widgets(self):
        # Number of dice
        self.num_dice_label = ttk.Label(self, text='Number of dice:')
        self.num_dice_label.grid(row=0, column=0, padx=5, pady=5)
        self.num_dice_entry = ttk.Entry(self)
        self.num_dice_entry.insert(0, '1')
        self.num_dice_entry.grid(row=0, column=1, padx=5, pady=5)

        # Number of sides
        self.num_sides_label = ttk.Label(self, text='Number of sides:')
        self.num_sides_label.grid(row=1, column=0, padx=5, pady=5)
        self.num_sides_entry = ttk.Entry(self)
        self.num_sides_entry.insert(0, '6')
        self.num_sides_entry.grid(row=1, column=1, padx=5, pady=5)

        # Roll button
        self.roll_button = ttk.Button(self, text='Roll', command=self.roll_dice)
        self.roll_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        # Roll results
        self.roll_results_label = ttk.Label(self, text='Roll results:')
        self.roll_results_label.grid(row=3, column=0, padx=5, pady=5)
        self.roll_results_text = tk.Text(self, height=5, width=20)
        self.roll_results_text.grid(row=3, column=1, padx=5, pady=5)

        # Histogram
        self.histogram_label = ttk.Label(self, text='Roll histogram:')
        self.histogram_label.grid(row=4, column=0, padx=5, pady=5)
        self.histogram_canvas = tk.Canvas(self, width=300, height=200)
        self.histogram_canvas.grid(row=4, column=1, padx=5, pady=5)

    def roll_dice(self):
        num_dice = int(self.num_dice_entry.get())
        num_sides = int(self.num_sides_entry.get())
        rolls = roll_dice(num_dice, num_sides)
        self.roll_results_text.delete('1.0', tk.END)
        self.roll_results_text.insert(tk.END, str(rolls))
        plot_histogram(rolls, num_sides, self.histogram_canvas)

def roll_dice(num_dice, num_sides):
    rolls = []
    for i in range(num_dice):
        rolls.append(random.randint(1, num_sides))
    return rolls

def plot_histogram(rolls, num_sides, canvas):
    fig = Figure(figsize=(3, 2), dpi=100)
    ax = fig.add_subplot(111)
    ax.hist(rolls, bins=range(1, num_sides+2), align='left', rwidth=0.8)
    ax.set_xticks(range(1, num_sides+1))
    ax.set_xlabel('Dice Roll')
    ax.set_ylabel('Frequency')
    ax.set_title('Dice Roll Histogram')
    canvas.delete('all')
    canvas.fig = fig
    canvas.draw()

def main():
    root = tk.Tk()
    DiceRoller(root).pack()
    root.mainloop()

if __name__ == '__main__':
    main()