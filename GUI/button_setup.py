

def left_bar(widget):

    #current game
    widget.ui.pushButton_left_bar_current_game.clicked.connect(
            lambda:[
                    widget.ui.stackedWidget_menus.setCurrentWidget(widget.ui.page_current_adventure),
                    widget.ui.label_display.setText(   
                                                    f"DND HELPER\n\n"
                                                    f"clicking YES will erase permanently\n\n"
                                                    f"\t{widget.curr_game.adventure_name}\n\n"
                                                    f"click NO button go back to current game\n"
                                                    )
                    ])

    #new game
    widget.ui.pushButton_left_bar_new_game.clicked.connect(
            lambda:[
                    widget.ui.stackedWidget_menus.setCurrentWidget(widget.ui.page_new_adventure),
                    widget.ui.label_display.setText(   f"DND HELPER\n\n"
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

    return widget.ui
