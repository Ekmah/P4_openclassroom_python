from tinydb import TinyDB, Query
db = TinyDB('db.json')


class Tournoi:
    def __init__(self, players_id, rounds_id, nb_rounds: int = 1):
        self.players_id = players_id
        self.rounds_id = rounds_id
        self.nb_rounds = nb_rounds


class Player:
    def __init__(self, identification, elo: int = 1, score: float = 0):
        self.identification = identification
        self.elo = elo
        self.score = score


class StatutPlayer:
    def __init__(self, color: str, game_status, match_id: int, player_id: int):
        self.color = color
        self.game_status = game_status
        self.match_id = match_id
        self.player_id = player_id
        pass


class Match:
    def __init__(self, players_id):
        self.players_id = players_id


class Round:
    def __init__(self, matches_id, round_nb: int = 1):
        self.matches_id = matches_id
        self.round_nb = round_nb
