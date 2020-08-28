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

import s1_record_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    s1_record_support.set_Tk_var()
    top = New_Toplevel (root)
    s1_record_support.init(root, top)
    root.mainloop()

w = None
def create_New_Toplevel(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    s1_record_support.set_Tk_var()
    top = New_Toplevel (w)
    s1_record_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_New_Toplevel():
    global w
    w.destroy()
    w = None


class New_Toplevel:
    def myquit(self):
        s1_record_support.destroy_window()
        import student
        student.vp_start_gui()
    def add(self):
        self.db = pymysql.connect("127.0.0.1", "root", "1234", "institute", 3307)
        self.c = self.db.cursor()
        try:
            self.roll = self.Entry1.get()
            self.name = self.Entry2.get()
            self.sem = self.Spinbox1.get()
            self.course = self.TCombobox1.get()
            self.fname = self.Entry3.get()
            self.mname = self.Entry4.get()
            self.yoa = self.TCombobox2.get()
            self.email = self.Entry6.get()
            self.addr = self.Entry7.get()
            #print(roll, name, sem, course,fname,mname,yoa,email,addr)
            self.c.execute( "insert into students values("+self.roll+",'" + self.name + "'," + self.sem + ",'" + self.course + "','" + self.fname + "','" + self.mname + "'," + self.yoa + ",'" + self.email + "','" + self.addr + "')")
            #sql = "insert into students(ROLL_NO,NAME,SEMESTER,COURSE,F_NAME,M_NAME,EMAIL,ADDRESS,YEAR_OF_ADM) values(" + roll + ",'" + name + "'," + sem + ",'" + course + "','" + fname + "','" + mname + "','" + email + "','" + addr + "'," + yoa + ")"
           # self.c.execute(sql)
            self.db.commit()
            messagebox.showinfo('STUDENT RECORD', 'SUCCESSFULLY INSERTED')
        except:
            self.db.rollback()
            self.db.close()
            messagebox.showinfo('insert', 'something went wrong')
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

        top.geometry("600x450+470+130")
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")



        self.Frame1 = Frame(top)
        self.Frame1.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#61a889")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")
        self.Frame1.configure(width=125)

        self.Label1 = Label(self.Frame1)
        self.Label1.place(relx=0.25, rely=0.04, height=21, width=304)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#fcf535")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''REGISTRATION  FORM''')

        self.Label2 = Label(self.Frame1)
        self.Label2.place(relx=0.07, rely=0.18, height=21, width=64)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Roll_no.''')

        self.Entry1 = Entry(self.Frame1)
        self.Entry1.place(relx=0.22, rely=0.18,height=20, relwidth=0.24)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font=font10)
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="#c4c4c4")
        self.Entry1.configure(selectforeground="black")
        self.Entry1.configure(width=144)

        self.Label3 = Label(self.Frame1)
        self.Label3.place(relx=0.53, rely=0.18, height=21, width=64)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''Name''')

        self.Entry2 = Entry(self.Frame1)
        self.Entry2.place(relx=0.68, rely=0.18,height=20, relwidth=0.26)
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
        self.Label4.place(relx=0.07, rely=0.33, height=21, width=64)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='''Semester''')

        self.Label5 = Label(self.Frame1)
        self.Label5.place(relx=0.53, rely=0.33, height=21, width=64)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(activeforeground="black")
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(highlightbackground="#d9d9d9")
        self.Label5.configure(highlightcolor="black")
        self.Label5.configure(text='''Course''')

        self.Spinbox1 = Spinbox(self.Frame1, from_=1.0, to=100.0)
        self.Spinbox1.place(relx=0.22, rely=0.33, relheight=0.04, relwidth=0.24)
        self.Spinbox1.configure(activebackground="#f9f9f9")
        self.Spinbox1.configure(background="white")
        self.Spinbox1.configure(buttonbackground="#d9d9d9")
        self.Spinbox1.configure(disabledforeground="#a3a3a3")
        self.Spinbox1.configure(font=font9)
        self.Spinbox1.configure(foreground="black")
        self.Spinbox1.configure(from_="1.0")
        self.Spinbox1.configure(highlightbackground="black")
        self.Spinbox1.configure(highlightcolor="black")
        self.Spinbox1.configure(insertbackground="black")
        self.Spinbox1.configure(selectbackground="#c4c4c4")
        self.Spinbox1.configure(selectforeground="black")
        self.Spinbox1.configure(textvariable=s1_record_support.spinbox)
        self.Spinbox1.configure(to="100.0")
        self.Spinbox1.configure(width=145)

        self.TCombobox1 = ttk.Combobox(self.Frame1)
        self.TCombobox1.place(relx=0.69, rely=0.33, relheight=0.05
                , relwidth=0.26)
        self.value_list = ['BTECH','MBA','MCA','BBA','PGDM',]
        self.TCombobox1.configure(values=self.value_list)
        self.TCombobox1.configure(textvariable=s1_record_support.c2)
        self.TCombobox1.configure(width=153)
        self.TCombobox1.configure(takefocus="")

        self.Label6 = Label(self.Frame1)
        self.Label6.place(relx=0.07, rely=0.46, height=21, width=64)
        self.Label6.configure(activebackground="#f9f9f9")
        self.Label6.configure(activeforeground="black")
        self.Label6.configure(background="#d9d9d9")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(highlightbackground="#d9d9d9")
        self.Label6.configure(highlightcolor="black")
        self.Label6.configure(text='''F_name''')

        self.Entry3 = Entry(self.Frame1)
        self.Entry3.place(relx=0.22, rely=0.47,height=20, relwidth=0.24)
        self.Entry3.configure(background="white")
        self.Entry3.configure(disabledforeground="#a3a3a3")
        self.Entry3.configure(font=font10)
        self.Entry3.configure(foreground="#000000")
        self.Entry3.configure(highlightbackground="#d9d9d9")
        self.Entry3.configure(highlightcolor="black")
        self.Entry3.configure(insertbackground="black")
        self.Entry3.configure(selectbackground="#c4c4c4")
        self.Entry3.configure(selectforeground="black")
        self.Entry3.configure(width=144)

        self.Label7 = Label(self.Frame1)
        self.Label7.place(relx=0.53, rely=0.47, height=21, width=64)
        self.Label7.configure(activebackground="#f9f9f9")
        self.Label7.configure(activeforeground="black")
        self.Label7.configure(background="#d9d9d9")
        self.Label7.configure(disabledforeground="#a3a3a3")
        self.Label7.configure(foreground="#000000")
        self.Label7.configure(highlightbackground="#d9d9d9")
        self.Label7.configure(highlightcolor="black")
        self.Label7.configure(text='''M_name''')

        self.Entry4 = Entry(self.Frame1)
        self.Entry4.place(relx=0.68, rely=0.47,height=20, relwidth=0.26)
        self.Entry4.configure(background="white")
        self.Entry4.configure(disabledforeground="#a3a3a3")
        self.Entry4.configure(font=font10)
        self.Entry4.configure(foreground="#000000")
        self.Entry4.configure(highlightbackground="#d9d9d9")
        self.Entry4.configure(highlightcolor="black")
        self.Entry4.configure(insertbackground="black")
        self.Entry4.configure(selectbackground="#c4c4c4")
        self.Entry4.configure(selectforeground="black")

        self.Label8 = Label(self.Frame1)
        self.Label8.place(relx=0.07, rely=0.6, height=21, width=64)
        self.Label8.configure(activebackground="#f9f9f9")
        self.Label8.configure(activeforeground="black")
        self.Label8.configure(background="#d9d9d9")
        self.Label8.configure(disabledforeground="#a3a3a3")
        self.Label8.configure(foreground="#000000")
        self.Label8.configure(highlightbackground="#d9d9d9")
        self.Label8.configure(highlightcolor="black")
        self.Label8.configure(text='''Year of Adm''')

        self.Label9 = Label(self.Frame1)
        self.Label9.place(relx=0.53, rely=0.6, height=21, width=64)
        self.Label9.configure(activebackground="#f9f9f9")
        self.Label9.configure(activeforeground="black")
        self.Label9.configure(background="#d9d9d9")
        self.Label9.configure(disabledforeground="#a3a3a3")
        self.Label9.configure(foreground="#000000")
        self.Label9.configure(highlightbackground="#d9d9d9")
        self.Label9.configure(highlightcolor="black")
        self.Label9.configure(text='''Email''')

        self.Entry6 = Entry(self.Frame1)
        self.Entry6.place(relx=0.68, rely=0.6,height=20, relwidth=0.26)
        self.Entry6.configure(background="white")
        self.Entry6.configure(disabledforeground="#a3a3a3")
        self.Entry6.configure(font=font10)
        self.Entry6.configure(foreground="#000000")
        self.Entry6.configure(highlightbackground="#d9d9d9")
        self.Entry6.configure(highlightcolor="black")
        self.Entry6.configure(insertbackground="black")
        self.Entry6.configure(selectbackground="#c4c4c4")
        self.Entry6.configure(selectforeground="black")

        self.Label10 = Label(self.Frame1)
        self.Label10.place(relx=0.07, rely=0.73, height=21, width=64)
        self.Label10.configure(activebackground="#f9f9f9")
        self.Label10.configure(activeforeground="black")
        self.Label10.configure(background="#d9d9d9")
        self.Label10.configure(disabledforeground="#a3a3a3")
        self.Label10.configure(foreground="#000000")
        self.Label10.configure(highlightbackground="#d9d9d9")
        self.Label10.configure(highlightcolor="black")
        self.Label10.configure(text='''Address''')

        self.Entry7 = Entry(self.Frame1)
        self.Entry7.place(relx=0.22, rely=0.73,height=20, relwidth=0.24)
        self.Entry7.configure(background="white")
        self.Entry7.configure(disabledforeground="#a3a3a3")
        self.Entry7.configure(font=font10)
        self.Entry7.configure(foreground="#000000")
        self.Entry7.configure(highlightbackground="#d9d9d9")
        self.Entry7.configure(highlightcolor="black")
        self.Entry7.configure(insertbackground="black")
        self.Entry7.configure(selectbackground="#c4c4c4")
        self.Entry7.configure(selectforeground="black")
        self.Entry7.configure(width=144)

        self.Button1 = Button(self.Frame1)
        self.Button1.place(relx=0.75, rely=0.71, height=34, width=87)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#20a811")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(command=self.add,text='''Insert Records''')

        self.Button2 = Button(self.Frame1)
        self.Button2.place(relx=0.75, rely=0.84, height=34, width=87)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d8230f")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(command=self.myquit,text='''Back''')

        self.TCombobox2 = ttk.Combobox(self.Frame1)
        self.TCombobox2.place(relx=0.22, rely=0.6, relheight=0.05, relwidth=0.24)

        self.value_list = [2014,2015,2016,2017,2018,2019,2020,]
        self.TCombobox2.configure(values=self.value_list)
        self.TCombobox2.configure(textvariable=s1_record_support.c1)
        self.TCombobox2.configure(width=143)
        self.TCombobox2.configure(takefocus="")

if __name__ == '__main__':
    vp_start_gui()



