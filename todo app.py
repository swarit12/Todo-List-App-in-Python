from tkinter import *
import tkinter.messagebox as msg
import os
import pickle

root= Tk()

root.geometry("355x515")
root.title("TODO APP")

frame1= Frame(root)
frame1.grid(row= 0, pady= 0)

def save_task(event):
    task = input_value.get()
    if task!='':
        listbox.insert(END, task)
        ui.delete(0, END)
        tasks = listbox.get(0, listbox.size())
        pickle.dump(tasks, open("other files/tasks.dat", "wb"))
                        
    else:
        msg.showwarning("ERROR", "PLEASE WRITE SOME TASK BEFORE SAVING IT!")


def load_tasks(event):
    try:
        tasks= pickle.load(open("other files/tasks.dat", "rb"))
        listbox.delete(0, END)
        for task in tasks:
            listbox.insert(END, task)
    except:
        msg.showerror("ERROR", "YOU DON'T HAVE ANY SAVED TASKS")

def delete_task(event):
    try:
        delete =listbox.curselection()[0]
        listbox.delete(delete)
        tasks = listbox.get(0, listbox.size())
        pickle.dump(tasks, open("other files/tasks.dat", "wb"))
    except:
        msg.showerror("ERROR", "YOU MUST SELECT A TASK")
def clear_tasks(event):
    try:
        listbox.delete(0, END)
        os.remove("other files/tasks.dat")

    except:
        msg.showerror("ERROR", "YOU DON'T HAVE ANY SAVED TASKS")

input_value= StringVar()

scrollbar= Scrollbar(frame1)
scrollbar.grid(row= 0, sticky= "e", padx= 10)

listbox= Listbox(frame1, width= 56 , height= 10, font=("Comic Sans MS", 14, "bold"))
listbox.grid(row=0)

listbox.config(yscrollcommand= scrollbar.set)
scrollbar.config(command= listbox.yview)

ui= Entry(frame1,textvariable= input_value,width= 28,font= ("Georgia", 14))
ui.grid(row= 40,pady= 15, sticky= "w", padx= 6)


add_button= Button(frame1,text="SAVE TASK", width= 46)
add_button.bind("<Button-1>", save_task)
add_button.grid( sticky= "w", padx= 10, ipady= 5)

load_button= Button(frame1,text="LOAD ALL TASKS",  width= 46)
load_button.bind("<Button-1>", load_tasks)
load_button.grid( sticky= "w", padx= 10, ipady= 5)

delete_button= Button(frame1,text="DELETE TASK",  width= 46)
delete_button.bind("<Button-1>", delete_task)
delete_button.grid( sticky= "w",padx= 10, ipady= 5)
clear_button= Button(frame1,text="DELETE ALL TASKS",  width= 46)
clear_button.bind("<Button-1>", clear_tasks)
clear_button.grid( sticky= "w",padx= 10, ipady=5)


root.mainloop()