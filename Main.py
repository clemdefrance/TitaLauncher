from tkinter import *

root = Tk()
root.geometry("800x600")  
root.title("TitanoLauncher")

#background
background_image = PhotoImage(file="background.png")
background_label = Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

root.mainloop()

