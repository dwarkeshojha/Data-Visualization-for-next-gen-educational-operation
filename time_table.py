
import sys
import os

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

import time_table_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = New_Toplevel (root)
    time_table_support.init(root, top)
    root.mainloop()

w = None
def create_New_Toplevel(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = New_Toplevel (w)
    time_table_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_New_Toplevel():
    global w
    w.destroy()
    w = None


class New_Toplevel:
    def backy(self):
        time_table_support.destroy_window()
        import panel
        panel.vp_start_gui()
    def cse(self):
        os.startfile("cse2.pdf")
    def me(self):
        os.startfile("cse2.pdf")
    def ce(self):
        os.startfile("cse2.pdf")
    def ece(self):
        os.startfile("cse2.pdf")
    def ee(self):
        os.startfile("cse2.pdf")

    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font11 = "-family {Segoe UI} -size 12 -weight bold -slant "  \
            "italic -underline 1 -overstrike 0"

        top.geometry("600x450+403+176")
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")



        self.Frame1 = Frame(top)
        self.Frame1.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#bfb397")
        self.Frame1.configure(width=125)

        self.Label1 = Label(self.Frame1)
        self.Label1.place(relx=0.13, rely=0.03, height=21, width=444)
        self.Label1.configure(background="#b7ef56")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font11)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''TIME TABLE''')
        self.Label1.configure(width=444)

        self.Button1 = Button(self.Frame1)
        self.Button1.place(relx=0.2, rely=0.16, height=24, width=387)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#5fccd8")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(command=self.cse,text='''CSE (1st,2nd,3rd,4th years)''')
        self.Button1.configure(width=387)

        self.Button2 = Button(self.Frame1)
        self.Button2.place(relx=0.2, rely=0.3, height=24, width=387)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#c2a0d8")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(command=self.me,text='''ME (1st,2nd,3rd,4th years)''')
        self.Button2.configure(width=387)

        self.Button3 = Button(self.Frame1)
        self.Button3.place(relx=0.2, rely=0.46, height=24, width=387)
        self.Button3.configure(activebackground="#d9d9d9")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#5fccd8")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(command=self.ce,text='''CE (1st,2nd,3rd,4th years)''')
        self.Button3.configure(width=387)

        self.Button4 = Button(self.Frame1)
        self.Button4.place(relx=0.2, rely=0.6, height=24, width=387)
        self.Button4.configure(activebackground="#d9d9d9")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#c2a0d8")
        self.Button4.configure(disabledforeground="#a3a3a3")
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(command=self.ece,text='''ECE (1st,2nd,3rd,4th years)''')
        self.Button4.configure(width=387)

        self.Button5 = Button(self.Frame1)
        self.Button5.place(relx=0.2, rely=0.75, height=24, width=387)
        self.Button5.configure(activebackground="#d9d9d9")
        self.Button5.configure(activeforeground="#000000")
        self.Button5.configure(background="#5fccd8")
        self.Button5.configure(disabledforeground="#a3a3a3")
        self.Button5.configure(foreground="#000000")
        self.Button5.configure(highlightbackground="#d9d9d9")
        self.Button5.configure(highlightcolor="black")
        self.Button5.configure(pady="0")
        self.Button5.configure(command=self.ee,text='''EEE (1st,2nd,3rd,4th years)''')
        self.Button5.configure(width=387)

        self.Button6 = Button(self.Frame1)
        self.Button6.place(relx=0.48, rely=0.87, height=24, width=47)
        self.Button6.configure(activebackground="#d9d9d9")
        self.Button6.configure(activeforeground="#000000")
        self.Button6.configure(background="red")
        self.Button6.configure(disabledforeground="#a3a3a3")
        self.Button6.configure(foreground="#000000")
        self.Button6.configure(highlightbackground="#d9d9d9")
        self.Button6.configure(highlightcolor="black")
        self.Button6.configure(pady="0")
        self.Button6.configure(command=self.backy,text='''BACK''')

if __name__ == '__main__':
    vp_start_gui()



