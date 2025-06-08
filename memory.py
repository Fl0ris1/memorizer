from tkinter import *
from tkinter.filedialog import *

def openFile():
    file1=askopenfile(title="Open File")
    if file1 is not None:
        listbox.delete(0,END)
        items=file1.readlines()
        for item in items:
            listbox.insert(END,item.strip())

def saveFile():
    file1=asksaveasfile(defaultextension=".txt")
    if file1 is not None:
        for item in listbox.get(0,END):
            print(item.strip(),file=file1)
        listbox.delete(0,END)

def addItem():
    listbox.insert(END,item.get())
    item.delete(0,END)

def deleteItem():
    index=listbox.curselection()
    if index:
        listbox.delete(index)

root=Tk()
root.title("Memorizer")
root.config(background="#8FD694")

saveBtn=Button(root,text="SAVE",fg="#A1C084",bg="#516B4F",width=15,font=("consolas",16,"bold"),command=saveFile)
saveBtn.pack(padx=5,pady=5)

item=Entry(root,width=25)
item.pack(padx=5,pady=5)

addBtn=Button(root,text="ADD",fg="#96BE8C",bg="#283D3B",width=15,font=("consolas",16,"bold"),command=addItem)
addBtn.pack(padx=5,pady=5)

openBtn=Button(root,text="OPEN",font=("consolas",16,"bold"),fg="#6BA368",bg="#515B3A",width=15,command=openFile)
openBtn.pack(side=LEFT,padx=5,pady=5)

deleteBtn=Button(root,text="DELETE",font=("consolas",16,"bold"),fg="#32A287",bg="#03312E",width=15,command=deleteItem)
deleteBtn.pack(side=RIGHT,padx=5,pady=5)

frame=Frame(root)
frame.pack(side=RIGHT)

scrollbar=Scrollbar(frame,orient="vertical")
scrollbar.pack(side=RIGHT,fill=Y)

listbox=Listbox(frame,width=70,bg="#AAC0AA",fg="#4D5743",font=("consolas",18,"bold"),yscrollcommand=scrollbar.set)
for i in range(1,51):
    listbox.insert(END,str(i))

listbox.pack(side=LEFT,padx=5)
scrollbar.config(command=listbox.yview)





root.mainloop()