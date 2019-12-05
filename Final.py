from tkinter import*

def runme1(event):
    try:
      if (int(e1.get()) <= 49):  #converts the Entry box from a string to an int so it can be compared to other ints
        e11.insert(0, "1")
      elif (int(e1.get()) <=60 and int(e1.get()) >=50):
        e11.insert(0,"2")
      elif (int(e1.get()) <=71 and int(e1.get()) >=61):
        e11.insert(0,"3")
      elif (int(e1.get()) <=83 and int(e1.get()) >=72):
        e11.insert(0,"4")
      elif (int(e1.get()) <=92 and int(e1.get()) >=84):
        e11.insert(0,"6") 
      elif (int(e1.get()) <=96 and int(e1.get()) >93):
        e11.insert(0,"6")
      elif (int(e1.get()) >96 and int(e1.get()) <=100):
        e11.insert(0,"7")
      if (int(e1.get()) <=51):
        e111.insert(0, "1")
      elif (int(e1.get()) <=57 and int(e1.get()) >=52):
        e111.insert(0,"2")
      elif (int(e1.get()) <=66 and int(e1.get()) >=58):
        e111.insert(0,"3")
      elif (int(e1.get()) <=77 and int(e1.get()) >=67):
        e111.insert(0,"4")
      elif (int(e1.get()) <=86 and int(e1.get()) >=78):
        e111.insert(0,"6") 
      elif (int(e1.get()) <=93 and int(e1.get()) >=87):
        e111.insert(0,"6")
      elif (int(e1.get()) <=97 and int(e1.get()) >=94):
        e111.insert(0,"7")
      elif (int(e1.get()) >=98 and int(e1.get()) <=100):
        e111.insert(0,"8")
    except:
        l1 = Label(root,text="Use Numerical Whole Intergers only")  #if the user doesnt enter a str or a Boolean this message will show up on the screen 
        l1.pack()

    
  
#I have a series of functions. These functions actually convert the number

def runme2(event):
    try: 
      if (int(e2.get()) <= 49):
        e22.insert(0, "1")
      elif (int(e2.get()) <=60 and int(e2.get()) >=50):
        e22.insert(0,"2")
      elif (int(e2.get()) <=71 and int(e2.get()) >=61):
        e22.insert(0,"3")
      elif (int(e2.get()) <=83 and int(e2.get()) >=72):
        e22.insert(0,"4")
      elif (int(e2.get()) <=92 and int(e2.get()) >=84):
        e22.insert(0,"6") 
      elif (int(e2.get()) <=96 and int(e2.get()) >93):
        e22.insert(0,"6")
      elif (int(e2.get()) >96):
        e22.insert(0,"7")
      if (int(e2.get()) <= 51):
        e222.insert(0, "1")
      elif (int(e2.get()) <=57 and int(e2.get()) >=52):
        e222.insert(0,"2")
      elif (int(e2.get()) <=66 and int(e2.get()) >=58):
        e222.insert(0,"3")
      elif (int(e2.get()) <=77 and int(e2.get()) >=67):
        e222.insert(0,"4")
      elif (int(e2.get()) <=86 and int(e2.get()) >=78):
        e222.insert(0,"6") 
      elif (int(e2.get()) <=93 and int(e2.get()) >=87):
        e222.insert(0,"6")
      elif (int(e2.get()) <=97 and int(e2.get()) >=94):
        e222.insert(0,"7")
      elif (int(e2.get()) >=98 and int(e2.get()) <=100):
        e222.insert(0,"8")
    except:
        l1 = Label(root,text="Use Numerical Whole Intergers only")  #if the user doesnt enter a str or a Boolean this message will show up on the screen 
        l1.pack()


def runme3(event):
    try:
      if (int(e3.get()) <= 49):
        e33.insert(0, "1")
      elif (int(e3.get()) <=60 and int(e3.get()) >=50):
        e33.insert(0,"2")
      elif (int(e3.get()) <=71 and int(e3.get()) >=61):
        e33.insert(0,"3")
      elif (int(e3.get()) <=83 and int(e3.get()) >=72):
        e33.insert(0,"4")
      elif (int(e3.get()) <=92 and int(e3.get()) >=84):
        e33.insert(0,"6") 
      elif (int(e3.get()) <=96 and int(e3.get()) >93):
        e33.insert(0,"6")
      elif (int(e3.get()) >96):
        e33.insert(0,"7")
      if (int(e3.get()) <=51):
        e333.insert(0, "1")
      elif (int(e3.get()) <=57 and int(e3.get()) >=52):
        e333.insert(0,"2")
      elif (int(e3.get()) <=66 and int(e3.get()) >=58):
        e333.insert(0,"3")
      elif (int(e3.get()) <=77 and int(e3.get()) >=67):
        e333.insert(0,"4")
      elif (int(e3.get()) <=86 and int(e3.get()) >=78):
        e333.insert(0,"6") 
      elif (int(e3.get()) <=93 and int(e3.get()) >=87):
        e333.insert(0,"6")
      elif (int(e3.get()) <=97 and int(e3.get()) >=94):
        e333.insert(0,"7")
      elif (int(e3.get())>=98 and int(e3.get()) <=100):
        e333.insert(0,"8")
    except:
        l1 = Label(root,text="Use Numerical Whole Intergers only")  #if the user doesnt enter a str or a Boolean this message will show up on the screen 
        l1.pack()

def runme4(event):
    try:
      if (int(e4.get()) <= 49):
        e44.insert(0, "1")
      elif (int(e4.get()) <=60 and int(e4.get()) >=50):
        e44.insert(0,"2")
      elif (int(e4.get()) <=71 and int(e4.get()) >=61):
        e44.insert(0,"3")
      elif (int(e4.get()) <=83 and int(e4.get()) >=72):
        e44.insert(0,"4")
      elif (int(e4.get()) <=92 and int(e4.get()) >=84):
        e44.insert(0,"6") 
      elif (int(e4.get()) <=96 and int(e4.get()) >93):
        e44.insert(0,"6")
      elif (int(e4.get()) >96):
        e44.insert(0,"7")
      if (int(e4.get()) <=51):
        e444.insert(0, "1")
      elif (int(e4.get()) <=57 and int(e4.get()) >=52):
        e444.insert(0,"2")
      elif (int(e4.get()) <=66 and int(e4.get()) >=58):
        e444.insert(0,"3")
      elif (int(e4.get()) <=77 and int(e4.get()) >=67):
        e444.insert(0,"4")
      elif (int(e4.get()) <=86 and int(e4.get()) >=78):
        e444.insert(0,"6") 
      elif (int(e4.get()) <=93 and int(e4.get()) >=87):
        e444.insert(0,"6")
      elif (int(e4.get()) <=97 and int(e4.get()) >=94):
        e444.insert(0,"7")
      elif (int(e4.get())>=98 and int(e4.get()) <=100):
        e444.insert(0,"8")
    except:
        l1 = Label(root,text="Use Numerical Whole Intergers only")  #if the user doesnt enter a str or a Boolean this message will show up on the screen 
        l1.pack()

def runme5(event):
    try:
      if (int(e5.get()) <= 49):
        e55.insert(0, "1")
      elif (int(e5.get()) <=60 and int(e5.get()) >=50):
        e55.insert(0,"2")
      elif (int(e5.get()) <=71 and int(e5.get()) >=61):
        e55.insert(0,"3")
      elif (int(e5.get()) <=83 and int(e5.get()) >=72):
        e55.insert(0,"4")
      elif (int(e5.get()) <=92 and int(e5.get()) >=84):
        e55.insert(0,"6") 
      elif (int(e5.get()) <=96 and int(e5.get()) >93):
        e55.insert(0,"6")
      elif (int(e5.get()) >96):
        e55.insert(0,"7")
      if (int(e5.get()) <=51):
        e555.insert(0, "1")
      elif (int(e5.get()) <=57 and int(e5.get()) >=52):
        e555.insert(0,"2")
      elif (int(e5.get()) <=66 and int(e5.get()) >=58):
        e555.insert(0,"3")
      elif (int(e5.get()) <=77 and int(e5.get()) >=67):
        e555.insert(0,"4")
      elif (int(e5.get()) <=86 and int(e5.get()) >=78):
        e555.insert(0,"6") 
      elif (int(e5.get()) <=93 and int(e5.get()) >=87):
        e555.insert(0,"6")
      elif (int(e5.get()) <=97 and int(e5.get()) >=94):
        e555.insert(0,"7")
      elif (int(e5.get())>=98 and int(e5.get()) <=100):
        e555.insert(0,"8")
    except:
        l1 = Label(root,text="Use Numerical Whole Intergers only")  #if the user doesnt enter a str or a Boolean this message will show up on the screen 
        l1.pack()


def runme6(event):
    try:
      if (int(e6.get()) <= 49):
        e66.insert(0, "1")
      elif (int(e6.get()) <=60 and int(e6.get()) >=50):
        e66.insert(0,"2")
      elif (int(e6.get()) <=71 and int(e6.get()) >=61):
        e66.insert(0,"3")
      elif (int(e6.get()) <=83 and int(e6.get()) >=72):
        e66.insert(0,"4")
      elif (int(e6.get()) <=92 and int(e6.get()) >=84):
        e66.insert(0,"6") 
      elif (int(e6.get()) <=96 and int(e6.get()) >93):
        e66.insert(0,"6")
      elif (int(e6.get()) >96):
        e66.insert(0,"7")
      if (int(e6.get()) <=51):
        e666.insert(0, "1")
      elif (int(e6.get()) <=57 and int(e6.get()) >=52):
        e666.insert(0,"2")
      elif (int(e6.get()) <=66 and int(e6.get()) >=58):
        e666.insert(0,"3")
      elif (int(e6.get()) <=77 and int(e6.get()) >=67):
        e666.insert(0,"4")
      elif (int(e6.get()) <=86 and int(e6.get()) >=78):
        e666.insert(0,"6") 
      elif (int(e6.get()) <=93 and int(e6.get()) >=87):
        e666.insert(0,"6")
      elif (int(e6.get()) <=97 and int(e6.get()) >=94):
        e666.insert(0,"7")
      elif (int(e6.get())>=98 and int(e6.get()) <=100):
        e666.insert(0,"8")
    except:
        l1 = Label(root,text="Use Numerical Whole Intergers only")  #if the user doesnt enter a str or a Boolean this message will show up on the screen 
        l1.pack()

def runme11(event):
    try:
      if (int(e11.get())==1):
        e1.insert(0, "0-49")
      elif (int(e11.get()) ==2):
        e1.insert(0,"52-60")
      elif (int(e11.get()) ==3):
        e1.insert(0,"62-71")
      elif (int(e11.get()) ==4):
        e1.insert(0,"74-83")
      elif (int(e11.get()) ==5):
        e1.insert(0,"84-92") 
      elif (int(e11.get()) ==6):
        e1.insert(0,"93-96")
      elif (int(e11.get()) ==7):
        e1.insert(0,"97-100")
    except:
        l1 = Label(root,text="Use Numerical Whole Intergers only")  #if the user doesnt enter a str or a Boolean this message will show up on the screen 
        l1.pack()


#These functions covert it from the IB final to the percentage


def runme22(event):
    try:
      if (int(e22.get())==1):
        e2.insert(0, "0-49")
      elif (int(e22.get()) ==2):
        e2.insert(0,"52-60")
      elif (int(e22.get()) ==3):
        e2.insert(0,"62-71")
      elif (int(e22.get()) ==4):
        e2.insert(0,"74-83")
      elif (int(e22.get()) ==5):
        e2.insert(0,"84-92") 
      elif (int(e22.get()) ==6):
        e2.insert(0,"93-96")
      elif (int(e22.get()) ==7):
        e2.insert(0,"97-100")
    except:
        l1 = Label(root,text="Use Numerical Whole Intergers only")  #if the user doesnt enter a str or a Boolean this message will show up on the screen 
        l1.pack()


def runme33(event):
    try:
      if (int(e33.get())==1):
        e3.insert(0, "0-49")
      elif (int(e33.get()) ==2):
        e3.insert(0,"52-60")
      elif (int(e33.get()) ==3):
        e3.insert(0,"62-71")
      elif (int(e33.get()) ==4):
        e3.insert(0,"74-83")
      elif (int(e33.get()) ==5):
        e3.insert(0,"84-92") 
      elif (int(e33.get()) ==6):
        e3.insert(0,"93-96")
      elif (int(e33.get()) ==7):
        e3.insert(0,"97-100")
    except:
        l1 = Label(root,text="Use Numerical Whole Intergers only")  #if the user doesnt enter a str or a Boolean this message will show up on the screen 
        l1.pack()



def runme44(event):
    try:
      if (int(e44.get())==1):
        e4.insert(0, "0-49")
      elif (int(e44.get()) ==2):
        e4.insert(0,"52-60")
      elif (int(e44.get()) ==3):
        e4.insert(0,"62-71")
      elif (int(e44.get()) ==4):
        e4.insert(0,"74-83")
      elif (int(e44.get()) ==5):
        e4.insert(0,"84-92") 
      elif (int(e44.get()) ==6):
        e4.insert(0,"93-96")
      elif (int(e44.get()) ==7):
        e4.insert(0,"97-100")
    except:
        l1 = Label(root,text="Use Numerical Whole Intergers only")  #if the user doesnt enter a str or a Boolean this message will show up on the screen 
        l1.pack()


def runme55(event):
    try:
      if (int(e55.get())==1):
        e5.insert(0, "0-49")
      elif (int(e55.get()) ==2):
        e5.insert(0,"52-60")
      elif (int(e55.get()) ==3):
        e5.insert(0,"62-71")
      elif (int(e55.get()) ==4):
        e5.insert(0,"74-83")
      elif (int(e55.get()) ==5):
        e5.insert(0,"84-92") 
      elif (int(e55.get()) ==6):
        e5.insert(0,"93-96")
      elif (int(e55.get()) ==7):
        e5.insert(0,"97-100")
    except:
        l1 = Label(root,text="Use Numerical Whole Intergers only")  #if the user doesnt enter a str or a Boolean this message will show up on the screen 
        l1.pack()


def runme66(event):
    try:
      if (int(e66.get())==1):
        e6.insert(0, "0-49")
      elif (int(e66.get()) ==2):
        e6.insert(0,"52-60")
      elif (int(e66.get()) ==3):
        e6.insert(0,"62-71")
      elif (int(e66.get()) ==4):
        e6.insert(0,"74-83")
      elif (int(e66.get()) ==5):
        e6.insert(0,"84-92") 
      elif (int(e66.get()) ==6):
        e6.insert(0,"93-96")
      elif (int(e66.get()) ==7):
        e6.insert(0,"97-100")
    except:
        l1 = Label(root,text="Use Numerical Whole Intergers only")  #if the user doesnt enter a str or a Boolean this message will show up on the screen 
        l1.pack()


def runme111(event):
    try:
      if (int(e111.get())==1):
        e1.insert(0, "49")
      elif (int(e111.get()) ==2):
        e1.insert(0,"57")
      elif (int(e111.get()) ==3):
        e1.insert(0,"66")
      elif (int(e111.get()) ==4):
        e1.insert(0,"77")
      elif (int(e111.get()) ==5):
        e1.insert(0,"86") 
      elif (int(e111.get()) ==6):
        e1.insert(0,"93")
      elif (int(e111.get()) ==7):
        e1.insert(0,"97")
      elif (int(e111.get()) ==8):
        e1.insert(0,"100")
    except:
        l1 = Label(root,text="Use Numerical Whole Intergers only")  #if the user doesnt enter a str or a Boolean this message will show up on the screen 
        l1.pack()


#The convert to percentage from IB summatives



def runme222(event):
    try:
      if (int(e222.get())==1):
        e2.insert(0, "49")
      elif (int(e222.get()) ==2):
        e2.insert(0,"57")
      elif (int(e222.get()) ==3):
        e2.insert(0,"66")
      elif (int(e222.get()) ==4):
        e2.insert(0,"77")
      elif (int(e222.get()) ==5):
        e2.insert(0,"86") 
      elif (int(e222.get()) ==6):
        e2.insert(0,"93")
      elif (int(e222.get()) ==7):
        e2.insert(0,"97")
      elif (int(e222.get()) ==8):
        e2.insert(0,"100")
    except:
        l1 = Label(root,text="Use Numerical Whole Intergers only")  #if the user doesnt enter a str or a Boolean this message will show up on the screen 
        l1.pack()


def runme333(event):
    try:
      if (int(e333.get())==1):
        e3.insert(0, "49")
      elif (int(e333.get()) ==2):
        e3.insert(0,"57")
      elif (int(e333.get()) ==3):
        e3.insert(0,"66")
      elif (int(e333.get()) ==4):
        e3.insert(0,"77")
      elif (int(e333.get()) ==5):
        e3.insert(0,"86") 
      elif (int(e333.get()) ==6):
        e3.insert(0,"93")
      elif (int(e333.get()) ==7):
        e3.insert(0,"97")
      elif (int(e333.get()) ==8):
        e3.insert(0,"100")
    except:
        l1 = Label(root,text="Use Numerical Whole Intergers only")  #if the user doesnt enter a str or a Boolean this message will show up on the screen 
        l1.pack()

def runme444(event):
    try:
      if (int(e444.get())==1):
        e4.insert(0, "49")
      elif (int(e444.get()) ==2):
        e4.insert(0,"57")
      elif (int(e444.get()) ==3):
        e4.insert(0,"66")
      elif (int(e444.get()) ==4):
        e4.insert(0,"77")
      elif (int(e444.get()) ==5):
        e4.insert(0,"86") 
      elif (int(e444.get()) ==6):
        e4.insert(0,"93")
      elif (int(e444.get()) ==7):
        e4.insert(0,"97")
      elif (int(e444.get()) ==8):
        e4.insert(0,"100")
    except:
        l1 = Label(root,text="Use Numerical Whole Intergers only")  #if the user doesnt enter a str or a Boolean this message will show up on the screen 
        l1.pack()

def runme555(event):
    try:
      if (int(e555.get())==1):
        e5.insert(0, "49")
      elif (int(e555.get()) ==2):
        e5.insert(0,"57")
      elif (int(e555.get()) ==3):
        e5.insert(0,"66")
      elif (int(e555.get()) ==4):
        e5.insert(0,"77")
      elif (int(e555.get()) ==5):
        e5.insert(0,"86") 
      elif (int(e555.get()) ==6):
        e5.insert(0,"93")
      elif (int(e555.get()) ==7):
        e5.insert(0,"97")
      elif (int(e555.get()) ==8):
        e5.insert(0,"100")
    except:
        l1 = Label(root,text="Use Numerical Whole Intergers only")  #if the user doesnt enter a str or a Boolean this message will show up on the screen 
        l1.pack()


def runme666(event):
    try:
      if (int(e666.get())==1):
        e6.insert(0, "49")
      elif (int(e666.get()) ==2):
        e6.insert(0,"57")
      elif (int(e666.get()) ==3):
        e6.insert(0,"66")
      elif (int(e666.get()) ==4):
        e6.insert(0,"77")
      elif (int(e666.get()) ==5):
        e6.insert(0,"86") 
      elif (int(e666.get()) ==6):
        e6.insert(0,"93")
      elif (int(e666.get()) ==7):
        e6.insert(0,"97")
      elif (int(e666.get()) ==8):
        e6.insert(0,"100")
    except:
        l1 = Label(root,text="Use Numerical Whole Intergers only")  #if the user doesnt enter a str or a Boolean this message will show up on the screen 
        l1.pack()









def e1_delete():
    e1.delete(first=0,last=100) #it will clear the digits from  the 0 spot to the 100th spot
    e2.delete(first=0,last=100)
    e3.delete(first=0,last=100)
    e4.delete(first=0,last=100)
    e5.delete(first=0,last=100)
    e6.delete(first=0,last=100)
    e11.delete(first=0,last=100)
    e22.delete(first=0,last=100)
    e33.delete(first=0,last=100)
    e44.delete(first=0,last=100)
    e55.delete(first=0,last=100)
    e66.delete(first=0,last=100)
    e111.delete(first=0,last=100)
    e222.delete(first=0,last=100)
    e333.delete(first=0,last=100)
    e444.delete(first=0,last=100)
    e555.delete(first=0,last=100)
    e666.delete(first=0,last=100)


#this clears all the input boxes so instead of individually clearing the boxes you can clear them all at once



def write_slogan():
    l1 = Label(root,text="Enter a Number in any of the boxes and press")
    l1.pack()
    l2 = Label(root,text="the enter key to convert the numbers)")
    l2.pack()

# this shows the instructions of my window
# it is broken into two because as one it cant fit on the window unless it is expanded however I want my window to work when its vertical


def test(event):
    root.geometry("2000x2000") #makes the window fullscreen

root=Tk()                     # this is my window 
root.title("IB converter")
root.geometry("300x800")

topframe = Frame(root,bg='blue',height='20')  #creates the topbar of the Window
topframe.pack(fill=X) # make as wide as root
can1 = Canvas(topframe,height='20',width='20',bg="blue",highlightthickness=0)
can1.create_line(0, 5, 20, 5,fill='white')
can1.create_line(0, 10, 20, 10,fill='white')
can1.create_line(0, 15, 20, 15,fill='white')
can1.bind("<Button-1>",test ) # keyword 
can1.pack(side=LEFT, padx=5, pady=5)

myframe = Frame(root) #the frame on the window
myframe.pack()

button = Button(myframe,               #this button closes the window
                   text="QUIT", 
                   fg="red",
                   command=quit)
button.pack(side=LEFT)



slogan = Button(myframe,                      #this button prints the instructions
                   text="Instuctions",
                   fg="Blue",
                   command=write_slogan)
slogan.pack(side=LEFT)


B=Button(root,text="Clear All", command=e1_delete)        #this button uses the clear screen function above
B.pack()




l1 = Label(root,text="Enter Standard Mark (Percentage)")
l1.pack()

e1 = Entry(root)
e1.bind('<Return>',runme1)
e1.pack()

e2 = Entry(root)
e2.bind('<Return>',runme2)
e2.pack()

e3 = Entry(root)
e3.bind('<Return>',runme3)
e3.pack()

e4 = Entry(root)
e4.bind('<Return>',runme4)
e4.pack()

e5 = Entry(root)
e5.bind('<Return>',runme5)
e5.pack()

e6 = Entry(root)
e6.bind('<Return>',runme6)
e6.pack()

l2 = Label(root,text="IB Final (out of 7)")
l2.pack()

e11 = Entry(root)
e11.bind('<Return>',runme11)
e11.pack()

e22 = Entry(root)
e22.bind('<Return>',runme22)
e22.pack()

e33 = Entry(root)
e33.bind('<Return>',runme33)
e33.pack()

e44 = Entry(root)
e44.bind('<Return>',runme44)
e44.pack()

e55 = Entry(root)
e55.bind('<Return>',runme55)
e55.pack()

e66 = Entry(root)
e66.bind('<Return>',runme66)
e66.pack()

l3 = Label(root,text="IB Summatives (out of 8)")
l3.pack()

e111 = Entry(root)
e111.bind('<Return>',runme111)
e111.pack()

e222 = Entry(root)
e222.bind('<Return>',runme222)
e222.pack()

e333 = Entry(root)
e333.bind('<Return>',runme333)
e333.pack()

e444 = Entry(root)
e444.bind('<Return>',runme444)
e444.pack()

e555 = Entry(root)
e555.bind('<Return>',runme555)
e555.pack()

e666 = Entry(root)
e666.bind('<Return>',runme666)
e666.pack()


root.mainloop() #my loop for the code to keep rnning so my code doesnt close right away















