import datetime
from models.tournament_model import Tournament
from models.player_models import PlayerScore
from views.tournament_views import TournoiCreation
from views.utils_views import input_error
from controllers.utils_controller import has_number, go_menu
from tinydb import TinyDB

db = TinyDB('db.json')


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
                                time_control=self.c_time_control(),
                                description=description,
                                players_id=players_id, nb_rounds=nb_rounds)
        tournoi_id = tournament.save()
        for player_id in players_id:
            player_score = PlayerScore(tournoi_id, player_id)
            player_score.save()
        self.tournament_view.success()
        return go_menu()

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
            except ValueError:
                input_error()
                continue

    def c_date(self):
        while True:
            try:
                day, month, year = map(int,
                                       self.tournament_view.get_date().split(
                                           '/'))
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
        players_nb = 0
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
