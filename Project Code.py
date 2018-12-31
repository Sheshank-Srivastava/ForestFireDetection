from tkinter import *
import os
import webbrowser
from tkinter import messagebox as tm
import xlrd
from threading import Thread
from time import sleep
import winsound


def exitFunction(root):
    root.quit()
    root.destroy()

def web():
    webbrowser.open_new('index.html')




def getData(root, entryTemperature, varTemperature, entryHumidity, varHumidity):
    runT = Thread(target=setData, args=(
    root, entryTemperature, varTemperature, entryHumidity, varHumidity))
    runT.daemon = True
    runT.start()


def setData(root, entryTemperature, varTemperature, entryHumidity, varHumidity):
    file_location = "C:/Users/rajinder/PycharmProjects/CSIR/excel.xlsx"
    workbook = xlrd.open_workbook(file_location)
    sheet = workbook.sheet_by_index(0)
    num_cols = sheet.ncols
    num_rows = sheet.nrows
    table = list()
    record = list()
    for x in range(num_rows):
        for y in range(num_cols):
            record.append(sheet.cell(x, y).value)
        table.append(record)
        record = []
        x += 1

    for y in range(num_rows):
        varTemperature.set(table[y][1])
        varHumidity.set(table[y][2])

        if float(entryTemperature.get()) > 27.04 and float(entryHumidity.get()) > 65.76:
            fireLabel = Label(root, text="FIRE FIRE", padx=10, relief=SUNKEN, bg='#FF0000',font = ("Times", "26", "bold italic"),height = 2)
            fireLabel.grid(row = 1,rowspan = 5,column = 2)
            winsound.PlaySound("C:/Users/rajinder/PycharmProjects/CSIR/BuzzerSound.wav", winsound.SND_ASYNC)
        else:
            fireLabel = Label(root, text=" NO    FIRE", padx=10, relief=SUNKEN, bg='#0000FF',font = ("Times", "26", "bold italic"),height = 2)
            fireLabel.grid(row = 1,rowspan = 5, column=2)
        sleep(2)

creds = 'tempfile.temp'

def Signup():
    global pwordE
    global nameE
    global roots

    roots = Tk()
    roots.title('Signup ')
    roots.resizable(False, False)
    w = 670
    h = 400


    ws = roots.winfo_screenwidth()
    hs = roots.winfo_screenheight()

    # calculate x and y coordinates for the Tk root window
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)


    roots.geometry('%dx%d+%d+%d' % (w, h, x, y))



    intruction = Label(roots, text='Please   Enter   new   Credidentials',font = ("Times", "30", "bold italic"),relief = SUNKEN,justify = CENTER,padx = 20,pady = 10,bd = 25)
    intruction.grid(row = 0,column = 0,columnspan = 2)



    nameL = Label(roots, text='New   Username: ',font = ("Times", "22", "bold italic"),padx = 5,pady = 40)
    pwordL = Label(roots, text='New   Password: ',font = ("Times", "22", "bold italic"),padx = 5,pady = 10)
    nameL.grid(row=1, column=0, sticky=W)
    pwordL.grid(row=2, column=0, sticky=W)

    nameE = Entry(roots,font = ("Times", "22", "bold italic"),relief = SUNKEN,bd = 5)
    pwordE = Entry(roots, show='*',font = ("Times", "22", "bold italic"),relief = SUNKEN,bd = 5)
    nameE.grid(row=1, column=1)
    pwordE.grid(row=2, column=1)

    signupButton = Button(roots, text='SignUp', command=FSSignup,font = ("Times", "22", "bold italic"),relief = SUNKEN,bd = 5)
    signupButton.grid(columnspan=2,padx = 10,pady = 40)
    roots.mainloop()

def FSSignup():
    if len(nameE.get()) == 0 or len(pwordE.get()) == 0:
        tm.showerror("Signup Error", "Invalid Username Or Password")

    else:
       with open(creds, 'w') as f:
           f.write(nameE.get())
           f.write('\n')
           f.write(pwordE.get())
           f.close()

       roots.destroy()
       Login()

def Login():
    global nameEL
    global pwordEL
    global rootA

    rootA = Tk()
    rootA.title('Login')
    rootA.resizable(False, False)
    w = 580
    h = 430


    ws = rootA.winfo_screenwidth()
    hs = rootA.winfo_screenheight()

    # calculate x and y coordinates for the Tk root window
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)


    rootA.geometry('%dx%d+%d+%d' % (w, h, x, y))

    intruction = Label(rootA, text='Please    Login    Here',font = ("Times", "40", "bold italic"),relief = SUNKEN,justify = CENTER,padx = 20,pady = 10,bd = 25)
    intruction.grid(row = 0,column = 0,columnspan = 2)

    nameL = Label(rootA, text='Username: ',font = ("Times", "22", "bold italic"),padx = 20,pady = 10)
    pwordL = Label(rootA, text='Password: ',font = ("Times", "22", "bold italic"),padx = 20,pady = 10)
    nameL.grid(row=1, sticky=W)
    pwordL.grid(row=2, sticky=W)

    nameEL = Entry(rootA,font = ("Times", "22", "bold italic"),relief = SUNKEN,bd = 5) # The entry input
    pwordEL = Entry(rootA, show='*',font = ("Times", "22", "bold italic"),relief = SUNKEN,bd = 5)
    nameEL.grid(row=1, column=1)
    pwordEL.grid(row=2, column=1)

    loginB = Button(rootA, text='Login', command=CheckLogin,font = ("Times", "22", "bold italic"),relief = SUNKEN,bd = 5)
    loginB.grid(columnspan=2,padx = 10,pady = 10)

    rmuser = Button(rootA, text='Delete   User', fg='red', command=DelUser,font = ("Times", "22", "bold italic"),relief = SUNKEN,bd = 10)
    rmuser.grid(columnspan=2,padx = 40,pady = 10)
    rootA.mainloop()

def CheckLogin():
    with open(creds) as f:
        data = f.readlines()
        uname = data[0].rstrip()
        pword = data[1].rstrip()

    if nameEL.get() == uname and pwordEL.get() == pword:
         rootA.destroy()
         root = Tk()
         root.title('Main Window')
         root.resizable(False, False)
         w = 590
         h = 320


         ws = root.winfo_screenwidth()
         hs = root.winfo_screenheight()


         x = (ws / 2) - (w / 2)
         y = (hs / 2) - (h / 2)


         root.geometry('%dx%d+%d+%d' % (w, h, x, y))

         intruction = Label(root, text='Detect      Forest        Fire', font=("Times", "35", "bold italic"), relief=SUNKEN,
                             padx=10, pady=10, bd=25)
         intruction.grid(row=0, column=0,columnspan = 3,sticky = E)
         ##########################################Variables List##########################################
         varTemperature = StringVar()
         varHumidity = StringVar()
         varCarbonMonoxide = StringVar()
         varCarbonDioxide = StringVar()
         varMethane = StringVar()
         ############################################TEMPERATURE###########################################
         labelTemperature = Label(root, text='Temperature',font = ("Times", "22", "bold italic"),padx = 5,pady = 5)
         labelTemperature.grid(row=1, column=0)
         entryTemperature = Entry(root, textvariable=varTemperature,font = ("Times", "10", "bold italic"),relief = SUNKEN,bd = 4)
         entryTemperature.grid(row=1, column=1, sticky=W)
          #############################################HUMIDITY###############################################
         labelHumidity = Label(root, text='Humidity',font = ("Times", "22", "bold italic"),padx = 5,pady = 5)
         labelHumidity.grid(row=2, column=0)
         entryHumidity = Entry(root, textvariable=varHumidity,font = ("Times", "10", "bold italic"),relief = SUNKEN,bd = 4)
         entryHumidity.grid(row=2, column=1, sticky=W)
         ###############################################CARBON  MONOXIDE#######################################
         labelCarbonMonoxide = Label(root, text='Carbon Monoxide',font = ("Times", "22", "bold italic"),padx = 5,pady = 5)
         labelCarbonMonoxide.grid(row=3, column=0)
         entryCarbonMonoxide = Entry(root, textvariable=varCarbonMonoxide,font = ("Times", "10", "bold italic"),relief = SUNKEN,bd = 4)
         entryCarbonMonoxide.grid(row=3, column=1, sticky=W)
         ################################################CARBON  DIOXIDE####################################
         labelCarbonDioxide = Label(root, text='Carbon Dioxide',font = ("Times", "22", "bold italic"),padx = 5,pady = 5)
         labelCarbonDioxide.grid(row=4, column=0)
         entryCarbonDioxide = Entry(root, textvariable=varCarbonDioxide,font = ("Times", "10", "bold italic"),relief = SUNKEN,bd = 4)
         entryCarbonDioxide.grid(row=4, column=1, sticky=W)
         #######################################METHANE###############################################
         labelMethane = Label(root, text='Methane',font = ("Times", "22", "bold italic"),padx = 5,pady = 5)
         labelMethane.grid(row=5, column=0)
         entryMethane = Entry(root, textvariable=varMethane,font = ("Times", "10", "bold italic"),relief = SUNKEN,bd = 4)
         entryMethane.grid(row=5, column=1, sticky=W)
         #########################################GETTING THE DATA FROM EXCEL################################
         getButton = Button(root, font = ("Times", "15", "bold italic"),relief = SUNKEN,bd = 10,text='GET   DATA',
                           command=lambda: getData(root, entryTemperature, varTemperature, entryHumidity, varHumidity,
                                                   ))
         getButton.grid(row=6, columnspan=3,pady = 5)
         ##########################################HELP############################################
         helpButton = Button(root, text='ABOUT', command=lambda: web(), font = ("Times", "12", "bold italic"),relief = SUNKEN,bd = 5)
         helpButton.grid(row=7, column=0,sticky = W)
         #############################################EXIT   BUTTON###########################################
         exitButton = Button(root, text='EXIT', command=lambda: exitFunction(root), font = ("Times", "12", "bold italic"),relief = SUNKEN,bd = 5)
         exitButton.grid(row=7, column=2,sticky = E)

         root.mainloop()
    else:
        tm.showerror("Login Error", "Incorrect Username Or Password")
def DelUser():
    os.remove(creds)
    rootA.destroy()
    Signup()

if os.path.isfile(creds):
    Login()
else:
    Signup()















