#
from tkinter import *

class Multichoicequiz:
    def __init__(self, parent):
        '''Create the objects and radiobuttons'''

        Questions = Label(parent, text = "Question: ")
        Questions.grid(column= 0, row=0, sticky=W, columnspan=1)

        Question1= Label(parent, text = "What is the capital of Mongolia?")
        Question1.grid(column= 1, row=0)

        self.check = Label(parent, text = "")
        self.check.grid(column=1, row=5)

        self.opt_list = ["Vladivostok", "Astana", "Ulan Bator", "Lhasa"]
        self.opt_btns = []
        self.opt_var = StringVar()
        self.opt_var.set("*")

        for i in range(len(self.opt_list)):
            btns = Radiobutton(parent, text=self.opt_list[i], variable=self.opt_var,
            anchor = W, value=self.opt_list[i], command= self.checkans)
            btns.grid(column = 1, row = i+1, sticky=W)
            self.opt_btns.append(btns)

    def checkans(self):
        '''Check is radiobutton is correct or not'''
        answer = "Ulan Bator"
        if self.opt_var.get() == answer:
            self.check.configure(text="Correct")
        else:
            self.check.configure(text="Incorrect")

#main routine
root = Tk()
root.geometry("300x200")
multiquestion = Multichoicequiz(root)
root.mainloop()