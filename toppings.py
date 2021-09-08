import tkinter, tkinter.messagebox,os

class toppings:
    def __init__(self):

        self.window = tkinter.Tk()
        #Change Title of the window
        self.window.title("Toppings")
        #Change Window Size
        self.window.geometry("600x350")

        self.window.resizable(0,0)

        self.tframe = tkinter.Frame()
        self.rightFrame = tkinter.Frame()
        self.pictureFrameRight1 = tkinter.Frame()
        self.pictureFrameRight2 = tkinter.Frame()
        self.pictureFrameLeft1 = tkinter.Frame()
        self.pictureFrameLeft2 = tkinter.Frame()
        self.leftFrame = tkinter.Frame()
        self.bframe = tkinter.Frame()

        #Get image named "logo.gif" in pictures folder
        logo = tkinter.PhotoImage(file="pictures/logo.gif")

        #Create Label containing the image.
        self.logo = tkinter.Label(self.tframe, image = logo)

        #Create Label with text
        self.titleName = tkinter.Label(self.tframe, text = "Pizza Pizza Ordering Application")

        self.toppings = tkinter.Label(self.tframe, text = "Choose any toppings. Minimum 1 topping.")
        #Create variables
        self.selection1 = tkinter.IntVar()
        self.selection2 = tkinter.IntVar()
        self.selection3 = tkinter.IntVar()
        self.selection4 = tkinter.IntVar()
        self.selection5 = tkinter.IntVar()
        self.selection6 = tkinter.IntVar()
        self.selection7 = tkinter.IntVar()
        self.selection8 = tkinter.IntVar()
        self.selection9 = tkinter.IntVar()
        self.selection10 = tkinter.IntVar()

        #Set variables to 0
        self.selection1.set(0)
        self.selection2.set(0)
        self.selection3.set(0)
        self.selection4.set(0)
        self.selection5.set(0)
        self.selection6.set(0)
        self.selection7.set(0)
        self.selection8.set(0)
        self.selection9.set(0)
        self.selection10.set(0)

        #Create check buttons for all the toppings:
        self.pepperoni = tkinter.Checkbutton(self.leftFrame, text = "Pepperoni", variable = self.selection1)
        self.onion = tkinter.Checkbutton(self.leftFrame, text = "Onion", variable = self.selection2)
        self.mushroom = tkinter.Checkbutton(self.leftFrame, text = "Mushroom", variable = self.selection3)
        self.sausage = tkinter.Checkbutton(self.leftFrame, text = "Sausage", variable = self.selection4)
        self.redPeppers = tkinter.Checkbutton(self.leftFrame, text = "Red Peppers", variable = self.selection5)
        self.greenPeppers = tkinter.Checkbutton(self.rightFrame, text = "Green Peppers", variable = self.selection6)
        self.bacon = tkinter.Checkbutton(self.rightFrame, text = "Bacon", variable = self.selection7)
        self.chicken = tkinter.Checkbutton(self.rightFrame, text = "Chicken", variable = self.selection8)
        self.pineapple = tkinter.Checkbutton(self.rightFrame, text = "Pineapple", variable = self.selection9)
        self.artichoke = tkinter.Checkbutton(self.rightFrame, text = "Artichoke", variable = self.selection10)

        self.select = tkinter.Button(self.bframe, text = "Select Toppings", command = self.choice)

        #Create Images for each of the toppings:
        pepperoniPic = tkinter.PhotoImage(file="pictures/pepperoni.gif")
        onionPic = tkinter.PhotoImage(file="pictures/onion.gif")
        mushroomPic = tkinter.PhotoImage(file="pictures/mushroom.gif")
        sausagePic = tkinter.PhotoImage(file="pictures/sausage.gif")
        redPepperPic = tkinter.PhotoImage(file="pictures/redPepper.gif")
        greenPepperPic = tkinter.PhotoImage(file="pictures/greenPepper.gif")
        baconPic = tkinter.PhotoImage(file="pictures/bacon.gif")
        chickenPic = tkinter.PhotoImage(file="pictures/chicken.gif")
        pineapplePic = tkinter.PhotoImage(file="pictures/pineapple.gif")
        artichokePic = tkinter.PhotoImage(file="pictures/artichoke.gif")


        #Create labels with their respective images:
        self.pepperoniPic = tkinter.Label(self.pictureFrameLeft1, image = pepperoniPic)
        self.onionPic = tkinter.Label(self.pictureFrameLeft2, image = onionPic)
        self.mushroomPic = tkinter.Label(self.pictureFrameLeft1, image = mushroomPic)
        self.sausagePic = tkinter.Label(self.pictureFrameLeft2, image = sausagePic)
        self.redPepperPic = tkinter.Label(self.pictureFrameLeft1, image = redPepperPic)

        self.greenPepperPic = tkinter.Label(self.pictureFrameRight1, image = greenPepperPic)
        self.baconPic = tkinter.Label(self.pictureFrameRight2, image = baconPic)
        self.chickenPic = tkinter.Label(self.pictureFrameRight1, image = chickenPic)
        self.pineapplePic = tkinter.Label(self.pictureFrameRight2, image = pineapplePic)
        self.artichokePic = tkinter.Label(self.pictureFrameRight1, image = artichokePic)

        #Must pack and add functionality to these buttons:
        self.back = tkinter.Button(self.bframe, text = "Back", command = self.back)
        self.quit = tkinter.Button(self.bframe, text = "Quit", command = self.window.destroy)

        #Pack Frames:
        self.tframe.pack(side="top")

        self.pictureFrameRight1.pack(side="right")
        self.rightFrame.pack(side="right")
        self.pictureFrameRight2.pack(side="right")

        self.pictureFrameLeft1.pack(side="left")
        self.leftFrame.pack(side="left")
        self.pictureFrameLeft2.pack(side="left")

        self.bframe.pack(side="bottom")
        #---
        self.toppings.pack(side="bottom")
        self.pepperoni.pack()
        self.onion.pack()
        self.mushroom.pack()
        self.sausage.pack()
        self.redPeppers.pack()
        self.greenPeppers.pack()
        self.bacon.pack()
        self.chicken.pack()
        self.pineapple.pack()
        self.artichoke.pack()

        self.pepperoniPic.pack()
        self.onionPic.pack()
        self.mushroomPic.pack()
        self.sausagePic.pack()
        self.redPepperPic.pack()
        self.greenPepperPic.pack()
        self.baconPic.pack()
        self.chickenPic.pack()
        self.pineapplePic.pack()
        self.artichokePic.pack()

        self.back.pack(side="left")
        self.select.pack(side="left")
        self.quit.pack(side="left")

        self.titleName.pack(side='right')
        self.logo.pack(side='right')

        tkinter.mainloop()

    #Verify and save selection of toppings from user to the file:
    def choice(self):
        #Get what the user chose for their toppings:
        pepperoni = str(self.selection1.get())
        onion = str(self.selection2.get())
        mushroom = str(self.selection3.get())
        sausage = str(self.selection4.get())
        redPeppers = str(self.selection5.get())
        greenPeppers = str(self.selection6.get())
        bacon = str(self.selection7.get())
        chicken = str(self.selection8.get())
        pineapple = str(self.selection9.get())
        artichoke = str(self.selection10.get())

        #Verify.
        if pepperoni == '0' and onion == '0' and mushroom == '0' and sausage == '0' and redPeppers == '0' and \
        greenPeppers == '0' and bacon == '0' and chicken == '0' and pineapple == '0' and artichoke == '0':
            tkinter.messagebox.showerror("Error", "You have at least one choice of topping.")

        # :)
        if pepperoni == '0' and onion == '0' and mushroom == '0'and \
           sausage == '1' and redPeppers == '0' and greenPeppers == '0' and \
           bacon == '0' and chicken == '0' and pineapple == '1' and \
           artichoke == '1':
            tkinter.messagebox.showinfo("c", "WHAT IS A MAINFRAME COMPUTER?!?")
            f = open("data/order.txt", "a+")
            f.write(pepperoni+ "\n"+ onion+ "\n"+ mushroom+ "\n"+ sausage+ "\n"+ redPeppers+ "\n"+ greenPeppers+ "\n"+ bacon+ "\n"+ chicken+ "\n"+ pineapple+ "\n"+ artichoke+ "\n")
            f.close()
            self.window.destroy()
            os.system("checkout.py")

        #Take down what they choose.
        else:
            f = open("data/order.txt", "a+")
            f.write(pepperoni+ "\n"+ onion+ "\n"+ mushroom+ "\n"+ sausage+ "\n"+ redPeppers+ "\n"+ greenPeppers+ "\n"+ bacon+ "\n"+ chicken+ "\n"+ pineapple+ "\n"+ artichoke+ "\n")
            f.close()

            self.window.destroy()
            os.system("checkout.py")



    def back(self):
        self.window.destroy()

        #Open "menu.py" file.
        os.system("menu.py")


toppings = toppings()
