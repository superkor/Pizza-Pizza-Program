#January 7, 2018 - Checkout
#Created by Justin Chow and Mike Kim

#rev 1/10/19


import tkinter




class gooey:
    def __init__(self):

        f = open("data/order.txt", "r")
        fLines = f.readlines()
        f.close()

        self.window = tkinter.Tk()
        self.topFrame = tkinter.Frame()
        self.pizzaSpecs = tkinter.Frame()
        self.botFrame = tkinter.Frame()


        self.classicPizza = tkinter.Label(self.pizzaSpecs, text = "Base: Classic", font = ("Footlight MT Light", 15))
        self.csCrust = tkinter.Label(self.pizzaSpecs, text = "Base: Cheese-Stuffed Crust", font = ("Footlight MT Light", 15))
        self.thinPizza = tkinter.Label(self.pizzaSpecs, text = "Base: Thin Crust", font = ("Footlight MT Light", 15))
        self.stylePizza = tkinter.Label(self.pizzaSpecs, text = "Base: Sicilian Style", font = ("Footlight MT Light", 15))
        self.selectedToppings = tkinter.Label(self.pizzaSpecs, text ="Selected Toppings:", font = ("Footlight MT Light", 15, 'bold'))
        
        self.XLsize = tkinter.Label(self.pizzaSpecs, text = "Size: Extra Large", font = ("Footlight MT Light", 15))
        self.largeSize = tkinter.Label(self.pizzaSpecs, text = "Size: Large", font = ("Footlight MT Light", 15))
        self.mediumSize = tkinter.Label(self.pizzaSpecs, text = "Size: Medium", font = ("Footlight MT Light", 15))
        self.smallSize = tkinter.Label(self.pizzaSpecs, text = "Size: Small", font = ("Footlight MT Light", 15))
        
        self.toppingsTitle = tkinter.Label(self.pizzaSpecs, text = "Your Order:", font = ("Footlight MT Light", 18,'bold'))
        
        self.pepperoniSelection = tkinter.Label(self.botFrame, text = "Pepperoni", font = ("Footlight MT Light", 13))
        self.onionSelection = tkinter.Label(self.botFrame, text = "Onions", font = ("Footlight MT Light", 13))
        self.mushroomSelection = tkinter.Label(self.botFrame, text = "Mushroom", font = ("Footlight MT Light", 13))
        self.sausageSelection = tkinter.Label(self.botFrame, text = "Sausages", font = ("Footlight MT Light", 13))
        self.redPepperSelection = tkinter.Label(self.botFrame, text = "Red Pepper", font = ("Footlight MT Light", 13))
        self.greenPepperSelection = tkinter.Label(self.botFrame, text = "Green Pepper", font = ("Footlight MT Light", 13))
        self.baconSelection = tkinter.Label(self.botFrame, text = "Bacon", font = ("Footlight MT Light", 13))
        self.chickenSelection = tkinter.Label(self.botFrame, text = "Chicken", font = ("Footlight MT Light", 13))
        self.pineappleSelection = tkinter.Label(self.botFrame, text = "Pineapple", font = ("Footlight MT Light", 13))
        self.artichokeSelection = tkinter.Label(self.botFrame, text = "Artichoke", font = ("Footlight MT Light", 13))
        
        self.toppingsTitle.pack(side="top")
        
        
        base = fLines[0]

        if base == "Classic Pizza\n":
            cost = 7
            self.classicPizza.pack(side="top")
            
        elif base == "Cheese-Stuffed Crust\n": 
            cost = 8
            self.csCrust.pack(side="top")

        elif base == "Pizza Bagels\n":
            cost = 9
            self.bagel.pack(side="top")
            
        elif base == "Thin Crust\n":
            cost = 10
            self.thinPizza.pack(side="top")
            
        elif base == "Sicilian Style\n":
            cost = 12
            self.stylePizza.pack(side="top")

        self.selectedToppings.pack(side="bottom")

        size = fLines[1]

        if size == "Small\n":
            costMultiplier = 0.75
            self.smallSize.pack(side="bottom")
            
        elif size == "Medium\n":
            costMultiplier = 1
            self.mediumSize.pack(side="bottom")
            
        elif size == "Large\n":
            costMultiplier = 1.25
            self.largeSize.pack(side="bottom")

            
        elif size == "Extra Large\n":
            costMultiplier = 1.5
            self.XLsize.pack(side="bottom")

        toppingsPrice = 0

        pepperoni = fLines[2]
        if pepperoni == "1\n":
            toppingsPrice += 0.75
            self.pepperoniSelection.pack(side="top")

        onion = fLines[3]
        if onion == "1\n":
            toppingsPrice += 0.5
            self.onionSelection.pack(side="top")

        mushroom = fLines[4]
        if mushroom == "1\n":
            toppingsPrice += 0.5
            self.mushroomSelection.pack(side="top")

        sausage = fLines[5]
        if sausage == "1\n":
            toppingsPrice += 1
            self.sausageSelection.pack(side="top")
            
        redPepper = fLines[6]
        if redPepper == "1\n":
            toppingsPrice += .25
            self.redPepperSelection.pack(side="top")
            
        greenPepper = fLines[7]
        if greenPepper == "1\n":
            toppingsPrice += .25
            self.greenPepperSelection.pack(side="top")

        bacon = fLines[8]
        if bacon == "1\n":
            toppingsPrice += 1
            self.baconSelection.pack(side="top")

        chicken = fLines[9]
        if chicken == "1\n":
            toppingsPrice += 1
            self.chickenSelection.pack(side="top")

        pineapple = fLines[10]
        if pineapple == "1\n":
            toppingsPrice += 1
            self.pineappleSelection.pack(side="top")

        artichoke = fLines[11]
        if artichoke == "1\n":
            toppingsPrice += 0.75
            self.artichokeSelection.pack(side="top")

        

        totalCost = cost * costMultiplier + toppingsPrice
       
        self.window.title("Checkout")
        self.window.geometry("500x500")
        self.window.resizable(0,0)
        
        self.price = tkinter.Label(self.botFrame, text = "$" + str(format(totalCost, '.2f')), font = ("Verdana", 30), fg="red")


        self.price.pack(side="bottom")
    
        

        #Get image named "logo.gif" in pictures folder
##        logo = tkinter.PhotoImage(file="pictures/logo2.gif")

        #Create Label containing the image.
##        self.logo = tkinter.Label(self.topFrame, image = logo)
        self.titleName = tkinter.Label(self.topFrame, text = "Pizza Pizza Ordering Application", font = ("Verdana", 15))

  
        
        
##        self.logo.pack(side="top")
        self.titleName.pack(side="left")

        
        self.topFrame.pack()
        self.pizzaSpecs.pack()
        self.botFrame.pack()

        tkinter.mainloop()

gui = gooey()
