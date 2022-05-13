from tinydb import TinyDB, where


class Match:
    def __init__(self, game_status: bool):
        self.game_status = game_status

    def save(self):
        db = TinyDB('db.json')
        table = db.table('Match')
        return table.insert(self.__dict__)

    def update_by_field(self, field, value):
        db = TinyDB('db.json')
        table = db.table('Match')
        return table.update(self.__dict__, where(field) == value)

    def update(self, model_id):
        db = TinyDB('db.json')
        table = db.table('Match')
        return table.update(self.__dict__, doc_ids=[int(model_id)])
