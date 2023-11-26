# To make the GUI more attractive, we can add some styling and organize the widgets using frames.
# Since the execution environment does not support GUI operations, the code below is written to be run in a local Python environment.

import tkinter as tk
from tkinter import messagebox

# Constants for hexagon properties
HEXAGON_ANGLE_SUM = 720  # Total internal angles of hexagon
HEXAGON_ANGLE = 120  # Each angle of hexagon
HEXAGON_MULTIPLIER = 1.5 * (3**0.5)  # Multiplier for area of hexagon

# Placeholder for the last digit of CNIC
# This should be replaced by the actual last digit of the user's CNIC
CNIC_LAST_DIGIT = 2  # Example last digit

class Hexagon:
    def __init__(self, side_length):
        self.side_length = side_length

    def calcArea(self):
        return HEXAGON_MULTIPLIER * self.side_length * self.side_length

    def calcPeri(self):
        return 6 * self.side_length

    def calcAngleSum(self):
        return HEXAGON_ANGLE_SUM

    def display(self):
        area = self.calcArea()
        perimeter = self.calcPeri()
        angle_sum = self.calcAngleSum()
        messagebox.showinfo("Hexagon Details", 
                            f"Area: {area}\nPerimeter: {perimeter}\nSum of Angles: {angle_sum}")

class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def calcAreaSquare(self):
        return self.side_length * self.side_length

    def calcPeriSquare(self):
        return 4 * self.side_length

    def display(self):
        area = self.calcAreaSquare()
        perimeter = self.calcPeriSquare()
        messagebox.showinfo("Square Details", f"Area: {area}\nPerimeter: {perimeter}")

def main():
    # Create the main window
    root = tk.Tk()
    root.title("Geometry Calculator")
    
    # Set a minimum size for the window
    root.minsize(300, 200)

    # Use a frame for better organization and layout
    frame = tk.Frame(root)
    frame.pack(padx=10, pady=10)

    # Create a label with a larger font
    title_label = tk.Label(frame, text="Geometry Calculator", font=("Helvetica", 16))
    title_label.pack(side=tk.TOP, pady=(0, 20))

    # Instructions label
    instruction_label = tk.Label(frame, text="Enter '1' for hexagon or '2' for square:")
    instruction_label.pack(side=tk.TOP)

    # Create an entry field
    entry = tk.Entry(frame, width=5, font=("Helvetica", 14))
    entry.pack(side=tk.TOP, pady=5)

    # Function to handle user input
    def handle_input():
        user_input = entry.get()
        if user_input == '1':
            hexagon.display()
        elif user_input == '2':
            square.display()
        else:
            messagebox.showerror("Error", "Number is not valid. Please enter 1 or 2.")
            entry.delete(0, tk.END)

    # Create a calculate button
    calculate_button = tk.Button(frame, text="Calculate", command=handle_input)
    calculate_button.pack(side=tk.TOP, pady=10)

    # Initialize the hexagon and square with the CNIC last digit
    hexagon = Hexagon(CNIC_LAST_DIGIT)
    square = Square(CNIC_LAST_DIGIT + 1)

    # Start the GUI loop
    root.mainloop()

if __name__ == "__main__":
    main()
