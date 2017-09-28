import tkinter
from tkinter import messagebox
import tweepy

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
        tweet=self.t1.get('1.0',tkinter.END)
        self.t1.delete('1.0',tkinter.END)
        print(tweet)

        if not (tweet and tweet.strip()):
            messagebox.showwarning("Warning","There is nothing to submit. Try Again.")
            return
        if len(tweet)>140:
            messagebox.showwarning("Warning","Your current tweet is too long. Please shorten.")
            return

        messagebox.showinfo("Success", "Tweet Sent.")

root = tkinter.Tk()
root.configure(background='coral1')
app = guiWindow(master=root)
root.mainloop()
