
import sys
import pymysql
from tkinter import messagebox
import matplotlib.pyplot as plt
from collections import Counter

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import book_details_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    book_details_support.set_Tk_var()
    top = New_Toplevel (root)
    book_details_support.init(root, top)
    root.mainloop()

w = None
def create_New_Toplevel(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    book_details_support.set_Tk_var()
    top = New_Toplevel (w)
    book_details_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_New_Toplevel():
    global w
    w.destroy()
    w = None


class New_Toplevel:
    def myquit(self):
        book_details_support.destroy_window()
        import panel
        panel.vp_start_gui()

    def add(self):
        try:
            title = self.Entry1.get()
            author = self.Entry2.get()
            year = self.Entry3.get()
            isbn = self.Entry4.get()
            cat=self.TCombobox1.get()
            self.c.execute("insert into book values('" + title + "','" + author + "','"+ cat +"'," + year + "," + isbn + ")")
            self.db.commit()
            self.showdata()
            messagebox.showinfo('book Details', 'YOU HAVE SUCCESFULLY INSERTED')
            self.Entry1.delete(0, END)
            self.Entry2.delete(0, END)
            self.Entry3.delete(0, END)
            self.Entry4.delete(0, END)
            self.TCombobox1.delete(0,END)

        except:
            self.db.rollback()
            self.db.close()
            messagebox.showinfo('book Details', 'SOMETHING WENT WRONG...!')

    def modify(self):
        try:
            title = self.Entry1.get()
            author = self.Entry2.get()
            year = self.Entry3.get()
            isbn = self.Entry4.get()
            cat = self.TCombobox1.get()
            self.c.execute("update book set title='" + title + "', author='" + author +"', category='"+ cat +"', year=" + year + " where isbn=" + isbn + "")
            self.db.commit()
            self.showdata()
            messagebox.showinfo('book Details', 'YOU HAVE SUCESSFULLY UPDATED ')
            self.Entry1.delete(0, END)
            self.Entry2.delete(0, END)
            self.Entry3.delete(0, END)
            self.Entry4.delete(0, END)
            self.TCombobox1.delete(0, END)
        except:
            self.db.rollback()
            self.db.close()
            messagebox.showinfo('Book Details', 'Something Went wrong....!')

    def delete(self):
        try:
            isbn = self.Entry4.get()
            self.c.execute("delete from book where isbn=" + isbn)
            self.db.commit()
            self.showdata()
            messagebox.showinfo('Book Details', "YOU HAVE SUCCESSFULLY DELETED")
            self.Entry1.delete(0, END)
            self.Entry2.delete(0, END)
            self.Entry3.delete(0, END)
            self.Entry4.delete(0, END)
            self.TCombobox1.delete(0, END)
        except:
            self.db.rollback()
            self.db.close()
            messagebox.showinfo('Book Details', 'SOMEHING WENT WRONG...!')

    def showdata(self):
        sql = "select *from book"
        self.c.execute(sql)
        results = self.c.fetchall()
        i = 0
        self.Listbox1.delete(0, END)
        for row in results:
            self.Listbox1.insert(i, row)
            i = i + 1

    def selection(self, event):
        index = self.Listbox1.curselection()  [0]
        self.selected_tuple = self.Listbox1.get(index)
        print(index)
        self.Entry1.delete(0, END)
        self.Entry1.insert(END, self.selected_tuple[0])
        self.Entry2.delete(0, END)
        self.Entry2.insert(END, self.selected_tuple[1])
        self.TCombobox1.delete(0, END)
        self.TCombobox1.insert(END, self.selected_tuple[2])
        self.Entry3.delete(0, END)
        self.Entry3.insert(END, self.selected_tuple[3])
        self.Entry4.delete(0, END)
        self.Entry4.insert(END, self.selected_tuple[4])

    def histo(self):
        self.db = pymysql.connect("127.0.0.1", "root", "1234", "institute", 3307)
        self.c = self.db.cursor()
        self.s = "select category from book"
        self.c.execute(self.s)
        self.result = self.c.fetchall()
        print(self.result)
        genre_dict = dict(Counter(self.result))
        plt.pie(genre_dict.values(), labels=genre_dict.keys())
        plt.title("Genre distribution of Books")
        plt.show()


    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font10 = "-family {Courier New} -size 10 -weight normal -slant"  \
            " roman -underline 0 -overstrike 0"
        font11 = "-family {Tempus Sans ITC} -size 9 -weight bold "  \
            "-slant roman -underline 0 -overstrike 0"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("600x450+435+147")
        top.title("BOOKS DETAILS")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.db=pymysql.connect("127.0.0.1","root","1234","institute",3307)
        self.c=self.db.cursor()

        self.Frame1 = Frame(top)
        self.Frame1.place(relx=0.0, rely=0.0, relheight=2.0, relwidth=2.02)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#72d898")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="#646464")
        self.Frame1.configure(width=1210)

        self.Label2 = Label(self.Frame1)
        self.Label2.place(relx=0.0, rely=0.04, height=21, width=64)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#72d898")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font11)
        self.Label2.configure(foreground="#cc0e00")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''TITLE''')

        self.Entry1 = Entry(self.Frame1)
        self.Entry1.place(relx=0.08, rely=0.04,height=20, relwidth=0.14)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font=font10)
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="#c4c4c4")
        self.Entry1.configure(selectforeground="black")

        self.Entry2 = Entry(self.Frame1)
        self.Entry2.place(relx=0.32, rely=0.04,height=20, relwidth=0.14)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font=font10)
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(highlightbackground="#d9d9d9")
        self.Entry2.configure(highlightcolor="black")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(selectbackground="#c4c4c4")
        self.Entry2.configure(selectforeground="black")

        self.Label3 = Label(self.Frame1)
        self.Label3.place(relx=0.26, rely=0.04, height=21, width=64)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#72d898")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font=font11)
        self.Label3.configure(foreground="#cc0e00")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="SystemWindow")
        self.Label3.configure(text='''AUTHOR''')

        self.Entry3 = Entry(self.Frame1)
        self.Entry3.place(relx=0.24, rely=0.12,height=20, relwidth=0.07)
        self.Entry3.configure(background="white")
        self.Entry3.configure(disabledforeground="#a3a3a3")
        self.Entry3.configure(font=font10)
        self.Entry3.configure(foreground="#000000")
        self.Entry3.configure(highlightbackground="#d9d9d9")
        self.Entry3.configure(highlightcolor="black")
        self.Entry3.configure(insertbackground="black")
        self.Entry3.configure(selectbackground="#c4c4c4")
        self.Entry3.configure(selectforeground="black")
        self.Entry3.configure(width=84)

        self.Label4 = Label(self.Frame1)
        self.Label4.place(relx=0.33, rely=0.12, height=21, width=31)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(background="#72d898")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(font=font11)
        self.Label4.configure(foreground="#cc0e00")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='''ISBN''')

        self.Entry4 = Entry(self.Frame1)
        self.Entry4.place(relx=0.38, rely=0.12,height=20, relwidth=0.08)
        self.Entry4.configure(background="white")
        self.Entry4.configure(disabledforeground="#a3a3a3")
        self.Entry4.configure(font=font10)
        self.Entry4.configure(foreground="#000000")
        self.Entry4.configure(highlightbackground="#d9d9d9")
        self.Entry4.configure(highlightcolor="black")
        self.Entry4.configure(insertbackground="black")
        self.Entry4.configure(selectbackground="#c4c4c4")
        self.Entry4.configure(selectforeground="black")
        self.Entry4.configure(width=94)

        self.Button1 = Button(self.Frame1)
        self.Button1.place(relx=0.03, rely=0.18, height=24, width=67)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#30a0d8")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(command=self.add,text='''ADD''')
        self.Button1.configure(width=67)

        self.Button2 = Button(self.Frame1)
        self.Button2.place(relx=0.13, rely=0.18, height=24, width=67)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#db3778")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(command=self.delete,text='''DELETE''')
        self.Button2.configure(width=67)

        self.Button3 = Button(self.Frame1)
        self.Button3.place(relx=0.22, rely=0.18, height=24, width=67)
        self.Button3.configure(activebackground="#d9d9d9")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#30a0d8")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(command=self.modify,text='''UPDATE''')
        self.Button3.configure(width=67)

        self.Button4 = Button(self.Frame1)
        self.Button4.place(relx=0.32, rely=0.18, height=24, width=67)
        self.Button4.configure(activebackground="#d9d9d9")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#db3778")
        self.Button4.configure(disabledforeground="#a3a3a3")
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(command=self.myquit,text='''QUIT''')
        self.Button4.configure(width=67)

        self.Frame2 = Frame(self.Frame1)
        self.Frame2.place(relx=0.02, rely=0.22, relheight=0.26, relwidth=0.45)
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(background="#ffb0bd")
        self.Frame2.configure(highlightbackground="#d9d9d9")
        self.Frame2.configure(highlightcolor="black")
        self.Frame2.configure(width=545)

        self.Listbox1 = Listbox(self.Frame2)
        self.Listbox1.place(relx=0.1, rely=0.11, relheight=0.77, relwidth=0.8)
        self.Listbox1.configure(background="white")
        self.Listbox1.configure(disabledforeground="#a3a3a3")
        self.Listbox1.configure(font=font10)
        self.Listbox1.configure(foreground="#000000")
        self.Listbox1.configure(highlightbackground="#d9d9d9")
        self.Listbox1.configure(highlightcolor="black")
        self.Listbox1.configure(selectbackground="#c4c4c4")
        self.Listbox1.configure(selectforeground="black")
        self.Listbox1.configure(width=434)
        self.Listbox1.bind('<<ListboxSelect>>', self.selection)
        self.showdata()

        self.Label5 = Label(self.Frame1)
        self.Label5.place(relx=0.19, rely=0.12, height=22, width=40)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(activeforeground="black")
        self.Label5.configure(background="#72d898")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(font=font11)
        self.Label5.configure(foreground="#cc0e00")
        self.Label5.configure(highlightbackground="#d9d9d9")
        self.Label5.configure(highlightcolor="black")
        self.Label5.configure(text='''YEAR''')

        self.Label1 = Label(self.Frame1)
        self.Label1.place(relx=0.01, rely=0.12, height=21, width=74)
        self.Label1.configure(background="#72d898")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font11)
        self.Label1.configure(foreground="#cc0e00")
        self.Label1.configure(text='''CATEGORY''')
        self.Label1.configure(width=74)

        self.TCombobox1 = ttk.Combobox(self.Frame1)
        self.TCombobox1.place(relx=0.08, rely=0.12, relheight=0.025
                , relwidth=0.09)
        self.value_list = ['CSE','ME','CE','ECE','EE','ACCOUNT','BUSINESS','ECONOMICS',]
        self.TCombobox1.configure(values=self.value_list)
        self.TCombobox1.configure(textvariable=book_details_support.combobox)
        self.TCombobox1.configure(width=103)
        self.TCombobox1.configure(takefocus="")

        self.Button5 = Button(self.Frame1)
        self.Button5.place(relx=0.41, rely=0.18, height=24, width=67)
        self.Button5.configure(activebackground="#d9d9d9")
        self.Button5.configure(activeforeground="#000000")
        self.Button5.configure(background="#30a0d8")
        self.Button5.configure(disabledforeground="#a3a3a3")
        self.Button5.configure(foreground="#000000")
        self.Button5.configure(highlightbackground="#d9d9d9")
        self.Button5.configure(highlightcolor="black")
        self.Button5.configure(pady="0")
        self.Button5.configure(command=self.histo,text='''ANALYSE''')
        self.Button5.configure(width=67)






if __name__ == '__main__':
    vp_start_gui()



