import datetime
from models import Tournament, Player, Round, Match, StatutPlayer
from views import UserCreation, TournoiCreation, RoundCreation, input_error
# from tinydb import TinyDB, Query
# db = TinyDB('db.json')


class Menu:
    def __init__(self):
        self.r = 0

    # créer tournoi
    # créer joueur
    # edit elo joueur
    #  -> sous menu tournoi
    #   rapports
    #   finir le round en cours si en cours


class TournamentInit:

    def __init__(self):
        self.tournament_view = TournoiCreation()

    def tournament_creation(self):
        nb_rounds = self.c_nb_rounds()
        Tournament(name=self.c_name(), location=self.c_location(), date=self.c_date(),
                   time_control=self.c_time_control(), description=self.c_description(), players_id=self.c_players_id(),
                   nb_rounds=nb_rounds)
    
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
                day, month, year = map(int, self.tournament_view.get_date().split('/'))
                try:
                    date = datetime.date(year, month, day)
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
            except ValueError:
                input_error()
                continue
        players_id = []
        for i in range(players_nb):
            while True:
                try:
                    player_id = int(self.tournament_view.get_player_id())
                    players_id.append(player_id)
                except ValueError:
                    input_error()
                    continue
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

    def c_birth_date(self):
        while True:
            try:
                day, month, year = map(int, self.user_view.get_birth_date().split('/'))
                try:
                    birth_date = datetime.date(year, month, day)
                    return birth_date
                except ValueError:
                    input_error()
                    continue
            except ValueError:
                input_error()
                continue

    def c_last_name(self):
        while True:
            try:
                last_name = self.user_view.get_last_name().upper()
                if has_number(last_name):
                    input_error()
                    continue
                else:
                    return last_name

            except ValueError:
                input_error()
                continue

    def c_first_name(self):
        while True:
            try:
                first_name = self.user_view.get_first_name().lower().capitalize()
                if has_number(first_name):
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
        self.tournament = tournament_id

    def c_round(self, tournament_id):
        round_nb = len(self.tournament.rounds_id)
        if round_nb + 1 < self.tournament.nb_rounds:
            round_nb_actual = round_nb + 1

            matches_id = 0  # Appel algo création matches + status

            Round(round_name=f"Round {round_nb_actual}", round_nb=round_nb_actual, datetime_start=datetime.datetime.now(),
                  matches_id=matches_id)

        else:
            tournament_finished = True  # The tournament has ended

    # algo autre fichier
    # precedent top 2 player from any round must not encounter each other again
    # Round()  # init
    # Match()  # init
    # StatutPlayer()  # init

# Controlleur fin de tour (input score de match)
