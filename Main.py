from tkinter import *
from tkinter import messagebox
import tkinter
import tweepy

class guiWindow(tkinter.Frame):
    manualTweetOpenFlag = False
    lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
    def __init__(self, master=None):
        super().__init__(master)
        #move into function that will be called in constructor
        master.LFrame = tkinter.LabelFrame(master, text="Twitter/Email Interface",
                                           padx=15, pady=15,relief='sunken')
        master.LFrame.grid(row=0, column=0, columnspan=2,rowspan=2, padx=5,pady=5,stick=NS)
        master.l1 = tkinter.Label(master.LFrame, text="What would you like to do?")
        master.l1.grid(row=1, column=0)
        master.tweetButton = tkinter.Button(master.LFrame, text="Send Manual Tweet",
                                            command = lambda: self.create_widgets(master))
        master.tweetButton.grid(row=2, column=0)

        master.LFrame2 = tkinter.LabelFrame(master, text = "Import New Submissions",
                                            padx=15,relief='sunken')
        master.LFrame2.grid(row=3,columnspan=2,rowspan=2, padx=5, pady=5,stick=NS)
        master.l2 = tkinter.Label(master.LFrame2, text="What would you like to do?")
        master.l2.grid(row=4, column=1)
        master.importButtons = tkinter.Button(master.LFrame2, text="Import",
                                            command = lambda: self.dummyButton(master))
        master.importButtons.grid(row=5, column=1)

        master.LFrame3 = tkinter.LabelFrame(master, text="Most recent Tweets",
                                           padx=15, relief='sunken')
        master.LFrame3.grid(row=0, column=2, columnspan=4,rowspan=2, padx=5,pady=5,stick=NS)

        master.l3 = tkinter.Label(master.LFrame3, text="Here are your most recent tweets.")
        master.l3.grid(row=1, column=2)
        master.recentTweets = tkinter.Label(master.LFrame3,text=self.lorem)
        master.recentTweets.grid(row=2, column=2)


    def create_widgets(self,master):
        if self.manualTweetOpenFlag:
            return
        self.manualTweetOpenFlag = True
        top = tkinter.Toplevel(master)
        top.title('Send Manual Tweet')
        top.protocol('WM_DELETE_WINDOW',lambda: self.closeManualTweetWindow(top))

        top.l1 = tkinter.Label(top, text="What would you like to tweet?")
        top.l1.grid(row=0)
        top.t1 = tkinter.Text(top)
        top.t1.grid(row=1)

        top.b1 = tkinter.Button(top, text="Submit", command=lambda: self.submit(top))
        top.b1.grid(row=2)
    def submit(self, topLevel):
        tweet = topLevel.t1.get('1.0', tkinter.END)
        topLevel.t1.delete('1.0', tkinter.END)
        print(tweet)

        if not (tweet and tweet.strip()):
            messagebox.showwarning("Warning", "There is nothing to submit. Try Again.",
                                   parent=topLevel)
            return
        if len(tweet) > 140:
            messagebox.showwarning("Warning", "Your current tweet is too long. Please shorten.",
                                   parent=topLevel)
            return

        messagebox.showinfo("Success", "Text Captured.", parent=topLevel)
        #implement tweet mechanism when oath tokens are set up
        topLevel.destroy()
        self.manualTweetOpenFlag = False
    def closeManualTweetWindow(self, topLevel):
        self.manualTweetOpenFlag=False
        topLevel.destroy()

    def dummyButton(self,master):
        messagebox.showinfo('dummy button', 'dummy button', parent=master)
root = tkinter.Tk()
root.title('Root Window')
app = guiWindow(master=root)
root.mainloop()
