from tkinter import *
import pyshorteners
import pyperclip

root = Tk()
root.title('URL shortner')
root.geometry('480x200')
root.configure(background='orange')
def shot():
    def copy():
        pyperclip.copy(f'{var2.get()}')
        pyperclip.paste()
    link = var1.get()
    shortIt = pyshorteners.Shortener()
    x = shortIt.tinyurl.short(link)
    var2 = StringVar()
    var2.set(x)
    frm2 = Frame(root)
    Entry(frm2, textvariable=var2, font='arial 15 bold',width='30', relief=FLAT).pack(side=LEFT,padx=2)
    Button(frm2, text='copy',font='arial',command=copy).pack(side=RIGHT,padx=5)
    frm2.pack(pady=10)

frm1 = Frame(root)
Label(frm1, text='Enter Link ',font='arial 15 bold', relief=FLAT).pack(side=LEFT)
var1=StringVar()
Entry(frm1, textvariable=var1,font='arial 15 bold', relief=SUNKEN, width='30').pack(side=RIGHT,padx=5)
frm1.pack(pady=20)
Button(root, text='GENERATE', font='arial 10 bold', command=shot).pack()
endfrm = Frame(root,bg='gold')
Label(endfrm,text="By Starkk's", bg='gold').pack(side=RIGHT)
Label(endfrm,text='©by stkk.UShort.0.1').pack(side=LEFT)
endfrm.pack(side=BOTTOM, fill=X)
root.mainloop()
