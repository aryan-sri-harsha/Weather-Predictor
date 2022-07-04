from tkinter import*
from tkinter import messagebox

def clear_all():
    city_field.delete(0, END)
    temp_field.delete(0, END)
    atm_field.delete(0, END)
    humid_field.delete(0, END)
    desc_field.delete(0, END)
    city_field.focus_set()


def clear_some():
    temp_field.delete(0, END)
    atm_field.delete(0, END)
    humid_field.delete(0, END)
    desc_field.delete(0, END)
    city_field.focus_set()


def test():
    from predictions import get_predictions
    city_name = city_field.get()
    res = get_predictions(city_name)
    clear_some()
    desc = ""
    temperature = (res[0]+res[1])/2
    if temperature > 40:
        desc = "Very Hot"
    elif temperature > 28:
        desc = "Hot"
    elif temperature > 25:
        desc = "Moderate"
    elif temperature > 20:
        desc = "Cool"
    else:
        desc = "Very Cool"
    temperature = str(res[0])+"C "+str(res[1])+"C"
    windSpeed = str(res[2]) + "KMPH"
    humidity = str(res[3]) + " %"
    temp_field.insert(15, temperature)
    atm_field.insert(10, windSpeed)
    humid_field.insert(15, humidity)
    desc_field.insert(10, desc)  # str("no clue")



if __name__ == "__main__":
    root = Tk()
    root.title("Weather Application")

    root.configure(background="#A1D6E2")

    root.geometry("1280x720")
    headlabel = Label(root, text="Weather Gui Application",
                      fg='black', bg='#7D4427', font=("Arial", 17))


    la1 = Label(root, text="City name : ",
                   fg='black', bg='#1995AD', font=("Arial", 15))


    la2 = Label(root, text="Temperature :",
                   fg='black', bg='#1995AD', font=("Arial", 15))

    la3 = Label(root, text="wind speed:   ",
                   fg='black', bg='#1995AD', font=("Arial", 15))

    la4 = Label(root, text="  humidity :     ",
                   fg='black', bg='#1995AD', font=("Arial", 15))

    la5 = Label(root, text="  description : ",
                   fg='black', bg='#1995AD', font=("Arial", 15))
    headlabel.grid(row=0, column=1)
    la1.grid(row=1, column=0, sticky="E")
    la2.grid(row=3, column=0, sticky="E")
    la3.grid(row=4, column=0, sticky="E")
    la4.grid(row=5, column=0, sticky="E")
    la5.grid(row=6, column=0, sticky="E")
    city_field = Entry(root)
    temp_field = Entry(root)
    atm_field = Entry(root)
    humid_field = Entry(root)
    desc_field = Entry(root)
    city_field.grid(row=1, column=1, ipadx="500", ipady="5")
    temp_field.grid(row=3, column=1, ipadx="500", ipady="5")
    atm_field.grid(row=4, column=1, ipadx="500", ipady="5")
    humid_field.grid(row=5, column=1, ipadx="500", ipady="5")
    desc_field.grid(row=6, column=1, ipadx="500", ipady="5")
    button1 = Button(root, text="Submit", bg="#7D4427",
                     fg="black", command=test, font=("Arial", 16))

    button2 = Button(root, text="Clear", bg="#7D4427",
                     fg="black", command=clear_all, font=("Arial", 16))

    button1.grid(row=2, column=1)
    button2.grid(row=7, column=1)
    root.mainloop()