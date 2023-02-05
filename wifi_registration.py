#Wifi-registration program.py
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror
from datetime import date
import time
import getmac
import os    
import re
import subprocess


link = 'https://c4rb0n.in/'

def mactype():
    command = "netsh interface ip show config"
    output = subprocess.check_output(command,shell=True)
    # Iterate over the output and search for dynamic IP address
    for line in output.splitlines():
        if line.lower().startswith("dynamic".encode('utf-8')):
            return showerror(title='Dynamic MAC ERROR', message='"Error: Dynamic MAC Address detected." '\
                                            '\nPlease change your MAC address to a static configuration '\
                                          'to ensure proper network connectivity. '\
                                        'If you require assistance, please contact your network administrator.'\
                                            'to configure manually visit this link: {}'.format(link))
        else:
            mac = getmac.get_mac_address()
            return mac
            break

def submit():
    email = email_entry.get()
    password = password_entry.get()
    print(email,password)
    # Store the email and password in variables

# creating the main window
window = Tk()
# the title for the window
window.title('WiFi - Registration Appliation')
# the dimensions and position of the windodw
window.geometry('700x400')
# making the window nonresizabale
window.resizable(height=FALSE, width=FALSE)
#window color
window.configure(background="grey")

# the canvas to contain all the widgets
canvas = Canvas(window, width=670, height=580)#,background='black')
canvas.pack()
# ttk styles for the labels
label_style = ttk.Style()
label_style.configure('TLabel', foreground='#000000', font=('OCR A Extended', 14))

# ttk styles for the button

# ttk styles for the entries
entry_style = ttk.Style()
entry_style.configure('TEntry', font=('Dotum', 15))
# the label for displaying the big text
big_label = Label(window, text='WiFi Registration', font=('OCR A Extended', 25))

# placing the big label inside the canvas
canvas.create_window(348, 100, window=big_label)

email_label = ttk.Label(window,text="Email:",style='TLabel')
email_entry = ttk.Entry(window,width  = 20,style = 'TEntry')
# email_entry = ttk.Entry(window)


password_label = ttk.Label(window,text="Password:",style="TLabel")
password_entry = ttk.Entry(window,width = 20,style="TEntry",show="•")

#sign_in_button = ttk.Button(window,text="Sign in",style="TButton",command=0)#----------------------!!!!

time.sleep(0)
check_mac_type = mactype()

mac_address = check_mac_type#"12:34:56:78:90:AB" - Example MAC address #-------------------------------------------!!!!
Mac_fetch = ttk.Label(window, text=mac_address, style="TLabel",foreground = "red")
Mac_entry = ttk.Label(window,text = "MAC:",style = "TLabel",foreground = "red")

canvas.create_window(179,200,window=email_label)
canvas.create_window(340, 200, window = email_entry)

canvas.create_window(197,240,window = password_label)
canvas.create_window(340,240,window = password_entry)


button = Button(window, text = 'Submit', bg='#ffffff', activebackground='#4444ff',command = submit)  
button.pack()   
canvas.create_window(480, 240, window=button)

canvas.create_window(360,300,window = Mac_fetch)
canvas.create_window(178,300,window = Mac_entry)


# runs the window infinitely until uses closes it
window.mainloop()