#Decemeber 20, 2018 - Pizza Menu Version 3
#Created by Justin Chow and Mike Kim

import tkinter, tkinter.messagebox,os

class menu:
    def __init__(self):
        #Create window
        self.window = tkinter.Tk()

        #Set window title to Menu
        self.window.title("Menu")

        #Set window size to 500 pixels by 250 pixels
        self.window.geometry("500x250")

        #Set the Window to be non resizable (Can't be maximized or resized)
        self.window.resizable(0,0)

        #Create 5 frames
        self.title = tkinter.Frame(master=self.window)
        self.frame1 = tkinter.Frame(master=self.window)
        self.frame2 = tkinter.Frame(master=self.window)
        self.frame3 = tkinter.Frame(master=self.window)
        self.frame4 = tkinter.Frame(master=self.window)

        #Title ---------
        #Get image named "logo.gif" in pictures folder
        logo = tkinter.PhotoImage(file="pictures/logo.gif")

        #Create Label containing the image.
        self.logo = tkinter.Label(self.title, image = logo)

        #Create Label with text
        self.titleName = tkinter.Label(self.title, text = "Pizza Pizza Ordering Application")

        #--------

        #Create label
        self.label = tkinter.Label(self.frame1, text="Order your pizza:")

        #Pizza Base choices -------
        #Create String Variable
        self.pizzaBase = tkinter.StringVar()

        #List of all the pizza bases the user can choose
        pizza = ["Classic Pizza", "Cheese-Stuffed Crust", "Pizza Bagels","Sicilian Style","Thin Crust"]

        #Set default option for dropdown
        self.pizzaBase.set("Choose a pizza base")

        #Create Dropdown menu in frame2, with the default option (self.pizzaBase) and pizza base options (pizza)
        self.pizzaMenu = tkinter.OptionMenu(self.frame2, self.pizzaBase, *pizza)

        #Change the width and height of the drop down menu
        self.pizzaMenu.config(width=17, height =2)

        #--------

        #Pizza Size ---------
        self.pizzaSize = tkinter.StringVar()

        size = ["Small", "Medium", "Large", "Extra Large"]

        self.pizzaSize.set("Choose a pizza size")

        self.sizeMenu = tkinter.OptionMenu(self.frame2, self.pizzaSize, *size)

        self.sizeMenu.config(width=17, height = 2)

        #--------
        self.okButton = tkinter.Button(self.frame4, text="Ok", command = self.showPizza)
        self.Quit = tkinter.Button(self.frame4, text="Quit", command = self.window.destroy)

        #Pack
        self.title.pack()
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()
        self.titleName.pack(side='right')
        self.logo.pack(side='right')
        self.okButton.pack(side="left")
        self.Quit.pack(side="left")
        self.pizzaMenu.pack()
        self.sizeMenu.pack()

        self.label.pack()

        tkinter.mainloop()

    def showPizza(self):
        f = open("data/order.txt", "w+")

        base = self.pizzaBase.get()
        size = self.pizzaSize.get()

        if base == "Choose a pizza base" and size == "Choose a pizza size":
            tkinter.messagebox.showerror("Error", "You must choose a pizza base and size.")

        elif base == "Choose a pizza base":
            tkinter.messagebox.showerror("Error", "You must choose a pizza base.")

        elif size == "Choose a pizza size":
            tkinter.messagebox.showerror("Error", "You must choose a pizza size.")

        else:
            f.write(base+"\n"+size+"\n")
            f.close()
            self.window.destroy()

            #Open "toppings.py" file.
            os.system("toppings.py")

menu = menu()
