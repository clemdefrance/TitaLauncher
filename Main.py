import customtkinter

root = customtkinter.CTk()
root.title("TitanoLauncher")
root.geometry("500x500")
def launch():
    print("l")

Btu = customtkinter.CTkButton(master=root, text="button", command=launch())
Btu.pack()

root.mainloop()
