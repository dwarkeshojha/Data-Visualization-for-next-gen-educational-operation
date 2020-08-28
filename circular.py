
import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from  tkinter import messagebox
from tkinter.filedialog import askopenfilename

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

import circular_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = New_Toplevel (root)
    circular_support.init(root, top)
    root.mainloop()

w = None
def create_New_Toplevel(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = New_Toplevel (w)
    circular_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_New_Toplevel():
    global w
    w.destroy()
    w = None


class New_Toplevel:
    def backy(self):
        circular_support.destroy_window()
        import panel
        panel.vp_start_gui()
    def mail(self):
        if(self.flag > 0):
            fromaddr = "aamir.abdine@gmail.com"
            toaddr = self.Entry1.get()
            msg = MIMEMultipart()
            msg['from'] = fromaddr
            msg['to'] = toaddr
            msg['subject'] = self.Entry2.get()
            body = self.Text1.get('1.0', END)
            msg.attach(MIMEText(body, 'plain'))
            f = self.filename
            attachment = open(f, "rb")
            self.part = MIMEBase('application', 'octet-stream')
            self.part.set_payload((attachment).read())
            encoders.encode_base64(self.part)
            self.part.add_header('content-Disposition', "attachment;filename=%s" % f)
            msg.attach(self.part)
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(fromaddr, "abdineasif")
            text = msg.as_string()
            server.sendmail(fromaddr, toaddr, text)
            server.quit()
            messagebox.showinfo('MAIL', 'YOU HAVE SUCESSFULLY SEND')
            self.Entry1.delete(0, END)
            self.Entry2.delete(0, END)
            self.Text1.delete('1.0', END)
        else:
            fromaddr = "aamir.abdine@gmail.com"
            toaddr = self.Entry1.get()
            msg = MIMEMultipart()
            msg['from'] = fromaddr
            msg['to'] = toaddr
            msg['subject'] = self.Entry2.get()
            body = self.Text1.get('1.0', END)
            msg.attach(MIMEText(body, 'plain'))
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(fromaddr, "abdineasif")
            text = msg.as_string()
            server.sendmail(fromaddr, toaddr, text)
            messagebox.showinfo('MAIL', 'YOU HAVE SUCESSFULLY SEND')
            server.quit()
    def choose(self):
        self.flag=1
        self.filename = askopenfilename()  # show an "Open" dialog box and return the path to the selected file
        print(self.filename)


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
        font11 = "-family {Segoe UI} -size 12 -weight bold -slant "  \
            "italic -underline 1 -overstrike 0"

        top.geometry("600x450+452+127")
        top.title("CIRCULARS")
        top.configure(background="#d9d9d9")
        self.flag=0



        self.Frame1 = Frame(top)
        self.Frame1.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#99d8b5")
        self.Frame1.configure(width=125)

        self.Entry1 = Entry(self.Frame1)
        self.Entry1.place(relx=0.42, rely=0.19,height=20, relwidth=0.39)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font=font10)
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(width=234)

        self.Label1 = Label(self.Frame1)
        self.Label1.place(relx=0.25, rely=0.03, height=21, width=294)
        self.Label1.configure(background="#84d866")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font11)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''CIRCULAR''')
        self.Label1.configure(width=294)

        self.Label2 = Label(self.Frame1)
        self.Label2.place(relx=0.22, rely=0.19, height=21, width=84)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''TO''')
        self.Label2.configure(width=84)

        self.Label3 = Label(self.Frame1)
        self.Label3.place(relx=0.22, rely=0.34, height=21, width=84)
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''SUBJECT''')
        self.Label3.configure(width=84)

        self.Entry2 = Entry(self.Frame1)
        self.Entry2.place(relx=0.42, rely=0.34,height=20, relwidth=0.39)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font=font10)
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(width=234)

        self.Label4 = Label(self.Frame1)
        self.Label4.place(relx=0.29, rely=0.47, height=21, width=274)
        self.Label4.configure(background="#d2d830")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(text='''WRITE YOUR MESSAGE BELOW''')
        self.Label4.configure(width=274)

        self.Text1 = Text(self.Frame1)
        self.Text1.place(relx=0.22, rely=0.57, relheight=0.34, relwidth=0.59)
        self.Text1.configure(background="white")
        self.Text1.configure(font="font9")
        self.Text1.configure(foreground="black")
        self.Text1.configure(highlightbackground="#d9d9d9")
        self.Text1.configure(highlightcolor="black")
        self.Text1.configure(insertbackground="black")
        self.Text1.configure(selectbackground="#c4c4c4")
        self.Text1.configure(selectforeground="black")
        self.Text1.configure(width=344)
        self.Text1.configure(wrap=WORD)

        self.Button1 = Button(self.Frame1)
        self.Button1.place(relx=0.84, rely=0.75, height=24, width=87)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="green")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(command=self.mail,text='''SEND''')
        self.Button1.configure(width=57)

        self.Button2 = Button(self.Frame1)
        self.Button2.place(relx=0.84, rely=0.85, height=24, width=87)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="light green")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(command=self.choose, text='''choose file''')
        self.Button2.configure(width=57)

        self.Button3 = Button(self.Frame1)
        self.Button3.place(relx=0.44, rely=0.93, height=24, width=87)
        self.Button3.configure(activebackground="#d9d9d9")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="RED")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(command=self.backy, text='''BACK''')
        self.Button3.configure(width=57)






if __name__ == '__main__':
    vp_start_gui()



