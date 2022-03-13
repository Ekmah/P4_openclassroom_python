from tinydb import TinyDB


class Tournament:
    def __init__(self, name: str, location: str, date, time_control: str,
                 description: str, players_id, rounds_id=None, nb_rounds: int = 1):
        self.name = name
        self.location = location
        self.date = date
        self.time_control = time_control
        self.description = description
        self.players_id = players_id
        self.rounds_id = rounds_id
        self.nb_rounds = nb_rounds

    def save(self):
        db = TinyDB('db.json')
        table = db.table('Tournament')
        return table.insert(self.__dict__)


class PlayerScore:
    def __init__(self, tournament_id, player_id: int, score: float = 0, player_already_matched_id=None):
        self.tournament_id = tournament_id
        self.player_id = player_id
        self.score = score
        self.player_already_matched_id = player_already_matched_id

    def save(self):
        db = TinyDB('db.json')
        table = db.table('PlayerScore')
        return table.insert(self.__dict__)


class Player:
    def __init__(self, last_name: str, first_name: str, birth_date,
                 gender: str, elo: int = 0):
        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.gender = gender
        self.elo = elo

    def save(self):
        db = TinyDB('db.json')
        table = db.table('Player')
        return table.insert(self.__dict__)


class StatutPlayer:
    def __init__(self, match_id: int, player_id: int, player_match_score: float = None,
                 color: str = None):
        self.color = color
        self.player_match_score = player_match_score
        self.match_id = match_id
        self.player_id = player_id
        pass

    def save(self):
        db = TinyDB('db.json')
        table = db.table('StatutPlayer')
        return table.insert(self.__dict__)


class Match:
    def __init__(self, game_status: bool):
        self.game_status = game_status

    def save(self):
        db = TinyDB('db.json')
        table = db.table('Match')
        return table.insert(self.__dict__)


class Round:
    def __init__(self, tournament_id: int, round_name: str, datetime_start, datetime_end=None,
                 matches_id=None, round_nb: int = 1):
        self.tournament_id = tournament_id
        self.round_name = round_name
        self.datetime_start = datetime_start
        self.datetime_end = datetime_end
        self.matches_id = matches_id
        self.round_nb = round_nb

    def save(self):
        db = TinyDB('db.json')
        table = db.table('Round')
        return table.insert(self.__dict__)
