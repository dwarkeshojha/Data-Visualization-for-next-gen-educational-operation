
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

import teacher_details_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    teacher_details_support.set_Tk_var()
    top = New_Toplevel (root)
    teacher_details_support.init(root, top)
    root.mainloop()

w = None
def create_New_Toplevel(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    teacher_details_support.set_Tk_var()
    top = New_Toplevel (w)
    teacher_details_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_New_Toplevel():
    global w
    w.destroy()
    w = None


class New_Toplevel:
    def myquit(self):
        teacher_details_support.destroy_window()
        import panel
        panel.vp_start_gui()
    def add(self):
        self.db = pymysql.connect("127.0.0.1", "root", "1234", "institute", 3307)
        self.c = self.db.cursor()
        try:
            self.ids = self.Entry1.get()
            self.name = self.Entry2.get()
            self.dept = self.TCombobox1.get()
            self.desg = self.TCombobox2.get()
            self.email = self.Entry5.get()
            self.addr = self.Entry6.get()
            self.c.execute("insert into teachers values("+self.ids+",'"+self.name+"','"+self.dept+"','"+self.desg+"','"+self.email+"','"+self.addr+"')")
            self.db.commit()
            messagebox.showinfo('INSERT','SUCCESSFULLY INSERTED')
        except:
            self.db.rollback()
            self.db.close()
            messagebox.showinfo('INSERT','SOMETHING WENT WRONG')
    def go(self):
        teacher_details_support.destroy_window()
        import view_f_details
        view_f_details.vp_start_gui()


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
        font11 = "-family {Segoe UI} -size 10 -weight bold -slant "  \
            "italic -underline 1 -overstrike 0"
        font9 = "-family {Segoe UI} -size 9 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("600x450+493+143")
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")



        self.Frame1 = Frame(top)
        self.Frame1.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#61bcd8")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")
        self.Frame1.configure(width=125)

        self.Label1 = Label(self.Frame1)
        self.Label1.place(relx=0.26, rely=0.05, height=21, width=314)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#fcf535")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font11)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''FACULTY  DETAILS''')

        self.Label2 = Label(self.Frame1)
        self.Label2.place(relx=0.05, rely=0.2, height=21, width=74)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''ID''')

        self.Entry1 = Entry(self.Frame1)
        self.Entry1.place(relx=0.22, rely=0.2,height=20, relwidth=0.27)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font=font10)
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="#c4c4c4")
        self.Entry1.configure(selectforeground="black")

        self.Label3 = Label(self.Frame1)
        self.Label3.place(relx=0.53, rely=0.2, height=21, width=64)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''NAME''')

        self.Entry2 = Entry(self.Frame1)
        self.Entry2.place(relx=0.68, rely=0.2,height=20, relwidth=0.27)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font=font10)
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(highlightbackground="#d9d9d9")
        self.Entry2.configure(highlightcolor="black")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(selectbackground="#c4c4c4")
        self.Entry2.configure(selectforeground="black")

        self.Label4 = Label(self.Frame1)
        self.Label4.place(relx=0.05, rely=0.36, height=21, width=74)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(font=font9)
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='''DEPT.''')

        self.Label5 = Label(self.Frame1)
        self.Label5.place(relx=0.53, rely=0.36, height=21, width=64)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(activeforeground="black")
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(font=font9)
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(highlightbackground="#d9d9d9")
        self.Label5.configure(highlightcolor="black")
        self.Label5.configure(text='''DESG.''')

        self.Label6 = Label(self.Frame1)
        self.Label6.place(relx=0.05, rely=0.51, height=21, width=74)
        self.Label6.configure(activebackground="#f9f9f9")
        self.Label6.configure(activeforeground="black")
        self.Label6.configure(background="#d9d9d9")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(highlightbackground="#d9d9d9")
        self.Label6.configure(highlightcolor="black")
        self.Label6.configure(text='''EMAIL''')

        self.Entry5 = Entry(self.Frame1)
        self.Entry5.place(relx=0.22, rely=0.51,height=20, relwidth=0.27)
        self.Entry5.configure(background="white")
        self.Entry5.configure(disabledforeground="#a3a3a3")
        self.Entry5.configure(font=font10)
        self.Entry5.configure(foreground="#000000")
        self.Entry5.configure(highlightbackground="#d9d9d9")
        self.Entry5.configure(highlightcolor="black")
        self.Entry5.configure(insertbackground="black")
        self.Entry5.configure(selectbackground="#c4c4c4")
        self.Entry5.configure(selectforeground="black")

        self.Label7 = Label(self.Frame1)
        self.Label7.place(relx=0.53, rely=0.51, height=21, width=64)
        self.Label7.configure(activebackground="#f9f9f9")
        self.Label7.configure(activeforeground="black")
        self.Label7.configure(background="#d9d9d9")
        self.Label7.configure(disabledforeground="#a3a3a3")
        self.Label7.configure(foreground="#000000")
        self.Label7.configure(highlightbackground="#d9d9d9")
        self.Label7.configure(highlightcolor="black")
        self.Label7.configure(text='''ADDRESS''')

        self.Entry6 = Entry(self.Frame1)
        self.Entry6.place(relx=0.68, rely=0.51,height=20, relwidth=0.27)
        self.Entry6.configure(background="white")
        self.Entry6.configure(disabledforeground="#a3a3a3")
        self.Entry6.configure(font=font10)
        self.Entry6.configure(foreground="#000000")
        self.Entry6.configure(highlightbackground="#d9d9d9")
        self.Entry6.configure(highlightcolor="black")
        self.Entry6.configure(insertbackground="black")
        self.Entry6.configure(selectbackground="#c4c4c4")
        self.Entry6.configure(selectforeground="black")

        self.Button1 = Button(self.Frame1)
        self.Button1.place(relx=0.17, rely=0.67, height=34, width=97)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#19a819")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(command=self.add,text='''INSER RECORDS''')

        self.Button2 = Button(self.Frame1)
        self.Button2.place(relx=0.47, rely=0.67, height=34, width=87)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#e5291b")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(command=self.myquit,text='''BACK''')

        self.TCombobox1 = ttk.Combobox(self.Frame1)
        self.TCombobox1.place(relx=0.22, rely=0.36, relheight=0.05
                , relwidth=0.27)
        self.value_list = ['CSE','IT','ME','CE','EE','ECE','EEE','MCA','MBA','BBA',]
        self.TCombobox1.configure(values=self.value_list)
        self.TCombobox1.configure(textvariable=teacher_details_support.c1)
        self.TCombobox1.configure(takefocus="")

        self.TCombobox2 = ttk.Combobox(self.Frame1)
        self.TCombobox2.place(relx=0.68, rely=0.36, relheight=0.05
                , relwidth=0.27)
        self.value_list = ['HOD','PROFESSOR','ASST. PROFESSOR','LAB ASSISTANT',]
        self.TCombobox2.configure(values=self.value_list)
        self.TCombobox2.configure(textvariable=teacher_details_support.c2)
        self.TCombobox2.configure(takefocus="")

        self.Button3 = Button(self.Frame1)
        self.Button3.place(relx=0.72, rely=0.67, height=34, width=97)
        self.Button3.configure(activebackground="#d9d9d9")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d827c0")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(command=self.go,text='''VIEW FACULTIES''')

if __name__ == '__main__':
    vp_start_gui()



