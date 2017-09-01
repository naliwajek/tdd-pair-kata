class PointTranslator:
    def __init__(self):
        pass

    def translate(self, point_1, point_2):
        score_1 = self.__translation_table(point_1)
        score_2 = self.__translation_table(point_2)

        if point_1 == 0 and point_2 == 0:
            return 'Love-Love'

        if point_1 == point_2:
            all_score = score_1 + '-All'
            if point_1 >= 3:
                return 'Deuce'
            else:
                return all_score

        return score_1 + '-' + score_2

    def __translation_table(self, point):
        try:
            return {
                '0': 'Zero',
                '1': 'Fifteen',
                '2': 'Thirty',
                '3': 'Fourty',
            }[str(point)]
        except KeyError:
            return ''


class TennisGame:
    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2
        self.player_1_score = 0
        self.player_2_score = 0
        self.game_over = False
        self.translator = PointTranslator()

    def score(self):
        if self.advantage_over(self.player_1_score, self.player_2_score):
            return 'Advantage for ' + self.player_1

        if self.advantage_over(self.player_2_score, self.player_1_score):
            return 'Advantage for ' + self.player_2

        if self.player_1_score == 4:
            self.game_over = True
            return 'Won for ' + self.player_1

        if self.player_2_score == 4:
            self.game_over = True
            return 'Won for ' + self.player_2

        return self.translator.translate(self.player_1_score, self.player_2_score)

    def advantage_over(self, player_with, player_without):
      return player_with > 3 and (player_without == player_with - 1)

    def won_point(self, player_name):
        if self.game_over:
            raise GameOverException

        if player_name == self.player_1:
            self.player_1_score += 1
        elif player_name == self.player_2:
            self.player_2_score += 1
        else:
            raise UnknownPlayerException


class UnknownPlayerException(Exception):
    pass

class GameOverException(Exception):
    pass
