import tkinter.ttk
from tkinter import *
from tkinter import messagebox

#Window
window = Tk()
window.title("Length Unit Converter")
#window.minsize(width=200, height=100)
window.minsize(width=300, height=100)
window.config(padx = 10, pady = 10)

units = ["km", "m", "cm", "mm", "μm", "nm", "mile", "yd", "ft", "in", "M"]

#Labels
label_1 = Label(text="Is equal to:")
label_2 = Label(text="")
label_3 = Label(text="")
label_4 = Label(text="")
label_1.grid(column = 0, row = 1)
label_2.grid(column = 1, row = 1)
label_2.config(padx = 10, pady = 5)
label_3.grid(column = 2, row = 0)
label_3.config(padx = 2, pady = 2)
label_4.grid(column = 2, row = 2)
label_4.config(padx = 2, pady = 2)

#Calculate
def each_unit():
    entry_1_value = float(entry_1.get())
    entry_2_value = float(entry_2.get())

    kilometers_equals_to = [1, 1000, 100000, 1000000, 1000000000,
                           1000000000000, 0.621371, 1093.61, 3280.84, 39370.1, 0.539957]

    meters_equals_to = [(a/1000) for a in kilometers_equals_to]
    centimeters_equals_to = [(b/100000) for b in kilometers_equals_to]
    milimeters_equals_to = [(c/1000000) for c in kilometers_equals_to]
    micrometers_equals_to = [(d/1000000000) for d in kilometers_equals_to]
    nanometers_equals_to = [(e/1000000000000) for e in kilometers_equals_to]
    miles_equals_to = [(f/0.621371) for f in kilometers_equals_to]
    yards_equals_to = [(g/1093.61) for g in kilometers_equals_to]
    feets_equals_to = [(h/3280.84) for h in kilometers_equals_to]
    inches_equals_to = [(i/39370.1) for i in kilometers_equals_to]
    nmiles_equals_to = [(j/0.539957) for j in kilometers_equals_to]

    each_units_conversion = [kilometers_equals_to, meters_equals_to, centimeters_equals_to, milimeters_equals_to,
                             micrometers_equals_to, nanometers_equals_to, miles_equals_to, yards_equals_to,
                             feets_equals_to, inches_equals_to, nmiles_equals_to]

    #print(units.index(option_1.get()))
    #unit_operation = each_units_conversion[units.index(option_1.get())]
    #print(unit_operation)

    #Same units
    if (conversion_direction.get() == "1_a_2" \
            and option_1.get() == "Select an option" and option_2.get() == "Select an option") or \
            (conversion_direction.get() == "1_a_2" \
             and option_1.get() != "Select an option" and option_2.get() == "Select an option") or \
            (conversion_direction.get() == "1_a_2" \
             and option_1.get() == "Select an option" and option_2.get() != "Select an option"):
        label_1.grid(column=0, row=1)
        print("Select an option")
        messagebox.showinfo(title="Ooops!", message="Select an option")
    elif (conversion_direction.get() == "2_a_1" \
            and option_1.get() == "Select an option" and option_2.get() == "Select an option") or \
            (conversion_direction.get() == "2_a_1" \
             and option_1.get() == "Select an option" and option_2.get() != "Select an option") or \
            (conversion_direction.get() == "2_a_1" \
             and option_1.get() != "Select an option" and option_2.get() == "Select an option"):
        label_1.grid(column=0, row=1)
        print("Select an option")
        messagebox.showinfo(title="Ooops!", message="Select an option")

    elif (conversion_direction.get() == "1_a_2" and option_1.get() != "Select an option" and option_2.get() != "Select an option") or (conversion_direction.get() == "2_a_1" and option_1.get() != "Select an option" and option_2.get() != "Select an option"):

        #Operation
        unit_operation = each_units_conversion[units.index(option_1.get())]

        for l in unit_operation:
            if units.index(option_2.get()) == unit_operation.index(l):
                find_operation = unit_operation.index(l)
                operation = unit_operation[find_operation]
                print(operation)

        #Do "for loop" and make option_1.get() == "km"
        #first entry
        for n in units:
            if n == option_1.get():
                first_option = n

        #second entry
        for m in units:
            if m == option_2.get():
                second_option = m

        #Conversion
        if conversion_direction.get() == "1_a_2" and option_1.get() == first_option and option_2.get() == second_option:
            label_1.grid(column=0, row=1)
            conversion_value = entry_1_value * operation
            entry_2.delete(0, END)
            entry_2.insert(0, f"{conversion_value:.2f}")

        elif conversion_direction.get() == "2_a_1" and option_2.get() == second_option and option_1.get() == first_option:
            label_1.grid(column=0, row=0)
            conversion_value_2 = entry_2_value / operation
            entry_1.delete(0, END)
            entry_1.insert(0, f"{conversion_value_2:.2f}")

#Button
button_calculate = Button(text="Calculate", command=each_unit, activebackground="white") #Cuando no se utiliza una señal
#para cambiar el color de la opción
button_calculate.grid(column = 1, row = 2)

# Variable de control para la dirección de la conversión
conversion_direction = StringVar(value="1_a_2")

# Crear un menú de opciones para seleccionar la dirección
direction_menu = OptionMenu(window, conversion_direction, "1_a_2", "2_a_1")
direction_menu.grid(row=2, column=2, padx=5, pady=5)

#Entries
entry_1 = Entry(width=12)
entry_2 = Entry(width=12)
entry_1.insert(END, string="0")
entry_2.insert(END, string="0")
entry_1.focus()
entry_1.grid(column=1, row=0, padx=10, pady=10)
entry_2.grid(column=1, row=1, padx=10, pady=10)

#Combobox
option_1 = tkinter.ttk.Combobox(state = "readonly", width = 14, values = units,
                                font=("Arial", 8, "normal"), foreground="black")
option_1.set("Select an option")
option_2 = tkinter.ttk.Combobox(state = "readonly", width = 14, values = units,
                                font=("Arial", 8, "normal"), foreground="black")
option_2.set("Select an option")
option_1.grid(column = 2, row = 0)
option_2.grid(column = 2, row = 1)

window.mainloop()