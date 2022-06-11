from tkinter import *
from tkinter import filedialog

def openFile():
    filepath = filedialog.askopenfilename()
    f = open(filepath,'r')
    content = f.read()
    f.close()
    print(content)
    
def openFiles():
    filepath = filedialog.askopenfilenames()
    file_list = list(filepath)
    print(file_list)
    


window = Tk()
window.title("File Reader")
window.geometry("300x300")
button = Button(text="Open", command=openFile)
button2 = Button(text="Open Files", command=openFiles)
button.pack()
button2.pack()
window.mainloop()
