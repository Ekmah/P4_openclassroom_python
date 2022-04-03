from models import Player, Match, StatutPlayer, PlayerScore, Tournament
from tinydb import TinyDB, Query
db = TinyDB('db.json')


def algo(tournament_id, new):
    tournament = Tournament(**db.table('Tournament').get(doc_id=int(tournament_id)))
    all_players = []
    for player_id in tournament.players_id:
        player = Player(**db.table('Player').get(doc_id=player_id))
        q = Query()
        player_score_db = db.table('PlayerScore').get((q.player_id == int(player_id)) &
                                                      (q.tournament_id == int(tournament_id)))
        player_score_id = player_score_db.doc_id
        player_score = PlayerScore(**player_score_db)
        # nom,prénom, élo, score, already matched players
        compiled_player = {"player_id": player_id, "elo": player.elo, "player_score": player_score,
                           "player_score_id": player_score_id, "score": player_score.score,
                           "last_name": player.last_name, "first_name": player.first_name}
        all_players.append(compiled_player)
    newlist = sorted(all_players, key=lambda d: (d['score'], d['elo']), reverse=True)
    if new:
        group_1 = newlist[:len(newlist) // 2]
        group_2 = newlist[len(newlist) // 2:]
    else:
        group_1 = newlist[::2]
        group_2 = newlist[1::2]
    matches_id = []
    matched = []
    for player_1 in group_1:
        for player_2 in group_2:
            if not player_1["player_score"].player_already_matched_id:
                match_id = Match(False).save()
                # print(match_id)
                StatutPlayer(match_id, player_1["player_id"]).save()
                StatutPlayer(match_id, player_2["player_id"]).save()

                player_1["player_score"].player_already_matched_id = [player_2['player_id']]
                player_2["player_score"].player_already_matched_id = [player_1['player_id']]
                player_1["player_score"].update(player_1['player_score_id'])
                player_2["player_score"].update(player_2['player_score_id'])

                group_2.remove(player_2)
                matches_id.append(match_id)
                matched.append([player_1, player_2])
                break
            elif player_2["player_id"] not in player_1["player_score"].player_already_matched_id:
                match_id = Match(False).save()
                # print(match_id)
                StatutPlayer(match_id, player_1["player_id"]).save()
                StatutPlayer(match_id, player_2["player_id"]).save()

                player_1["player_score"].player_already_matched_id.append(player_2['player_id'])
                player_2["player_score"].player_already_matched_id.append(player_1['player_id'])
                player_1["player_score"].update(player_1['player_score_id'])
                player_2["player_score"].update(player_2['player_score_id'])

                group_2.remove(player_2)
                matches_id.append(match_id)
                matched.append([player_1, player_2])
                break
                # go to next group_2 player

    return matches_id, matched
# algo autre fichier
    # precedent top 2 player from any round must not encounter each other again
# trié par score puis par classment/elo mais comme score = 0 au premier round cela reviens à tri par classement/elo
