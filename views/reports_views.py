class ReportsView:
    def __init__(self):
        print("This is the reports interface.\n")

    @staticmethod
    def global_reports():
        print("0: Go to main menu")
        print("1: See players ordered by name")
        print("2: See players ordered by ranking")
        print("3: See Tournaments")
        return input("To choose an option, type it's number here:")

    @staticmethod
    def local_reports():
        print("0: Go to main menu")
        print("1: See players ordered by name")
        print("2: See players ordered by ranking")
        print("3: See Round's Matches")
        print("4: See Tournament's Matches")
        return input("To choose an option, type it's number here:")

    @staticmethod
    def players(players):
        print("| ID | LAST NAME | FIRST NAME | RANKING |")
        for player in players:
            print(f"| {player.doc_id} | {player['last_name']} "
                  f"| {player['first_name']} | {player['elo']} |")
        return input("\nPress enter to continue...")

    @staticmethod
    def tournaments(tournaments):
        print("| NAME | LOCATION | DATE | NUMBER OF ROUNDS |")
        for tournament in tournaments:
            print(f"| {tournament['name']} | {tournament['location']} "
                  f"| {tournament['date']} | "
                  f"{tournament['nb_rounds']} |")
        return input("\nPress enter to continue...")

    @staticmethod
    def matches(all_matches, separated):
        if separated:
            for round_nb, round_matches in enumerate(all_matches):
                print(f"Round {int(round_nb)+1}")
                print("LAST NAME FIRST NAME |"
                      " WON/LOST/TIED VS LAST NAME FIRST NAME | WON/LOST/TIED")
                for match in round_matches:
                    player_1, player_2 = match
                    print(f"{player_1['last_name']} {player_1['first_name']} "
                          f"| {player_1['player_match_score']} VS "
                          f"{player_2['last_name']} {player_2['first_name']} "
                          f"| {player_2['player_match_score']}")
        else:
            print("LAST NAME FIRST NAME |"
                  " WON/LOST/TIED VS LAST NAME FIRST NAME | WON/LOST/TIED")
            for match in all_matches:
                player_1, player_2 = match
                print(f"{player_1['last_name']} {player_1['first_name']} "
                      f"| {player_1['player_match_score']} VS "
                      f"{player_2['last_name']} {player_2['first_name']} "
                      f"| {player_2['player_match_score']}")
        input("\nPress enter to continue...")
