from tkinter import *
from tkinter import filedialog, messagebox

# Initialize the main application window
root = Tk()
root.title("POLZ Notepad")
root.config(bg='teal')
root.geometry("600x400")  # Set default window size
root.resizable(True, True)

# Functions
def save_file():
    """Save the content to a file."""
    open_file = filedialog.asksaveasfile(mode='w', defaultextension='.txt', filetypes=[('Text Files', '*.txt')])
    if open_file is None:
        return
    text = entry.get(1.0, END).strip()
    open_file.write(text)
    open_file.close()
    messagebox.showinfo("Success", "File saved successfully!")

def open_file():
    """Open a file and display its content in the text area."""
    file = filedialog.askopenfile(mode='r', filetypes=[('Text Files', '*.txt')])
    if file is not None:
        content = file.read()
        entry.delete(1.0, END)
        entry.insert(INSERT, content)
        file.close()

def clear_text():
    """Clear the text area."""
    entry.delete(1.0, END)


def word_count():
    """Display the word count in the text area."""
    text = entry.get(1.0, END).strip()
    words = len(text.split())
    messagebox.showinfo("Word Count", f"Word Count: {words}")

def change_bg_color():
    """Change the background color of the text area."""
    colors = ['white', 'lightyellow', 'lightblue', 'lightgreen']
    current_color = entry.cget('bg')
    new_color = colors[(colors.index(current_color) + 1) % len(colors)] if current_color in colors else 'white'
    entry.config(bg=new_color)

# Function to create rounded buttons
def create_rounded_button(parent, text, command, bg, fg):
    return Button(parent, text=text, command=command, bg=bg, fg=fg, relief=FLAT, borderwidth=2, highlightbackground=bg, highlightcolor=bg, padx=10, pady=5)

# Button Frame
button_frame = Frame(root, bg='teal')
button_frame.pack(fill=X, padx=10, pady=10)

# Buttons
b1 = create_rounded_button(button_frame, text='Save File', command=save_file, bg='#dcdcdc', fg='#333333')
b1.pack(side=LEFT, padx=10)

b2 = create_rounded_button(button_frame, text='Open File', command=open_file, bg='#dcdcdc', fg='#333333')
b2.pack(side=LEFT, padx=10)

b3 = create_rounded_button(button_frame, text='Clear Text', command=clear_text, bg='#dcdcdc', fg='#333333')
b3.pack(side=LEFT, padx=10)

b4 = create_rounded_button(button_frame, text='Word Count', command=word_count, bg='#dcdcdc', fg='#333333')
b4.pack(side=LEFT, padx=10)

b5 = create_rounded_button(button_frame, text='Change BG Color', command=change_bg_color, bg='#dcdcdc', fg='#333333')
b5.pack(side=LEFT, padx=10)

# Text Entry
entry = Text(root, wrap=WORD, font=("Arial", 12), relief=FLAT, borderwidth=5)
entry.pack(fill=BOTH, expand=True, padx=10, pady=10)

root.mainloop()
