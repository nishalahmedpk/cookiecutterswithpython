from task import *
import tkinter
class App:
    def __init__(self) -> None:
        self.root = tkinter.Tk()
        self.root.geometry("500x600+50+30")

        newtaskframe =  tkinter.Frame(self.root,relief="ridge",height=100,width=600,padx=200,pady=20)
        newtaskframe.grid(row=0)

        texbox = tkinter.Entry(newtaskframe)
        texbox.grid(row=0,column=0)

        addbutton = tkinter.Button(newtaskframe, text='Add')
        addbutton.grid(row=0,column=1)

        tasksframe =  tkinter.Frame(self.root,height=400,width=600)
        tasksframe.grid(row=1)

        construct()
        for task in TaskList : tkinter.Button(tasksframe,text=task.taskname,width=40).grid(row=TaskList.index(task))

        self.root.mainloop()

App()