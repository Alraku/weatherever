# -*- coding: UTF-8 -*-
import time

from simple_term_menu import TerminalMenu
from app.src.request_weather import Weather
from app.interface.menu_items import MenuItems


class Menu():

    def get_interface():

        weather = Weather()
        back_menu = MenuItems.get_back_menu()
        main_menu = MenuItems.get_main_menu()
        edit_menu = MenuItems.get_edit_menu()
        main_menu_exit = False
        edit_menu_back = False

        while not main_menu_exit:
            main_sel = main_menu.show()

            if main_sel == 0:
                while not edit_menu_back:
                    edit_sel = edit_menu.show()
                    if edit_sel == 0:
                        print("Edit Config Selected")
                        time.sleep(5)
                    elif edit_sel == 1:
                        print("Save Selected")
                        time.sleep(5)
                    elif edit_sel == 2:
                        edit_menu_back = True
                        print("Back Selected")
                edit_menu_back = False
            elif main_sel == 1:
                weather.show_weather_default()
                back_menu.show()
            elif main_sel == 2:
                weather.show_weather()
                back_menu.show()
            elif main_sel == 3:
                main_menu_exit = True


       

