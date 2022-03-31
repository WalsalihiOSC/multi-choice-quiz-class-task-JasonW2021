#
from tkinter import *


class Multichoicequiz:
    def __init__(self, parent):
    #Text = Question: What is the capital of Mongolia
    #Possible - Vladivostok, Astana, Ulan Bator, Lhasa
    #Incorrect / Correct label 
        button= Radiobutton(parent, text="", variable="", value="")
        button.grid(row=0, column=0, sticky =0)

        self.check = Label(parent, text = "",)
        self.check.grid(column=0, row=0)

    def checkans(self):
        answer = "Ulan Bator"
        if self.check.get() == answer:
            self.check.configure(text="correct")
        else:
            self.check.configure(text="incorrect")

#columnspan

#main routine
root = Tk()
opt_list = ["Vladivostok", "Astana", "Ulan Bator", "Lhasa"]
options = StringVar()
options 
multiquestion = Multichoicequiz(root)
root.mainloop()