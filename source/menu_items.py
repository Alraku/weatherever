import json
from pip import main
from simple_term_menu import TerminalMenu
from types import SimpleNamespace

class MenuItems():

    def __init__(self):

        self.config = json.load(open("config.json"), object_hook=lambda d: SimpleNamespace(**d))

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

        edit_menu_title = "  [WEATHER APP - Edit Menu]\n"
        edit_menu_items = [
            "[1] Edit Units",
            "[2] Edit Language",
            "[3] Edit Default City",
            "[4] Back to Main Menu"]

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


    def get_unit_menu(self):

        unit_menu_title = "  [WEATHER APP - Unit Menu]\n"
        unit_menu_items = [
            "[1] Standard Units",
            "[2] Metric Units",
            "[3] Imperial Units",
            "[4] Back to Edit Menu"]

        unit_menu = TerminalMenu (
            menu_entries = unit_menu_items,
            title = unit_menu_title,
            menu_cursor = "> ",
            menu_cursor_style = ("fg_red", "bold"),
            menu_highlight_style = ("bg_red", "fg_yellow"),
            cycle_cursor = True,
            clear_screen = True,
        )
        return unit_menu