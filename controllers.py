import datetime
from models import Tournament, Player, Round, Match, StatutPlayer, PlayerScore
from views import UserCreation, TournoiCreation, RoundCreation, MenuView, input_error, id_error
from algo_sort_round import algo
from tinydb import TinyDB, where
db = TinyDB('db.json')

# PASSER LYNTER PYLINT PEP8
# pip freeze > requirements.txt
# create folder controller/view and files for each big view/controller


class Menu:
    def __init__(self):
        self.menu_view = MenuView()

    # créer tournoi
    def main_menu(self):
        choice = self.menu_view.main_menu()
        if int(choice) == 0:
            TournamentInit().tournament_creation()
        elif int(choice) == 1:
            PlayerInit().player_creation()
        elif int(choice) == 2:
            PlayerInit().player_elo_edit()
        elif int(choice) == 3:
            self.tournament_sub_menu()

    def tournament_sub_menu(self):
        all_tournaments = [[Tournament(**t), t.doc_id] for t in db.table('Tournament').all()]
        tournament_id = self.menu_view.choose_tournament(all_tournaments)
        tournament = Tournament(**db.table('Tournament').get(doc_id=int(tournament_id)))
        if tournament:
            choice = self.menu_view.sub_menu_tournament()
            if int(choice) == 0:
                return self.main_menu()
            if int(choice) == 1:
                RoundMatchsInit(tournament_id).round_controller()  # finir le round en cours si en cours
            elif int(choice) == 2:
                pass
                #   rapports


class TournamentInit:

    def __init__(self):
        self.tournament_view = TournoiCreation()

    def tournament_creation(self):
        name = self.c_name()
        description = self.c_description()
        location = self.c_location()
        date = self.c_date()
        nb_rounds = self.c_nb_rounds()
        players_id = self.c_players_id()
        tournament = Tournament(name=name, location=location, date=date,
                                time_control=self.c_time_control(), description=description,
                                players_id=players_id, nb_rounds=nb_rounds)
        tournoi_id = tournament.save()
        for player_id in players_id:
            player_score = PlayerScore(tournoi_id, player_id)
            player_score.save()
            # id_error(player_id, "PlayerS")
        self.tournament_view.success()
        return Menu().main_menu()
    
    def c_name(self):
        while True:
            try:
                name = self.tournament_view.get_name()
                if has_number(name):
                    input_error()
                    continue
                else:
                    return name

            except ValueError:
                input_error()
                continue
    
    def c_location(self):
        while True:
            try:
                location = self.tournament_view.get_location()
                return str(location)
                # must have characters?
            except ValueError:
                input_error()
                continue
    
    def c_date(self):
        while True:
            try:
                day, month, year = map(int, self.tournament_view.get_date().split('/'))
                try:
                    date = datetime.date(year, month, day).isoformat()
                    return date
                except ValueError:
                    input_error()
                    continue
            except ValueError:
                input_error()
                continue
    
    def c_time_control(self):
        while True:
            try:
                location = self.tournament_view.get_time_control()
                return str(location)

            except ValueError:
                input_error()
                continue
        
    def c_description(self):
        while True:
            try:
                location = self.tournament_view.get_description()
                return str(location)

            except ValueError:
                input_error()
                continue
        
    def c_players_id(self):
        while True:
            try:
                players_nb = int(self.tournament_view.get_nb_players())
                break
            except ValueError:
                input_error()
                continue
        players_id = []
        i = 1
        while i <= players_nb:
            while True:
                try:
                    player_id = int(self.tournament_view.get_player_id(i))
                    players_id.append(player_id)
                    break
                except ValueError:
                    input_error()
                    continue
            i += 1
        return players_id
        
    def c_nb_rounds(self):
        while True:
            try:
                nb_rounds = int(self.tournament_view.get_nb_rounds())
                return nb_rounds
            except ValueError:
                input_error()
                continue
        

class PlayerInit:

    def __init__(self):
        self.user_view = UserCreation()

    def player_creation(self):
        last_name = self.c_last_name()
        first_name = self.c_first_name()
        birth_date = self.c_birth_date()
        gender = self.c_gender()
        elo = self.c_elo()
        player = Player(last_name=last_name, first_name=first_name, birth_date=birth_date,
                        gender=gender, elo=elo)  # init
        player_id = player.save()
        self.user_view.success(player_id)
        return Menu().main_menu()

    def player_elo_edit(self):
        player_id = self.user_view.get_player()
        player = Player(**db.table('Player').get(doc_id=int(player_id)))
        new_elo = self.user_view.get_new_elo(player.elo)
        player.elo = int(new_elo)
        player.update(player_id)
        return Menu().main_menu()

    def c_birth_date(self):
        while True:
            try:
                day, month, year = map(int, self.user_view.get_birth_date().split('/'))
                try:
                    birth_date = datetime.date(year, month, day).isoformat()
                    return birth_date
                except ValueError:
                    input_error()
                    continue
            except ValueError:
                input_error()
                continue

    def c_last_name(self):
        try:
            last_name = self.user_view.get_last_name().upper()
            if not last_name or has_number(last_name):
                input_error()
                return self.c_last_name()
            else:
                return last_name

        except ValueError:
            input_error()
            return self.c_last_name()

    def c_first_name(self):
        while True:
            try:
                first_name = self.user_view.get_first_name().lower().capitalize()
                if not first_name or has_number(first_name):
                    input_error()
                    continue
                else:
                    return first_name
            except ValueError:
                input_error()
                continue

    def c_elo(self):
        while True:
            try:
                elo = int(self.user_view.get_elo())
                return elo
            except ValueError:
                input_error()
                continue

    def c_gender(self):
        while True:
            try:
                gender = self.user_view.get_gender()
                if has_number(gender):
                    input_error()
                    continue
                else:
                    return gender
            except ValueError:
                input_error()
                continue


def has_number(char):
    return any(char.isdigit() for char in char)


class RoundMatchsInit:

    def __init__(self, tournament_id):
        self.round_view = RoundCreation()
        self.tournament = Tournament(**db.table('Tournament').get(doc_id=int(tournament_id)))
        if self.tournament:
            self.tournament_id = tournament_id

# FINISH MATCH HERE + PROPOSAL DISPLAY SCOREBOARD

    def round_controller(self):
        try:
            self.round_end()
            self.round_init()
        except TypeError:
            self.round_init()

    def round_end(self):
        round_actual_id = self.tournament.rounds_id[-1]
        print(len(self.tournament.rounds_id))
        round_actual = Round(**db.table('Round').get(doc_id=int(round_actual_id)))
        players_score = []
        for match_id in round_actual.matches_id:
            players_statut = db.table('StatutPlayer').search(where('match_id') == match_id)
            compiled_players = []
            for player_statut in players_statut:
                player_id = player_statut['player_id']
                player = Player(**db.table('Player').get(doc_id=int(player_id)))
                player_statut = StatutPlayer(**player_statut)
                compiled_players.append({"player_id": player_id, "player_statut": player_statut, "elo": player.elo,
                                         "last_name": player.last_name, "first_name": player.first_name})
            # print(compiled_players)
            player_1_match_score, player_2_match_score = self.round_view.get_player_score(compiled_players)

            player_1 = compiled_players[0]
            player_1_id = player_1['player_id']
            player_1['player_statut'].update_by_field('player_id', player_1_id)
            player_1_score = PlayerScore(**db.table('PlayerScore').get(where('player_id') == player_1_id))
            player_1_score.score += player_1_match_score
            player_1_score.update_by_field('player_id', player_1_id)
            player_1['score'] = player_1_score.score
            players_score.append(player_1)

            player_2 = compiled_players[1]
            player_2_id = player_2['player_id']
            player_2['player_statut'].update_by_field('player_id', player_2_id)
            player_2_score = PlayerScore(**db.table('PlayerScore').get(where('player_id') == player_2_id))
            player_2_score.score += player_2_match_score
            player_2['score'] = player_2_score.score
            players_score.append(player_2)

        scoreboard = sorted(players_score, key=lambda d: (d['score'], d['elo']), reverse=True)
        self.round_view.show_scoreboard(scoreboard)
    # calcul top 1 add already matched players
    # creation scoreboard

    def round_init(self):
        try:
            round_nb = len(self.tournament.rounds_id)
            first_sorting = False
        except TypeError:
            self.tournament.rounds_id = []
            round_nb = 0
            first_sorting = True
        if round_nb < self.tournament.nb_rounds:
            round_nb_actual = round_nb + 1
            print("new round!: ", round_nb_actual)
            matches_id, matched = algo(self.tournament, first_sorting)
            round_obj = Round(tournament_id=self.tournament_id, round_name=f"Round {round_nb_actual}",
                              round_nb=round_nb_actual, datetime_start=datetime.datetime.now().isoformat(),
                              matches_id=matches_id)
            round_id = round_obj.save()
            self.tournament.rounds_id.append(round_id)
            self.tournament.update(self.tournament_id)
            self.round_view.show_matches(matched)
            return Menu().main_menu()
        else:
            pass  # The tournament has ended

    # Round()  # init # Done
    # Match()  # init # Done
    # StatutPlayer()  # init # Done
    # Controlleur fin de tour (input score de match)


if __name__ == '__main__':
    Menu().main_menu()
