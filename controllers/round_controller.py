import datetime
from models.match_model import Match
from models.tournament_model import Tournament
from models.player_models import Player, PlayerScore, StatutPlayer
from models.rounds_model import Round
from views.round_views import RoundCreation
from controllers.utils_controller import go_menu
from algo_sort_round import algo
from tinydb import TinyDB, where, Query
db = TinyDB('db.json')


class RoundMatchsInit:

    def __init__(self, tournament_id):
        self.round_view = RoundCreation()
        self.tournament = Tournament(
            **db.table('Tournament').get(doc_id=int(tournament_id)))
        if self.tournament:
            self.tournament_id = int(tournament_id)

    def round_controller(self):
        try:
            self.round_end()
            self.round_init()
        except TypeError:
            self.round_init()

    def round_end(self):
        round_actual_id = self.tournament.rounds_id[-1]
        print(len(self.tournament.rounds_id))
        round_actual = Round(
            **db.table('Round').get(doc_id=int(round_actual_id)))
        players_score = []
        if Match(**db.table('Match').get(
                doc_id=int(round_actual.matches_id[0]))).game_status:
            print("\033[92mAll Rounds have already been finished.\033[0m")

            return go_menu()
        for match_id in round_actual.matches_id:
            players_statut = db.table('StatutPlayer').search(
                where('match_id') == match_id)
            compiled_players = []
            for player_statut in players_statut:
                player_statut_id = player_statut.doc_id
                player_id = player_statut['player_id']
                player = Player(
                    **db.table('Player').get(doc_id=int(player_id)))
                player_statut = StatutPlayer(**player_statut)
                compiled_players.append(
                    {"player_id": player_id, "player_statut": player_statut,
                     "elo": player.elo,
                     "last_name": player.last_name,
                     "first_name": player.first_name,
                     "player_statut_id": player_statut_id})
            self.round_view.show_player_match(compiled_players)
            for player in compiled_players:
                player_match_score = self.round_view.get_player_score(player)
                player_id = player['player_id']
                player['player_statut'].player_match_score = player_match_score
                player['player_statut'].update(player['player_statut_id'])
                q = Query()
                player_score_db = db.table('PlayerScore').get(
                    (q.player_id == player_id) &
                    (q.tournament_id == self.tournament_id))
                player_score_id = player_score_db.doc_id
                player_score = PlayerScore(**player_score_db)
                player_score.score += player_match_score
                player_score.update(player_score_id)
                player['score'] = player_score.score
                players_score.append(player)
            match = Match(**db.table('Match').get(doc_id=int(match_id)))
            match.game_status = True
            match.update(match_id)
        scoreboard = sorted(players_score,
                            key=lambda d: (d['score'], d['elo']), reverse=True)
        self.round_view.show_scoreboard(scoreboard)

    def round_init(self):
        try:
            round_nb = len(self.tournament.rounds_id)
            first_sorting = False
        except TypeError:
            self.tournament.rounds_id = []
            round_nb = 0
            first_sorting = True
        if round_nb < self.tournament.nb_rounds:
            round_nb_actual = round_nb + 1
            print("new round!: ", round_nb_actual)
            matches_id, matched = algo(self.tournament_id, first_sorting)
            date = datetime.datetime.now().isoformat()
            round_obj = Round(tournament_id=self.tournament_id,
                              round_name=f"Round {round_nb_actual}",
                              round_nb=round_nb_actual,
                              datetime_start=date,
                              matches_id=matches_id)
            round_id = round_obj.save()
            self.tournament.rounds_id.append(round_id)
            self.tournament.update(self.tournament_id)
            self.round_view.show_matches(matched)
            return go_menu()
        else:
            return go_menu()
