from tkinter import Label,Tk, Button
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
root = Tk()


myvar=Label(root, image=None)
myvar.pack()

def browse():
    path = askopenfilename()
    im = Image.open(path)
    global tkimage
    tkimage = ImageTk.PhotoImage(im)
    myvar.configure(image=tkimage)
    # myvar.pack()


b = Button(root, text='Open file', command=browse)
b.pack()

root.mainloop()