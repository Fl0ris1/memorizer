from tkinter import *
from tkinter.filedialog import *

root=Tk()
root.title("Memorizer")
root.config(background="#8FD694")

saveBtn=Button(root,text="SAVE",fg="#A1C084",bg="#516B4F",width=15,font=("consolas",16,"bold"))
saveBtn.pack(padx=5,pady=5)

item=Entry(root,width=25)
item.pack(padx=5,pady=5)

addBtn=Button(root,text="ADD",fg="#96BE8C",bg="#283D3B",width=15,font=("consolas",16,"bold"))
addBtn.pack(padx=5,pady=5)

openBtn=Button(root,text="OPEN",font=("consolas",16,"bold"),fg="#6BA368",bg="#515B3A",width=15)
openBtn.pack(side=LEFT,padx=5,pady=5)

deleteBtn=Button(root,text="DELETE",font=("consolas",16,"bold"),fg="#32A287",bg="#03312E",width=15)
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