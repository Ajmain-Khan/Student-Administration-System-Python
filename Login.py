from tkinter import Tk, Label, Entry, Button, W, Frame, messagebox as msgbox
import time
from StudentLedger import *

class Login(Frame):
    #Hard code the username and password for the purposes of this project
    default_username = "admin"
    default_password = "password"
    def __init__(self, root):  #Constructor(Java), self == this(Java)
        super().__init__()
        self.root = root
        self.root.title('Admin Access Portal')
        self.root.call('wm', 'iconphoto', root._w, PhotoImage(file='otu.png'))
        self.root.configure(bg='lightblue')
        self.root.geometry('285x120')
        center(self.root, -80, 70)
        

        #Username/Password Labels and Grid Alignment
        self.pad1 = Label(self, width=8, bg='lightblue')
        self.pad2 = Label(self, width=17, bg='lightblue')
        self.username = Label(self, pady=4, text="Username")
        self.password = Label(self, pady=2, text="Password")
        #Username/Password Entry Boxes
        self.userEntry = Entry(self)
        self.passEntry = Entry(self, show="*")
        #Aligning Each Element To Grid By Row and Column
        self.pad1.grid(row=0)
        self.pad2.grid(row=0, column=1)
        self.username.grid(row=1, sticky=W)
        self.password.grid(row=2, sticky=W)
        self.userEntry.grid(row=1, column=1)
        self.passEntry.grid(row=2, column=1)
        #Login Button
        self.login = Button(self, activebackground='lightskyblue', text="Login", pady=2, width=6, command=self.login_event)
        self.login.grid(columnspan=2)  #Merge columns & place element in center
        self.root.bind('<Return>', lambda event=None: self.login.invoke())  #Bind login button to enter key
        self.pack()

    def login_event(self):
        username = self.userEntry.get()
        password = self.passEntry.get()

        if username == "admin" and password == "password":
            if msgbox.askokcancel("Login Successful", "Logged in as admin.\n\nNew Session Created. Continue?"):
                root.destroy()  #Destroy popup and current window
                root2 = Tk()  #Create a new window
                center(root2, 0, 0)
                run = Ledger(root2)
                root2.mainloop()
            else:
                root.destroy()

        elif username == '' or password == '' or username == '' and password == '':
            msgbox.showwarning("Invalid Input", "Please Complete All Fields.")
        else:
            msgbox.showerror("Error", "Incorrect Username or Password.")

        """rows = 0
        while rows<10:
            self.root.rowconfigure(rows, weight=1)
            self.root.columnconfigure(rows, weight=1)
            rows+=1

        f = LabelFrame(self.root, text="Login")
        f.grid(row=1, column=1, columnspan=10, rowspan=10)

        Label(f, text=' Username ').grid(row=2, column=1, sticky=W)
        self.username = Entry(f)
        self.username.grid(row=2, column=2)

        Label(f, text=' Password ').grid(row=5, column=1, sticky=W)
        self.password = Entry(f, show='*')
        self.password.grid(row=5, column=2)

        # Button
        tk.Button(f, text = 'LOGIN',command = self.login_user).grid(row=7,column=2)"""


root = Tk()  #As per convention, the base window is named root
run = Login(root)
root.mainloop()
