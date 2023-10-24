'''
Author: Alden Tilley
https://github.com/eatAWESOME
'''

import os
import glob
import time
import datetime
import winsound
import pyautogui
import threading
import tkinter as tk
from tkinter import filedialog, ttk

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
    pyautogui.FAILSAFE = False
    if os.path.exists(Folder1Var.get()):
        file = Folder1Var.get() + "/**"
    else:
        file = ""
    A1 = glob.glob(file, recursive = True)
    if A1 != []:
        AT1 = os.path.getmtime(max(A1, key = os.path.getmtime))
    else:
        AT1 = 0
        
        
    if os.path.exists(Folder2Var.get()):
        file = Folder2Var.get() + "/**"
    else:
        file = ""
    A2 = glob.glob(file, recursive = True)
    if A2 != []:
        AT2 = os.path.getmtime(max(A2, key = os.path.getmtime))
    else:
        AT2 = 0
        
        
    if os.path.exists(Folder3Var.get()):
        file = Folder3Var.get() + "/**"
    else:
        file = ""
    A3 = glob.glob(file, recursive = True)
    if A3 != []:
        AT3 = os.path.getmtime(max(A3, key = os.path.getmtime))
    else:
        AT3 = 0
        
        
    if os.path.exists(Folder4Var.get()):
        file = Folder4Var.get() + "/**"
    else:
        file = ""
    A4 = glob.glob(file, recursive = True)
    if A4 != []:
        AT4 = os.path.getmtime(max(A4, key = os.path.getmtime))
    else:
        AT4 = 0
        
        
    if os.path.exists(Folder5Var.get()):
        file = Folder5Var.get() + "/**"
    else:
        file = ""
    A5 = glob.glob(file, recursive = True)
    if A5 != []:
        AT5 = os.path.getmtime(max(A5, key = os.path.getmtime))
    else:
        AT5 = 0
        
        
    i = 0
    w = 0
    while StopButton["state"] != tk.DISABLED:
        if i == 0:
            if os.path.exists(Folder1Var.get()):
                file = Folder1Var.get() + "/**"
            else:
                file = ""
            B1 = glob.glob(file, recursive = True)
            if B1 != []:
                BT1 = os.path.getmtime(max(B1, key = os.path.getmtime))
            else:
                BT1 = 0
                
                
            if os.path.exists(Folder2Var.get()):
                file = Folder2Var.get() + "/**"
            else:
                file = ""
            B2 = glob.glob(file, recursive = True)
            if B2 != []:
                BT2 = os.path.getmtime(max(B2, key = os.path.getmtime))
            else:
                BT2 = 0
                
                
            if os.path.exists(Folder3Var.get()):
                file = Folder3Var.get() + "/**"
            else:
                file = ""
            B3 = glob.glob(file, recursive = True)
            if B3 != []:
                BT3 = os.path.getmtime(max(B3, key = os.path.getmtime))
            else:
                BT3 = 0
                
                
            if os.path.exists(Folder4Var.get()):
                file = Folder4Var.get() + "/**"
            else:
                file = ""
            B4 = glob.glob(file, recursive = True)
            if B4 != []:
                BT4 = os.path.getmtime(max(B4, key = os.path.getmtime))
            else:
                BT4 = 0
                
                
            if os.path.exists(Folder5Var.get()):
                file = Folder5Var.get() + "/**"
            else:
                file = ""
            B5 = glob.glob(file, recursive = True)
            if B5 != []:
                BT5 = os.path.getmtime(max(B5, key = os.path.getmtime))
            else:
                BT5 = 0
                
                
            if A1 != B1 or AT1 != BT1:
                A1 = B1
                AT1 = BT1
                t = datetime.datetime.now()
                Text1_1["text"] = str(t.hour) + ":" + "%02d" % t.minute
                if os.path.exists(Folder1Var.get()):
                    Text1_2["text"] = "Folder 1 Changed"
                    if AlertVar.get() == "Beep on Change":
                        winsound.Beep(200, 1000)
                else:
                    Text1_2["text"] = "Folder 1 Not Found"
                    winsound.Beep(200, 1000)
            else:
                if Folder1Var.get() == "":
                    Text1_2["text"] = ""
                elif os.path.exists(Folder1Var.get()):
                    if AlertVar.get() == "Beep on No Change":
                        winsound.Beep(200, 1000)
                else:
                    Text1_2["text"] = "Folder 1 Not Found"
                    winsound.Beep(200, 1000)
                
                
            if A2 != B2 or AT2 != BT2:
                A2 = B2
                AT2 = BT2
                t = datetime.datetime.now()
                Text2_1["text"] = str(t.hour) + ":" + "%02d" % t.minute
                if os.path.exists(Folder1Var.get()):
                    Text2_2["text"] = "Folder 2 Changed"
                    if AlertVar.get() == "Beep on Change":
                        winsound.Beep(200, 1000)
                else:
                    Text2_2["text"] = "Folder 2 Not Found"
                    winsound.Beep(200, 1000)
            else:
                if Folder2Var.get() == "":
                    Text2_2["text"] = ""
                elif os.path.exists(Folder2Var.get()):
                    if AlertVar.get() == "Beep on No Change":
                        winsound.Beep(200, 1000)
                else:
                    Text2_2["text"] = "Folder 1 Not Found"
                    winsound.Beep(200, 1000)
                
                
            if A3 != B3 or AT3 != BT3:
                A3 = B3
                AT3 = BT3
                t = datetime.datetime.now()
                Text3_1["text"] = str(t.hour) + ":" + "%02d" % t.minute
                if os.path.exists(Folder3Var.get()):
                    Text3_2["text"] = "Folder 3 Changed"
                    if AlertVar.get() == "Beep on Change":
                        winsound.Beep(200, 1000)
                else:
                    Text3_2["text"] = "Folder 3 Not Found"
                    winsound.Beep(200, 1000)
            else:
                if Folder3Var.get() == "":
                    Text3_2["text"] = ""
                elif os.path.exists(Folder3Var.get()):
                    if AlertVar.get() == "Beep on No Change":
                        winsound.Beep(200, 1000)
                else:
                    Text3_2["text"] = "Folder 3 Not Found"
                    winsound.Beep(200, 1000)
                
                
            if A4 != B4 or AT4 != BT4:
                A4 = B4
                AT4 = BT4
                t = datetime.datetime.now()
                Text4_1["text"] = str(t.hour) + ":" + "%02d" % t.minute
                if os.path.exists(Folder4Var.get()):
                    Text4_2["text"] = "Folder 4 Changed"
                    if AlertVar.get() == "Beep on Change":
                        winsound.Beep(200, 1000)
                else:
                    Text4_2["text"] = "Folder 4 Not Found"
                    winsound.Beep(200, 1000)
            else:
                if Folder4Var.get() == "":
                    Text4_2["text"] = ""
                elif os.path.exists(Folder4Var.get()):
                    if AlertVar.get() == "Beep on No Change":
                        winsound.Beep(200, 1000)
                else:
                    Text4_2["text"] = "Folder 4 Not Found"
                    winsound.Beep(200, 1000)
                
                
            if A5 != B5 or AT5 != BT5:
                A5 = B5
                AT5 = BT5
                t = datetime.datetime.now()
                Text5_1["text"] = str(t.hour) + ":" + "%02d" % t.minute
                if os.path.exists(Folder5Var.get()):
                    Text5_2["text"] = "Folder 5 Changed"
                    if AlertVar.get() == "Beep on Change":
                        winsound.Beep(200, 1000)
                else:
                    Text5_2["text"] = "Folder 5 Not Found"
                    winsound.Beep(200, 1000)
            else:
                if Folder5Var.get() == "":
                    Text5_2["text"] = ""
                elif os.path.exists(Folder5Var.get()):
                    if AlertVar.get() == "Beep on No Change":
                        winsound.Beep(200, 1000)
                else:
                    Text5_2["text"] = "Folder 5 Not Found"
                    winsound.Beep(200, 1000)
                
        
        try:
            CheckInterval = int(CheckIntervalVar.get())
            if CheckIntervalUnitsVar.get() == "minutes":
                CheckInterval *= 60
            elif CheckIntervalUnitsVar.get() == "hours":
                CheckInterval *= 60 * 60
            if CheckInterval < 1:
                CheckInterval = 1
        except:
            CheckInterval = 60
            if CheckIntervalVar.get() != "":
                CheckIntervalVar.delete(0, tk.END)
                CheckIntervalVar.insert(0, "60")
        
        i += 1
        if i == CheckInterval:
            i = 0
            
            
        if Wake.get():
            try:
                WakeInterval = int(WakeIntervalVar.get())
                if WakeIntervalUnitsVar.get() == "minutes":
                    WakeInterval *= 60
                elif WakeIntervalUnitsVar.get() == "hours":
                    WakeInterval *= 60 * 60
                if WakeInterval < 1:
                    WakeInterval = 1
            except:
                WakeInterval = 60
                if WakeIntervalVar.get() != "":
                    WakeIntervalVar.delete(0, tk.END)
                    WakeIntervalVar.insert(0, "60")
                
            w += 1
            if w == WakeInterval:
                pyautogui.press('volumemute')
                time.sleep(0.1)
                pyautogui.press('volumemute')
                w = 0
        
        
        time.sleep(1)

def StopThread():
    if not thread.is_alive():
        StartButton["state"] = tk.NORMAL
        StopButton["state"] = tk.NORMAL
    else:
        root.after(1000, StopThread) 

def Folder1Browser():
    if Folder1Var.get() != "" and os.path.exists(Folder1Var.get()):
        InitialDirectory = os.path.dirname(Folder1Var.get())
    else:
        InitialDirectory = "C:/"
    root.filename = filedialog.askdirectory(initialdir = InitialDirectory, title = "Browse")
    Folder1Var.delete(0, tk.END)
    Folder1Var.insert(0, root.filename)
    
def Folder2Browser():
    if Folder2Var.get() != "" and os.path.exists(Folder2Var.get()):
        InitialDirectory = os.path.dirname(Folder2Var.get())
    else:
        InitialDirectory = "C:/"
    root.filename = filedialog.askdirectory(initialdir = InitialDirectory, title = "Browse")
    Folder2Var.delete(0, tk.END)
    Folder2Var.insert(0, root.filename)

def Folder3Browser():
    if Folder3Var.get() != "" and os.path.exists(Folder3Var.get()):
        InitialDirectory = os.path.dirname(Folder3Var.get())
    else:
        InitialDirectory = "C:/"
    root.filename = filedialog.askdirectory(initialdir = InitialDirectory, title = "Browse")
    Folder3Var.delete(0, tk.END)
    Folder3Var.insert(0, root.filename)
    
def Folder4Browser():
    if Folder4Var.get() != "" and os.path.exists(Folder4Var.get()):
        InitialDirectory = os.path.dirname(Folder4Var.get())
    else:
        InitialDirectory = "C:/"
    root.filename = filedialog.askdirectory(initialdir = InitialDirectory, title = "Browse")
    Folder4Var.delete(0, tk.END)
    Folder4Var.insert(0, root.filename)
    
def Folder5Browser():
    if Folder5Var.get() != "" and os.path.exists(Folder5Var.get()):
        InitialDirectory = os.path.dirname(Folder5Var.get())
    else:
        InitialDirectory = "C:/"
    root.filename = filedialog.askdirectory(initialdir = InitialDirectory, title = "Browse")
    Folder5Var.delete(0, tk.END)
    Folder5Var.insert(0, root.filename)

def WakeIntervalToggle():
    if Wake.get():
        WakeIntervalText.grid(row = 24, column = 2, columnspan = 15, sticky = tk.E)
        WakeIntervalVar.grid(row = 24, column = 17, sticky = tk.W)
        WakeIntervalUnitsBox.grid(row = 24, column = 18, columnspan = 14, sticky = tk.W)
    else:
        WakeIntervalText.grid_forget()
        WakeIntervalVar.grid_forget()
        WakeIntervalUnitsBox.grid_forget()

if __name__ == "__main__":
    
    root = tk.Tk()
    root.title("Folder Update Checker")
    
    Title = tk.Label(root, text = "Folder Update Checker").grid(row = 0, column = 0, columnspan = 34)
    
    Spacer1 = tk.Label(root, text = "     ").grid(row = 10, column = 0)
    Spacer2 = tk.Label(root, text = "     ").grid(row = 20, column = 33)
    Spacer3 = tk.Label(root, text = "     ").grid(row = 30, column = 0)
    Spacer4 = tk.Label(root, text = "     ").grid(row = 40, column = 0)
    Spacer4 = tk.Label(root, text = "     ").grid(row = 50, column = 0)
    
    Folder1Text = tk.Label(root, text = "Folder 1:").grid(row = 11, column = 1)
    Folder1Var = tk.Entry(root, width = 90)
    Folder1Var.grid(row = 11, column = 2, columnspan = 30)
    Folder1Button = tk.Button(root, text = "Browse", command = Folder1Browser).grid(row = 11, column = 32)
    
    Folder2Text = tk.Label(root, text = "Folder 2:").grid(row = 12, column = 1)
    Folder2Var = tk.Entry(root, width = 90)
    Folder2Var.grid(row = 12, column = 2, columnspan = 30)
    Folder2Button = tk.Button(root, text = "Browse", command = Folder2Browser).grid(row = 12, column = 32)
    
    Folder3Text = tk.Label(root, text = "Folder 3:").grid(row = 13, column = 1)
    Folder3Var = tk.Entry(root, width = 90)
    Folder3Var.grid(row = 13, column = 2, columnspan = 30)
    Folder3Button = tk.Button(root, text = "Browse", command = Folder3Browser).grid(row = 13, column = 32)
    
    Folder4Text = tk.Label(root, text = "Folder 4:").grid(row = 14, column = 1)
    Folder4Var = tk.Entry(root, width = 90)
    Folder4Var.grid(row = 14, column = 2, columnspan = 30)
    Folder4Button = tk.Button(root, text = "Browse", command = Folder4Browser).grid(row = 14, column = 32)
    
    Folder5Text = tk.Label(root, text = "Folder 5:").grid(row = 15, column = 1)
    Folder5Var = tk.Entry(root, width = 90)
    Folder5Var.grid(row = 15, column = 2, columnspan = 30)
    Folder5Button = tk.Button(root, text = "Browse", command = Folder5Browser).grid(row = 15, column = 32)
    
    CheckIntervalText = tk.Label(root, text = "Check Interval:").grid(row = 21, column = 2, columnspan = 15, sticky = tk.E)
    CheckIntervalVar = tk.Entry(root, width = 3, justify = "center")
    CheckIntervalVar.insert(0, "60")
    CheckIntervalVar.grid(row = 21, column = 17, sticky = tk.W)
    CheckIntervalUnitsVar = tk.StringVar()
    CheckIntervalUnitsBox = ttk.Combobox(root, width = 7, textvariable = CheckIntervalUnitsVar, values = ["seconds", "minutes", "hours"])
    CheckIntervalUnitsBox.current(0)
    CheckIntervalUnitsBox.grid(row = 21, column = 18, columnspan = 14, sticky = tk.W)
    
    AlertText = tk.Label(root, text = "Alert:").grid(row = 22, column = 2, columnspan = 15, sticky = tk.E)
    AlertVar = tk.StringVar()
    AlertBox = ttk.Combobox(root, width = 18, textvariable = AlertVar, values = ["Beep on Change", "Beep on No Change", "No Alert"])
    AlertBox.current(0)
    AlertBox.grid(row = 22, column = 17, columnspan = 15, sticky = tk.W)
    
    WakeText = tk.Label(root, text = "Keep Awake:").grid(row = 23, column = 2, columnspan = 15, sticky = tk.E)
    Wake = tk.BooleanVar()
    WakeBox = tk.Checkbutton(root, var = Wake, onvalue = True, offvalue = False, command = WakeIntervalToggle)
    WakeBox.grid(row = 23, column = 17, columnspan = 15, sticky = tk.W)
    
    WakeIntervalText = tk.Label(root, text = "Wake Interval:")
    WakeIntervalVar = tk.Entry(root, width = 3, justify = "center")
    WakeIntervalVar.insert(0, "60")
    WakeIntervalUnitsVar = tk.StringVar()
    WakeIntervalUnitsBox = ttk.Combobox(root, width = 7, textvariable = WakeIntervalUnitsVar, values = ["seconds", "minutes", "hours"])
    WakeIntervalUnitsBox.current(0)
    
    WakeBox.select()
    WakeIntervalToggle()
    
    Text1_1 = tk.Label(root, text = "")
    Text1_1.grid(row = 31, column = 2, columnspan = 6)
    Text1_2 = tk.Label(root, text = "")
    Text1_2.grid(row = 32, column = 2, columnspan = 6)
    Text2_1 = tk.Label(root, text = "")
    Text2_1.grid(row = 31, column = 8, columnspan = 6)
    Text2_2 = tk.Label(root, text = "")
    Text2_2.grid(row = 32, column = 8, columnspan = 6)
    Text3_1 = tk.Label(root, text = "")
    Text3_1.grid(row = 31, column = 14, columnspan = 6)
    Text3_2 = tk.Label(root, text = "")
    Text3_2.grid(row = 32, column = 14, columnspan = 6)
    Text4_1 = tk.Label(root, text = "")
    Text4_1.grid(row = 31, column = 20, columnspan = 6)
    Text4_2 = tk.Label(root, text = "")
    Text4_2.grid(row = 32, column = 20, columnspan = 6)
    Text5_1 = tk.Label(root, text = "")
    Text5_1.grid(row = 31, column = 26, columnspan = 6)
    Text5_2 = tk.Label(root, text = "")
    Text5_2.grid(row = 32, column = 26, columnspan = 6)
    
    StartButton = tk.Button(root, text = "Start", command = Start)
    StartButton.grid(row = 41, column = 0, columnspan = 34)
    StopButton = tk.Button(root, text = "Stop", command = Stop)
    StopButton.grid(row = 42, column = 0, columnspan = 34)
    
    root.mainloop()