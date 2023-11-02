import customtkinter

root = customtkinter.CTk()
root.title("TitanoLauncher")
root.geometry("500x500")
Btu = customtkinter.button(window = root, command = launch, text = "button")

def launch():

     root.mainloop()
