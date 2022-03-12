'''
File Checking
Date: March 8, 2022

Author: Alden Tilley
'''

import glob
import time
import datetime
import winsound
import pyautogui
import threading
import tkinter as tk
from tkinter import filedialog

def Start():
    StartButton["state"] = tk.DISABLED
    global thread
    thread = threading.Thread(target = CheckFolders)
    thread.start()

def Stop():
    StopButton["state"] = tk.DISABLED
    StopThread()
    pass

def CheckFolders():
    if Folder1Var.get() != "":
        A1 = glob.glob(Folder1Var.get() + "/*")
        do1 = True
    else:
        do1 = False
    if Folder2Var.get() != "":
        A2 = glob.glob(Folder2Var.get() + "/*")
        do2 = True
    else:
        do2 = False
    if Folder3Var.get() != "":
        A3 = glob.glob(Folder3Var.get() + "/*")
        do3 = True
    else:
        do3 = False
    if Folder4Var.get() != "":
        A4 = glob.glob(Folder4Var.get() + "/*")
        do4 = True
    else:
        do4 = False
    if Folder5Var.get() != "":
        A5 = glob.glob(Folder5Var.get() + "/*")
        do5 = True
    else:
        do5 = False
    while True:
        if StopButton["state"] == tk.DISABLED:
            break
        if do1:
            B1 = glob.glob(Folder1Var.get() + "/*")
        if do2:
            B2 = glob.glob(Folder2Var.get() + "/*")
        if do3:
            B3 = glob.glob(Folder3Var.get() + "/*")
        if do4:
            B4 = glob.glob(Folder4Var.get() + "/*")
        if do5:
            B5 = glob.glob(Folder5Var.get() + "/*")
        if do1:
            if A1 != B1:
                A1 = B1
                t = datetime.datetime.now()
                Text1_1["text"] = str(t.hour) + ":" + str(t.minute)
                Text1_2["text"] = "New Folder 1 File"
                winsound.Beep(200, 1000)
            else:
                Text1_2["text"] = ""
        if do2:
            if A2 != B2:
                A2 = B2
                t = datetime.datetime.now()
                Text2_1["text"] = str(t.hour) + ":" + str(t.minute)
                Text2_2["text"] = "New Folder 2 File"
                winsound.Beep(200, 1000)
            else:
                Text2_2["text"] = ""
        if do3:
            if A3 != B3:
                A3 = B3
                t = datetime.datetime.now()
                Text3_1["text"] = str(t.hour) + ":" + str(t.minute)
                Text3_2["text"] = "New Folder 3 File"
                winsound.Beep(200, 1000)
            else:
                Text3_2["text"] = ""
        if do4:
            if A4 != B4:
                A4 = B4
                t = datetime.datetime.now()
                Text4_1["text"] = str(t.hour) + ":" + str(t.minute)
                Text4_2["text"] = "New Folder 4 File"
                winsound.Beep(200, 1000)
            else:
                Text4_2["text"] = ""
        if do5:
            if A5 != B5:
                A5 = B5
                t = datetime.datetime.now()
                Text5_1["text"] = str(t.hour) + ":" + str(t.minute)
                Text5_2["text"] = "New Folder 5 File"
                winsound.Beep(200, 1000)
            else:
                Text5_2["text"] = ""
        if StopButton["state"] != tk.DISABLED:
            if Wake.get():
                pyautogui.press('volumedown')
                time.sleep(1)
                pyautogui.press('volumeup')
            time.sleep(60)

def StopThread():
    if not thread.is_alive():
        StartButton["state"] = tk.NORMAL
        StopButton["state"] = tk.NORMAL
    else:
        root.after(1000, StopThread) 

def Folder1Browser():
    InitialDirectory = "C:/"
    root.filename = filedialog.askdirectory(initialdir = InitialDirectory, title = "Browse")
    Folder1Var.delete(0, tk.END)
    Folder1Var.insert(0, root.filename)
    
def Folder2Browser():
    InitialDirectory = "C:/"
    root.filename = filedialog.askdirectory(initialdir = InitialDirectory, title = "Browse")
    Folder2Var.delete(0, tk.END)
    Folder2Var.insert(0, root.filename)

def Folder3Browser():
    InitialDirectory = "C:/"
    root.filename = filedialog.askdirectory(initialdir = InitialDirectory, title = "Browse")
    Folder3Var.delete(0, tk.END)
    Folder3Var.insert(0, root.filename)
    
def Folder4Browser():
    InitialDirectory = "C:/"
    root.filename = filedialog.askdirectory(initialdir = InitialDirectory, title = "Browse")
    Folder4Var.delete(0, tk.END)
    Folder4Var.insert(0, root.filename)
    
def Folder5Browser():
    InitialDirectory = "C:/"
    root.filename = filedialog.askdirectory(initialdir = InitialDirectory, title = "Browse")
    Folder5Var.delete(0, tk.END)
    Folder5Var.insert(0, root.filename)

if __name__ == "__main__":
    
    root = tk.Tk()
    root.title("Folder Update Checker")
    
    Title = tk.Label(root, text = "Folder Update Checker").grid(row = 0, column = 0, columnspan = 9)
    
    Spacer1 = tk.Label(root, text = "     ").grid(row = 10, column = 0)
    Spacer2 = tk.Label(root, text = "     ").grid(row = 20, column = 10)
    Spacer3 = tk.Label(root, text = "     ").grid(row = 30, column = 0)
    Spacer4 = tk.Label(root, text = "     ").grid(row = 40, column = 0)
    
    Folder1Text = tk.Label(root, text = "Folder 1:").grid(row = 11, column = 1)
    Folder1Var = tk.Entry(root, width = 90)
    Folder1Var.grid(row = 11, column = 2, columnspan = 5)
    Folder1Button = tk.Button(root, text = "Browse", command = Folder1Browser).grid(row = 11, column = 7)
    
    Folder2Text = tk.Label(root, text = "Folder 2:").grid(row = 12, column = 1)
    Folder2Var = tk.Entry(root, width = 90)
    Folder2Var.grid(row = 12, column = 2, columnspan = 5)
    Folder2Button = tk.Button(root, text = "Browse", command = Folder2Browser).grid(row = 12, column = 7)
    
    Folder3Text = tk.Label(root, text = "Folder 3:").grid(row = 13, column = 1)
    Folder3Var = tk.Entry(root, width = 90)
    Folder3Var.grid(row = 13, column = 2, columnspan = 5)
    Folder3Button = tk.Button(root, text = "Browse", command = Folder3Browser).grid(row = 13, column = 7)
    
    Folder4Text = tk.Label(root, text = "Folder 4:").grid(row = 14, column = 1)
    Folder4Var = tk.Entry(root, width = 90)
    Folder4Var.grid(row = 14, column = 2, columnspan = 5)
    Folder4Button = tk.Button(root, text = "Browse", command = Folder4Browser).grid(row = 14, column = 7)
    
    Folder5Text = tk.Label(root, text = "Folder 5:").grid(row = 15, column = 1)
    Folder5Var = tk.Entry(root, width = 90)
    Folder5Var.grid(row = 15, column = 2, columnspan = 5)
    Folder5Button = tk.Button(root, text = "Browse", command = Folder5Browser).grid(row = 15, column = 7)
    
    Wake = tk.BooleanVar()
    WakeBox = tk.Checkbutton(root, text = "Keep Awake", var = Wake, onvalue = True, offvalue = False)
    WakeBox.select()
    WakeBox.grid(row = 19, column = 0, columnspan = 9)
    
    Text1_1 = tk.Label(root, text = "")
    Text1_1.grid(row = 21, column = 2)
    Text1_2 = tk.Label(root, text = "")
    Text1_2.grid(row = 22, column = 2)
    Text2_1 = tk.Label(root, text = "")
    Text2_1.grid(row = 21, column = 3)
    Text2_2 = tk.Label(root, text = "")
    Text2_2.grid(row = 22, column = 3)
    Text3_1 = tk.Label(root, text = "")
    Text3_1.grid(row = 21, column = 4)
    Text3_2 = tk.Label(root, text = "")
    Text3_2.grid(row = 22, column = 4)
    Text4_1 = tk.Label(root, text = "")
    Text4_1.grid(row = 21, column = 5)
    Text4_2 = tk.Label(root, text = "")
    Text4_2.grid(row = 22, column = 5)
    Text5_1 = tk.Label(root, text = "")
    Text5_1.grid(row = 21, column = 6)
    Text5_2 = tk.Label(root, text = "")
    Text5_2.grid(row = 22, column = 6)
    
    StartButton = tk.Button(root, text = "Start", command = Start)
    StartButton.grid(row = 31, column = 0, columnspan = 9)
    StopButton = tk.Button(root, text = "Stop", command = Stop)
    StopButton.grid(row = 32, column = 0, columnspan = 9)
    
    root.mainloop()
