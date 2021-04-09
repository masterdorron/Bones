from tkinter import *


class Application(Frame):
    def say_hi(self):
        self.label["text"] = "hi there, everyone!"

    def createWidgets(self):
        self.f1 = Frame(self)
        self.f1.pack()
        self.QUIT = Button(self.f1)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit

        self.QUIT.pack({"side": "left"})

        self.hi_there = Button(self.f1)
        self.hi_there["text"] = "Hello",
        self.hi_there["command"] = self.say_hi

        self.hi_there.pack({"side": "left"})
        self.label = Label(self, text='Place for hello')
        self.label.pack()

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()



root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()

tex = Text(root,width=40,
          font="Verdana 12",
          wrap=WORD)