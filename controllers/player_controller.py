import datetime
from models.player_models import Player
from views.user_views import UserCreation
from views.utils_views import input_error
from controllers.utils_controller import has_number, go_menu
from tinydb import TinyDB

db = TinyDB('db.json')


class PlayerInit:

    def __init__(self):
        self.user_view = UserCreation()

    def player_creation(self):
        last_name = self.c_last_name()
        first_name = self.c_first_name()
        birth_date = self.c_birth_date()
        gender = self.c_gender()
        elo = self.c_elo()
        player = Player(last_name=last_name, first_name=first_name,
                        birth_date=birth_date,
                        gender=gender, elo=elo)  # init
        player_id = player.save()
        self.user_view.success(player_id)
        return go_menu()

    def player_elo_edit(self):
        player_id = self.user_view.get_player()
        player = Player(**db.table('Player').get(doc_id=int(player_id)))
        new_elo = self.user_view.get_new_elo(player.elo)
        player.elo = int(new_elo)
        player.update(player_id)
        return go_menu()

    def c_birth_date(self):
        while True:
            try:
                day, month, year = map(int,
                                       self.user_view.get_birth_date().split(
                                           '/'))
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
                first_name = self.user_view.get_first_name()
                first_name = first_name.lower().capitalize()

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
