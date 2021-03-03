'''
-nome personaggio, id
-classe
-razza
-livello
-background
-attributi
-bonus proficiency
-saving throws
-proficiency
'''
import sys
import pickle
import character_sheet as cs
from tkinter import *



def save_game(game):

    fileObj = open(f"{game.n_adventure}.adv", 'wb')
    pickle.dump(game,fileObj)
    fileObj.close()
    return


def load_game(game_name):
    game_file = open(f"{game_name}.adv", 'rb')
    game = pickle.load(game_file)
    game_file.close()
    return game


def initialize_player (name):
    while True :
        classes = cs.classes
        races = cs.races
        print(f"supported CLASSES:{classes}")
        print(f"supported RACES{races}")

        choice = [input(f"enter {name} {i}:") for i in ["name",
                                                        "race",
                                                        "class",
                                                        "alignment"]]

        stats = [int(input(f"choose {i}:")) for i in    ["strength",
                                                        "dexterity",
                                                        "constitution",
                                                        "intelligence",
                                                        "wisdom",
                                                        "charisma"]]


        if (choice[1] not in races) or (choice[2] not in classes):
            print("input error retry")
            continue

        break

    return cs.character_sheet(choice,stats)


class game():

    def __init__(self):

        #initializing player list
        self.n_adventure = input("enter adventure name")
        self.players = []
        self.add_players()
        return 

    def add_players(self):

        while True:
            try:
                p_num = int(input("enter player number\t"))
                break
            except:
                print("not an int type, retry")
        p_names = [input(f"enter Player{i+1} name\t") for i in range(p_num)] 
        for player in p_names:
            self.players.append(initialize_player(player))


    def __repr__(self):
        for player in self.players:
            print(player)
        return""


class TextOut(Text):

        def write(self, s):
            self.insert(CURRENT, s)

        def flush(self):
            pass
    
def new_game():
    game_label=Toplevel()
    game_label.configure(bg="#262626")

    stdout_text = TextOut(game_label)
    sys.stdout = stdout_text
    stdout_text.pack(expand=True, fill=BOTH)
    game_label.mainloop()
    return


def main_widget():

    root = Tk()
    root.title("5e DnD manager")
    root.geometry('300x300')
    root.configure(bg="#262626")

    b_new_game = Button(root,
                        text = "New Adventure",
                        width=30,
                        height=5,
                        bg="#3F3F3F",
                        command=new_game,
                        fg="white")

    b_load_game = Button(root,
                        text = "Load Adventure",
                        width=30,
                        height=5,
                        bg="#3F3F3F",
                        fg="white")

    b_delete_all = Button(root,
                        text = "Delete all Adventures",
                        width=30,
                        height=5,
                        bg="#3F3F3F",
                        fg="white")

    b_new_game.pack()
    b_load_game.pack()
    b_delete_all.pack()
    root.mainloop()
    return



if __name__ == "__main__":

    main_widget()


'''

    

    _ = input("init a new game? y to confirm\t")
    curr_game=0
    if _ == 'y': curr_game = game() 
    print(curr_game)
    scelte_base = ['gigi','high_elf','rogue','tarallo']
    array_statistiche = [8,14,13,15,12,10]
    player = cs.character_sheet(scelte_base,array_statistiche)
    _ = input("export player to pdf? y to confirm\t")
    if _ == 'y' : player.export_pdf()
    print("progay")
'''
