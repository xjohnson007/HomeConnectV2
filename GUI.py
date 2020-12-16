from tkinter import *
import tkinter as tk


##### have get settings make a pop up window with the settings
##### For changing temperature have Current Temperature, Entry Box with number, Have "Change Whatever as the Enter button"
window=Tk()



def input():
    win= tk.Tk()
    prompt = "What would you like to change the temperature too?"

    label= tk.Label(win, text=prompt)
    label.pack()

    userinput= tk.StringVar(win)
    entry= tk.Entry(win, textvariable=userinput)
    entry.pack()

    # pressing the button should stop the mainloop
    button= tk.Button(win, text="ok", command=win.quit)
    button.pack()

    # block execution until the user presses the OK button
    win.mainloop()

    # mainloop has ended. Read the value of the Entry, then destroy the GUI.
    userinput= userinput.get()
    win.destroy()
    print(userinput)
    return userinput






btn=Button(window, text="Change Freezer Temperature", fg='blue', width = 25, height = 25, command = input)
btn.grid(column=0, row=0)

btn2 = Button(window, text="Change Fridge Temperature", fg='blue', width = 25, height = 25)
btn2.grid(column=1, row=0)

btn3=Button(window, text="Get Settings", fg='blue',width = 25, height = 25)
btn3.grid(column=2, row=0)

btn4 = Button(window, text="Get Fridge Settings", fg='blue',width = 25, height = 25)
btn4.grid(column=3, row=0)

btn5=Button(window, text="Get Freezer Settings", fg='blue',width = 25, height = 25)
btn5.grid(column=0, row=1)

btn6 = Button(window, text="Get SQL data", fg='blue',width = 25, height = 25)
btn6.grid(column=1, row=1)

btn7=Button(window, text="This is Button widget", fg='blue',width = 25, height = 25)
btn7.grid(column=2, row=1)

btn8 = Button(window, text="Exit", fg='blue',width = 25, height = 25)
btn8.grid(column=3, row=1)

window.title('Hello Python')
window.geometry("1000x810")
window.mainloop()
