from tinydb import TinyDB, where


class Round:
    def __init__(self, tournament_id: int, round_name: str, datetime_start,
                 datetime_end=None,
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

    def update_by_field(self, field, value):
        db = TinyDB('db.json')
        table = db.table('Round')
        return table.update(self.__dict__, where(field) == value)

    def update(self, model_id):
        db = TinyDB('db.json')
        table = db.table('Round')
        return table.update(self.__dict__, doc_ids=[int(model_id)])
