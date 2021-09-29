from tkinter import *
from tkinter import ttk

from server import *

clientConnected = create_server()

root = Tk()
root.geometry("500x300")
Label(root,text="Python Form",font = "ar 15 bold").grid(row=0,column =3)

def close_window():
  print ("Window closed")
  message = "CLOSE 000"
  clientConnected.send(message.encode())
  root.destroy()

root.protocol("WM_DELETE_WINDOW", close_window )

# Buttons
boton = ttk.Button(text="turn ON white" , command=lambda: action_on_Led("white","turn on",clientConnected) )
boton.place(x=50, y=50)
boton = ttk.Button(text="turn OFF white" , command=lambda: action_on_Led("white","turn off",clientConnected) )
boton.place(x=50, y=70)

boton = ttk.Button(text="turn ON blue" , command=lambda: action_on_Led("blue","turn on",clientConnected) )
boton.place(x=150, y=50)
boton = ttk.Button(text="turn OFF blue" , command=lambda: action_on_Led("blue","turn off",clientConnected) )
boton.place(x=150, y=70)

boton = ttk.Button(text="turn ON yellow" , command=lambda: action_on_Led("yellow","turn on",clientConnected) )
boton.place(x=250, y=50)
boton = ttk.Button(text="turn OFF yellow" , command=lambda: action_on_Led("yellow","turn off",clientConnected) )
boton.place(x=250, y=70)

boton = ttk.Button(text="Take action depending on distance" , command=lambda: action_on_Led_distance(clientConnected) )
boton.place(x=350, y=50)

root.mainloop()