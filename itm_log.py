
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

import itm_log_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = New_Toplevel (root)
    itm_log_support.init(root, top)
    root.mainloop()

w = None
def create_New_Toplevel(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = New_Toplevel (w)
    itm_log_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_New_Toplevel():
    global w
    w.destroy()
    w = None


class New_Toplevel:
    def backy(self):
        itm_log_support.destroy_window()
        import ITM_PROJECT
        ITM_PROJECT.vp_start_gui()

    def forgot(self):
        itm_log_support.destroy_window()
        import forgot
        forgot.vp_start_gui()

    def log(self):
        self.uname = self.Entry1.get()
        self.pword = self.Entry2.get()
        self.c.execute("select * from login where username='%s' and password='%s'" % (self.uname, self.pword))
        self.result = self.c.fetchone()
        self.db.commit()

        if self.result:
            messagebox.showinfo('LOGIN', 'LOGIN SUCCESSFULLY')
            itm_log_support.destroy_window()
            import panel
            panel.vp_start_gui()
            self.db.commit()
        else:
            messagebox.showwarning('LOGIN', 'INVALID USER')
            #self.valid.set("Invalid User")

        '''except:
            self.db.rollback()
            self.db.close()
            print("something went wrong")
            messagebox.showwarning('LOGIN', 'SOMETHING WENT WRONG')'''
    def up(self):
        itm_log_support.destroy_window()
        import signup
        signup.vp_start_gui()
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
        font13 = "-family {Segoe UI} -size 14 -weight bold -slant "  \
            "italic -underline 1 -overstrike 0"
        font16 = "-family {Segoe UI} -size 10 -weight normal -slant "  \
            "italic -underline 0 -overstrike 0"

        top.geometry("603x450+435+141")
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.db = pymysql.connect("127.0.0.1", "root", "1234", "institute", 3307)
        self.c = self.db.cursor()
        #self.valid=StringVar

        self.Frame1 = Frame(top)
        self.Frame1.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#d5d88c")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")
        self.Frame1.configure(width=605)

        self.Frame2 = Frame(self.Frame1)
        self.Frame2.place(relx=0.11, rely=0.3, relheight=0.57, relwidth=0.79)
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(background="#b18db2")
        self.Frame2.configure(highlightbackground="#d8cfff")
        self.Frame2.configure(highlightcolor="black")
        self.Frame2.configure(width=475)

        self.Label1 = Label(self.Frame2)
        self.Label1.place(relx=0.13, rely=0.11, height=21, width=84)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font16)
        self.Label1.configure(foreground="#06040a")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''User Name''')

        self.Label2 = Label(self.Frame2)
        self.Label2.place(relx=0.13, rely=0.31, height=21, width=84)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font16)
        self.Label2.configure(foreground="#020503")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Password''')

        self.Entry1 = Entry(self.Frame2)
        self.Entry1.place(relx=0.42, rely=0.12,height=20, relwidth=0.35)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font=font10)
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="#c4c4c4")
        self.Entry1.configure(selectforeground="black")

        self.Entry2 = Entry(self.Frame2)
        self.Entry2.place(relx=0.42, rely=0.31,height=20, relwidth=0.35)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font=font10)
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(highlightbackground="#d9d9d9")
        self.Entry2.configure(highlightcolor="black")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(selectbackground="#c4c4c4")
        self.Entry2.configure(selectforeground="black")
        self.Entry2.configure(show='*')

        self.Button1 = Button(self.Frame2)
        self.Button1.place(relx=0.67, rely=0.47, height=24, width=46)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#19a819")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(command=self.log,text='''LOGIN''')

        self.Button2 = Button(self.Frame2)
        self.Button2.place(relx=0.44, rely=0.47, height=24, width=47)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#cc260c")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(command=self.backy,text='''BACK''')

        self.Label4 = Label(self.Frame2)
        self.Label4.place(relx=0.49, rely=0.62, height=31, width=114)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(background="#b18db2")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        #self.Label4.configure(textvariable=self.valid)

        self.Button3 = Button(self.Frame2)
        self.Button3.place(relx=0.68, rely=0.78, height=24, width=105)
        self.Button3.configure(activebackground="#d9d9d9")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#8fd88a")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(command=self.up,text='''new user? sign up''')

        self.Button4 = Button(self.Frame2)
        self.Button4.place(relx=0.44, rely=0.78, height=24, width=98)
        self.Button4.configure(activebackground="#d9d9d9")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#d85b74")
        self.Button4.configure(disabledforeground="#a3a3a3")
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(command=self.forgot,text='''Forget password''')

        self.Label5 = Label(self.Frame1)
        self.Label5.place(relx=0.23, rely=0.03, height=71, width=294)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(activeforeground="black")
        self.Label5.configure(background="#d5d88c")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(font=font13)
        self.Label5.configure(foreground="#1495e0")
        self.Label5.configure(highlightbackground="#d9d9d9")
        self.Label5.configure(highlightcolor="black")
        self.Label5.configure(text='''WELCOME! 
LOGIN TO YOUR ACCOUNT''')

if __name__ == '__main__':
    vp_start_gui()



