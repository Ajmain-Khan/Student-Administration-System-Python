'''
PYTHON Student Ledger Project
29/11/2019
'''

import sys
import os
import platform
from prettytable import PrettyTable
from prettytable import MSWORD_FRIENDLY
from getpass import getpass
from time import sleep

###############################
'''PrettyTable Configuration'''
###############################
pT = PrettyTable()
pT.field_names = ["ID", "First Name", "Middle Name", "Last Name", "Birthday", "Gender", \
        "Department", "Email", "Emergency Contact", "Courses", "Fees Due", \
            "Awards & Financial Aid", "Final Grades"]

###_Global Variables_###
ctr_ID = 0  #Counter that increments each time a student is recorded, used to calculate student ID number


####################
'''Login Function'''
####################
def login():
    username = 'admin'  #Hard code the credentials for the purposes of this project
    password = 'password'
    print("|=======Admin Login Portal=======|")
    print()
    while True:
        login_User = input('\tUsername: ')
        login_Pass = getpass('\tPassword: ')  #Keeps password invisible while typing
        if login_User == username and login_Pass == password:
            print("\n|====== Logged in as", login_User, '======|\n')
            mainMenu()
        else:
            print("\n  Incorrect Username or Password\n")
            while True:
                retry = input('Try Again? (y/n): ').lower()
                if retry == 'y':
                    print()
                    break
                elif retry == 'n':
                    sys.exit()
                else:
                    print("\nPlease type 'y' to retry or 'n' to quit!\n")                      


##########################
'''Add Student Function'''
##########################
def add():
    global ctr_ID
    sentinel = False  #Exit condition; all user input fields are encapsulated by a while loop which only exits if the input is valid and sentinel is returned True

    def id_ctr(ctr):  #Define function to summate & return student ID
        n = 2000
        n = n+ctr  #Calculate student ID # by adding the value of ctr each time
        return n
    
    ###_Assign Values To PrettyTable Fields_###
    print('\nEnter The Following Data:\n')
    in_firstName = input('First Name: ').title()
    in_middleName = input('Middle Name: ').title()
    in_lastName = input('Last Name: ').title()
    in_dob = input('Date of Birth: ')
    in_gender = input('Gender: ').title()
    in_department = input('Department: ')
    in_email = input('Email: ')
    in_emergency = input('Emergency Contacts: ')
    in_courses = input('Courses: ')
    in_fees = input('Fees Due: ')
    in_awards = input('Awards & Financial Aids: ')
    in_grades = input('Final Grades: ')
    
    while sentinel == False:  #User Input Loop
        in_save = input('\nSave Data? (y/n): ').lower()
        if in_save == 'y':
            ctr_ID += 1  #Add 1 to counter each time a student is added to database.
            ###_Add user inputs to row fields in PrettyTable_###
            pT.add_row([id_ctr(ctr_ID), in_firstName, in_middleName, in_lastName, in_dob, in_gender, \
                in_department, in_email, in_emergency, in_courses, in_fees, in_awards, in_grades])
            while sentinel == False:
                in_addMore = input('\nAdd Another Student? (y/n): ').lower()
                if in_addMore == 'y':
                    sentinel = True
                    add()
                elif in_addMore =='n':
                    sentinel = True
                    displayAdded()
                else:
                    print("\nPlease type 'y' to add another student or 'n' to continue!\n")
        elif in_save == 'n':
            sentinel = True
            print('\nChanges Discarded.')
            load()
            _return()
        else:
            print("\nPlease type 'y' to save entries or 'n' to discard!\n")


###############################
'''Display Database Function'''
###############################
def display():
    sentinel = False
    check_table = pT.get_string(header=False, border=False, fields=["ID"]).strip()  #Define a string as a pTable containing only the "ID" column and without borders, headers, or spaces.
                                                                                    #Using len() on this variable will return the # of characters in the column, which will be 0 if there's no data.
    if len(check_table) == 0:  #If there is no data in the prettytable, len() should return 0.
        print('No Records In Database. Please Add Student Data.')
        print('''
[1] Main Menu
[2] Exit
        ''')
        while sentinel == False:
            in_select = input('Select: ')
            if in_select == '1':
                sentinel = True
                load()
                _return()
            elif in_select == '2':
                sys.exit()
            else:
                print('Invalid Input. Please select [1] or [2].')
    else:
        print(pT)
        print('''
[1] Main Menu
[2] Return (Keep Data Onscreen)
[3] Exit
        ''')
        while sentinel == False:
            in_select = input('Select: ')
            if in_select == '1':
                sentinel = True
                load()
                _return()
            elif in_select == '2':
                sentinel = True
                load()
                mainMenu()
            elif in_select == '3':
                sys.exit()
            else:
                print('Invalid Input. Please select [1] or [2].')

def displayAdded():  #Slightly different display function that is called only by the add() function 
    sentinel = False
    pT_tempMS = pT
    pT_tempMS.set_style(MSWORD_FRIENDLY)
    print(pT_tempMS)
    print('''
[1] Main Menu
[2] Exit
        ''')
    while sentinel == False:
        in_select = input('Select: ')
        if in_select == '1':
            sentinel = True
            load()
            _return()
        elif in_select == '2':
            sys.exit()
        else:
            print('Invalid Input. Please select [1] or [2].')


##############################
'''Search Database Function'''
##############################
def search():
    sentinel = False
    ###_Search By ID Function_###
    def idSearch(userIn):  #Search using student "ID" field
        if userIn in pT.get_string(header=False, border=False, fields=["ID"]):  #Views only the "ID" column
            print('Searching...')
            sleep(1)
            print("\nID Match!\n")
            sleep(0.5)
            y1 = int(userIn) - 2001  #start(inclusive): index of the row to be printed
            y2 = int(userIn) - 2000  #end(exclusive): index of row that is 1 above the starting row
            pT_tempMS = pT  #Make a copy of prettytable for the purpose of using a different table style
            pT_tempMS.set_style(MSWORD_FRIENDLY)  #Change table style
            print(pT_tempMS.get_string(start=y1, end=y2), '\n')  #Print table within specified indicies
            search()
        else:
            print('Searching...')
            sleep(1)
            print('\nStudent ID not found in database.\n')
            search()

    ###_Search By Name Function_###
    def fnameSearch(userIn):  #Search using "First Name" field
        if userIn in pT.get_string(header=False, border=False, fields=["First Name"]):  #Views only the "First Name" column
            print('Searching...')
            sleep(0.8)
            print("\nID Match!\n")
            sleep(0.5)
            y1 = int(userIn) - 2001
            y2 = int(userIn) - 2000
            pT_tempMS = pT
            pT_tempMS.set_style(MSWORD_FRIENDLY)
            print(pT_tempMS.get_string(start=y1, end=y2))
            search()
        else:
            print('Searching...')
            sleep(0.8)
            print('\nStudent ID not found in database.\n')
            sleep(1)
            search()

    while sentinel == False:
        print('\n    Search Using ID [1] or First Name [2]?')
        print('''
[1] ID
[2] First Name
[3] Cancel
        ''')
        in_select = input('Select: ')
        if in_select == '1':
            sentinel = True
            in_search = input('\nSearch ID: ')
            idSearch(in_search)  #Call function to search by ID
        elif in_select == '2':
            sentinel = True
            in_search = input('\nSearch First Name: ').title()
            fnameSearch(in_search)  #Call function to search by First Name
        elif in_select == '3':
            sentinel = True
            load()
            _return()
        else:
            print('\nInvalid Input. Please select a valid option!\n')


#############################
'''Return To Menu Function'''
#############################
def _return():  #Check user OS and clear screen, then return to mainMenu menu
	if platform.system() == "Windows":
		os.system('cls')  #Clear console
	else:
		os.system('clear')  #For other operating systems
	mainMenu()


########################
'''"Loading" Function'''
########################
def load():  #Purely for a visual improvements
    sleep(0.4)
    print('\nReturning To Main Menu.')
    sleep(0.5)
    dots = '→→→'
    for i in range(3):  #Print characters one at a time with a delay
        print(dots[i], sep='', end=' ', flush=True); sleep(0.4)


#########################
'''"MAIN MENU FUNCTION'''
#########################
def mainMenu():
    sentinel = False
    print('''
 ------------------------------------------------------
|======================================================| 
|========  Ontario Tech Student Ledger System  ========|
|======================================================|
 ------------------------------------------------------

    [1] Add A New Student

    [2] Display Student Database

    [3] Search Student Details

    [4] Exit
		''')
    while sentinel == False:
        try:  #Error handling in case of invalid inputs
            menu_option = input('Select: ')
            if int(menu_option) == 1:
                print('''
 ----------------------------------------------
|=========  New Student Data Entries  =========|
 ----------------------------------------------
                ''')
                sentinel = True
                add()  #Call add function to add new students to database
            elif int(menu_option) == 2:
                print('''
 ----------------------------------------------
|=========  Display Student Database  =========|
 ----------------------------------------------
                ''')
                sentinel = True
                display()  #Call display function to view PrettyTable
            elif int(menu_option) == 3:
                print('''
 ----------------------------------------------
|==========  Search Student Details  ==========|
 ----------------------------------------------
                ''')
                sentinel = True
                search()  #Call search function to search items in PrettyTable
            elif int(menu_option) == 4:
                sys.exit()
            else:
                print('\nInvalid Input! Please select a valid option!\n')
        except ValueError:
            print('\nValueError: Please enter numbers only!\n')
        
login()  #Run the login function, which directs to mainMenu function upon successful login.


