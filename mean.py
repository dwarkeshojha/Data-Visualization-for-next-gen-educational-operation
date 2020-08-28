
import sys
import pymysql
import numpy as np
import pandas as pd

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

import mean_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = New_Toplevel (root)
    mean_support.init(root, top)
    root.mainloop()

w = None
def create_New_Toplevel(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = New_Toplevel (w)
    mean_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_New_Toplevel():
    global w
    w.destroy()
    w = None


class New_Toplevel:
    def histo(self):
        mean_support.destroy_window()
        import  marks_detail
        marks_detail.vp_start_gui()
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

        top.geometry("600x450+439+146")
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")

        self.db = pymysql.connect("127.0.0.1", "root", "1234", "institute", 3307)
        self.c = self.db.cursor()
        self.s = "select total from marks"
        self.c.execute(self.s)
        self.result = self.c.fetchall()
        print(self.result)
        print("Mean",np.mean(self.result))
        self.means=np.mean(self.result)

        self.medians=np.median(self.result)
        print(self.medians)

        self.sql='select ROLL_NO, name, total from marks order by total desc limit 3'
        self.c.execute(self.sql)
        self.results = self.c.fetchall()
        print(self.results)
        self.titles_df=self.results
        #self.titles_df.groupby(['roll no','name'],as_index=False).mean().sort_values(by='total',ascending=False).head(3)
        #print(self.titles_df.groupby(['ROLL_NO' ,'name' , 'total'], as_index=False).mean().sort_values(by='total',ascending=False).head(3))
        print(len(self.titles_df))




        self.Frame1 = Frame(top)
        self.Frame1.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#9cd4d8")
        self.Frame1.configure(width=125)

        self.Label1 = Label(self.Frame1)
        self.Label1.place(relx=0.17, rely=0.04, height=21, width=391)
        self.Label1.configure(background="#d875c7")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''MARKS ANALYSIS''')
        self.Label1.configure(width=391)

        self.Label2 = Label(self.Frame1)
        self.Label2.place(relx=0.2, rely=0.3, height=21, width=86)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Mean''')
        self.Label2.configure(width=86)

        self.Label3 = Label(self.Frame1)
        self.Label3.place(relx=0.2, rely=0.46, height=21, width=86)
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''Median''')
        self.Label3.configure(width=86)

        self.Entry1 = Entry(self.Frame1)
        self.Entry1.place(relx=0.5, rely=0.29,height=30, relwidth=0.27)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font=font10)
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(width=164)
        self.Entry1.delete(0,END)
        self.Entry1.insert(0,self.means)

        self.Entry2 = Entry(self.Frame1)
        self.Entry2.place(relx=0.5, rely=0.44,height=30, relwidth=0.27)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font=font10)
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(width=164)
        self.Entry2.delete(0, END)
        self.Entry2.insert(0, self.medians)

        self.Listbox1 = Listbox(self.Frame1)
        self.Listbox1.place(relx=0.17, rely=0.62, relheight=0.32, relwidth=0.66)
        self.Listbox1.configure(background="white")
        self.Listbox1.configure(disabledforeground="#a3a3a3")
        self.Listbox1.configure(font=font10)
        self.Listbox1.configure(foreground="#000000")
        self.Listbox1.configure(width=394)
        msg1="                Institute Toppers   "
        self.Listbox1.insert(0,msg1)
        msg2="NAME                      TOTAL MARKS"
        self.Listbox1.insert(1,msg2)
        i=2
        for row in self.titles_df:
            self.Listbox1.insert(i,str(row[1]).ljust(5)+"                       "+str(row[2]))
            i=i+1

        self.Button1 = Button(self.Frame1)
        self.Button1.place(relx=0.85, rely=0.85, height=34, width=73)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="RED")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(command=self.histo, text='''BACK''')

if __name__ == '__main__':
    vp_start_gui()



