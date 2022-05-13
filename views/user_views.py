class UserCreation:
    def __init__(self):
        print("This is the user creation/edition interface."
              "\nPlease complete the needed information:\n")

    @staticmethod
    def success(player_id):
        print("\033[92m The player has been successfully created!"
              " Here is his ID: " + str(player_id) +
              "\n Write it down, you may need it later...\033[0m")

    @staticmethod
    def get_player():
        print("Input the wanted player ID:")
        return input()

    @staticmethod
    def get_new_elo(elo):
        print(f"Current Elo: {elo}")
        return input("New Elo: ")

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
