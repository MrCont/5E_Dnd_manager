def setup_page_new_adventure(widget):

    widget.ui.pushButton_create_adventure.clicked.connect(
            lambda:[
                    widget.ui.stackedWidget_menus.setCurrentWidget(widget.ui.page_current_adventure),
                    widget.ui.label_display.setText(   
                                                    f"DND HELPER\n\n"
                                                    f"clicking YES will erase permanently\n\n"
                                                    f"\t{widget.curr_game.adventure_name}\n\n"
                                                    f"click NO button go back to current game\n"
                                                    )
                    ])
    return widget.ui
