import tkinter as gui
from tkinter import PhotoImage

print('widget_generator v0.1 by Pepe Bola')
print("write anything in the gray text boxes and click 'done' to create a window")
window = gui.Tk()
window.configure(bg= 'lightgray')
window.geometry('300x130')
window.title('widget_generator.py')
icon_path = r"C:\Users\USUARIO 2\Downloads\Workspace\python programs\widget_generator\WindowCreate.ico"
window.iconbitmap(icon_path)

text_label = gui.Label(window, text= 'text(E.g: UrMom)', bg= 'lightgray') 
text_label.pack() 
text_box = gui.Entry(window, bg= 'gray')
text_box.pack(fill= gui.X ,expand= True)

size_label = gui.Label(window, text= 'size (E.g: 110x110)', bg= 'lightgray') 
size_label.pack()
size = ''
size_box = gui.Entry(window, bg= 'gray', )
size_box.pack(fill= gui.X ,expand= True)

def create_window(textoe, sizeo):
    another_window = gui.Tk()
    another_window.geometry(sizeo)
    another_window.configure(bg= 'gray')
    label = gui.Label(another_window, text= textoe, bg= 'lightgray')
    label.pack(fill= 'both', expand= True)
    another_window.title(textoe)
    another_window.iconbitmap(icon_path)
    print('window properties:')
    print('text: ' + textoe)
    print('size: ' + sizeo)
    
def text_get():
    text = text_box.get()
    size = size_box.get()
    
    create_window(text, size)
    return text

create_button = gui.Button(window, text= 'create window', command= text_get, bg= 'green')
create_button.pack(fill= gui.X)
    
destroy_button = gui.Button(window, text= 'quit', command= quit, bg= 'red')
destroy_button.pack(fill= gui.X)

window.mainloop()