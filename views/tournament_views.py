class TournoiCreation:
    def __init__(self):
        print("This is the tournament creation interface."
              "\nPlease complete the needed information:\n")

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
