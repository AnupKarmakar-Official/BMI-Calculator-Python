import tkinter as tk


def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        feet = float(feet_entry.get())
        inches = float(inches_entry.get())

        # Convert height to meters
        height = (feet * 12 + inches) * 0.0254

        # Calculate BMI
        bmi = round(weight / (height ** 2), 2)

        # Determine BMI category
        if bmi < 18.5:
            category = "Underweight"
            color = "yellow"
        elif 18.5 <= bmi < 25:
            category = "Normal"
            color = "green"
        elif 25 <= bmi < 30:
            category = "Overweight"
            color = "orange"
        else:
            category = "Obese"
            color = "red"

        # Display the result
        result_label.config(text=f"BMI: {bmi} ({category})", fg=color)
    except ValueError:
        result_label.config(text="Invalid input!", fg="red")


def close_window():
    root.destroy()


root = tk.Tk()
root.title("BMI Calculator")
border_color = "#e74c3c"
root.configure(background=border_color)
root.attributes("-alpha", 10)
root.resizable(width=False, height=False)
root.geometry("320x240")
root.overrideredirect(False)
root.geometry("+250+150")

canvas = tk.Canvas(root, width=280, height=200, bg="white")
canvas.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

weight_label = tk.Label(canvas, text="Weight (kg):", font=("Arial", 12), anchor="w")
weight_label.place(x=10, y=10)

weight_entry = tk.Entry(canvas, font=("Arial", 12), justify="center", width=12)
weight_entry.place(x=120, y=10)

height_label = tk.Label(canvas, text="Height (ft/in):", font=("Arial", 12), anchor="w")
height_label.place(x=10, y=50)

feet_entry = tk.Entry(canvas, font=("Arial", 12), justify="center", width=4)
feet_entry.place(x=120, y=50)

feet_label = tk.Label(canvas, text="ft", font=("Arial", 12))
feet_label.place(x=170, y=50)

inches_entry = tk.Entry(canvas, font=("Arial", 12), justify="center", width=4)
inches_entry.place(x=190, y=50)

inches_label = tk.Label(canvas, text="in", font=("Arial", 12))
inches_label.place(x=240, y=50)

calculate_button = tk.Button(canvas, text="Calculate BMI", font=("Arial", 12), command=calculate_bmi)
calculate_button.place(x=10, y=90, width=260)

result_label = tk.Label(canvas, font=("Arial", 16, "bold"))
result_label.place(x=10, y=130, width=260)

close_button = tk.Button(root, text="Close", font=("Arial", 12), command=close_window, bg="white")
close_button.pack(side=tk.BOTTOM, pady=5)

root.mainloop()
