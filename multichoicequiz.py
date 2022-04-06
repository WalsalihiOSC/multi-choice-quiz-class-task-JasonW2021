#
from tkinter import *

class Quiz:
    def __init__(self):
        '''Set values'''
        self.opt_list = ["Vladivostok", "Astana", "Ulan Bator", "Lhasa"]
        self.opt_var = StringVar()
        self.opt_var.set("*")
    
    def cap_list(self): 
        return self.opt_list

    def checkans(self):
        '''Check is radiobutton is correct or not'''
        answer = "Ulan Bator"
        
        if self.opt_var.get() == answer:
            self.check.configure(text="Correct")
        else:
            self.check.configure(text="Incorrect")    

class Interface(Quiz):
    def __init__(self, parent):
        '''Create the objects and radiobuttons'''
        self.opt_var = StringVar()

        Questions = Label(parent, text = "Question: ")
        Questions.grid(column= 0, row=0, sticky=W, columnspan=1)

        Question1= Label(parent, text = "What is the capital of Mongolia?")
        Question1.grid(column= 1, row=0)

        self.check = Label(parent, text = "")
        self.check.grid(column=1, row=6)

        #Brings the data in this class
        Quiz.__init__(self)

        for i in range(len(self.opt_list)):
            btns = Radiobutton(parent, text=self.opt_list[i], variable=self.opt_var,
            anchor = W, value=self.opt_list[i], command= self.checkans)
            btns.grid(column = 1, row = i+1, sticky=W)

#main routine
root = Tk()
root.geometry("300x200")
multiquestion = Interface(root)
root.mainloop()