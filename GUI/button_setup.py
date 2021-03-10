def left_bar(widget):

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
                    widget.ui.label_display.setText(   f"DND HELPER\n\n"
                                                    f"choose which adventure you want to load\n"
                                                    f"then click LOAD ADVENTURE button\n")
                    ])

    widget.ui.pushButton_left_bar_delete_game.clicked.connect(
            lambda:[
                    widget.ui.stackedWidget_menus.setCurrentWidget(widget.ui.page_delete_adventure),
                    widget.ui.label_display.setText(   f"DND HELPER\n\n"
                                                    f"clicking YES will erase permanently\n\n"
                                                    f"\t{widget.curr_game.adventure_name}\n\n"
                                                    f"click NO button go back to current game\n")
                    ])

    widget.ui.pushButton_left_bar_add_player.clicked.connect(
            lambda:widget.ui.stackedWidget_menus.setCurrentWidget(widget.ui.page_add_player))
    return widget.ui

def button_bind(widget):
    widget= left_bar(widget)
    return widget
