from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=20, pady=20)

miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

# Button
def calculate():
    miles = float(miles_input.get())
    km = miles * 1.609
    km_result.config(text=f"{km}")

kilo_label = Label(text="Km")
kilo_label.grid(column=2, row=1)

km_result = Label(text="0")
km_result.grid(column=1, row=1)



button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)


# Label
label = Label(text="is equal to")
label.grid(column=0, row=1)


window.mainloop()
