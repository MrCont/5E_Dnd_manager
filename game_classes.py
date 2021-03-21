import pickle
import character_sheet as cs


def save_game(game,path):

    fileObj = open(f"{path}/{game.n_adventure}.adv", 'wb')
    pickle.dump(game,fileObj)
    fileObj.close()
    return


def load_game(game_name,path):
    game_file = open(f"{path}/{game_name}.adv", 'rb')
    game = pickle.load(game_file)
    game_file.close()
    return game



'''
        choice = [input(f"enter {name} {i}:") for i in ["name",
                                                        "race",
                                                        "class",
                                                        "alignment"]]
'''
'''
        stats = [int(input(f"choose {i}:")) for i in    ["strength",
                                                        "dexterity",
                                                        "constitution",
                                                        "intelligence",
                                                        "wisdom",
                                                        "charisma"]]

'''




def GUI_add_player(choice,stats):
    global curr_game
    curr_game.players.append(cs.character_sheet(choice,stats))
    return


class game():

    def __init__(self):
        self.players = []
        self.n_adventure = "NO ADVENTURE SELECTED"
        self.n_p_add = 0
        self.adventure_name="EMPTY GAME"
        return

    def export_pdf(self):
        for player in self.players:
            player.export_pdf()
        return


    def __len__(self):
        return len(self.players)

    def __repr__(self):
        
        # for player in self.players:
            # print(player)
        return "\n\n".join((repr(player) for player in self.players))




if __name__ == "__main__":
    print ("main")
