from tkinter import *
from tkinter import filedialog

root=Tk()
root.title("POLZ")
root.config(bg='teal')
root.resizable(True,True)


def save_file():
    open_file=filedialog.asksaveasfile(mode='w' ,defaultextension='.txt')
    if open_file is None:
        return
    text=str(entry.get(1.0,END))
    open_file.write(text)
    open_file.close()
    
def open_file():
    file=filedialog.askopenfile(mode='r' ,filetypes=[('text files', '*.txt')])
    if file is not None:
        content=file.read()
    entry.insert(INSERT,content)
    

button_frame=Frame(root, bg='teal')
button_frame.pack(fill=X, padx=10, pady=10)


b1=Button(button_frame, bg='#dcdcdc' ,text='save_file' ,command=save_file, fg='#333333')
b1.pack(side=LEFT, padx=10)

b2=Button(button_frame, bg='#dcdcdc' ,text='open_file' ,command=open_file, fg='#333333')
b2.pack(side=LEFT, padx=10)

entry=Text(root, wrap=WORD)
entry.pack(fill=BOTH, expand=True, padx=10, pady=10)

root.mainloop()