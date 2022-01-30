import json
from pip import main
from simple_term_menu import TerminalMenu
from types import SimpleNamespace

class MenuItems():

    def __init__(self):

        self.config = json.load(open("config/config.json"), object_hook=lambda d: SimpleNamespace(**d))

    def get_main_menu(self):

        main_menu_title = "  [WEATHER APP - ver 0.3]\n"
        main_menu_items = [
            f"[1] Weather for {self.config.default_city}", 
            "[2] Weather for Location", 
            "[3] Edit Config",
            "[4] Quit Weather App"]
        
        main_menu = TerminalMenu (
            menu_entries = main_menu_items,
            title = main_menu_title,
            menu_cursor = "> ",
            menu_cursor_style = ("fg_red", "bold"),
            menu_highlight_style = ("bg_blue", "fg_black", "bold"),
            cycle_cursor = True,
            clear_screen = True,
        )
        return main_menu


    def get_back_menu(self):

        back_menu = TerminalMenu (
            menu_entries = ["Back to Main Menu"],
            title = "",
            menu_cursor = "> ",
            menu_cursor_style = ("fg_red", "bold"),
            menu_highlight_style = ("bg_red", "fg_yellow"),
            cycle_cursor = True,
            clear_screen = False,
        )
        return back_menu


    def get_edit_menu(self):

        edit_menu_title = "  Edit Menu\n"
        edit_menu_items = ["Edit Config", "Save Settings", "Back to Main Menu"]

        edit_menu = TerminalMenu (
            menu_entries = edit_menu_items,
            title = edit_menu_title,
            menu_cursor = "> ",
            menu_cursor_style = ("fg_red", "bold"),
            menu_highlight_style = ("bg_red", "fg_yellow"),
            cycle_cursor = True,
            clear_screen = True,
        )
        return edit_menu