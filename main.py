import pyglet
import pyglet.window.key
from pyglet.window import key
import os
import sys
from time import sleep
width = 1280
height = 720
title = "Book Reader"
text = "Put here a file with text or click enter"
thing = ""
textp = 2
name = input("Give the name of the book (you MUST type it's end like test.pdf) ")
with open(str(name)) as f:
    thing = f.read()
    etc = str(name)

window = pyglet.window.Window(width, height, title, resizable=True, vsync=True) 
book = pyglet.resource.image('assets/openbook.png')
end = pyglet.resource.image('assets/openbook.png')
label = pyglet.text.Label(text, 
                          font_name ='Josefin Sans', 
                          font_size = 24, 
                          x = window.width//2, y = window.height//1.1, 
                          anchor_x ='center', anchor_y ='center') 
  
new_label = pyglet.text.Label(text, 
                          font_name ='Josefin Sans', 
                          font_size = 10, 
                          x = 25, y = 25) 

label2 = pyglet.text.Label(etc, 
                          font_name ='Josefin Sans', 
                          font_size = 18, 
                          x = window.width//2, y = window.height//1.1, 
                          anchor_x ='center', anchor_y ='center') 

label3 = pyglet.text.Label(thing, 
                          font_name ='Josefin Sans', 
                          font_size = 20, 
                          x = window.width//textp, y = window.height//1.3, 
                          anchor_x ='center', anchor_y ='center') 

@window.event 
def on_draw():      
    window.clear() 
#    label.draw() 
    label2.draw()
    label3.draw()
    end.blit(750,580)
    book.blit(400,580)
img = image = pyglet.resource.image("assets/icon.png")
window.set_icon(img)
pyglet.app.run() 