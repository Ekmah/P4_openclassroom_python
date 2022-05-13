from models.tournament_model import Tournament
from views.menu_views import MenuView
from views.utils_views import input_error
import controllers.tournament_controllers as tournament_c
import controllers.player_controller as player_c
import controllers.round_controller as round_c
import controllers.reports_controller as reports_c
from tinydb import TinyDB
db = TinyDB('db.json')


class Menu:
    def __init__(self):
        self.menu_view = MenuView()

    # créer tournoi
    def main_menu(self):
        choice = self.menu_view.main_menu()
        if int(choice) == 0:
            tournament_c.TournamentInit().tournament_creation()
        elif int(choice) == 1:
            player_c.PlayerInit().player_creation()
        elif int(choice) == 2:
            player_c.PlayerInit().player_elo_edit()
        elif int(choice) == 3:
            self.tournament_sub_menu()
        elif int(choice) == 4:
            self.reports_sub_menu()
        else:
            input_error()
            Menu().main_menu()

    def tournament_sub_menu(self):
        all_tournaments = [[Tournament(**t), t.doc_id] for t in
                           db.table('Tournament').all()]
        tournament_id = self.menu_view.choose_tournament(all_tournaments)
        if int(tournament_id) == 0:
            return Menu().main_menu()
        tournament = Tournament(
            **db.table('Tournament').get(doc_id=int(tournament_id)))
        if tournament:
            choice = self.menu_view.sub_menu_tournament()
            if int(choice) == 0:
                return self.main_menu()
            if int(choice) == 1:
                round_c.RoundMatchsInit(tournament_id).round_controller()
            else:
                input_error()
                Menu().tournament_sub_menu()

    def reports_sub_menu(self):
        choice = self.menu_view.sub_menu_reports()
        if int(choice) == 0:
            return self.main_menu()
        if int(choice) == 1:
            reports_c.Reports().reports_global()
        if int(choice) == 2:
            all_tournaments = [[Tournament(**t), t.doc_id] for t in
                               db.table('Tournament').all()]
            tournament_id = self.menu_view.choose_tournament(all_tournaments)
            if tournament_id and int(tournament_id) != 0:
                reports_c.Reports().reports_local(tournament_id)
            elif int(tournament_id) == 0:
                return Menu().reports_sub_menu()
        else:
            input_error()
            Menu().main_menu()
