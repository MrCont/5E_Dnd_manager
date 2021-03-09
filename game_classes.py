import pickle
import character_sheet as cs


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

def new_game(name):
    global curr_game 
    curr_game = game()
    curr_game.n_adventure = name.get()


def GUI_add_player(choice,stats):
    global curr_game
    curr_game.players.append(cs.character_sheet(choice,stats))
    return


class game():

    def __init__(self):
        self.players = []
        self.n_adventure = ""

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

    def export_pdf(self):
        for player in self.players:
            player.export_pdf()
        return


    def __repr__(self):
        
        # for player in self.players:
            # print(player)
        return "\n\n".join((repr(player) for player in self.players))




if __name__ == "__main__":
    print ("main")
