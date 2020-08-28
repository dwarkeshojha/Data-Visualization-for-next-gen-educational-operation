
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

import forgot_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = New_Toplevel (root)
    forgot_support.init(root, top)
    root.mainloop()

w = None
def create_New_Toplevel(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = New_Toplevel (w)
    forgot_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_New_Toplevel():
    global w
    w.destroy()
    w = None


class New_Toplevel:
    def backy(self):
        forgot_support.destroy_window()
        import itm_log
        itm_log.vp_start_gui()
    def log(self):
        self.uname=self.Entry1.get()
        self.pword=self.Entry2.get()
        self.cnf=self.Entry3.get()
        self.db = pymysql.connect("localhost", "root", "1234", "institute", 3307)
        self.c = self.db.cursor()
        self.c.execute("select *from login where username='%s'"%(self.uname))
        self.result=self.c.fetchall()
        self.db.commit()
        if self.result:
            self.sql = "update login set password='%s' where username='%s'" % (self.pword, self.uname)
            if (self.pword == self.cnf):
                self.c.execute(self.sql)
                messagebox.showinfo('FORGOT', 'YOU HAVE SUCESSFULLY UPDATED YOUR PASSWORD')
                self.db.commit()
                forgot_support.destroy_window()
                import itm_log
                itm_log.vp_start_gui()
            else:
                self.db.rollback()
                self.db.close()
                messagebox.showwarning('FORGOT', 'BOTH FIELD OF PASSWORD MUST BE SAME')
        else:
            self.db.rollback()
            self.db.close()
            messagebox.showwarning('FORGOT','YOUR USERNAME DOES NOT EXIST')





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

        top.geometry("600x450+436+126")
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")



        self.Frame1 = Frame(top)
        self.Frame1.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#abd5d8")
        self.Frame1.configure(width=125)

        self.Frame2 = Frame(self.Frame1)
        self.Frame2.place(relx=0.15, rely=0.21, relheight=0.61, relwidth=0.71)
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(background="#9ed863")
        self.Frame2.configure(width=425)

        self.Label1 = Label(self.Frame2)
        self.Label1.place(relx=0.08, rely=0.15, height=21, width=124)
        self.Label1.configure(background="#d870bc")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Enter User Name''')
        self.Label1.configure(width=124)

        self.Entry1 = Entry(self.Frame2)
        self.Entry1.place(relx=0.49, rely=0.15,height=20, relwidth=0.39)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font=font10)
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")

        self.Label2 = Label(self.Frame2)
        self.Label2.place(relx=0.08, rely=0.38, height=21, width=124)
        self.Label2.configure(background="#d870bc")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Enter New Password''')
        self.Label2.configure(width=124)

        self.Entry2 = Entry(self.Frame2)
        self.Entry2.place(relx=0.49, rely=0.38,height=20, relwidth=0.39)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font=font10)
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(insertbackground="black")

        self.Label3 = Label(self.Frame2)
        self.Label3.place(relx=0.08, rely=0.62, height=21, width=124)
        self.Label3.configure(background="#d870bc")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''Confirm Password''')
        self.Label3.configure(width=124)

        self.Entry3 = Entry(self.Frame2)
        self.Entry3.place(relx=0.49, rely=0.62,height=20, relwidth=0.39)
        self.Entry3.configure(background="white")
        self.Entry3.configure(disabledforeground="#a3a3a3")
        self.Entry3.configure(font=font10)
        self.Entry3.configure(foreground="#000000")
        self.Entry3.configure(insertbackground="black")

        self.Button1 = Button(self.Frame2)
        self.Button1.place(relx=0.78, rely=0.76, height=24, width=49)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#53ad1f")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(command=self.log,text='''Submit''')

        self.Button2 = Button(self.Frame2)
        self.Button2.place(relx=0.51, rely=0.76, height=24, width=47)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#ff0d2d")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(command=self.backy,text='''Back''')

        self.Label4 = Label(self.Frame1)
        self.Label4.place(relx=0.18, rely=0.04, height=21, width=394)
        self.Label4.configure(background="#d870bc")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(font=font11)
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(text='''RESET PASSWORD''')
        self.Label4.configure(width=394)






if __name__ == '__main__':
    vp_start_gui()



