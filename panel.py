import sys

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

import panel_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = New_Toplevel (root)
    panel_support.init(root, top)
    root.mainloop()

w = None
def create_New_Toplevel(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = New_Toplevel (w)
    panel_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_New_Toplevel():
    global w
    w.destroy()
    w = None


class New_Toplevel:
    def cm(self):
        panel_support.destroy_window()
        import circular
        circular.vp_start_gui()
    def bd(self):
        panel_support.destroy_window()
        import book_details
        book_details.vp_start_gui()
    def std(self):
        panel_support.destroy_window()
        import student
        student.vp_start_gui()
    def td(self):
        panel_support.destroy_window()
        import teacher_details
        teacher_details.vp_start_gui()
    def myquit(self):
        panel_support.destroy_window()
        import ITM_PROJECT
        ITM_PROJECT.vp_start_gui()
    def tb(self):
        panel_support.destroy_window()
        import time_table
        time_table.vp_start_gui()

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

        top.geometry("600x450+470+141")
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")



        self.Frame1 = Frame(top)
        self.Frame1.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#c47680")
        self.Frame1.configure(highlightbackground="#000000")
        self.Frame1.configure(highlightcolor="black")
        self.Frame1.configure(width=125)

        self.Label2 = Label(self.Frame1)
        self.Label2.place(relx=0.27, rely=0.02, height=34, width=306)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#d2d7d8")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font11)
        self.Label2.configure(foreground="#161616")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''INSTITUTE MANAGEMENT SYSTEM''')

        self.Button1 = Button(self.Frame1)
        self.Button1.place(relx=0.08, rely=0.16, height=34, width=147)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#e5291b")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(command=self.bd,text='''BOOK DETAILS''')

        self.Button2 = Button(self.Frame1)
        self.Button2.place(relx=0.08, rely=0.30, height=34, width=147)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#7855b5")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(command=self.std,text='''STUDENT DETAILS''')

        self.Button3 = Button(self.Frame1)
        self.Button3.place(relx=0.08, rely=0.45, height=34, width=147)
        self.Button3.configure(activebackground="#d9d9d9")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#e5291b")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(command=self.td,text='''TEACHER DETAILS''')

        self.Button4 = Button(self.Frame1)
        self.Button4.place(relx=0.08, rely=0.60, height=34, width=147)
        self.Button4.configure(activebackground="#d9d9d9")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#7855b5")
        self.Button4.configure(disabledforeground="#a3a3a3")
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(command=self.cm,text='''CIRCULAR''')

        self.Button5 = Button(self.Frame1)
        self.Button5.place(relx=0.08, rely=0.75, height=34, width=147)
        self.Button5.configure(activebackground="#d9d9d9")
        self.Button5.configure(activeforeground="#000000")
        self.Button5.configure(background="#e5291b")
        self.Button5.configure(disabledforeground="#a3a3a3")
        self.Button5.configure(foreground="#000000")
        self.Button5.configure(highlightbackground="#d9d9d9")
        self.Button5.configure(highlightcolor="black")
        self.Button5.configure(pady="0")
        self.Button5.configure(command=self.tb,text='''TIME TABLE''')

        self.Button6 = Button(self.Frame1)
        self.Button6.place(relx=0.08, rely=0.9, height=34, width=147)
        self.Button6.configure(activebackground="#d9d9d9")
        self.Button6.configure(activeforeground="#000000")
        self.Button6.configure(background="#7855b5")
        self.Button6.configure(disabledforeground="#a3a3a3")
        self.Button6.configure(foreground="#000000")
        self.Button6.configure(highlightbackground="#d9d9d9")
        self.Button6.configure(highlightcolor="black")
        self.Button6.configure(pady="0")
        self.Button6.configure(command=self.myquit, text='''QUIT''')

        self.Label1 = Label(self.Frame1)
        self.Label1.place(relx=0.45, rely=0.29, height=181, width=284)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self._img1 = PhotoImage(file="./new-student-clipart-2.png")
        self.Label1.configure(image=self._img1)
        self.Label1.configure(text='''Label''')
        self.Label1.configure(width=284)






if __name__ == '__main__':
    vp_start_gui()



