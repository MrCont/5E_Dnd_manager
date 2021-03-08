import pickle
import character_sheet as cs
import tkinter as tk


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

        # initializing player list
        # self.n_adventure = input("enter adventure name")
        # self.players = []
        # self.add_players()
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


def main_widget():

    root = tk.Tk()

    #MAIN FRAME
    main_menu = tk.Frame(root)
    main_menu.configure(bg="#262626")
    b_new_game = tk.Button(main_menu,
                        text = "NEW ADVENTURE",
                        width= 60,
                        height=  8,
                        bg="#3F3F3F",
                        command=lambda:[new_adventure_menu.pack(pady=80),
                                        main_menu.pack_forget()],
                        fg="white").pack()

    b_load_game = tk.Button(main_menu,
                        text = "LOAD ADVENTURE",
                        width= 60,
                        height=  8,
                        bg="#3F3F3F",
                        fg="white").pack()


    b_delete_all = tk.Button(main_menu,
                        text = "DELETE ALL ADVENTURES",
                        width= 60,
                        height=  8,
                        bg="#3F3F3F",
                        fg="white").pack()


    # NEW ADVENTURE FRAME
    new_adventure_menu = tk.Frame(root)
    e_adv_name = tk.Entry(new_adventure_menu,
                        bg="#3F3F3F",
                        fg="white")
    
    b_adv_name = tk.Button(new_adventure_menu,
                            text="NEW ADVENTURE NAME",
                            bg="#3F3F3F",
                            command = lambda:[new_game(e_adv_name),
                                            game_menu.pack(pady=10),
                                            new_adventure_menu.pack_forget()],
                            fg="white").pack(side=tk.RIGHT)

    e_adv_name.pack(side=tk.LEFT)


    # GAME MENU FRAME
    game_menu = tk.Frame(root) 
    game_menu.configure(bg="#262626")

    b_save_game = tk.Button(game_menu,
                            text="SAVE GAME",
                            bg="#3F3F3F",
                            command=lambda:[save_game(curr_game)],
                            fg="white").grid(row=1,column=2)

    b_add_player_menu = tk.Button(game_menu,
                            text="ADD NEW PLAYER",
                            bg="#3F3F3F",
                            command=lambda:[add_player_menu.pack(),
                                            display.delete("1.0",tk.END),
                                            display.insert(tk.END,
                                                    f"CLASSES AVAILABLE:\n"
                                                    f"{' '.join(cs.classes)}\n"
                                                    f"\nRACES AVAILABLE:\n"
                                                    f"{' '.join(cs.races)}")],

                            fg="white").grid(row=1,column=3)

    b_export_pdf = tk.Button(game_menu,
                            text="EXPORT PDF",
                            bg="#3F3F3F",
                            command=lambda:[curr_game.export_pdf(),
                                            display.delete("1.0",tk.END),
                                            display.insert(tk.END,
                                                    f"GAME SUCCESSFULLY EXPORTED")  
                                            ],
                            fg="white").grid(row=1,column=4)
    b_main_menu = tk.Button(game_menu,
                            text="MAIN MENU",
                            bg="#3F3F3F",
                            command=lambda:[main_menu.pack(),
                                            add_player_menu.pack_forget(),
                                            game_menu.pack_forget()],
                            fg="white").grid(row=1,column=5)

    #ADD PLAYER MENU
    add_player_menu = tk.Frame(root)
    add_player_menu.configure(bg="#262626")
    #NAME ENTRY
    l_p_name = tk.Label(add_player_menu,
                        text="Character name:",
                        bg="#3F3F3F",
                        fg="white").grid(row=0,column=0)

    e_p_name = tk.Entry(add_player_menu,
                        bg="#3F3F3F",
                        fg="white")
    e_p_name.grid(row=0,column=1)

    #RACE ENTRY
    l_p_race = tk.Label(add_player_menu,
                        text="Race:",
                        bg="#3F3F3F",
                        fg="white").grid(row=0,column=2)

    e_p_race = tk.Entry(add_player_menu,
                        bg="#3F3F3F",
                        fg="white")
    e_p_race.grid(row=0,column=3)
    #CLASS ENTRY
    l_p_class = tk.Label(add_player_menu,
                        text="Class:",
                        bg="#3F3F3F",
                        fg="white").grid(row=1,column=0)

    e_p_class = tk.Entry(add_player_menu,
                        bg="#3F3F3F",
                        fg="white")
    e_p_class.grid(row=1,column=1)
    #ALIGNMENT ENTRY
    l_p_alignment = tk.Label(add_player_menu,
                        text="Alignment:",
                        bg="#3F3F3F",
                        fg="white").grid(row=1,column=2)

    e_p_alignment = tk.Entry(add_player_menu,
                        bg="#3F3F3F",
                        fg="white")
    e_p_alignment.grid(row=1,column=3)
    
    #STRENGTH ENTRY
    l_p_strength = tk.Label(add_player_menu,
                        text="Strength:",
                        bg="#3F3F3F",
                        fg="white").grid(row=2,column=0)

    e_p_strength = tk.Entry(add_player_menu,
                        bg="#3F3F3F",
                        fg="white")
    e_p_strength.grid(row=2,column=1)

    #DEXTERITY ENTRY
    l_p_dexterity = tk.Label(add_player_menu,
                        text="Dexterity:",
                        bg="#3F3F3F",
                        fg="white").grid(row=2,column=2)

    e_p_dexterity = tk.Entry(add_player_menu,
                        bg="#3F3F3F",
                        fg="white")
    e_p_dexterity.grid(row=2,column=3)

    #CONSTITUTION ENTRY
    l_p_constitution = tk.Label(add_player_menu,
                        text="Constitution:",
                        bg="#3F3F3F",
                        fg="white").grid(row=3,column=0)

    e_p_constitution = tk.Entry(add_player_menu,
                        bg="#3F3F3F",
                        fg="white")
    e_p_constitution.grid(row=3,column=1)

    #INTELLIGENCE ENTRY
    l_p_intelligence = tk.Label(add_player_menu,
                        text="Intelligence:",
                        bg="#3F3F3F",
                        fg="white").grid(row=3,column=2)

    e_p_intelligence = tk.Entry(add_player_menu,
                        bg="#3F3F3F",
                        fg="white")
    e_p_intelligence.grid(row=3,column=3)

    #WISDOM ENTRY
    l_p_wisdom = tk.Label(add_player_menu,
                        text="Wisdom:",
                        bg="#3F3F3F",
                        fg="white").grid(row=4,column=0)

    e_p_wisdom = tk.Entry(add_player_menu,
                        bg="#3F3F3F",
                        fg="white")
    e_p_wisdom.grid(row=4,column=1)

    #CHARISMA ENTRY
    l_p_charisma = tk.Label(add_player_menu,
                        text="Charisma:",
                        bg="#3F3F3F",
                        fg="white").grid(row=4,column=2)

    e_p_charisma = tk.Entry(add_player_menu,
                        bg="#3F3F3F",
                        fg="white")
    e_p_charisma.grid(row=4,column=3)
    #OTHER ADD PLAYER BUTTONS
    b_add_player = tk.Button(add_player_menu,
                            text="ADD PLAYER",
                            bg="#3F3F3F",
                            command=lambda:[GUI_add_player(
                                                        [e_p_name.get(),
                                                        e_p_race.get(),
                                                        e_p_class.get(),
                                                        e_p_alignment.get()],
                                                        [int(e_p_strength.get()),
                                                        int(e_p_dexterity.get()),
                                                        int(e_p_constitution.get()),
                                                        int(e_p_intelligence.get()),
                                                        int(e_p_wisdom.get()),
                                                        int(e_p_charisma.get())]),
                                            #RESET TK-TEXT
                                            e_p_name.delete("0",tk.END),
                                            e_p_race.delete("0",tk.END),
                                            e_p_class.delete("0",tk.END),
                                            e_p_alignment.delete("0",tk.END),
                                            e_p_strength.delete("0",tk.END),
                                            e_p_dexterity.delete("0",tk.END),
                                            e_p_constitution.delete("0",tk.END),
                                            e_p_intelligence.delete("0",tk.END),
                                            e_p_wisdom.delete("0",tk.END),
                                            e_p_charisma.delete("0",tk.END)
                                            ],
                            fg="white").grid(row=5,columnspan=9)

    b_add_player_menu_close = tk.Button(add_player_menu,
                                        text="CLOSE",
                                        width=50,
                                        bg="#3F3F3F",
                                        command=lambda:add_player_menu.pack_forget(),
                                        fg="white").grid(row=6,columnspan=9)

    l_tip = tk.Label(add_player_menu,
                    text=" ".join((  "Quick tip : pressing TAB will",
                                    "navigate through text boxes and buttons")),
                    bg="#3F3F3F",
                    fg="white").grid(row=7,columnspan=9)
    #GAME DISPLAY
    display = tk.Text(game_menu,height=20,width=60)
    display.config(bg="#6E7889")
    display.grid(row=0,column=0,columnspan= 8)
    b_print_all = tk.Button(game_menu,
                            text="SCREEN\nREFRESH",
                            bg="#3F3F3F",
                            command=lambda:[
                                display.delete("1.0",tk.END),
                                display.insert(tk.END,f"GAME STATE:\n{repr(curr_game)}")
                                ],
                                            
                            fg="white").grid(column=6, row=1,columnspan=9)
    main_menu.pack(padx=1,pady=80)


    root.title("5e DnD manager")
    root.geometry(
    f"{int(root.winfo_screenwidth()/2.0)}x{int(root.winfo_screenheight()/1.5)}")
    root.configure(bg="#262626")
    root.resizable(width=False,height=False)
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
