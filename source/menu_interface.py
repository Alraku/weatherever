# -*- coding: UTF-8 -*-
import time

from src.request_weather import Weather
from src.menu_items import MenuItems
from src.helpers import edit_config


class Menu():

    def get_interface():

        weather = Weather()
        back_menu = MenuItems().get_back_menu()
        main_menu = MenuItems().get_main_menu()
        edit_menu = MenuItems().get_edit_menu()
        unit_menu = MenuItems().get_unit_menu()
        main_menu_exit = False
        edit_menu_back = False
        unit_menu_back = False

        while not main_menu_exit:
            main_sel = main_menu.show()

            if main_sel == 0:
                weather.show_weather("default")
                back_menu.show()
            elif main_sel == 1:
                weather.show_weather()
                back_menu.show()
            elif main_sel == 2:
                while not edit_menu_back:
                    edit_sel = edit_menu.show()
                    if edit_sel == 0:
                        while not unit_menu_back:
                            unit_sel = unit_menu.show()
                            if unit_sel == 0:
                                edit_config("units", "standard")
                            if unit_sel == 1:
                                edit_config("units", "metric")
                            if unit_sel == 2:
                                edit_config("units", "imperial")
                            if unit_sel == 3:
                                unit_menu_back = True
                                weather.__init__()
                    elif edit_sel == 1:
                        print("Edit Language Selected")
                        time.sleep(5)
                    elif edit_sel == 2:
                        print("Edit Default City Selected")
                    elif edit_sel == 3:
                        edit_menu_back = True
                edit_menu_back = False
            elif main_sel == 3:
                main_menu_exit = True
