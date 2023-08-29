from tkinter import *
import random
import base64
import smtplib
import os
import qrcode
from stat import S_IREAD
from tkinter import ttk
from typing import Sized

#--------------------------------------------------------------------

win = Tk()
win.title("password saver")
win.maxsize(width=1000,height=600)
win.minsize(width=900,height=600)
win.iconbitmap("g.ico")

#--------------------------------------------------------------------

bg = PhotoImage(file="s.png")
lbl = Label(win, image=bg)
lbl.place(x=0,y=0,relwidth=1, relheight=1)

#-------------------------------------------------------------------

lblInfo = Label(win, font=('comic sans MS', 50, 'bold'),
                text="PASSWORD SAVER ",
                fg="Black", bd=10, anchor='w')

#-------------------------------------------------------------------

lblInfo.place(x=120,y=10)
Msg = StringVar()
key = StringVar()
mode = StringVar()
Result = StringVar()
y= StringVar()
R=StringVar()
p_info=StringVar()
t=StringVar()
password=StringVar()
send=StringVar()
gpass=StringVar()



#------------------------------------------------------------

lblMsg = Label(win, font=('arial', 10,'bold'),
               text="Password", bd=5, anchor="w")

lblMsg.place(x=30, y=120)

txtMsg = Entry(win, font=('arial', 10),
               textvariable=Msg, bd=5, insertwidth=4,
               bg="powder blue", justify='right')

txtMsg.place(x=120, y=120)

#----------------------------------------------------------------

lblkey = Label(win, font=('arial', 10,'bold'),
               text="Key(integers)", bd=5, anchor="w")

lblkey.place(x=30, y=160)

txtkey = Entry(win, font=('arial', 10),
               textvariable=key, bd=5, insertwidth=4,
               bg="powder blue", justify='right')

txtkey.place(x=120, y=160)

#-----------------------------------------------------------------


lblmode = Label(win, font=('arial', 10, 'bold'),
                text="Mode",
                bd=5, anchor="w")

lblmode.place(x=30, y=200)

txtmode = ttk.Combobox(win, width=20,
                       textvariable=mode )
txtmode['state'] = "readonly"
txtmode["values"] = ('encrypt',
                     'decrypt'
                     )
txtmode.place(x=120, y=200)

#--------------------------------------------------------------------

lbl = Label(win, text= "For Saving the Details",font=('arial', 16, 'bold'))
lbl.place(x=30, y=400)

lbl = Label(win, text= "For Sending the Details",font=('arial', 16, 'bold'))
lbl.place(x=570,y=400)




#------------------------------------------------------------------------

lblmail = Label(win, font=('arial', 10, 'bold'),
                text="Enter Mail",
                bd=5, anchor="w")

lblmail.place(x=500, y=450)

# Entry box for the mail
txtmail = Entry(win, font=('arial', 10),
                textvariable=y, bd=5, insertwidth=4,
                bg="powder blue", justify='right')

txtmail.place(x=600, y=450)

#------------------------------------------------------------------------

lblResult = Label(win, font=('arial', 10, 'bold'),
                  text="Result-", bd=5, anchor="w")

lblResult.place(x=30,y=240)

txtResult = Entry(win, font=('arial', 10),
                  textvariable=Result, bd=5, insertwidth=4,
                  bg="powder blue", justify='right')

txtResult.place(x=120,y=240)

#----------------------------------------------------------------------------


lblpassword = Label(win, font=('arial', 10, 'bold'),
                text="Password for",
                bd=5, anchor="w")

lblpassword.place(x=30,y=450)

txtpassword = Entry(win, font=('arial', 10),
                textvariable=password, bd=5, insertwidth=4,
                bg="powder blue", justify='right')

txtpassword.place(x=120,y=450)

#-----------------------------------------------------------------------------


lblfilename = Label(win, font=('arial', 10, 'bold'),
                text="Filename",
                bd=5, anchor="w")

lblfilename.place(x=30,y=500)

txtfilename = Entry(win, font=('arial', 10),
                textvariable=t, bd=5, insertwidth=4,
                bg="powder blue", justify='right')

txtfilename.place(x=120,y=500)

#--------------------------------------------------------------------------------

def qrcode():
    
    data = "Encypted message -"+txtResult.get()+key.get()+"\n This is the password for - "+txtpassword.get()
    filename = txtfilename.get()
    img = qrcode.make(data)
    img.save(f'C:\\Users\\user80\\Pictures\\{filename}.png')
    
        

#--------------------------------------------------------------------------------------------------

def insert():
    text="D:\\"
    rext=".txt"
    tj=len(txtfilename.get())
    txtfilename.insert(tj, rext)
    txtfilename.insert(0, text)
    return None


#----------------------------------------------------------------------------------------------------

def savefile():
    
    file=open(txtfilename.get(),"w")
    file.write("Encypted message -"+txtResult.get()+key.get()+"\n This is the password for - "+txtpassword.get())
    file.close()
    print("DEMO")


#--------------------------------------------------------------------------------------------------

def sendEmail(y, p_info):
    try:
            
                
            
                   
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.ehlo()
                server.starttls()
                #send_info=txtsendingmail.get()
                #gmailpas_info=txtgmailpas.get()
                server.login('itbsc2020@gmail.com', 'Bscit2020')
                y_info=y.get()
                p_info="Encypted message -"+txtResult.get()+key.get()
                server.sendmail('itbsc2020@gmail.com', y_info , p_info)
                server.close()
                print("Email has been sent!",p_info)
    except Exception as e:
                print(e)
                print("huh",p_info) 
    



#-------------------------------------------------------------------------------------

def encode(key, msg):
    enc = []
    for i in range(len(msg)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(msg[i]) +
                     ord(key_c)) % 256)
        enc.append(enc_c)
        
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()


#---------------------------------------------------------------------------------------

def decode(key, enc):
    dec = []

    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) -
                     ord(key_c)) % 256)

        dec.append(dec_c)
        print("dec:", dec)
    return "".join(dec)

#--------------------------------------------------------------------------------------
def Results():
    
    msg = Msg.get()
    k = key.get()
    m = mode.get()

    if (m == 'encrypt'):
        Result.set(encode(k, msg))
    else:
        Result.set(decode(k, msg))
        

#-----------------------------------------------------------------------------------------

def qExit():
    win.destroy()


#------------------------------------------------------------------------------------------

def Reset():

    Msg.set("")
    key.set("")
    mode.set("")
    Result.set("")
    t.set("")
    password.set("")

#-------------------------------------------------------------------------------------------
    
def read():
   os.chmod(txtfilename.get(), S_IREAD)

#--------------------------------------------------------------------------------------

btnTotal = Button(win, padx=16, pady=8, bd=10, fg="black",
                  font=('arial', 16, 'bold'), width=10,
                  text="Show Result", bg="powder blue",
                  command=Results).place(x=90,y=300)

#--------------------------------------------------------------------------------------

btnReset = Button(win, padx=16, pady=8, bd=10,
                  fg="black", font=('arial', 16, 'bold'),
                  width=10, text="Reset", bg="cyan",
                  command=Reset).place(x=600, y=130)

#---------------------------------------------------------------------------------------

btnExit = Button(win, padx=16, pady=8, bd=10,
                 fg="black", font=('arial', 16, 'bold'),
                 width=10, text="Exit", bg="red",
                 command=qExit).place(x=600,y=230)

#----------------------------------------------------------------------------------------
btnmail = Button(win, padx=4, pady=1, bd=5,
                 fg="black", font=('arial', 8,'bold' ),
                 width=6, text="SendMail", bg="powder blue",
                 command=lambda:sendEmail(y, p_info)).place(x=780,y=450)

#-----------------------------------------------------------------------------------------

btnsavetxt = Button(win, padx=4, pady=1, bd=5,
                 fg="black", font=('arial', 8,'bold'),
                 width=5, text="Save txt", bg="powder blue",
                 command=lambda:[insert(),savefile(),read()]).place(x=300,y=500)

#-----------------------------------------------------------------------------------------

btnqr = Button(win, padx=4, pady=1, bd=5,
                 fg="black", font=('arial', 8,'bold'),
                 width=5, text="QrCode", bg="powder blue",
                 command=lambda:qrcode()).place(x=400,y=500)

win.mainloop()
