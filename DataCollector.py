import shutil
import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox, filedialog
import os
import pyperclip
from threading import Timer
from time import sleep


class RepeatedTimer(object):
    def __init__(self, interval, function, *args, **kwargs):
        self._timer     = None
        self.interval   = interval
        self.function   = function
        self.args       = args
        self.kwargs     = kwargs
        self.is_running = False
        self.start()

    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False

def CreateWidgets():
    saveLabel = Label(root, text="Save Directory : ")
    saveLabel.grid(row=0, column=0,
                          pady=5, padx=5)

    root.destinationText = Entry(root, width=50,
                                 textvariable=destinationLocation)
    
    root.destinationText.insert('1',
                                defaultLocation)
    root.destinationText.grid(row=0, column=1,
                              pady=0, padx=0,
                              columnspan=2)

    dest_browseButton = Button(root, text="Browse",
                               command=DestinationBrowse, width=15)
    dest_browseButton.grid(row=0, column=4,
                           pady=5, padx=5)


    ###
    # Tier buttons
    ###
    tierLabel = Label(root, text="Tier : ")
    tierLabel.grid(row=1, column=0,
                          pady=5, padx=5)
    
    root.hptierButton = Button(root, text="Hp Tier",
                               command=lambda: ChangeStatHPTier("HpTier"), width=15)
    root.hptierButton.grid(row=1, column=1,
                           pady=5, padx=5)

    root.ForktierButton = Button(root, text="Fork Tier",
                               command=lambda: ChangeStatHPTier("ForkTier"), width=15)
    root.ForktierButton.grid(row=1, column=2,
                           pady=5, padx=5)
    
    root.HeartkelptierButton = Button(root, text="Heartkelp Tier",
                               command=lambda: ChangeStatHPTier("HeartkelpTier"), width=15)
    root.HeartkelptierButton.grid(row=1, column=3,
                           pady=5, padx=5)
    
    root.UmamitierButton = Button(root, text="Umami Tier",
                               command=lambda: ChangeStatHPTier("UmamiTier"), width=15)
    root.UmamitierButton.grid(row=1, column=4,
                           pady=5, padx=5)

    ###
    # Corpse buttons
    ###
    corpseLabel = Label(root, text="Corpse : ")
    corpseLabel.grid(row=4, column=0,
                          pady=5, padx=5)
    
    root.corpseMoneyButton = Button(root, text="Money on corpse",
                               command=lambda: ChangeStatHPTier("CorpseMoney"), width=15)
    root.corpseMoneyButton.grid(row=4, column=1,
                           pady=5, padx=5)
    
    ###
    # Total buttons
    ###
    totalLabel = Label(root, text="Total : ")
    totalLabel.grid(row=5, column=0,
                          pady=5, padx=5)
    
    root.totMoneyButton = Button(root, text="Total Money",
                               command=lambda: ChangeStatHPTier("totMoney"), width=15)
    root.totMoneyButton.grid(row=5, column=1,
                           pady=5, padx=5)
    
    root.totCrystButton = Button(root, text="Total Crystals",
                               command=lambda: ChangeStatHPTier("totCryst"), width=15)
    root.totCrystButton.grid(row=5, column=2,
                           pady=5, padx=5)
    
    root.DamageTakenButton = Button(root, text="Damage taken",
                               command=lambda: ChangeStatHPTier("DamageTaken"), width=15)
    root.DamageTakenButton.grid(row=5, column=3,
                           pady=5, padx=5)

    ###
    # Start buttons
    ###
    ReadFileButton = Button(root, text="Start", command=Start, width=15, bg="#00ff00")
    ReadFileButton.grid(row=6, column=0,
                           pady=5, padx=5, columnspan=5)
    

def GetSaveTxt(path):
    readFileRead = open(path, "r")
    read = readFileRead.readline()
    readFileRead.close()

    txt = read.split("assistTable")

    txt = txt[1].split("unlocks")
    assistTable = txt[0]
    txt = txt[1].split("progressData")
    unlocks = txt[0]
    txt = txt[1].split("inventoryData")
    progressData = txt[0]
    txt = txt[1].split("locationData")
    inventoryData = txt[0]
    txt = txt[1].split("storeData")
    locationData = txt[0]

    WriteSave("assistTable", assistTable)
    WriteSave("unlocks", unlocks)
    WriteSave("progressData", progressData)
    WriteSave("inventoryData", inventoryData)
    WriteSave("locationData", locationData)
    
def DestinationBrowse():
    estinationdirectory = filedialog.askopenfilename(initialdir="")
    WriteSavePath(estinationdirectory)
    fileName = os.path.basename(estinationdirectory)
    if fileName != "SaveFile_0.CRAB":
        messagebox.showinfo(title="Crab save", message="You need to put your save file")
    else:
        root.destinationText.delete(0, END)
        root.destinationText.insert(0, estinationdirectory)
        WriteSave1()

# Write the path in the savePath file
def WriteSavePath(message):
    writeFile = os.path.join(os.path.dirname(__file__), "savePath.txt")
    writeFileWrite = open(writeFile, "w")
    writeFileWrite.write('%s' % str(message))
    writeFileWrite.close()
    return

def WriteSave1():
    writeFile = os.path.join(os.path.dirname(__file__), "saveCopy.txt")
    with open(writeFile, "w") as out_file:        
        out_file.write('%s' % str(ReadSave()))
        out_file.close()
        return
    
def WriteSave(Type, saveTXT):
    writeFile = os.path.join(os.path.dirname(__file__), Type+".txt")
    with open(writeFile, "w") as out_file:
        out_file.write('%s' % str(saveTXT))
        out_file.close()
        return
    
def ReadSavePath():
    readFile = os.path.join(os.path.dirname(__file__), "savePath.txt")
    readFileRead = open(readFile, "r")
    read = readFileRead.readline()
    readFileRead.close()
    return read

def ReadSave():
    readFileRead = open(root.destinationText.get(), "r")
    read = readFileRead.readline()
    readFileRead.close()
    return read


def Start():    
    global rt 
    rt = RepeatedTimer(5, ReadFile)
    ReadFile()


def ReadFile():
    WriteSave1()
    GetSaveTxt(destinationLocation.get())
    try:
        GetSaveTxt(destinationLocation.get())
        WriteTier()
        Writetot()
    except:
        rt.stop()
        print("stoped")

def ChangeStatHPTier(button):
    match button:
        case "HpTier":
            pathFile = os.path.join(os.path.dirname(__file__),  "HpTier.txt")
            pyperclip.copy(pathFile)
        case "ForkTier":
            pathFile = os.path.join(os.path.dirname(__file__), "ForkTier.txt")
            pyperclip.copy(pathFile)
            pyperclip.copy(pathFile)
        case "HeartkelpTier":
            pathFile = os.path.join(os.path.dirname(__file__),"HeartkelpCapTier.txt")
            pyperclip.copy(pathFile)
            pyperclip.copy(pathFile)
        case "UmamiTier":
            pathFile = os.path.join(os.path.dirname(__file__),"umamiCapTier.txt")
            pyperclip.copy(pathFile)
            pyperclip.copy(pathFile)
        case "CorpseMoney":
            pathFile = os.path.join(os.path.dirname(__file__),"breadclips.txt")
            pyperclip.copy(pathFile)
            pyperclip.copy(pathFile)
        case "totMoney":
            pathFile = os.path.join(os.path.dirname(__file__),"clipsTotal.txt")
            pyperclip.copy(pathFile)
            pyperclip.copy(pathFile)
        case "totCryst":
            pathFile = os.path.join(os.path.dirname(__file__),"UmamiCrystalsTotal.txt")
            pyperclip.copy(pathFile)
            pyperclip.copy(pathFile)
        case "DamageTaken":
            pathFile = os.path.join(os.path.dirname(__file__),"totalDamageTaken.txt")
            pyperclip.copy(pathFile)

        
    messagebox.showinfo(title="Crab save", message="Path to the text file copied")

def GetTier():
    readFile = os.path.join(os.path.dirname(__file__), "inventoryData.txt")
    readFileRead = open(readFile, "r")
    read = readFileRead.readline()
    readFileRead.close()

    hpTier = read.split(r'hpTier\":')
    hpTier = int(float(hpTier[1][0]))

    forkTier = read.split(r'forkTier\":')
    forkTier = int(float(forkTier[1][0]))

    HeartkelpCapTier = read.split(r'HeartkelpCapTier\":')
    HeartkelpCapTier = int(float(HeartkelpCapTier[1][0]))
    
    umamiCapTier = read.split(r'umamiCapTier\":')
    umamiCapTier = int(float(umamiCapTier[1][0]))

    return hpTier, forkTier, HeartkelpCapTier, umamiCapTier


def GetTot():
    readFile = os.path.join(os.path.dirname(__file__), "locationData.txt")
    readFileRead = open(readFile, "r")
    read = readFileRead.readline()
    readFileRead.close()
    totDamage = read.split(r'totalDamageTaken\":')
    totDamage = totDamage[1].split(",")
    totDamage = int(float(totDamage[0]))

    clipsTotal = read.split(r'clipsTotal\":')
    clipsTotal = clipsTotal[1].split(",")
    clipsTotal = int(float(clipsTotal[0]))

    umamiTotal = read.split(r'UmamiCrystalsTotal\"')
    umamiTotal = umamiTotal[1].split(r'total\":')
    umamiTotal = umamiTotal[1].split("}")
    umamiTotal = int(float(umamiTotal[0]))

    corpseMoney = read.split(r'breadclips\":')
    corpseMoney = corpseMoney[1].split(",")
    corpseMoney = int(float(corpseMoney[0]))


    return totDamage, clipsTotal, umamiTotal, corpseMoney

def WriteData(Type, saveTXT):
    writeFile = os.path.join(os.path.dirname(__file__), Type+".txt")
    writeFileWrite = open(writeFile, "w")
    writeFileWrite.write('%s' % str(saveTXT))
    writeFileWrite.close()
    return


def WriteTier():
    tier = GetTier()
    WriteData("hpTier", tier[0])
    WriteData("forkTier", tier[1])
    WriteData("HeartkelpCapTier", tier[2])
    WriteData("umamiCapTier", tier[3])

def Writetot():
    tier = GetTot()
    WriteData("totalDamageTaken", tier[0])
    WriteData("clipsTotal", tier[1])
    WriteData("UmamiCrystalsTotal", tier[2])
    WriteData("breadclips", tier[3])
    

root = tk.Tk()
root.title('Another Crab\'s Creasure Save Manager')
root.geometry('')
root.iconbitmap('./Crab.ico')
root.resizable(False, False)

destinationLocation = StringVar()
defaultLocation = ReadSavePath()


CreateWidgets()

root.mainloop()

