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
import pickle
import character_sheet as cs
import random as rn


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

#prov=('nome','classe','razza','background.txt',tuple([rn.choice(range(15))in range(6)]))
class game():
    def __init__(self):
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



if __name__ == "__main__":
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
