from Tkinter import *
# import time ## For timer ?
import Tkinter as tk
#import Tkinter.ttk as ttK

## ::----:: End Import ::----::
## ::----:: GUI Game Screen ::----::


## Creating GUI in one class (section)
class Application(Frame):


    ## ::--:: Create Widget Containers ::--::

    def __init__(self, master=None):

        Frame.__init__(self, master)
        
        ## ::--:: Window Attributes ::--::
        
        self.grid(sticky=N+S+E+W)
       # self.windowDivide() ## Incomplete - see notes.
       # self.gameWindow() ## Incomplete - see notes.

       
       ## ::--:: Menu Bar Icons ::--::
       
        self.fileDrop()
        self.helpDrop()
        self.viewDrop() ## contains simple, immediate screen changes ?
        

        ## ::--:: Game/Control Buttons/Items ::--::

        #self.timerZone() ## Incomeplete - see notes.
        self.startButton()
        self.resetButton()
        self.pauseButton()
        self.stopButton()



    ## ::----:: Widget code/screen structure ::----::
    ## This is where the widgets are coded/placed

        
    ## ::----:: Menu Code ::----::
            
    def fileDrop(self):
            
        self.mb = Menubutton(self, text="File", relief=RIDGE, font=("Arial", 10))
        self.mb.grid(row=0, column=0)
        self.mb.menu = Menu(self.mb, tearoff=1)
        self.mb["menu"] = self.mb.menu
        self.optionVar = IntVar()
        self.closeVar = IntVar()
        self.mb.menu.add_checkbutton(label="Options", variable=self.optionVar)
        self.mb.menu.add_command(label="Close", command=self.quit)


    def helpDrop(self):

        self.mb = Menubutton(self, text="Help", relief=RIDGE, font=("Arial", 10))
        self.mb.grid(row=0, column=1)
        self.mb.menu = Menu(self.mb, tearoff=1)
        self.mb["menu"] = self.mb.menu
        self.helpFileVar = IntVar()
        self.helpWikiVar = IntVar()
        self.creditVar = IntVar()
        self.mb.menu.add_checkbutton(label="Help File", variable=self.helpFileVar)
        self.mb.menu.add_checkbutton(label="Help Wiki", variable=self.helpWikiVar)
        self.mb.menu.add_checkbutton(label="Credits", variable=self.helpWikiVar)


    def viewDrop(self):

        self.mb = Menubutton(self, text="View", relief=RIDGE, font=("Arial", 10))
        self.mb.grid(row=0, column=2)
        self.mb.menu = Menu(self.mb, tearoff=1)
        self.mb["menu"] = self.mb.menu
        self.presetColourVar = IntVar()
        self.gridlinesVar = IntVar()
        self.mb.menu.add_checkbutton(label="Colours", variable=self.presetColourVar)
        self.mb.menu.add_checkbutton(label="Grid Lines", variable=self.gridlinesVar)

    ## ::----:: End Menu Code ::----::     
    ## ::----:: Game Window Code ::----::

    #def windowDivide(self):

      # m1 = PanedWindow():
       # m1.pack(fill=BOTH, expand=1)

       # top = Label(m1, text="top pane")

       

   # def gameWindow(self):

     #   self.gameWin = Toplevel(self, relief=FLAT)
     #   self.gameWin.grid(ipadx=6, ipady=6, sticky=CENTER)
        
        
    ## ::----:: End Game Window Code ::----::        
    ## ::----:: Button Code ::----::

    #def timerZone(self):

     #   curtime = ''
     #   clock = Tkinter.Label()
      #  clock.grid(row=6, column=5)

      #  def tick():
       #     global curtime
      #      newtime - time.strfttime('%H:%M:%S')
      #      if newtime != curtime:
       #         curtime = newtime
      #          clock.config(text=curtime)
      #      clock.after(200, tick)
      #  tick()

       
    def startButton(self):

        top=self.winfo_toplevel()
        top.rowconfigure(0, weight=1)
        top.columnconfigure(0, weight=1)
        self.rowconfigure(2, weight=1)
        self.columnconfigure(5, weight=1)
        self.start = Button(self, text="Start", relief=RAISED, font=("Arial", 10))
        self.start.grid(row=3, column=10, sticky=E)


    def resetButton(self):

        top=self.winfo_toplevel()
        top.rowconfigure(0, weight=1)
        top.columnconfigure(0, weight=1)
        self.rowconfigure(4, weight=1)
        self.columnconfigure(10, weight=1)
        self.reset = Button(self, text="Reset", relief=RAISED, font=("Arial", 10))
        self.reset.grid(row=4, column=10, sticky=E)


    def pauseButton(self):
        
        top=self.winfo_toplevel()
        top.rowconfigure(0, weight=1)
        top.columnconfigure(0, weight=1)
        self.rowconfigure(6, weight=1)
        self.columnconfigure(10, weight=1)
        self.pause = Button(self, text="Pause", relief=RAISED, font=("Arial", 10))
        self.pause.grid(row=5, column=10, sticky=E)


    def stopButton(self):

        top=self.winfo_toplevel()
        top.rowconfigure(0, weight=1)
        top.columnconfigure(0, weight=1)
        self.rowconfigure(8, weight=1)
        self.columnconfigure(10, weight=1)
        self.stop = Button(self, text="Stop", relief=RAISED, font=("Arial", 10))
        self.stop.grid(row=6, column=10, sticky=E)


    ## ::----:: Button Events ::----::
    ## ::--:: Controls ::--::

    #def (self, event):
        #if self.["background"] == "":
        #    self.["background"] = "red"
        #else:
        #    self.()

    ## ::----:: End Events ::----::

## ::----:: End GUI Screen ::----::    
## ::----:: GUI Run Script ::----::

## This prepares the program and runs it

## Sizes the tK window
root = tk.Tk()
root.geometry("1000x800+140+90")

app = Application()
app.master.title("Major Project - SDD. V.03")  ## This appears in the title bar
app.mainloop()

## ::----:: End Run Script ::----::
## ::----:: End Program ::----::
