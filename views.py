class TournoiCreation:
    def __init__(self):
        print("This is the tournament creation interface.\nPlease complete the needed information:\n")

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
    def get_player_id():
        print("Tournament player's id:")
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


def input_error():
    print("You made a mistake! Please retry.")
