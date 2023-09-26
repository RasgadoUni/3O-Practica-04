import tkinter as tk

App = tk.Tk()
App.title ("Conversor de Temperatura")

label1 = tk.Label(App, text='Farenheit:')
label1.grid(row=0, column=0)

entry1 = tk.Entry(App)
entry1.grid(row=0, column=1)

button1 = tk.Button(App, text='Convertir a Celcius:')#, command=convertir_a_celsius)
button1.grid(row=0, column=2)

label2 = tk.Label(App, text='Celcius:')
label2.grid(row=1, column=0)

entry2 = tk.Entry(App)
entry2.grid(row=1, column=1)

button2 = tk.Button(App, text='Convertir a Fahrenheir:')#, command=convertir_a_fahrenheit)
button2.grid(row=1, column=2)

button3 = tk.Button(App, text='Restablecer')#, command=borrar)
button3.grid(row=2, column=1)

App.geometry("")

App.mainloop()
