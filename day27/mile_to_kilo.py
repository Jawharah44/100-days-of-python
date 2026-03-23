from tkinter import *

def miles_kllo():
    miles = float(miles_input.get())
    km = round(miles * 1.609)
    kilometer_result_labbel.config(text=f"{km}")
    
window = Tk()
window.title("Miles To Kilometer Converter")
window.config(padx=20 , pady=20)

miles_input = Entry(width=7)
miles_input.grid(column=1,row=0)
milees_label = Label(text="Miles")
milees_label.grid(column= 2,row=0)
is_equal_label = Label(text= "is equal to")
is_equal_label.grid(column=0,row=1)
kilometer_result_labbel =Label(text="0")
kilometer_result_labbel.grid(column=1,row=1)
kilometer_Label = Label(text="km")
kilometer_Label.grid(column=2,row=1)
calcaulate = Button(text="Calculate",command=miles_kllo)
calcaulate.grid(column=1,row=2)
window.mainloop()
