from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import time
import random

characters = ["Basil", "Bill", "Brian", "Edna", "Gary", "Hannah", "Ian", "Isla", "Jennifer", "Joshua", "Kelly", "Kim",
              "Maggie", "Martine", "Melvin", "Mo", "Natalie", "Pete", "Roy", "Rupert", "Simone", "Stephen", "Susan", "Xiao Mei"]

class Attributes():
    def __init__(self):
        self.hair_colour = None
        self.eye_colour = None
        self.clothes = None
        self.glasses = None
        self.gender = None
        self.characters = ["Basil", "Bill", "Brian", "Edna", "Gary", "Hannah", "Ian", "Isla", "Jennifer", "Joshua", "Kelly", "Kim",
              "Maggie", "Martine", "Melvin", "Mo", "Natalie", "Pete", "Roy", "Rupert", "Simone", "Stephen", "Susan", "Xiao Mei"]
        self.pick_no = random.randint(0, 23)
        self.pick = self.characters[self.pick_no]

    
    def set_attributes(self):
        lst = class_list[self.pick_no]
        self.hair_colour = lst[0]
        self.eye_colour = lst[1]
        self.clothes = lst[2]
        self.glasses = lst[3]
        self.gender = lst[4]
        


##attributes for each of the guesses

class_list = [["Dark Brown", "Dark", "Blue", "No", "Male"], #Basil
    ["Brown", "Brown", "Blue and White", "No", "Male"], #Bill
    ["Brown", "Blue", "Green and White", "Yes", "Male"], #Brian
    ["Grey", "Green", "Green and White", "Yes", "Female"], #Edna
    ["Brown", "Green", "Blue", "No", "Male"], #Gary
    ["Brown", "Dark", "Grey", "No", "Female"], #Hannah
    ["Grey", "Brown", "Purple and White", "Yes", "Male"], #Ian
    ["Orange", "Green", "Purple and White", "No", "Female"], #Isla
    ["Brown", "Dark", "Blue", "No", "Female"], #Jennifer
    ["Brown", "Dark", "Blue", "No", "Male"], #Joshua
    ["Blonde", "Green", "Orange", "No", "Female"], #Kelly
    ["Brown", "Brown", "Grey and White", "Yes", "Female"], #Kim
    ["Brown", "Dark", "Blue", "No", "Female"], #Maggie
    ["Brown", "Dark", "Grey", "No", "Female"], #Martine
    ["Light Brown", "Dark", "Grey and White", "Yes", "Male"], #Melvin
    ["Dark Brown", "Dark", "White", "No", "Male"], #Mo
    ["Blonde", "Green", "Blue", "No", "Female"], #Natalie
    ["Brown", "Brown", "Grey", "No", "Male"], #Pete
    ["Brown", "Dark", "Purple and White", "Yes", "Male"], #Roy
    ["Brown", "Green", "Blue and White", "Yes", "Male"], #Rupert
    ["Brown", "Green", "Yellow", "No", "Female"], #Simone
    ["Dark Brown", "Dark", "Yellow", "No", "Male"], #Stephen
    ["Dark Brown", "Dark", "Purple", "No", "Female"], #Susan
    ["Dark Brown", "Dark", "Green", "No", "Female"]] #Xiao Mei


#Body of
class GUI(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master, bg = "light blue")
        self.master = master
        self.buttons()
        self.GuessList()
        self.lifecounter()

    def buttons(self):
        self.buttonframe = Frame(self, bg= "lightblue")
        self.buttonframe.pack()

        self.rupert_image = PhotoImage(file="lib//characters//rupert.png")
        self.rupert = Button(self.buttonframe, image=self.rupert_image, command=lambda: [chosen_names.append("Rupert"), self.click()])
        self.rupert.grid(row=1,column=0)

        self.susan_image = PhotoImage(file="lib//characters//susan.png")
        self.susan = Button(self.buttonframe,image=self.susan_image, command=lambda: [chosen_names.append("Susan"), self.click()])
        self.susan.grid(row=1, column=1)

        self.kim_image = PhotoImage(file="lib//characters//kim.png")
        self.kim = Button(self.buttonframe,image=self.kim_image, command=lambda: [chosen_names.append("Kim"), self.click()])
        self.kim.grid(row=1, column=2)

        self.stephen_image = PhotoImage(file="lib//characters//stephen.png")
        self.stephen = Button(self.buttonframe,image=self.stephen_image, command=lambda: [chosen_names.append("Stephen"), self.click()])
        self.stephen.grid(row=1, column=3)

        self.hannah_image = PhotoImage(file="lib//characters//hannah.png")
        self.hanna = Button(self.buttonframe,image=self.hannah_image, command=lambda: [chosen_names.append("Hannah"), self.click()])
        self.hanna.grid(row=1, column=4)

        self.bill_image = PhotoImage(file="lib//characters//bill.png")
        self.bill = Button(self.buttonframe,image=self.bill_image, command=lambda: [chosen_names.append("Bill"), self.click()])
        self.bill.grid(row=1, column=5)

        self.martine_image = PhotoImage(file="lib//characters//martine.png")
        self.martine = Button(self.buttonframe,image=self.martine_image, command=lambda: [chosen_names.append("Martine"), self.click()])
        self.martine.grid(row=2, column=0)

        self.edna_image = PhotoImage(file="lib//characters//edna.png")
        self.edna = Button(self.buttonframe,image=self.edna_image, command=lambda: [chosen_names.append("Edna"), self.click()])
        self.edna.grid(row=2, column=1)

        self.brian_image = PhotoImage(file="lib//characters//brian.png")
        self.brian = Button(self.buttonframe,image=self.brian_image, command=lambda: [chosen_names.append("Brian"), self.click()])
        self.brian.grid(row=2, column=2)

        self.maggie_image = PhotoImage(file="lib//characters//maggie.png")
        self.maggie = Button(self.buttonframe,image=self.maggie_image, command=lambda: [chosen_names.append("Maggie"), self.click()])
        self.maggie.grid(row=2, column=3)

        self.gary_image = PhotoImage(file="lib//characters//gary.png")
        self.gary = Button(self.buttonframe,image=self.gary_image, command=lambda: [chosen_names.append("Gary"), self.click()])
        self.gary.grid(row=2, column=4)

        self.roy_image = PhotoImage(file="lib//characters//roy.png")
        self.roy = Button(self.buttonframe,image=self.roy_image, command=lambda: [chosen_names.append("Roy"), self.click()])
        self.roy.grid(row=2, column=5)

        self.jennifer_image = PhotoImage(file="lib//characters//jennifer.png")
        self.jennifer = Button(self.buttonframe,image=self.jennifer_image, command=lambda: [chosen_names.append("Jennifer"), self.click()])
        self.jennifer.grid(row=3, column=0)

        self.xiao_mei_image = PhotoImage(file="lib//characters//xiao_mei.png")
        self.xiao_mei = Button(self.buttonframe,image=self.xiao_mei_image, command=lambda: [chosen_names.append("Xiao Mei"), self.click()])
        self.xiao_mei.grid(row=3, column=1)

        self.basil_image = PhotoImage(file="lib//characters//basil.png")
        self.basil = Button(self.buttonframe,image=self.basil_image, command=lambda: [chosen_names.append("Basil"), self.click()])
        self.basil.grid(row=3, column=2)

        self.mo_image = PhotoImage(file="lib//characters//mo.png")
        self.mo = Button(self.buttonframe,image=self.mo_image, command=lambda: [chosen_names.append("Mo"), self.click()])
        self.mo.grid(row=3, column=3)

        self.joshua_image = PhotoImage(file="lib//characters//joshua.png")
        self.joshua = Button(self.buttonframe,image=self.joshua_image, command=lambda: [chosen_names.append("Joshua"), self.click()])
        self.joshua.grid(row=3, column=4)

        self.melvin_image = PhotoImage(file="lib//characters//melvin.png")
        self.melvin = Button(self.buttonframe,image=self.melvin_image, command=lambda: [chosen_names.append("Melvin"), self.click()])
        self.melvin.grid(row=3, column=5)

        self.isla_image = PhotoImage(file="lib//characters//isla.png")
        self.isla = Button(self.buttonframe,image=self.isla_image, command=lambda: [chosen_names.append("Isla"), self.click()])
        self.isla.grid(row=4, column=0)

        self.natalie_image = PhotoImage(file="lib//characters//natalie.png")
        self.natalie = Button(self.buttonframe,image=self.natalie_image, command=lambda: [chosen_names.append("Natalie"), self.click()])
        self.natalie.grid(row=4, column=1)

        self.simone_image = PhotoImage(file="lib//characters//simone.png")
        self.simone = Button(self.buttonframe,image=self.simone_image, command=lambda: [chosen_names.append("Simone"), self.click()])
        self.simone.grid(row=4, column=2)

        self.kelly_image = PhotoImage(file="lib//characters//kelly.png")
        self.kelly = Button(self.buttonframe,image=self.kelly_image, command=lambda: [chosen_names.append("Kelly"), self.click()])
        self.kelly.grid(row=4, column=3)

        self.ian_image = PhotoImage(file="lib//characters//ian.png")
        self.ian = Button(self.buttonframe,image=self.ian_image, command=lambda: [chosen_names.append("Ian"), self.click()])
        self.ian.grid(row=4, column=4)

        self.pete_image = PhotoImage(file="lib//characters//pete.png")
        self.pete = Button(self.buttonframe,image=self.pete_image, command=lambda: [chosen_names.append("Pete"), self.click()])
        self.pete.grid(row=4, column=5)

        self.hint_title = Label(self.buttonframe, text="Hints", height=2, width=10,
                                font=("Calibri", 21), bg="light green", borderwidth=2, relief=SOLID)
        self.hint_title.grid(row =6, column=0, rowspan=2)

        #hint labels
        self.hair_title = Label(self.buttonframe, text="Hair colour", height=1, width=10,
                                font=("Calibri", 20), bg="light green", borderwidth=2, relief=SOLID)
        self.hair_title.grid(row =6, column=1, rowspan=1)

        self.eye_title = Label(self.buttonframe, text="Eye colour", height=1, width=10,
                                font=("Calibri", 20), bg="light green", borderwidth=2, relief=SOLID)
        self.eye_title.grid(row =6, column=2, rowspan=1)

        self.clothes_title = Label(self.buttonframe, text="Clothes", height=1, width=10,
                                font=("Calibri", 20), bg="light green", borderwidth=2, relief=SOLID)
        self.clothes_title.grid(row =6, column=3, rowspan=1)

        self.glasses_title = Label(self.buttonframe, text="Glasses?", height=1, width=10,
                                font=("Calibri", 20), bg="light green", borderwidth=2, relief=SOLID)
        self.glasses_title.grid(row =6, column=4, rowspan=1)

        self.gender_title = Label(self.buttonframe, text="Gender", height=1, width=10,
                                font=("Calibri", 20), bg="light green", borderwidth=2, relief=SOLID)
        self.gender_title.grid(row =6, column=5, rowspan=1)
    
        #textvariables
        self.hair_title = Label(self.buttonframe, textvariable=hair_variable, height=1, width=10,
                                font=("Calibri", 20), bg="light green", borderwidth=2, relief=SOLID)
        self.hair_title.grid(row =7, column=1, rowspan=1)

        self.eye_title = Label(self.buttonframe, textvariable=eyes_variable, height=1, width=10,
                                font=("Calibri", 20), bg="light green", borderwidth=2, relief=SOLID)
        self.eye_title.grid(row =7, column=2, rowspan=1)

        self.clothes_title = Label(self.buttonframe, textvariable=clothes_variable, height=1, width=10,
                                font=("Calibri", 20), bg="light green", borderwidth=2, relief=SOLID)
        self.clothes_title.grid(row =7, column=3, rowspan=1)

        self.glasses_title = Label(self.buttonframe, textvariable=glasses_variable, height=1, width=10,
                                font=("Calibri", 20), bg="light green", borderwidth=2, relief=SOLID)
        self.glasses_title.grid(row =7, column=4, rowspan=1)

        self.gender_title = Label(self.buttonframe, textvariable=gender_variable, height=1, width=10,
                                font=("Calibri", 20), bg="light green", borderwidth=2, relief=SOLID)
        self.gender_title.grid(row =7, column=5, rowspan=1)

    

    def GuessList(self):
        self.guess_title = Label(self.buttonframe, text="You have\nguessed:",height=2, width=12,
                                font=("Calibri", 25),bg = "light green", borderwidth=2, relief=SOLID)
        self.guess_title.grid(row=1, column=7, rowspan=1, columnspan=2)

        self.guess_list = Label(self.buttonframe, textvariable=String_chosen_names, height=8, width=12,
                                font=("Calibri", 25),bg = "light green", borderwidth=2, relief=SOLID)
        self.guess_list.grid(row=2, column=7, rowspan=2, columnspan=2,)
        self.give_up = Button(self.buttonframe,text="Give up?", command=self.giveup, height=1, width=7, 
                              font=("Calibri", 25), bg = "light green", borderwidth=2, relief=SOLID)
        self.give_up.grid(row=6, column=7, columnspan=2, rowspan=1)
        
        self.hint = Button(self.buttonframe,text="Get Hint", command=self.get_hint, height=1, width=7, 
                              font=("Calibri", 25), bg = "light green", borderwidth=2, relief=SOLID)
        self.hint.grid(row=7, column=7, columnspan=2, rowspan=1)



    def lifecounter(self):

        self.life_label=Label(self.buttonframe, text = "Lives Left: ",font=("Calibri", 25), bg="light green",
                              height=2, width=8)
        self.life_label.grid(row=4, column=7, rowspan=1, columnspan=1)
        self.life_counter = Label(self.buttonframe, textvariable=lives, font=("Calibri", 25), bg="light green",
                                  height=2, width=4, anchor=W)
        self.life_counter.grid(row = 4, column = 8, rowspan=1, columnspan=1)
        

    def get_hint(self):
        lives_left = int(lives.get()) - 1
        lives.set(str(lives_left))
        if int(lives.get()) == 0:
                lives.set(0)
                messagebox.showerror("Wah, Wah, Waaaaaahh","Game over! \nThe answer was "+answer)
                time.sleep(3)
                exit()
        
        hint_choice = random.randint(1,5)
        while hint_choice in hint_lst:
            hint_choice = random.randint(1,5)
        hint_lst.append(hint_choice)
        if hint_choice == 1:
            hair_variable.set(ans_pick.hair_colour)
            return
        elif hint_choice == 2:
            eyes_variable.set(ans_pick.eye_colour)
            return
        elif hint_choice == 3:
            clothes_variable.set(ans_pick.clothes)
            return
        elif hint_choice == 4:
            glasses_variable.set(ans_pick.glasses)
            return
        elif hint_choice == 5:
            gender_variable.set(ans_pick.gender)
            return


    def giveup(self):
        response = messagebox.askyesno("Give up", "Do you give up?")
        if response == True:
            messagebox.showinfo("Answer", "The answer is: " + answer)
            exit()
        elif response == False:
            pass

    def click(self):
        c_names = "\n".join(chosen_names)
        String_chosen_names.set(c_names)
        if answer in chosen_names:
            root2 = Toplevel(root, bg="purple")
            root2.geometry("600x300")
            root2.title("Congratulations")
            root2.wm_transient(root)
            Label(root2, font=("Impact", 30), text=("Congratulations, you are correct!")).pack(expand=True)
            Button(root2, text="Close Game", command=lambda: [(root2.destroy()), (exit())]).pack()

        elif answer not in chosen_names:
            lives_left = int(lives.get()) - 1
            lives.set(str(lives_left))
            if int(lives.get()) == 0:
                lives.set(0)
                messagebox.showerror("Wah, Wah, Waaaaaahh","Game over! \nThe answer was "+answer)
                time.sleep(3)
                exit()
            elif int(lives.get()) >= 0:
                pass


class MainW(Tk):
    def __init__(self, master=None):
        Tk.__init__(self, master)
        self.master = master


    def heading(self):
        self.label = Label(text="Guess WHO!", font=("impact", 40), bg="light yellow", width=46)
        self.label.grid(row=0, column = 0, columnspan= 8)

        self.guessbuttons = GUI(self)
        self.guessbuttons.grid(row=1, column=0, columnspan=8)

    def welcome(self):
        welcome = Toplevel(root, bg="light green")
        welcome.geometry(f'300x100+600+400')
        frame = Frame(welcome)
        frame.pack()
        welcome.title("Welcome to Guess Who!")
        welcome.wm_transient(root)
        Label(frame, text="Would you like to play?", font=("Calibri", 21), bg = "light green").grid(row=0, column=0, columnspan=2)
        Button(frame, text="Enter", command=welcome.destroy, font=("Arial", 22), bg = "light green", width = 15).grid(row=1, column=0, columnspan=2)


root = MainW()
root.title("Guess WHO!")
app_width = 1218
app_height = 1050

root.geometry(f'{app_width}x{app_height}')
root.resizable(False, False)

ans_pick = Attributes()
ans_pick.set_attributes()
answer = ans_pick.pick
hair_variable = StringVar()
eyes_variable = StringVar()
clothes_variable = StringVar()
glasses_variable = StringVar()
gender_variable = StringVar()


chosen_names = []
hint_lst = []
c_names= ""
String_chosen_names = StringVar()
lives = StringVar()

lives.set(5)
root.welcome()
root.heading()
root.mainloop()


