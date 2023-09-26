import tkinter as tk

def convertir_a_celsius():
    fahrenheit = float(entry1.get())
    Celsius = (fahrenheit - 32) * 5.0/9.0
    entry2.delete(0, tk.END)
    entry2.insert(0,f"{Celsius:.2f}")

def convertir_a_fahrenheit():
    celsius = float(entry2.get())
    fahrenheit = (celsius * 9 / 5) + 32
    entry1.delete(0, tk.END)
    entry1.insert(0, f"{fahrenheit:.2f}")

def borrar():
    entry1.delete(0, tk.END)
    entry1.insert(0, "0.0")
    entry2.delete(0, tk.END)
    entry2.insert(0, "0.0")

App = tk.Tk()
App.title ("Conversor de Temperatura")

label1 = tk.Label(App, text='Fahrenheit:')
label1.grid(row=0, column=0)

entry1 = tk.Entry(App)
entry1.grid(row=0, column=1)

button1 = tk.Button(App, text='Convertir a Celcius:', command=convertir_a_celsius)
button1.grid(row=0, column=2)

label2 = tk.Label(App, text='Celcius:')
label2.grid(row=1, column=0)

entry2 = tk.Entry(App)
entry2.grid(row=1, column=1)

button2 = tk.Button(App, text='Convertir a Fahrenheir:', command=convertir_a_fahrenheit)
button2.grid(row=1, column=2)

button3 = tk.Button(App, text='Restablecer', command=borrar)
button3.grid(row=2, column=1)

App.geometry("")

App.mainloop()
