import tkinter
from tkinter import filedialog
import os

def file_select():
    filename = filedialog.askopenfilename(initialdir='/', title='Выберите файл', filetypes=(('Text files', '*.txt'), ('All files', '*.*')))
    text['text'] = os.path.basename(filename)
    os.startfile(filename)

window = tkinter.Tk()
window.title('Проводник')
window.geometry('350x350')
window.configure(bg = 'skyblue')
window.resizable(0, 0)
text = tkinter.Label(window, text='Файл:', height= 10, width= 20, background= 'silver')
text.grid(row=1, column=1)
button_select = tkinter.Button(window, width= 20, height=3, text = 'Выбрать файл', command = file_select)
button_select.grid(row=2, column=1)


window.mainloop()

