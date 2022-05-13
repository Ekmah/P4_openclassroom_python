from tinydb import TinyDB, where


class Tournament:
    def __init__(self, name: str, location: str, date, time_control: str,
                 description: str, players_id, rounds_id=None,
                 nb_rounds: int = 1):
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

    def update_by_field(self, field, value):
        db = TinyDB('db.json')
        table = db.table('Tournament')
        return table.update(self.__dict__, where(field) == value)

    def update(self, model_id):
        db = TinyDB('db.json')
        table = db.table('Tournament')
        return table.update(self.__dict__, doc_ids=[int(model_id)])
