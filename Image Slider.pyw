from itertools import cycle
import tkinter as tk
class App(tk.Tk):
    # Tk window adjustment to size the image
    def __init__(self,image_files,x,y,delay):
        tk.Tk.__init__(self)
        self.geometry(f'+ {x}+ {y}')
        self.delay=delay
        self.pictures=cycle((tk.PhotoImage(file=image),image)for image in image_files)
        self.pictures_display=tk.Label(self)
        self.pictures_display.pack()
    def show_slides(self):
        # Cycle through images and display them
        img_object,img_name=next(self.pictures)
        self.pictures_display.config(image=img_object)
        self.title(img_name)
        self.after(self.delay,self.show_slides)
    def run(self):
        self.mainloop()
# set milliseconds time between sliders
delay=3500
# get a series of images you have in the working folder or
# useful path, or set directory to where the images are
image_files=[]
x=100
y=50
app=App(image_files,x,y,delay)
app.show_slides()
app.run()

