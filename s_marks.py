
import sys
import pymysql
from tkinter import messagebox

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

import s_marks_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = New_Toplevel (root)
    s_marks_support.init(root, top)
    root.mainloop()

w = None
def create_New_Toplevel(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = New_Toplevel (w)
    s_marks_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_New_Toplevel():
    global w
    w.destroy()
    w = None


class New_Toplevel:
    def log(self):
        self.db = pymysql.connect("127.0.0.1", "root", "1234", "institute", 3307)
        self.c = self.db.cursor()
        #self.roll=self.Entry1.get()
        try:
            self.c.execute("select * from students where ROLL_NO=%d" %(int(self.Entry1.get())))
            self.result = self.c.fetchone()
            self.db.commit()

            if self.result:
                messagebox.showinfo('RESULT','YOUR ROLL IS BEING FOUND')
                s_marks_support.destroy_window()
                import marks_detail
                marks_detail.vp_start_gui()
                self.db.commit()
            else:
                messagebox.showwarning('RESULT','ROLL NOT FOUND')

        except:
            self.db.rollback()
            self.db.close()
            print("something went wrong")
            messagebox.showwarning('RESULT', 'SOMETHING WENT WRONG.....')
    def myuit(self):
        s_marks_support.destroy_window()
        import student
        student.vp_start_gui()

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
        font11 = "-family {Segoe UI} -size 11 -weight bold -slant "  \
            "italic -underline 1 -overstrike 0"
        font15 = "-family {Segoe UI} -size 8 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"

        top.geometry("600x450+450+141")
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")



        self.Frame1 = Frame(top)
        self.Frame1.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#09a1d8")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")
        self.Frame1.configure(width=125)

        self.Label1 = Label(self.Frame1)
        self.Label1.place(relx=0.25, rely=0.07, height=21, width=294)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#c5d849")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font11)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''RESULT''')

        self.Frame2 = Frame(self.Frame1)
        self.Frame2.place(relx=0.12, rely=0.24, relheight=0.59, relwidth=0.78)
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(background="#d8707e")
        self.Frame2.configure(highlightbackground="#d9d9d9")
        self.Frame2.configure(highlightcolor="black")
        self.Frame2.configure(width=465)

        self.Label2 = Label(self.Frame2)
        self.Label2.place(relx=0.11, rely=0.26, height=21, width=144)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font15)
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''ENTER STUDENT ROLL NO.''')
        self.Label2.configure(width=144)

        self.Entry1 = Entry(self.Frame2)
        self.Entry1.place(relx=0.45, rely=0.26,height=20, relwidth=0.35)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font=font10)
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="#c4c4c4")
        self.Entry1.configure(selectforeground="black")

        self.Button1 = Button(self.Frame2)
        self.Button1.place(relx=0.69, rely=0.45, height=24, width=57)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#61d871")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(command=self.log,text='''SUBMIT''')
        self.Button1.configure(width=57)

        self.Button2 = Button(self.Frame2)
        self.Button2.place(relx=0.45, rely=0.45, height=24, width=57)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d86b18")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(command=self.myuit,text='''BACK''')
        self.Button2.configure(width=57)






if __name__ == '__main__':
    vp_start_gui()



