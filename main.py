import psutil

from pygame import mixer

from os import listdir

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

#“Sound effects obtained from https://www.zapsplat.com“

class MainWindow:
    def __init__(self,root):
        self.root=root
        root.geometry('230x170')
        nb = ttk.Notebook(root,padding=(5,5))
        nb.pack(expand=True,fill=BOTH)
        ###############################################################################

        frameGeneral=ttk.Frame(root,padding=(10,10))
        nb.add(frameGeneral, text="General")

        self.playMusic=IntVar()
        self.serverOn=IntVar()
        
        
        ttk.Checkbutton(frameGeneral,text='Play music when laptop \nis not charging', variable=self.playMusic).pack()

        ###############################################################################
        
        frameTime=ttk.Frame(root,padding=(10,10))
        nb.add(frameTime, text="Time")

        ttk.Label(frameTime,text='Check pc pugged every:').pack(expand=True)
        
        TimeValues=['5 seconds','30 seconds','1 minute']
        self.cbTime = ttk.Combobox(frameTime,state='readonly',values=TimeValues)
        self.cbTime.pack(expand=True)

        Button(frameTime,text='Apply',command=self.setInterval,width=10).pack()


        self.cbTime.set(TimeValues[0])#default value
        self.setInterval()
        ###############################################################################
        
        frameSound=ttk.Frame(root,padding=(10,10))
        nb.add(frameSound, text="Sound")

        ttk.Label(frameSound,text='Select Sound:').pack(expand=True)
        
        SoundValues=[f for f in listdir('sounds')]
        
        self.cbSound = ttk.Combobox(frameSound,state='readonly',values=SoundValues)
        self.cbSound.pack(expand=True)

        Button(frameSound,text='Apply',command=self.setSound,width=10).pack(side=LEFT)
        Button(frameSound,text='Test',command=self.testSound,width=10).pack(side=RIGHT)

        self.cbSound.set(SoundValues[1])#default value
        self.setSound()

        ###############################################################################
        nb.select(frameGeneral)
        nb.enable_traversal()
        
        self.update_clock()

        root.rowconfigure(0,weight=1)
        root.columnconfigure(0,weight=1)

    def update_clock(self):
        
        self.checkBattery=psutil.sensors_battery().power_plugged
        if self.checkBattery==False:

            if self.playMusic.get()==True:
                mixer.init()
                mixer.music.load('sounds/'+self.SoundName)
                mixer.music.play(-1)

                messagebox.showinfo("Warning", "PC plugged out")
                mixer.music.stop()
                
            
        self.root.after(self.Interval, self.update_clock)

    def setInterval(self):
        cbvalue=self.cbTime.get()

        if cbvalue=='5 seconds':
            self.Interval=5000
        elif cbvalue=='30 seconds':
            self.Interval=30000
        elif cbvalue=='1 minute':
            self.Interval=60000

    def setSound(self):
        self.SoundName=self.cbSound.get()

    def testSound(self):
        mixer.init()
        mixer.music.load('sounds/'+self.cbSound.get())
        mixer.music.play(1)



root=Tk()
MainWindow(root)
root.mainloop()
