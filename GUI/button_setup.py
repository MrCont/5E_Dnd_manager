import random as rn
from PySide2.QtWidgets import QPushButton, QListWidgetItem
from PySide2.QtGui import QFont
from PySide2.QtCore import QSize

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
    players=["gay","aborto"]
    widget.ui.listWidget.clear()
    for player in players:

        player_b = QListWidgetItem(player)

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
def setup_page_add_player(widget):
            
    return widget.ui

############################### LEFT BAR ####################################
def left_bar(widget):

    #current game
    widget.ui.pushButton_left_bar_current_game.clicked.connect(
            lambda:[
                    widget.ui.stackedWidget_menus.setCurrentWidget(widget.ui.page_current_adventure),
                    widget.ui.label_display.setText(   
                                                    f"DND HELPER\n\n"
                                                    f"adventure name:\n\n"
                                                    f"\t{widget.curr_game.adventure_name}\n\n"
                                                    f"player number:{len(widget.curr_game.players)}\n"
                                                    ),
                    setup_page_current_adventure(widget)
                    ])

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
                    ])

    #delete game
    widget.ui.pushButton_left_bar_delete_game.clicked.connect(
            lambda:[
                    widget.ui.stackedWidget_menus.setCurrentWidget(widget.ui.page_delete_adventure),
                    widget.ui.label_display.setText(   
                                                    f"DND HELPER\n\n"
                                                    f"clicking YES will erase permanently\n\n"
                                                    f"\t{widget.curr_game.adventure_name}\n\n"
                                                    f"click NO button go back to current game\n"
                                                    )
                    ])

    #add player
    widget.ui.pushButton_left_bar_add_player.clicked.connect(
            lambda:widget.ui.stackedWidget_menus.setCurrentWidget(widget.ui.page_add_player))


    #delete player
    widget.ui.pushButton_left_bar_delete_player.clicked.connect(
            lambda:[
                    widget.ui.stackedWidget_menus.setCurrentWidget(widget.ui.page_delete_player),
                    widget.ui.label_display.setText(   
                                                    f"DND HELPER\n\n"
                                                    f"choose player in combo box\n"
                                                    f"clicking DELETE will ERASE PERMANENTLY selected one\n\n"
                                                    f"click cancel button to go back to current adventure\n"
                                                    )
                    ])

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
                    ])

    return widget.ui


def button_bind(widget):
    widget.ui = left_bar(widget)
    widget.ui = setup_page_new_adventure(widget)
    widget.ui = setup_page_current_adventure(widget)

    return widget.ui
