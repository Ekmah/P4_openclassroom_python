from tinydb import TinyDB, where


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

    def update_by_field(self, field, value):
        db = TinyDB('db.json')
        table = db.table('Player')
        return table.update(self.__dict__, where(field) == value)

    def update(self, model_id):
        db = TinyDB('db.json')
        table = db.table('Player')
        return table.update(self.__dict__, doc_ids=[int(model_id)])


# Player model for Tournament specific values
class PlayerScore:
    def __init__(self, tournament_id, player_id: int, score: float = 0,
                 player_already_matched_id=None):
        self.tournament_id = tournament_id
        self.player_id = player_id
        self.score = score
        self.player_already_matched_id = player_already_matched_id

    def save(self):
        db = TinyDB('db.json')
        table = db.table('PlayerScore')
        return table.insert(self.__dict__)

    def update_by_field(self, field, value):
        db = TinyDB('db.json')
        table = db.table('PlayerScore')
        return table.update(self.__dict__, where(field) == value)

    def update(self, model_id):
        db = TinyDB('db.json')
        table = db.table('PlayerScore')
        return table.update(self.__dict__, doc_ids=[int(model_id)])


# Player model for match specific values
class StatutPlayer:
    def __init__(self, match_id: int, player_id: int,
                 player_match_score: float = 0,
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

    def update_by_field(self, field, value):
        db = TinyDB('db.json')
        table = db.table('StatutPlayer')
        return table.update(self.__dict__, where(field) == value)

    def update(self, model_id):
        db = TinyDB('db.json')
        table = db.table('StatutPlayer')
        return table.update(self.__dict__, doc_ids=[int(model_id)])
