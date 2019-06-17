from Tkinter import *
import tkMessageBox

#inicializacion de entorno
principal = Tk()
cancha = Canvas(principal, width=500, height=500)
principal.title("Fifa 2019 ps4 Premium Edition")
cancha.pack()

#crear los arcos
cancha.create_line(0,150,100,150,100,350,0,350)
cancha.create_line(500,150,400,150,400,350,500,350)

#creacion bola
coord = 250,250,300,300
oval=cancha.create_oval(coord,fill="red")

#centrar bola
def centrar():
    cancha.coords(oval ,250,250,300,300)    

#messagebox para cuando hagan gol
def anuncio():

    tkMessageBox.showinfo("Anuncio!!","Gooool")
#comprobador de gol

def hayGol():
    #regla para arco izquierdo
    intervaloY=cancha.coords(oval)[1]>150 and cancha.coords(oval)[1]<350
    intervaloX=cancha.coords(oval)[0]<100 
    #regla para arco derecho
    intervaloY1=cancha.coords(oval)[3]>150 and cancha.coords(oval)[3]<350
    intervaloX1=cancha.coords(oval)[2]>400

    if intervaloY and intervaloX: 
        anuncio()
        centrar()
        
    else :
        if intervaloY1 and intervaloX1:
            anuncio()
            centrar()

#movimiento de la bola
def izquierda(event):
    #movimiento horizontal
    cancha.move(oval, -30, 0)
    hayGol()

def derecha(event):
    #movimiento horizontal
    cancha.move(oval, 30, 0)
    hayGol()

def arriba(event):
    #movimiento vertical
    cancha.move(oval, 0, -30)    
    hayGol()

def abajo(event):
    #movimiento vertical
    cancha.move(oval, 0, 30)  
    hayGol()
#asignacion de keybindings
cancha.bind('<Left>', izquierda)
cancha.bind('<Right>', derecha)
cancha.bind('<Up>',arriba)
cancha.bind('<Down>',abajo)

cancha.focus_set()
cancha.pack()

principal.mainloop()


#comentario para probar sourcetree

    
