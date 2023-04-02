from tkinter import *
from tkinter import messagebox as msgbox
from tkinter import font
import tkinter.ttk as ttk
#import tkinter.ttk as ttk
import sqlite3

class Ledger(Tk):
    student_db = 'ledger.db'
    def __init__(self):
        Tk.__init__(self)
        self.title('Ontario Tech - Student Database')
        self.call('wm', 'iconphoto', self._w, PhotoImage(file='OTU.png'))
        #self.geometry('+600+200')#625x525
        center(self, 0, 0)
        #s=ttk.Style()
        #s.theme_use('clam')

        '''OTU Logo'''
        self.img = PhotoImage(file='OnTech.png')
        self.label = Label(image=self.img)
        self.label.pack(side=TOP, expand=1, fill=BOTH, padx=70)

        '''Menu Buttons'''
        frame = LabelFrame(self, bg='#0077CA', pady=self.winfo_reqheight()-150, padx=15)
        frame.pack(side=LEFT, fill=BOTH)
        btnfont = font.Font(family='Arial', size=14, weight='bold')  # define font

        Add = Button(frame, text='Add New Student', command=self.add, pady=5, fg='#003C71', bg='sienna1',
                            activebackground='#E75D2A', overrelief=GROOVE, font=btnfont)
        Add.pack(pady=10)

        Edit = Button(frame, text='Edit Student', command=self.edit, pady=5, padx=24, fg='#003C71', bg='sienna1',
                            activebackground='#E75D2A', overrelief=GROOVE, font=btnfont)
        Edit.pack(pady=10)

        Remove = Button(frame, text='Remove Student', pady=5, padx=4, fg='#003C71', bg='sienna1',
                            activebackground='#E75D2A', overrelief=GROOVE, font=btnfont)
        Remove.pack(pady=10)

        Search = Button(frame, text='Search Students', pady=5, padx=2, fg='#003C71', bg='sienna1',
                            activebackground='#E75D2A', overrelief=GROOVE, font=btnfont)
        Search.pack(pady=10)

        Exit = Button(frame, text='Exit', command=self.exit, pady=5, padx=30,
                            fg='#003C71', bg='sienna1', activebackground='#E75D2A',
                            cursor='pirate', overrelief=GROOVE, font=btnfont)
        Exit.pack(pady=15)
        
        '''Menu Bars'''
        menu = Menu()
        self.config(menu=menu)

        file = Menu(menu, tearoff=False)  #File Menu Bar
        menu.add_cascade(label='File', menu=file)
        file.add_command(label='Main Menu', command=self.nothing)
        file.add_separator()
        file.add_command(label='Exit', command=self.nothing)
        
        edit = Menu(menu, tearoff=False)  #Edit Menu Bar
        menu.add_cascade(label='Edit', menu=edit)
        edit.add_command(label='Add Student', command=self.add)
        edit.add_command(label='Edit Existing Student', command=self.edit)
        edit.add_command(label='Remove Student', command=self.nothing)
        
        search = Menu(menu, tearoff=False)  #Search Menu Bar
        menu.add_cascade(label='Search', menu=search)
        search.add_command(label='Search Student ID', command=self.nothing)

        help = Menu(menu, tearoff=False)  #About Menu Bar
        menu.add_cascade(label='About', menu=help)
        help.add_checkbutton(label='Ajmain K')
        help.add_separator()
        help.add_command(label='Help', command=self.nothing)

        '''Database Table display box '''
        self.treeView = ttk.Treeview(self, height=25, column=['', '', '', '', '', '', '', '', '', '','','','','','','','','','',''])
        self.treeView.pack(side=BOTTOM, fill=BOTH)
        self.treeView.heading('#0', text='ID')
        self.treeView.column('#0', width=70, stretch=False)
        self.treeView.heading('#1', text='First Name')
        self.treeView.column('#1', width=100)
        self.treeView.heading('#2', text='Middle Name')
        self.treeView.column('#2', width=100)
        self.treeView.heading('#3', text='Last Name')
        self.treeView.column('#3', width=100)
        self.treeView.heading('#4', text='Birthday')
        self.treeView.column('#4', width=150)
        self.treeView.heading('#5', text='Gender')
        self.treeView.column('#5', width=120)
        self.treeView.heading('#6', text='Department')
        self.treeView.column('#6', width=100)
        self.treeView.heading('#7', text='Email')
        self.treeView.column('#7', width=100)
        self.treeView.heading('#8', text='Phone Number')
        self.treeView.column('#8', width=150)
        self.treeView.heading('#9', text='Address')
        self.treeView.column('#9', width=150)
        self.treeView.heading('#10', text='Department')
        self.treeView.column('#10', width=100)
        self.treeView.heading('#11', text='Email')
        self.treeView.column('#11', width=150)
        self.treeView.heading('#12', text='Phone #')
        self.treeView.column('#12', width=150)
        self.treeView.heading('#13', text='Address')
        self.treeView.column('#13', width=100)
        self.treeView.heading('#14', text='Emergency Contacts')
        self.treeView.column('#14', width=150)
        self.treeView.heading('#15', text='Courses')
        self.treeView.column('#15', width=150)
        self.treeView.heading('#16', text='Fees Due')
        self.treeView.column('#16', width=100)
        self.treeView.heading('#17', text='Awards & Financial Aid')
        self.treeView.column('#17', width=150)
        self.treeView.heading('#18', text='Final Grades')
        self.treeView.column('#18', width=150)


    '''Setup Database Table Connection To SQLite Database'''
    def query_invoke(self, query, param=()):
        with sqlite3.connect(self.student_db) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, param)
            conn.commit()
            print (result)
        return result

    def view_records(self):
        records = self.treeView.get_children()
        for i in records:
            self.treeView.delete(i)
        query = 'SELECT * FROM studentlist'
        table = self.query_invoke(query)
        for n in table:
            self.treeView.insert('', 1000, text=n[0], values=n[1:])


    '''''''''''''''''''''''''''''''''''''''
    '           Button Fuctions           '
    '''''''''''''''''''''''''''''''''''''''

    '''Adding New Record'''
    def checkValid(self):  #Check if all fields are filled out
        return len(self.firstname.get()) != 0 and len(self.middlename.get()) != 0 and len(self.lastname.get()) != 0 and \
               len(self.dob.get()) != 0 and len(self.gender.get()) != 0 and len(self.department.get()) != 0 and \
                   len(self.email.get()) != 0 and len(self.phone.get()) != 0 and len(self.address.get()) != 0 and \
                       len(self.emrgcontact.get()) != 0 and len(self.courses.get()) != 0 and len(self.fees.get()) != 0 and \
                           len(self.awards.get()) != 0 and len(self.grades.get()) != 0

    def ledger_add(self):  #
        if self.checkValid():
            query = 'INSERT INTO studentlist VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'
            param = (self.firstname.get(), self.middlename.get(), self.lastname.get(), self.dob.get(), self.gender.get(),
                          self.department.get(), self.email.get(), self.phone.get(), self.address.get(), self.emrgcontact.get(),
                          self.courses.get(), self.fees.get(), self.awards.get(), self.grades.get())
            self.query_invoke(query, param)
            #self.msg['text'] = 'Record successfuly added to database!'

            self.firstname.delete(0, END)  #Clear Entry Fields
            self.middlename.delete(0, END)
            self.lastname.delete(0, END)
            self.dob.delete(0, END)
            self.gender.delete(0, END)
            self.department.delete(0, END)
            self.email.delete(0, END)
            self.phone.delete(0, END)
            self.address.delete(0, END)
            self.emrgcontact.delete(0, END)
            self.courses.delete(0, END)
            self.fees.delete(0, END)
            self.awards.delete(0, END)
            self.grades.delete(0, END)
        else:
            #self.msg['text'] = 'Fields not completed! Complete all fields...'
            pass

        self.view_records()
    

    def add(self):  #Fields for user input
        self.addWindow = Toplevel()
        center(self.addWindow, 0, 0)
        self.addWindow.geometry('270x350')
        self.addWindow.title('Add New Students To Record')

        '''New Record Fields'''
        Label(self.addWindow, text='First Name:').grid(row=1, column=1, sticky=W)
        self.firstname = Entry(self.addWindow)
        self.firstname.grid(row=1, column=2)

        Label(self.addWindow, text='Middle Name:').grid(row=2, column=1, sticky=W)
        self.middlename = Entry(self.addWindow)
        self.middlename.grid(row=2, column=2)

        Label(self.addWindow, text='Last Name:').grid(row=3, column=1, sticky=W)
        self.lastname = Entry(self.addWindow)
        self.lastname.grid(row=3, column=2)

        Label(self.addWindow, text='Date of Birth:').grid(row=4, column=1, sticky=W)
        self.dob = Entry(self.addWindow)
        self.dob.grid(row=4, column=2)

        Label(self.addWindow, text='Gender:').grid(row=5, column=1, sticky=W)
        self.gender = Entry(self.addWindow)
        self.gender.grid(row=5, column=2)

        Label(self.addWindow, text='Department:').grid(row=6, column=1, sticky=W)
        self.department = Entry(self.addWindow)
        self.department.grid(row=6, column=2)

        Label(self.addWindow, text='Email:').grid(row=7, column=1, sticky=W)
        self.email = Entry(self.addWindow)
        self.email.grid(row=7, column=2)

        Label(self.addWindow, text='Phone Number:').grid(row=8, column=1, sticky=W)
        self.phone = Entry(self.addWindow)
        self.phone.grid(row=8, column=2)

        Label(self.addWindow, text='Address:').grid(row=9, column=1, sticky=W)
        self.address = Entry(self.addWindow)
        self.address.grid(row=9, column=2)

        Label(self.addWindow, text='Emergency Contact Info:').grid(row=10, column=1, sticky=W)
        self.emrgcontact = Entry(self.addWindow)
        self.emrgcontact.grid(row=10, column=2)

        Label(self.addWindow, text='Courses:').grid(row=11, column=1, sticky=W)
        self.courses = Entry(self.addWindow)
        self.courses.grid(row=11, column=2)

        Label(self.addWindow, text='Fees Due:').grid(row=12, column=1, sticky=W)
        self.fees = Entry(self.addWindow)
        self.fees.grid(row=12, column=2)

        Label(self.addWindow, text='Awards & Financial Aids:').grid(row=13, column=1, sticky=W)
        self.awards = Entry(self.addWindow)
        self.awards.grid(row=13, column=2)

        Label(self.addWindow, text='Final Grades:').grid(row=14, column=1, sticky=W)
        self.grades = Entry(self.addWindow)
        self.grades.grid(row=14, column=2)

        add = Button(self.addWindow, command=self.ledger_add(), text='Add Student')
        add.grid(row=15, pady=20, columnspan=4)

        #self.msg = Label(self.addWindow, text='', fg='Red')
        #self.msg.grid(row=16, columnspan=4)

    


    def edit(self):  #Function to edit a prexisting record and update it in the database
        self.editWindow = Toplevel()
        center(self.editWindow, 0, 0)
        self.editWindow.geometry('300x350')
        self.editWindow.title('Edit An Existing Record')

        '''Editing Fields'''
        Label(self.editWindow, text='First Name:').grid(row=1, column=1, padx=10, sticky=W)
        firstname_edit = Entry(self.editWindow)
        firstname_edit.grid(row=1, column=2)

        Label(self.editWindow, text='Middle Name:').grid(row=2, column=1, padx=10, sticky=W)
        middlename_edit = Entry(self.editWindow)
        middlename_edit.grid(row=2, column=2)

        Label(self.editWindow, text='Last Name:').grid(row=3, column=1, padx=10, sticky=W)
        lastname_edit = Entry(self.editWindow)
        lastname_edit.grid(row=3, column=2)

        Label(self.editWindow, text='Date of Birth:').grid(row=4, column=1, padx=10, sticky=W)
        dob_edit = Entry(self.editWindow)
        dob_edit.grid(row=4, column=2)

        Label(self.editWindow, text='Gender:').grid(row=5, column=1, padx=10, sticky=W)
        gender_edit = Entry(self.editWindow)
        gender_edit.grid(row=5, column=2)

        Label(self.editWindow, text='Department:').grid(row=6, column=1, padx=10, sticky=W)
        department_edit = Entry(self.editWindow)
        department_edit.grid(row=6, column=2)

        Label(self.editWindow, text='Email:').grid(row=7, column=1, padx=10, sticky=W)
        email_edit = Entry(self.editWindow)
        email_edit.grid(row=7, column=2)

        Label(self.editWindow, text='Phone Number:').grid(row=8, column=1, padx=10, sticky=W)
        phone_edit = Entry(self.editWindow)
        phone_edit.grid(row=8, column=2)

        Label(self.editWindow, text='Address:').grid(row=9, column=1, padx=10, sticky=W)
        address_edit = Entry(self.editWindow)
        address_edit.grid(row=9, column=2)

        Label(self.editWindow, text='Emergency Contact Info:').grid(row=10, column=1, padx=10, sticky=W)
        emrgcontact_edit = Entry(self.editWindow)
        emrgcontact_edit.grid(row=10, column=2)

        Label(self.editWindow, text='Courses:').grid(row=11, column=1, padx=10, sticky=W)
        courses_edit = Entry(self.editWindow)
        courses_edit.grid(row=11, column=2)

        Label(self.editWindow, text='Fees Due:').grid(row=12, column=1, padx=10, sticky=W)
        fees_edit = Entry(self.editWindow)
        fees_edit.grid(row=12, column=2)

        Label(self.editWindow, text='Awards & Financial Aids:').grid(row=13, column=1, padx=10, sticky=W)
        awards_edit = Entry(self.editWindow)
        awards_edit.grid(row=13, column=2)

        Label(self.editWindow, text='Final Grades:').grid(row=14, column=1, padx=10, sticky=W)
        grades_edit = Entry(self.editWindow)
        grades_edit.grid(row=14, column=2)

        btnEdit = Button(self.editWindow, text='Save Changes')
        btnEdit.grid(row=15, column=1, columnspan=2, pady=15)

        self.editWindow.mainloop()

    
        
    '''Exit Function'''
    def exit(self):
        if msgbox.askokcancel('Exit Application','Are you sure you want to close this application?'):
            self.destroy()

    
    def nothing(self):
        print("Test")        



















def center(root, a, b):  #Function to center window in the middle of the display
    root.update_idletasks()
    #Returns height & width of the root window
    width = root.winfo_reqwidth()
    height = root.winfo_reqheight()
    #Gets half the screen width/height & subtracts window width/height from it.
    x = int((root.winfo_screenwidth()+a)/2 - width/2)
    y = int((root.winfo_screenheight()+b)/2 - height/2)
    root.geometry('+%s+%s' % (x, y))  #Set the geometry of the window

#Main Loop allows program to run as a standalone
if __name__ == "__main__":
    run = Ledger()
    run.mainloop()



