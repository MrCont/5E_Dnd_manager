import character_sheet as cs
import game_classes as gc
import random as rn
from PySide2.QtWidgets import QPushButton, QListWidgetItem
from PySide2.QtGui import QFont

def set_n_p_add(widget,num):
    widget.curr_game.n_p_add=num
    return
def set_created(widget):
    widget.curr_game.created = 1
    return
############################# CURRENT ADVENTURE ################################
#throws an n1 sized dice n2 times
def dice_throw(widget,n1,n2):
    try: 
        #check int type and compute results
        n1,n2 = map(int,(n1,n2))
        result = [str(rn.choice(range(1,n1+1)))+"\n" for i in range(n2)] #str() and \n to print in column

        #join to display results 
        widget.ui.label_display.setText(f"{''.join(result)}")

    except: 
        #excepion to avoid int type error
        widget.ui.label_display.setText(
                                        f"DND HELPER\n\n"
                                        f"error, an integer was not provided"
                                        )
        return
    return


#RESET ADVENURE PLAYER LIST
# def reset_list(widget):
    # widget.ui.listWidget.clear()
    # for player in widget.curr_game.players:
        # widget.ui.listWidget.addItem(player.pc_name)
    # return widget.ui
##########################################################COME BACK WHEN ADDING PPLAYER IS A THING
def reset_list(widget):
    widget.ui.listWidget.clear()
    for player in widget.curr_game.players:

        player_b = QListWidgetItem(player.pc_name)

        #font line setup
        font = QFont()
        font.setFamily(u"Copperplate Gothic Light")
        font.setPointSize(10)
        player_b.setFont(font)

        widget.ui.listWidget.addItem(player_b)
        
        widget.ui.listWidget.itemClicked.connect(   #change selected player when line is clicked
             lambda:
                widget.ui.label_selected_player.setText(
                                                     f"SELECTED PLAYER:\t"
                                                     f"{widget.ui.listWidget.currentItem().text()}"
                                                     ))

    return widget.ui

def setup_page_current_adventure(widget):

    #display adventure name
    widget.ui.label_current_game.setText(widget.curr_game.adventure_name)

    #setup dice throw
    widget.ui.pushButton_throw.clicked.connect(
            lambda:dice_throw(
                            widget,
                            widget.ui.lineEdit_size.displayText(),
                            widget.ui.lineEdit_times.displayText()
                            ))

    #setup player in game list
    widget.ui = reset_list(widget)
    widget.ui.label_selected_player.setText(f"SELECTED PLAYER:\t")
    widget.ui.pushButton_show_stats.clicked.connect(
            lambda:[
                widget.ui.label_display.setText(
                    f"STATS:\n\n"
                    #display starting from selected player
                    f"{widget.curr_game.players[widget.ui.listWidget.currentRow():]}"
                    f"{widget.curr_game.players[:widget.ui.listWidget.currentRow()]}"
                    ),
                ]
            )
                                            



    return widget.ui


############################# NEW ADVENTURE ####################################
#function binded to create adventure button in create adventure menu
def create_adv(widget):
    try: 
        #setup the number of players that still are not added to game
        widget.curr_game.n_p_add = int(widget.ui.lineEdit_player_number.text()) 

        #init the name of curr_adventure
        widget.curr_game.adventure_name = widget.ui.lineEdit_adventure_name.text()

        #change menu to add player
        widget.ui.stackedWidget_menus.setCurrentWidget(widget.ui.page_add_player),
        widget.ui.label_display.setText(   
                                        f"DND HELPER\n\n"
                                        f"please fill the form and add players\n"
                                        f"still there are {widget.curr_game.n_p_add} to create"
                                        )
    except:
        #avoid int input error in creating the adventure
        widget.ui.label_display.setText(   
                                        f"DND HELPER\n\n"
                                        f"value in Player number was not an integer"
                                        )
    return


def setup_page_new_adventure(widget):
    widget.ui.pushButton_create_adventure.clicked.connect(lambda:create_adv(widget))
    return widget.ui


############################## ADD PLAYER ###################################

def show_last_added(widget):

    last = widget.curr_game.players[-1]
    widget.ui.label_display.setText(   
                                    f"DND HELPER\n\n"
                                    f"please fill the form and add players\n"
                                    f"still there are {widget.curr_game.n_p_add} to create\n\n"
                                    f"last added player was\n"
                                    f"{last}"
                                    )
    return


def add_player(widget):

    choices = [[],[]]

    try:
        #SETUP STAT CHOICES (STR DEX ...)
        stats = []
        stats.append(widget.ui.lineEdit_strength.text())
        stats.append(widget.ui.lineEdit_dexterity.text())
        stats.append(widget.ui.lineEdit_constitution.text())
        stats.append(widget.ui.lineEdit_intelligence.text())
        stats.append(widget.ui.lineEdit_wisdom.text())
        stats.append(widget.ui.lineEdit_charisma.text())

        choices[1]=[int(stat) for stat in stats]

        #SETUP NAME, ALIGNMENT ECC..
        choices[0].append(widget.ui.lineEdit_player_name.text())
        choices[0].append(widget.ui.lineEdit_character_name.text())
        
        choices[0].append(str(widget.ui.comboBox_race.currentText()))
        choices[0].append(str(widget.ui.comboBox_class.currentText()))
        choices[0].append(str(widget.ui.comboBox_alignment.currentText()))
        
        widget.curr_game.players.append(cs.character_sheet(choices[0],choices[1]))
        show_last_added(widget)
    except:

        #excepion to avoid int type error
        widget.ui.label_display.setText(
                                        f"DND HELPER\n\n"
                                        f"error, an integer was not provided"
                                        )
    return


def setup_page_add_player(widget):
    #reset combo boxes
    widget.ui.comboBox_class.clear()
    widget.ui.comboBox_race.clear()
    widget.ui.comboBox_alignment.clear()

    widget.ui.comboBox_class.addItem("")
    widget.ui.comboBox_race.addItem("")
    widget.ui.comboBox_alignment.addItem("")

    #add chooices to combo boxes
    widget.ui.comboBox_class.addItems(cs.classes)
    widget.ui.comboBox_race.addItems(cs.races)
    widget.ui.comboBox_alignment.addItems(cs.alignments)

    widget.ui.pushButton_add_player.clicked.connect(
            lambda :[
                #decrease player to add count if game is not created
                set_n_p_add(widget,widget.curr_game.n_p_add-1) 
                if not widget.curr_game.created else set_n_p_add(widget,1),
                add_player(widget),
                print(widget.curr_game.players),        
                #go to curr adv page if there are no more player to add
                [
                show_current_adventure(widget),
                set_created(widget)]
                if widget.curr_game.n_p_add == 0 else print("")
                ])

    widget.ui.pushButton_add_back.clicked.connect(
            lambda :[
                    set_n_p_add(widget,0),
                    add_player(widget),
                    set_created(widget),
                    show_current_adventure(widget)
                    ])

    widget.ui.pushButton_back_menu.clicked.connect(
            lambda:[
                show_current_adventure(widget),
                set_created(widget)]
            )

    print(widget.curr_game.players)
    return widget.ui

############################## DELETE ADVENTURE ###################################
def reset_adventure(widget):
    widget.curr_game = gc.game()
    return

def setup_page_delete_adventure(widget):
    widget.ui.pushButton_yes.clicked.connect(lambda:reset_adventure(widget))
    widget.ui.pushButton_no.clicked.connect(
            lambda:show_current_adventure(widget) if widget.curr_game.created
            else widget.ui.label_display.setText(
                        f"DND HELPER\n\n"
                        f"no adventure is currently selected or created\n"
                        f"please click CREATE ADVENTURE or LOAD ADVENTURE button\n")
                )
    return widget.ui

############################# DELETE PLAYER ###################################
def reset_combo(widget):
    
    widget.ui.comboBox_choose_player.clear()
    widget.ui.comboBox_choose_player.addItem("")
    widget.ui.comboBox_choose_player.addItems(
                [f"{x.player_name}-{x.pc_name}" for x in widget.curr_game.players])
    return

def setup_page_delete_player(widget):
    print("gay")
    if widget.curr_game.created != 0 : 
        widget.ui.comboBox_choose_player.clear()
        widget.ui.comboBox_choose_player.addItem("")
        widget.ui.comboBox_choose_player.addItems(
                [f"{x.player_name}-{x.pc_name}" for x in widget.curr_game.players])

        widget.ui.pushButton_cancel.clicked.connect(
            lambda:show_current_adventure(widget) if widget.curr_game.created
            else widget.ui.label_display.setText(
                        f"DND HELPER\n\n"
                        f"no adventure is currently selected or created\n"
                        f"please click CREATE ADVENTURE or LOAD ADVENTURE button\n")
                )

        widget.ui.pushButton_delete.clicked.connect(
                lambda:[
                    widget.ui.label_display.setText(
                        f"DND HELPER\n\n"
                        f"{widget.curr_game.players.pop(widget.ui.comboBox_choose_player.currentIndex()-1)}"
                        f"\n\nwas successfully removed from game"),
                    reset_combo(widget)
                    ] if widget.ui.comboBox_choose_player.currentIndex()!=0
                    else widget.ui.label_display.setText(
                        f"DND HELPER\n\n"
                        f"player was not selected")
                )
    
    return widget.ui
############################### LEFT BAR ####################################

def show_current_adventure(widget):
    setup_page_current_adventure(widget)
    widget.ui.stackedWidget_menus.setCurrentWidget(widget.ui.page_current_adventure),
    widget.ui.label_display.setText(   
                                    f"DND HELPER\n\n"
                                    f"adventure name:\n\n"
                                    f"\t{widget.curr_game.adventure_name}\n\n"
                                    f"player number:{len(widget.curr_game.players)}\n"
                                    ),
    return


def left_bar(widget):

    #current game
    widget.ui.pushButton_left_bar_current_game.clicked.connect(
            lambda:show_current_adventure(widget) if widget.curr_game.created
            else widget.ui.label_display.setText(
                        f"DND HELPER\n\n"
                        f"no adventure is currently selected or created\n"
                        f"please click CREATE ADVENTURE or LOAD ADVENTURE button\n")
                )

    #new game
    widget.ui.pushButton_left_bar_new_game.clicked.connect(
            lambda:[
                    widget.ui.stackedWidget_menus.setCurrentWidget(widget.ui.page_new_adventure),
                    widget.ui.label_display.setText(   
                                                    f"DND HELPER\n\n"
                                                    f"insert adventure name and player number\n"
                                                    f"then click CREATE ADVENTURE button\n")
                    ])

    #load game
    widget.ui.pushButton_left_bar_load_game.clicked.connect(
            lambda:[
                    widget.ui.stackedWidget_menus.setCurrentWidget(widget.ui.page_load_adventure) ,
                    widget.ui.label_display.setText(   
                                                    f"DND HELPER\n\n"
                                                    f"choose which adventure you want to load\n"
                                                    f"then click LOAD ADVENTURE button\n"
                                                    )
                    ])

    #save game
    widget.ui.pushButton_left_bar_save_game.clicked.connect(
            lambda:[
#############################################################################   ADD WAY TO SAVE GAME                 
                    widget.ui.label_display.setText(   
                                                    f"DND HELPER\n\n"
                                                    f"the adventure:"
                                                    f"{widget.curr_game.adventure_name}"
                                                    f"was correctly saved"
                                                    )
                    if widget.curr_game.created 
                    else widget.ui.label_display.setText(
                                f"DND HELPER\n\n"
                                f"no adventure is currently selected or created\n"
                                f"please click CREATE ADVENTURE or LOAD ADVENTURE button\n")
                    ])

    #delete game
    widget.ui.pushButton_left_bar_delete_game.clicked.connect(
            lambda:[
                    [widget.ui.stackedWidget_menus.setCurrentWidget(widget.ui.page_delete_adventure),
                    widget.ui.label_display.setText(   
                                                    f"DND HELPER\n\n"
                                                    f"clicking YES will erase permanently\n\n"
                                                    f"\t{widget.curr_game.adventure_name}\n\n"
                                                    f"click NO button go back to current game\n"
                                                    )]
                    if widget.curr_game.created 
                    else widget.ui.label_display.setText(
                                f"DND HELPER\n\n"
                                f"no adventure is currently selected or created\n"
                                f"please click CREATE ADVENTURE or LOAD ADVENTURE button\n")
                    ])

    #add player
    widget.ui.pushButton_left_bar_add_player.clicked.connect(
            lambda:[
                widget.ui.stackedWidget_menus.setCurrentWidget(widget.ui.page_add_player),
                set_n_p_add(widget,1),
                widget.ui.label_display.setText(   
                                                f"DND HELPER\n\n"
                                                f"please fill the form and add players\n"
                                                f"still there are {widget.curr_game.n_p_add} to create"
                                                )
                ] if widget.curr_game
                else widget.ui.label_display.setText(
                            f"DND HELPER\n\n"
                            f"no adventure is currently selected or created\n"
                            f"please click CREATE ADVENTURE or LOAD ADVENTURE button\n")
                )



    #delete player
    widget.ui.pushButton_left_bar_delete_player.clicked.connect(
            lambda:[
                    setup_page_delete_player(widget),
                    widget.ui.stackedWidget_menus.setCurrentWidget(widget.ui.page_delete_player),
                    widget.ui.label_display.setText(   
                                                    f"DND HELPER\n\n"
                                                    f"choose player in combo box\n"
                                                    f"clicking DELETE will ERASE PERMANENTLY selected one\n\n"
                                                    f"click cancel button to go back to current adventure\n"
                                                    )
                    ]
                    if widget.curr_game.created 
                    else widget.ui.label_display.setText(
                                f"DND HELPER\n\n"
                                f"no adventure is currently selected or created\n"
                                f"please click CREATE ADVENTURE or LOAD ADVENTURE button\n")
            )

    #export pdf
    widget.ui.pushButton_left_bar_export_pdf.clicked.connect(
            lambda:[
#############################################################################   ADD WAY TO EXPORT PDF
                    widget.ui.label_display.setText(   
                                                    f"DND HELPER\n\n"
                                                    f"the adventure:\n\n"
                                                    f"{widget.curr_game.adventure_name}\n"
                                                    f"was correctly exported"
                                                    )
                    ]
                    if widget.curr_game.created 
                    else widget.ui.label_display.setText(
                                f"DND HELPER\n\n"
                                f"no adventure is currently selected or created\n"
                                f"please click CREATE ADVENTURE or LOAD ADVENTURE button\n")
            )

    return widget.ui


def button_bind(widget):
    widget.ui = left_bar(widget)
    widget.ui = setup_page_new_adventure(widget)
    widget.ui = setup_page_current_adventure(widget)
    widget.ui = setup_page_delete_adventure(widget)
    widget.ui = setup_page_add_player(widget)
    widget.ui = setup_page_delete_player(widget)
    return widget.ui
