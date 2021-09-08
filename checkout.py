import tkinter

f = open("data/order.txt", "r")
fLines = f.readlines()
f.close()


base = fLines[0]

if base == "Classic Pizza\n":
    cost = 7
elif base == "Cheese-Stuffed Crust\n" or "Pizza Bagels\n":
    cost = 8
elif  base == "Thin Crust\n":
    cost = 10
elif base == "Sicilian Style\n":
    cost = 12

size = fLines[1]

if size == "Small\n":
    costMultiplier = 0.75
elif size == "Medium\n":
    costMultiplier = 1
elif size == "Large\n":
    costMultiplier = 1.25
elif size == "Extra Large\n":
    costMultiplier = 1.5

toppingsPrice = 0

pepperoni = fLines[2]
if pepperoni == "1\n":
    toppingsPrice += 0.75
    pepperoniSelection = "yes"


onion = fLines[3]
if onion == "1\n":
    toppingsPrice += 0.5
    onionSelection = "yes"

mushroom = fLines[4]
if mushroom == "1\n":
    toppingsPrice += 0.5
    mushroomSelection = "yes"

sausage = fLines[5]
if sausage == "1\n":
    toppingsPrice += 1
    sausageSelection = "yes"

redPepper = fLines[6]
if redPepper == "1\n":
    toppingsPrice += .25
    redPepperSelection = "yes"

greenPepper = fLines[7]
if greenPepper == "1\n":
    toppingsPrice += .25
    greenPepperSelection = "yes"

bacon = fLines[8]
if bacon == "1\n":
    toppingsPrice += 1
    baconSelection = "yes"

chicken = fLines[9]
if chicken == "1\n":
    toppingsPrice += 1
    chickenSelection = "yes"

pineapple = fLines[10]
if pineapple == "1\n":
    toppingsPrice += 1
    pineappleSelection = "yes"

artichoke = fLines[11]
if artichoke == "1\n":
    toppingsPrice += 0.75
    artichokeSelection = "yes"

totalCost = cost * costMultiplier + toppingsPrice


class gooey:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title("Checkout")
        self.window.geometry("500x250")
        self.window.resizable(0,0)

        self.topFrame = tkinter.Frame()
        self.botFrame = tkinter.Frame()

        #Get image named "logo.gif" in pictures folder
        logo = tkinter.PhotoImage(file="pictures/logo.gif")

        #Create Label containing the image.
        self.logo = tkinter.Label(self.topFrame, image = logo)
        self.titleName = tkinter.Label(self.topFrame, text = "Pizza Pizza Ordering Application")

        self.label1 = tkinter.Label(self.botFrame, text = totalCost)
        self.label2 = tkinter.Label(self.botFrame)

        self.label1.pack()
        self.label2.pack()
        self.logo.pack(side="left")
        self.titleName.pack(side="left")
        self.topFrame.pack()
        self.botFrame.pack()

        tkinter.mainloop()

gui = gooey()
