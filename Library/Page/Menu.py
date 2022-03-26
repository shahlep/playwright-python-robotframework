class Menu:

    first_menu_locator = "#treemenu >> text=FIRST"
    snd_menu_locator = "#treemenu >> text=SECOND"

    @staticmethod
    def navigate_menu_item(page, first_level_menu, second_level_menu):
        #locators
        first_menu = Menu.first_menu_locator.replace('FIRST', first_level_menu)
        snd_menu = Menu.snd_menu_locator.replace('SECOND',second_level_menu)
        #select locators from menu
        page.click(first_menu)
        page.click(snd_menu)