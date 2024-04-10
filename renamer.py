import tkinter as tk
from PIL import ImageTk, Image
import os

def rename(captcha):
    global pos
    os.rename(l[pos],captcha +'.png')
    pos+=1
    text_widget.delete(0,'end')
    img2 = ImageTk.PhotoImage(Image.open(l[pos]))
    panel.configure(image = img2)
    panel.image = img2
    

l = []
#path = 'D:\Education\Coding\dataset_capatcha\E-courts_v6'
for file in os.listdir():
    if file.endswith('.png'):
        l.append(file)
pos = 0
print(len(l), l[pos])       

window = tk.Tk()
window.title("Type and Enter")
window.geometry("600x400")
window.configure(background = 'grey')

text_widget = tk.Entry(window)
text_widget.pack(padx = 50, pady = 50)
text_widget.bind('<Return>',(lambda event: rename(text_widget.get())))

img = ImageTk.PhotoImage(Image.open(l[pos]))
panel = tk.Label(window, image = img)
panel.pack( padx = 50, pady = 50)


window.mainloop()
