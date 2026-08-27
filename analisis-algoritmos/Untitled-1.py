import tkinter as tk
import matplotlib.pyplot as plt
#pip install matplotlib

x=[3, 4 ,5, 15. 22]
y=[10,40,625,700]
plt.plot(x,y)
plt.scatter(x,y)
plt.bar(x,y)
plt.title("mi primera grafica")
plt.xlabel("eje x")
plt.ylabel("eje y")

def saludar():
    nombre =entrada.get().strip()
    if not nombre:
        nombre = "mundo"
    lbl.config(text=f"Hola mundo, {nombre}")
root = tk.Tk()
root.title("Saludador")
root.geometry("360x220")

lbl =tk.Label(root, text="Eh compa, escribe tu nombre y presiona el boton",background="red", foreground="pink")
lbl.pack(pady=10)
entrada = tk.Entry(root)
entrada.pack(pady=10)
bot = tk.Button(root, text="puchale aqui mero", command=saludar)
bot.pack(pady=10)







root.mainloop()
plt.show()