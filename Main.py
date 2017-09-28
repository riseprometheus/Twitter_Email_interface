import tkinter
from tkinter import messagebox
import tweepy

class guiWindow(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        #move into function that will be called in constructor 
        master.l1 = tkinter.Label(master,text="What would you like to do?")
        master.l1.grid(row=1, column=1)
        master.tweetButton = tkinter.Button(master,text="Send Manual Tweet",command=self.create_widgets)
        master.tweetButton.grid(row=2, column=1)
        
        master.grid_rowconfigure(0, weight=1)
        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(3, weight=1)
        master.grid_columnconfigure(3, weight=1)

    def create_widgets(self):
        top = tkinter.Toplevel(self)
        top.title('Send Manual Tweet')
        top.l1 = tkinter.Label(top,text="What would you like to tweet?")
        top.l1.grid(row=0)
        top.t1 = tkinter.Text(top)
        top.t1.grid(row=1)

        top.b1 = tkinter.Button(top,text="Submit",command=lambda:self.submit(top))
        top.b1.grid(row=2)

    def submit(self,topLevel):
        tweet=topLevel.t1.get('1.0',tkinter.END)
        topLevel.t1.delete('1.0',tkinter.END)
        print(tweet)

        if not (tweet and tweet.strip()):
            messagebox.showwarning("Warning","There is nothing to submit. Try Again.",parent=topLevel)
            return
        if len(tweet)>140:
            messagebox.showwarning("Warning","Your current tweet is too long. Please shorten.",parent=topLevel)
            return

        messagebox.showinfo("Success", "Text Captured.",parent=topLevel)
        #implement tweet mechanism when oath tokens are set up
        topLevel.destroy()

root = tkinter.Tk()
root.title('Root Window')
root.geometry('500x100')
app = guiWindow(master=root)
root.mainloop()
