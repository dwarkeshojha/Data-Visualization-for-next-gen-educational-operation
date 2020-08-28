
import sys
import pymysql
from tkinter import messagebox
import matplotlib.pyplot as plt

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

import marks_detail_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = New_Toplevel (root)
    marks_detail_support.init(root, top)
    root.mainloop()

w = None
def create_New_Toplevel(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = New_Toplevel (w)
    marks_detail_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_New_Toplevel():
    global w
    w.destroy()
    w = None


class New_Toplevel:
    def dely(self):
        try:
            self.roll = self.Entry9.get()
            self.db = pymysql.connect("127.0.0.1", "root", "1234", "institute", 3307)
            self.c = self.db.cursor()
            self.sql = "delete from marks where ROLL_NO= %d" % int(self.roll)
            if (self.sql):
                self.c.execute(self.sql)
                messagebox.showinfo('RESULT', 'YOU HAVE SUCCESSFULLY DELETED..')
                self.db.commit()
            else:
                messagebox.showwarning('RESULT', 'THIS ROLL IS NOT EXIST')
                self.db.rollback()
                self.db.close()


            '''self.c.execute(self.sql)
            self.db.commit()
            messagebox.showinfo('RESULT', 'YOU HAVE SUCCESSFULLY DELETED..')'''
        except:
            self.db.rollback()
            self.db.close()
            messagebox.showwarning('RESULT','THIS ROLL IS NOT EXIST')
    def histo(self):
        t=[]
        self.roll = self.Entry9.get()
        self.db = pymysql.connect("127.0.0.1", "root", "1234", "institute", 3307)
        self.c = self.db.cursor()
        self.s="select sem1,sem2,sem3,sem4,sem5,sem6,sem7,sem8 from marks where ROLL_NO= %d"%int((self.roll))
        self.c.execute(self.s)
        self.result=self.c.fetchall()
        i=0
        for row in self.result:
            for i in range(0,8):
                t.append(row[i])
                print(row[i])

        plt.plot(t)
        plt.xlabel("# SEMESTER")
        plt.ylabel("#MARKS")
        plt.show()



    def add(self):
        self.db = pymysql.connect("127.0.0.1", "root", "1234", "institute", 3307)
        self.c = self.db.cursor()

        self.roll=self.Entry9.get()
        self.name=self.Entry10.get()
        self.course=self.Entry11.get()
        self.sem1=self.Entry1.get()
        self.sem2=self.Entry2.get()
        self.sem3=self.Entry3.get()
        self.sem4=self.Entry4.get()
        self.sem5=self.Entry5.get()
        self.sem6=self.Entry6.get()
        self.sem7=self.Entry7.get()
        self.sem8=self.Entry8.get()
        self.totals = int(self.sem1) + int(self.sem2) + int(self.sem3) + int(self.sem4) + int(self.sem5) + int(self.sem6) + int(self.sem7) + int(self.sem8)
        self.sql="insert into marks(ROLL_NO,name,course,sem1,sem2,sem3,sem4,sem5,sem6,sem7,sem8,total)values(%d,'%s','%s',%d,%d,%d,%d,%d,%d,%d,%d,%d)"%(int(self.roll),self.name,self.course,int(self.sem1),int(self.sem2),int(self.sem3),int(self.sem4),int(self.sem5),int(self.sem6),int(self.sem7),int(self.sem8),int(self.totals))

        #self.sql="insert into marks"
        self.c.execute(self.sql)
        self.db.commit()
        messagebox.showinfo('RESULT','SUCESSFULLY INSERTED')

    def myquit(self):
        marks_detail_support.destroy_window()
        import student
        student.vp_start_gui()
    def log(self):
        self.db = pymysql.connect("127.0.0.1", "root", "1234", "institute", 3307)
        self.c = self.db.cursor()
        # self.roll=self.Entry1.get()
        try:
            self.c.execute("select * from students where ROLL_NO=%d" % (int(self.Entry9.get())))
            self.result = self.c.fetchall()
            self.db.commit()
            self.Entry10.delete(0,END)
            self.Entry11.delete(0, END)
            if self.result:
                messagebox.showinfo('RESULT', 'YOUR ROLL IS BEING FOUND')
                self.Frame1.place(relx=0.0, rely=0.24, relheight=0.76, relwidth=1.0)
                for row in self.result:
                    self.name=row[1]
                    self.course=row[3]
                    print(self.name)
                    print(self.course)
                #self.Entry10.set(self.name)
                #self.Entry11.set(self.course)
                self.Entry10.insert(END,self.name)
                self.Entry11.insert(END, self.course)

                #self.db.commit()
            else:
                messagebox.showwarning('RESULT', 'ROLL NOT FOUND')

        except:
            self.db.rollback()
            self.db.close()
            print("something went wrong")
            messagebox.showwarning('RESULT', 'SOMETHING WENT WRONG.....')
    def goto(self):
        marks_detail_support.destroy_window()
        import mean
        mean.vp_start_gui()

    def backy(self):
        marks_detail_support.destroy_window()
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

        top.geometry("611x596+361+41")
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")



        self.Frame1 = Frame(top)
        #self.Frame1.place(relx=0.0, rely=0.24, relheight=0.76, relwidth=1.0)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#a6d87b")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")
        self.Frame1.configure(width=611)

        self.Label1 = Label(self.Frame1)
        self.Label1.place(relx=0.25, rely=0.02, height=31, width=304)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#ffff1c")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font11)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''STUDENT MARKS DETAILS''')

        self.Label2 = Label(self.Frame1)
        self.Label2.place(relx=0.06, rely=0.34, height=21, width=74)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''SEMESTER 1''')

        self.Entry1 = Entry(self.Frame1)
        self.Entry1.place(relx=0.21, rely=0.34,height=20, relwidth=0.27)
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
        self.Label3.place(relx=0.54, rely=0.34, height=21, width=74)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''SEMESTER 2''')

        self.Entry2 = Entry(self.Frame1)
        self.Entry2.place(relx=0.69, rely=0.34,height=20, relwidth=0.27)
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
        self.Label4.place(relx=0.06, rely=0.48, height=21, width=74)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='''SEMESTER 3''')

        self.Entry3 = Entry(self.Frame1)
        self.Entry3.place(relx=0.21, rely=0.48,height=20, relwidth=0.27)
        self.Entry3.configure(background="white")
        self.Entry3.configure(disabledforeground="#a3a3a3")
        self.Entry3.configure(font=font10)
        self.Entry3.configure(foreground="#000000")
        self.Entry3.configure(highlightbackground="#d9d9d9")
        self.Entry3.configure(highlightcolor="black")
        self.Entry3.configure(insertbackground="black")
        self.Entry3.configure(selectbackground="#c4c4c4")
        self.Entry3.configure(selectforeground="black")

        self.Label5 = Label(self.Frame1)
        self.Label5.place(relx=0.53, rely=0.48, height=21, width=74)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(activeforeground="black")
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(highlightbackground="#d9d9d9")
        self.Label5.configure(highlightcolor="black")
        self.Label5.configure(text='''SEMESTER 4''')

        self.Entry4 = Entry(self.Frame1)
        self.Entry4.place(relx=0.69, rely=0.48,height=20, relwidth=0.27)
        self.Entry4.configure(background="white")
        self.Entry4.configure(disabledforeground="#a3a3a3")
        self.Entry4.configure(font=font10)
        self.Entry4.configure(foreground="#000000")
        self.Entry4.configure(highlightbackground="#d9d9d9")
        self.Entry4.configure(highlightcolor="black")
        self.Entry4.configure(insertbackground="black")
        self.Entry4.configure(selectbackground="#c4c4c4")
        self.Entry4.configure(selectforeground="black")

        self.Label6 = Label(self.Frame1)
        self.Label6.place(relx=0.05, rely=0.61, height=21, width=74)
        self.Label6.configure(activebackground="#f9f9f9")
        self.Label6.configure(activeforeground="black")
        self.Label6.configure(background="#d9d9d9")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(highlightbackground="#d9d9d9")
        self.Label6.configure(highlightcolor="black")
        self.Label6.configure(text='''SEMESTER 5''')

        self.Entry5 = Entry(self.Frame1)
        self.Entry5.place(relx=0.21, rely=0.62,height=20, relwidth=0.27)
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
        self.Label7.place(relx=0.53, rely=0.62, height=21, width=74)
        self.Label7.configure(activebackground="#f9f9f9")
        self.Label7.configure(activeforeground="black")
        self.Label7.configure(background="#d9d9d9")
        self.Label7.configure(disabledforeground="#a3a3a3")
        self.Label7.configure(foreground="#000000")
        self.Label7.configure(highlightbackground="#d9d9d9")
        self.Label7.configure(highlightcolor="black")
        self.Label7.configure(text='''SEMESTER 6''')

        self.Entry6 = Entry(self.Frame1)
        self.Entry6.place(relx=0.68, rely=0.62,height=20, relwidth=0.27)
        self.Entry6.configure(background="white")
        self.Entry6.configure(disabledforeground="#a3a3a3")
        self.Entry6.configure(font=font10)
        self.Entry6.configure(foreground="#000000")
        self.Entry6.configure(highlightbackground="#d9d9d9")
        self.Entry6.configure(highlightcolor="black")
        self.Entry6.configure(insertbackground="black")
        self.Entry6.configure(selectbackground="#c4c4c4")
        self.Entry6.configure(selectforeground="black")

        self.Label8 = Label(self.Frame1)
        self.Label8.place(relx=0.05, rely=0.75, height=21, width=74)
        self.Label8.configure(activebackground="#f9f9f9")
        self.Label8.configure(activeforeground="black")
        self.Label8.configure(background="#d9d9d9")
        self.Label8.configure(disabledforeground="#a3a3a3")
        self.Label8.configure(foreground="#000000")
        self.Label8.configure(highlightbackground="#d9d9d9")
        self.Label8.configure(highlightcolor="black")
        self.Label8.configure(text='''SEMESTER 7''')

        self.Entry7 = Entry(self.Frame1)
        self.Entry7.place(relx=0.21, rely=0.75,height=20, relwidth=0.27)
        self.Entry7.configure(background="white")
        self.Entry7.configure(disabledforeground="#a3a3a3")
        self.Entry7.configure(font=font10)
        self.Entry7.configure(foreground="#000000")
        self.Entry7.configure(highlightbackground="#d9d9d9")
        self.Entry7.configure(highlightcolor="black")
        self.Entry7.configure(insertbackground="black")
        self.Entry7.configure(selectbackground="#c4c4c4")
        self.Entry7.configure(selectforeground="black")

        self.Label9 = Label(self.Frame1)
        self.Label9.place(relx=0.53, rely=0.75, height=21, width=74)
        self.Label9.configure(activebackground="#f9f9f9")
        self.Label9.configure(activeforeground="black")
        self.Label9.configure(background="#d9d9d9")
        self.Label9.configure(disabledforeground="#a3a3a3")
        self.Label9.configure(foreground="#000000")
        self.Label9.configure(highlightbackground="#d9d9d9")
        self.Label9.configure(highlightcolor="black")
        self.Label9.configure(text='''SEMESTER 8''')

        self.Entry8 = Entry(self.Frame1)
        self.Entry8.place(relx=0.68, rely=0.75,height=20, relwidth=0.27)
        self.Entry8.configure(background="white")
        self.Entry8.configure(disabledforeground="#a3a3a3")
        self.Entry8.configure(font=font10)
        self.Entry8.configure(foreground="#000000")
        self.Entry8.configure(highlightbackground="#d9d9d9")
        self.Entry8.configure(highlightcolor="black")
        self.Entry8.configure(insertbackground="black")
        self.Entry8.configure(selectbackground="#c4c4c4")
        self.Entry8.configure(selectforeground="black")

        self.Button1 = Button(self.Frame1)
        self.Button1.place(relx=0.11, rely=0.88, height=34, width=67)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#20d82d")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(command=self.add,text='''INSERT''')

        self.Button2 = Button(self.Frame1)
        self.Button2.place(relx=0.28, rely=0.88, height=34, width=67)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#5f7bd8")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(command=self.dely,text='''DELETE''')

        self.Button3 = Button(self.Frame1)
        self.Button3.place(relx=0.45, rely=0.88, height=34, width=73)
        self.Button3.configure(activebackground="#d9d9d9")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d84c88")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(command=self.histo,text='''VIEW RESULT''')

        self.Button4 = Button(self.Frame1)
        self.Button4.place(relx=0.79, rely=0.88, height=34, width=67)
        self.Button4.configure(activebackground="#d9d9d9")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#d80909")
        self.Button4.configure(disabledforeground="#a3a3a3")
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(command=self.myquit,text='''BACK''')

        self.Button6 = Button(self.Frame1)
        self.Button6.place(relx=0.62, rely=0.88, height=34, width=67)
        self.Button6.configure(activebackground="#d9d9d9")
        self.Button6.configure(activeforeground="#000000")
        self.Button6.configure(background="#d84c6c")
        self.Button6.configure(disabledforeground="#a3a3a3")
        self.Button6.configure(foreground="#000000")
        self.Button6.configure(highlightbackground="#d9d9d9")
        self.Button6.configure(highlightcolor="black")
        self.Button6.configure(pady="0")
        self.Button6.configure(command=self.goto, text='''ANALYSE''')

        self.Label11 = Label(self.Frame1)
        self.Label11.place(relx=0.07, rely=0.16, height=21, width=74)
        self.Label11.configure(background="#d9d9d9")
        self.Label11.configure(disabledforeground="#a3a3a3")
        self.Label11.configure(foreground="#000000")
        self.Label11.configure(text='''NAME''')
        self.Label11.configure(width=74)

        self.Entry10 = Entry(self.Frame1)
        self.Entry10.place(relx=0.22, rely=0.16,height=20, relwidth=0.27)
        self.Entry10.configure(background="white")
        self.Entry10.configure(disabledforeground="#a3a3a3")
        self.Entry10.configure(font=font10)
        self.Entry10.configure(foreground="#000000")
        self.Entry10.configure(insertbackground="black")

        self.Label12 = Label(self.Frame1)
        self.Label12.place(relx=0.54, rely=0.16, height=21, width=64)
        self.Label12.configure(background="#d9d9d9")
        self.Label12.configure(disabledforeground="#a3a3a3")
        self.Label12.configure(foreground="#000000")
        self.Label12.configure(text='''COURSE''')
        self.Label12.configure(width=64)

        self.Entry11 = Entry(self.Frame1)
        self.Entry11.place(relx=0.68, rely=0.16,height=20, relwidth=0.27)
        self.Entry11.configure(background="white")
        self.Entry11.configure(disabledforeground="#a3a3a3")
        self.Entry11.configure(font=font10)
        self.Entry11.configure(foreground="#000000")
        self.Entry11.configure(insertbackground="black")

        self.Frame2 = Frame(top)
        self.Frame2.place(relx=-0.01, rely=-0.01, relheight=0.24, relwidth=1.01)
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(background="#50d8b4")
        self.Frame2.configure(highlightbackground="#d9d9d9")
        self.Frame2.configure(highlightcolor="black")
        self.Frame2.configure(width=615)

        self.Entry9 = Entry(self.Frame2)
        self.Entry9.place(relx=0.47, rely=0.34,height=20, relwidth=0.27)
        self.Entry9.configure(background="white")
        self.Entry9.configure(disabledforeground="#a3a3a3")
        self.Entry9.configure(font=font10)
        self.Entry9.configure(foreground="#000000")
        self.Entry9.configure(highlightbackground="#d9d9d9")
        self.Entry9.configure(highlightcolor="black")
        self.Entry9.configure(insertbackground="black")
        self.Entry9.configure(selectbackground="#c4c4c4")
        self.Entry9.configure(selectforeground="black")

        self.Label10 = Label(self.Frame2)
        self.Label10.place(relx=0.23, rely=0.34, height=21, width=122)
        self.Label10.configure(activebackground="#f9f9f9")
        self.Label10.configure(activeforeground="black")
        self.Label10.configure(background="#d8b5c6")
        self.Label10.configure(disabledforeground="#a3a3a3")
        self.Label10.configure(foreground="#000000")
        self.Label10.configure(highlightbackground="#d9d9d9")
        self.Label10.configure(highlightcolor="black")
        self.Label10.configure(text='''Enter Student Roll No.''')

        self.Button5 = Button(self.Frame2)
        self.Button5.place(relx=0.67, rely=0.62, height=24, width=47)
        self.Button5.configure(activebackground="#d9d9d9")
        self.Button5.configure(activeforeground="#000000")
        self.Button5.configure(background="#d84c6c")
        self.Button5.configure(disabledforeground="#a3a3a3")
        self.Button5.configure(foreground="#000000")
        self.Button5.configure(highlightbackground="#d9d9d9")
        self.Button5.configure(highlightcolor="black")
        self.Button5.configure(pady="0")
        self.Button5.configure(command=self.log,text='''Submit''')

        self.Button7 = Button(self.Frame2)
        self.Button7.place(relx=0.47, rely=0.62, height=24, width=47)
        self.Button7.configure(activebackground="#d9d9d9")
        self.Button7.configure(activeforeground="#000000")
        self.Button7.configure(background="red")
        self.Button7.configure(disabledforeground="#a3a3a3")
        self.Button7.configure(foreground="#000000")
        self.Button7.configure(highlightbackground="#d9d9d9")
        self.Button7.configure(highlightcolor="black")
        self.Button7.configure(pady="0")
        self.Button7.configure(command=self.backy, text='''Back''')

if __name__ == '__main__':
    vp_start_gui()



