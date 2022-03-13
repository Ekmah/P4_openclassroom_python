from models import Player, Match, StatutPlayer, PlayerScore
from tinydb import TinyDB, where
db = TinyDB('db.json')


def algo(tournament):
    all_players = []
    for player_id in tournament.players_id:
        player = Player(**db.table('Player').get(doc_id=player_id))
        player_score = PlayerScore(**db.table('PlayerScore').get(where('player_id') == player_id))
        # nom,prénom, élo, score, already matched players
        compiled_player = {"player_id": player_id, "elo": player.elo, "score": player_score.score,
                           "matched_players": player_score.player_already_matched_id,
                           "last_name": player.last_name, "first_name": player.first_name}
        all_players.append(compiled_player)
    newlist = sorted(all_players, key=lambda d: (d['score'], d['elo']))

    group_1 = newlist[:len(newlist) // 2]
    group_2 = newlist[len(newlist) // 2:]
    matches_id = []
    matched = []
    for player_1 in group_1:
        for player_2 in group_2:
            if not player_1["matched_players"]:
                match_id = Match(False).save()
                print(match_id)
                StatutPlayer(match_id, player_1["player_id"]).save()
                StatutPlayer(match_id, player_2["player_id"]).save()
                group_1.remove(player_1)
                group_2.remove(player_2)
                matches_id.append(match_id)
                matched.append([player_1, player_2])
            elif player_2["player_id"] not in player_1["matched_players"]:
                match_id = Match(False).save()
                print(match_id)
                StatutPlayer(match_id, player_1["player_id"]).save()
                StatutPlayer(match_id, player_2["player_id"]).save()
                group_1.remove(player_1)
                group_2.remove(player_2)
                matches_id.append(match_id)
                matched.append([player_1, player_2])
            else:
                pass
                # go to next group_2 player

    return matches_id, matched
# algo autre fichier
    # precedent top 2 player from any round must not encounter each other again
# trié par score puis par classment/elo mais comme score = 0 au premier round cela reviens à tri par classement/elo
