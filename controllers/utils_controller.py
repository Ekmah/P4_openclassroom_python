import controllers.menu_controller as menu_c


def has_number(char):
    return any(char.isdigit() for char in char)


def go_menu():
    menu_c.Menu().main_menu()


def go_sub_menu():
    menu_c.Menu().reports_sub_menu()
