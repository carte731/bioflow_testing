#!/usr/bin/env python3

from tkinter import *
import paramiko
from scp import SCPClient
import os

def qAndA(root):

    choice = StringVar()
    usr = StringVar()
    pas = StringVar()
    hostStr = StringVar()

    questTextOne = "Did you like The Last Jedi?"
    question = Label(root, text=questTextOne).grid(columnspan=2)

    q1 = Radiobutton(root, text="YES", variable=choice, value='YES').grid(row=1, sticky=W)
    q2 = Radiobutton(root, text="NO", variable=choice, value='HELL NO').grid(row=2, sticky=W)

    username = Label(root, text="login").grid(row=3, sticky=E)
    password = Label(root, text="password").grid(row=4, sticky=E)
    host = Label(root, text="host").grid(row=5, sticky=E)
    
    entryUser = Entry(root, textvariable=usr)
    entryPassword = Entry(root, show="*", textvariable=pas)
    entryHost = Entry(root, textvariable=hostStr)

    entryUser.grid(row=3, column=1)
    entryPassword.grid(row=4, column=1)
    entryHost.grid(row=5, column=1)

    button_1 = Button(root, text="Send It", command = lambda: press(usr, pas, questTextOne, choice, hostStr))
    button_1.grid(row=7, columnspan=2)

def press(usrnme, psswrd, finalout, choice, hostStr):
    usn = usrnme.get()
    pas = psswrd.get()
    hos = hostStr.get()
    cho = choice.get()
    location = os.path.dirname(os.path.abspath(__file__))
    location += "/config_files"
    with open(location + "/TEST.Config", "w+") as fileChoices:
        fileChoices.write(finalout + "=" + cho)
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=hos,username=usn,password=pas)
    # stdin,stdout,stderr=ssh_client.exec_command("ls")
    ftp_client = ssh_client.open_sftp()
    ftp_client.put("TEST.Config","BIOFLOW.CONFIG")
    print("DONE\n")
    ftp_client.close()

def main():
    root = Tk()
    qAndA(root)
    root.mainloop()

main()