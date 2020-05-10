from tkinter import *
import csv as csv
import random as random

class Window(Frame):

    raffles = ['A', 'B', 'C', 'D', 'E', 'F', 'G']


    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("GUI")
        self.pack(fill=BOTH, expand=1)

        menu = Menu(self.master)
        self.master.config(menu=menu)

        file = Menu(menu)

        file.add_command(label="Exit", command=self.client_exit)

        menu.add_cascade(label="File", menu=file)

        edit = Menu(menu)

        edit.add_command(label="Undo")

        menu.add_cascade(label="Edit", menu=edit)

        Label(self, text="Name:").grid(row=0)
        
        self.entry_name = Entry(self)
        self.entry_name.grid(row=0, column=1)

        Label(self, text="# of entries:").grid(row=1, column=0)

        catText = StringVar()
        cat = OptionMenu(self, textvariable=catText, raffles).place(x=100, y=0)

        self.info = StringVar()
        self.infoLabel = Label(self, textvariable=self.info).place(x=0, y=200)

        self.winner = StringVar()
        self.winnerLabel = Label(self, textvariable=self.winner).place(x=0, y=250)

        self.entry_num = Entry(self)
        self.entry_num.grid(row=1, column=1)

        # BUTTONS
        #quitButton = Button(self, text="Quit", command=self.client_exit)
        #quitButton.place(x=0, y=0)

        getButton = Button(self, text="Submit", command=self.get_input)
        getButton.grid(row=2)

        readButton = Button(self, text="Read", command=self.readFile)
        readButton.grid(row=3)

        clearAllButton = Button(self, text="Clear All", command=self.clearFile)
        clearAllButton.grid(row=3, column=1)

        getWinnersButton = Button(self, text="Winners", command=self.getWinners)
        getWinnersButton.grid(row=3, column=2)
        

    def client_exit(self):
        exit()

    def get_input(self):
        name = self.entry_name.get()
        num = self.entry_num.get()
        self.writeToFile(name, num)
        self.info.set("Last Entry:\n" + name + "   Entries: " + num)

    def writeToFile(self, name, entries):
        file = open("file.csv", mode='a', newline="")
        csv.writer(file).writerow((name, entries))

    def getWinners(self):
        self.readFile()
        weight = []
        for i in list(self.entries.values()):
            weight.append(int(i))
        randomVal = random.choices(list(self.entries), weights=weight, k=1)
        print(randomVal)

    def readFile(self):
        file = open("file.csv", mode='r')
        self.entries = {}
        for row in csv.reader(file, delimiter=","):
            #self.entries[row[0]] = row[1]
            if(len(row) > 0):
                self.entries[row[0]] = row[1]


    def clearFile(self):
        file = open("file.csv", "w+")
        file.close()
        


    
root = Tk()

root.geometry("400x300")

app = Window(root)
root.mainloop()
