from models.tournament_model import Tournament
from models.rounds_model import Round
from views.reports_views import ReportsView
from views.utils_views import input_error
from controllers.utils_controller import go_menu, go_sub_menu
from tinydb import TinyDB, where

db = TinyDB('db.json')


class Reports:
    def __init__(self):
        self.report_view = ReportsView()

    def reports_global(self):
        choice = self.report_view.global_reports()
        if int(choice) == 0:
            return go_menu()
        if int(choice) == 1:
            self.player_report('last_name')
        if int(choice) == 2:
            self.player_report('elo')
        if int(choice) == 3:
            self.all_tournaments_report()
        else:
            input_error()
            Reports().reports_global()

    def reports_local(self, tournament_id):
        choice = self.report_view.local_reports()
        if int(choice) == 0:
            return go_menu()
        if int(choice) == 1:
            self.player_report('last_name', tournament_id)
        if int(choice) == 2:
            self.player_report('elo', tournament_id)
        if int(choice) == 3:
            self.tournaments_matches_report(tournament_id)
        if int(choice) == 4:
            self.tournaments_matches_report(tournament_id, False)
        else:
            input_error()
            go_sub_menu()

    def player_report(self, ordering, tournament=False):
        if tournament:
            tournament = Tournament(
                **db.table('Tournament').get(doc_id=tournament))
            players = [db.table('Player').get(doc_id=player_id) for player_id
                       in tournament.players_id]
        else:
            players = db.table('Player').all()
        if ordering == 'elo':
            players = sorted(players, key=lambda d: (d['elo']), reverse=True)
        elif ordering == 'last_name':
            players = sorted(players, key=lambda d: (d['last_name']))
        self.report_view.players(players)
        return go_menu()

    def all_tournaments_report(self):
        all_tournaments = db.table('Tournament').all()
        self.report_view.tournaments(all_tournaments)
        return go_menu()

    def tournaments_matches_report(self, tournament_id, separated=True):
        tournament = Tournament(
            **db.table('Tournament').get(doc_id=int(tournament_id)))
        all_matches = []
        for round_actual_id in tournament.rounds_id:
            round_actual = Round(
                **db.table('Round').get(doc_id=int(round_actual_id)))
            matches_round = []
            for match_id in round_actual.matches_id:
                players_statut = db.table('StatutPlayer').search(
                    where('match_id') == match_id)
                match = []
                for player_statut in players_statut:
                    if player_statut["player_match_score"] == 1:
                        player_statut["player_match_score"] = "WON"
                    elif player_statut["player_match_score"] == 0.5:
                        player_statut["player_match_score"] = "TIED"
                    elif player_statut["player_match_score"] == 0:
                        player_statut["player_match_score"] = "LOST"
                    player = dict(db.table('Player').get(
                        doc_id=player_statut['player_id']))
                    player.update(player_statut)
                    match.append(player)
                matches_round.append(match)
            if separated:
                all_matches.append(matches_round)
            else:
                all_matches.extend(matches_round)
        self.report_view.matches(all_matches, separated)
        return go_menu()
