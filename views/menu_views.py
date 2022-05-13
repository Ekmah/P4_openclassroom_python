class MenuView:

    @staticmethod
    def main_menu():
        print("This is the Main menu.")
        print("Here are the different choices:")
        print("0: Create tournament (all players must be created beforehand)")
        print("1: Create player")
        print("2: Edit player elo/classement")
        print("3: See tournament's rounds")
        print("4: See reports")
        return input("To choose an option, type it's number here:")

    @staticmethod
    def choose_tournament(all_tournaments):
        print("Please choose which tournament you want to select:\n")
        for tournament in all_tournaments:
            print(
                f"ID: {tournament[1]}| Name: {tournament[0].name}, "
                f"Date: {tournament[0].date}")
        print("0: Go to main menu")
        return input("\nTo choose a tournament, type it's ID here:")

    @staticmethod
    def sub_menu_tournament():
        print("0: Go to main menu")
        print("1: Finish a round & start a new one")
        return input("To choose an option, type it's number here:")

    @staticmethod
    def sub_menu_reports():
        print("0: Go to main menu")
        print("1: See Global")
        print("2: See per Tournament")
        return input("To choose an option, type it's number here:")
