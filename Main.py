import tkinter
from tkinter import messagebox
class guiWindow(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.l1 = tkinter.Label(self,text="What would you like to tweet?")
        self.l1.grid(row=0)
        self.t1 = tkinter.Text(self)
        self.t1.grid(row=1)
        self.t1.config(background='PeachPuff2')
        self.b1 = tkinter.Button(self,text="Submit",command=self.submit)
        self.b1.grid(row=2)

    def submit(self):
        self.t1.delete('1.0',tkinter.END)
        messagebox.showinfo("Succes", "Tweet Sent.")
        print("Button was pressed.")

root = tkinter.Tk()
root.configure(background='coral1')
app = guiWindow(master=root)
root.mainloop()
