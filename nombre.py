import turtle
import random
from Tkinter import * 
#diccionario con coordenadas de cada punto de la letra
diccionario = {
'R': ((0,0),(0,1),(0.625,1),(0.75,0.875),(0.75,0.625),(0.625,0.5),(0,0.5),(0.625,0.5),(0.875,0)),
'O': ((0.75,0.125),(0.625,0),(0.125,0),(0,0.125),(0,0.875),(0.125,1),(0.625,1),(0.75,0.875),(0.75,0.125)),
'N': ((0,0),(0,1),(0.75,0),(0.75,1)),
'Y': ((0,1),(0.375,0.5),(0.375,0),(0.375,0.5),(0.75,1)),
'C': ((0.75,0.125),(0.625,0),(0.125,0),(0,0.125),(0,0.875),(0.125,1),(0.625,1),(0.75,0.875)),
'A': ((0,0),(0.5,1),(0.75,0.5),(0.25,0.5),(0.75,0.5),(1,0)),
'J': ((0,0.125),(0.125,0),(0.375,0),(0.5,0.125),(0.5,1)),
'A': ((0,0),(0.5,1),(0.75,0.5),(0.25,0.5),(0.75,0.5),(1,0)),
'S': ((0,0.125),(0.125,0),(0.625,0),(0.75,0.125),(0.75,0.375),(0.675,0.5),(0.125,0.5),(0,0.625),(0,0.875),(0.125,1),(0.625,1),(0.75,0.875)),
}

#objetos turtle
pluma = turtle.Turtle()
pluma.hideturtle()
pluma.speed(0)
window = turtle.Screen()
pluma.pensize(2)
#auto trazo
def pantalla(nombre,tamanoFuente,x,y):
  nombre=nombre.upper()
  
  for letra in nombre:
    if letra in diccionario:
      letter=diccionario[letra]
      pluma.penup()
      for punto in letter:
        pluma.goto(x + punto[0]*tamanoFuente, y + punto[1]*tamanoFuente)
        pluma.pendown()
        
      x += tamanoFuente
      
    if letra == " ":
      x += tamanoFuente
    

#llamado a la rutina


pantalla("RONNY",20,-190,0)


