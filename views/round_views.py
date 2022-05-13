class RoundCreation:

    @staticmethod
    def show_player_match(statutplayers):
        print(f"{statutplayers[0]['last_name']} "
              f"{statutplayers[0]['first_name']} vs "
              f"{statutplayers[1]['last_name']} "
              f"{statutplayers[1]['first_name']}:")
        print("Match score possible value: WIN: 1, LOSS: 0, TIE: 0.5")

    @staticmethod
    def get_player_score(statutplayer):
        player1 = input(f"Match score for {statutplayer['last_name']} "
                        f"{statutplayer['first_name']}: ")
        return float(player1)

    @staticmethod
    def show_scoreboard(scoreboard):
        print("Scoreboard for this round:")
        print("SCORE | ELO | ID | LAST NAME | FIRST NAME")
        for score in scoreboard:
            print(f"{score['score']} | {score['elo']} | {score['player_id']} "
                  f"| {score['last_name']} | "
                  f"{score['first_name']}")

        return input("\nPress enter to continue...")

    @staticmethod
    def get_round_name():
        print("Round name:")
        return input()

    @staticmethod
    def show_matches(matched):
        print("Here are the matches:")
        for match in matched:
            print(f"{match[0]['last_name']} {match[0]['first_name']} vs "
                  f"{match[1]['last_name']} "
                  f"{match[1]['first_name']}")
        return input("Press Enter to go to menu...")
