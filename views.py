# final view enable input to go to menu or redirect to menu controller with end message

class MenuView:

    @staticmethod
    def main_menu():
        print("This is the Main menu.")
        print("Here are the different choices:")
        print("0: Create tournament (all players must be created beforehand)")
        print("1: Create player")
        print("2: Edit player elo/classement")
        print("3: See tournament's rounds & reports")
        return input("To choose an option, type it's number here:")

    @staticmethod
    def choose_tournament(all_tournaments):
        print("Please choose which tournament you want to select:\n")
        for tournament in all_tournaments:
            print(f"ID: {tournament[1]}| Name: {tournament[0].name}, Date: {tournament[0].date}")
        return input("\nTo choose a tournament, type it's ID here:")

    @staticmethod
    def sub_menu_tournament():
        print("0: Go to main menu")
        print("1: Finish a round & start a new one")
        print("2: See the tournament's reports")
        return input("To choose an option, type it's number here:")


class TournoiCreation:
    def __init__(self):
        print("This is the tournament creation interface.\nPlease complete the needed information:\n")

    @staticmethod
    def success():
        print("\033[92m The tournament has been successfully created! \033[0m")

    @staticmethod
    def get_name():
        print("Tournament name:")
        return input()

    @staticmethod
    def get_location():
        print("Tournament location:")
        return input()

    @staticmethod
    def get_date():
        print("Date:")
        print("(DD/MM/YYYY)")
        return input()

    @staticmethod
    def get_time_control():
        print("Tournament time control:")
        return input()

    @staticmethod
    def get_description():
        print("Tournament description:")
        return input()

    @staticmethod
    def get_nb_players():
        print("Tournament number of players:")
        return input()

    @staticmethod
    def get_player_id(i):
        print(f"Tournament player number {i} ID:")
        return input()

    @staticmethod
    def get_nb_rounds():
        print("Tournament number of rounds:")
        return input()

    @staticmethod
    def get_round_id():
        print("Tournament round's id:")
        return input()


class UserCreation:
    def __init__(self):
        print("This is the user creation interface.\nPlease complete the needed information:\n")

    @staticmethod
    def success(player_id):
        print("\033[92m The player has been successfully created! Here is his ID: " + str(player_id) +
              "\n Write it down, you may need it later...\033[0m")

    @staticmethod
    def get_last_name():
        print("Last Name:")
        return input()

    @staticmethod
    def get_first_name():
        print("First Name:")
        return input()

    @staticmethod
    def get_birth_date():
        print("Birth date:")
        print("(DD/MM/YYYY)")
        return input()

    @staticmethod
    def get_gender():
        print("Gender:")
        print("(male/female/other)")
        return input()

    @staticmethod
    def get_elo():
        print("Elo/Ranking:")
        print("(number)")
        return input()


class RoundCreation:

    @staticmethod
    def get_round_name():
        print("Round name:")
        return input()

    @staticmethod
    def show_matches(matched):
        print("Here are the matches:")
        for match in matched:
            print(f"{match[0]['last_name']} {match[0]['first_name']} vs {match[1]['last_name']} {match[1]['first_name']}")
        return input("Press Enter to go to menu...")


def id_error(the_id, the_model):
    print(f"The {the_model} with the id {the_id} does not exist!")


def input_error():
    print("You made a mistake! Please retry.")
