from tkinter import *
from tkinter import messagebox
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://root:1234@careerbot.i0gdj.mongodb.net/<dbname>?retryWrites=true&w=majority")
db = cluster["res_data"]
collection = db["res_data"]


def insertdata(otpt):
    inputdata = inptvar.get().lower()
    outputdata = otptEntry.get('1.0', END+'-1c')
    try:
        train_dict = {'input':inputdata, 'output':outputdata}
        collection.insert_one(train_dict)
        inptvar.set('')
        otptEntry.delete('1.0', END)
        messagebox.showinfo(title="Success", message="Entry inserted successfully!")
    except:
        messagebox.showerror(title="ERROR",message="SOMETHING WENT WRONG")


tkWindow = Tk()
tkWindow.geometry('400x300')
tkWindow.title('Train Response Data')


inptLabel = Label(tkWindow, text="Input").grid(row=0, column=0)
inptvar = StringVar()
inptEntry = Entry(tkWindow, width=50, textvariable=inptvar).grid(row=0, column=1)

otptLabel = Label(tkWindow, text="Output").grid(row=1, column=0)
otptEntry = Text(tkWindow, width=25, height=10)
otptEntry.grid(row=1, column=1)
otptEntry.configure(font=('Courier'))

def shortcuting(event):
    if event.char == "\x1b":
        insertdata(inptvar)


sendButton = Button(tkWindow, text="Save", command=lambda : insertdata(None)).grid(row=2, column=1)
tkWindow.bind("<Key>", shortcuting)

tkWindow.mainloop()
