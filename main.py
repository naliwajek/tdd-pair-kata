from collections import OrderedDict

class Tennis:
    def __init__(self, player_one_name, player_two_name):
        self.player_one_name = player_one_name
        self.player_two_name = player_two_name
        self.players = OrderedDict({player_one_name: 0, player_two_name: 0})
        self.score_names = {0: 'love', 1: 'fifteen', 2: 'thirty', 3: 'forty'}

    def score(self):
        try:
            if self.players[self.player_one_name] == 3 and self.players[self.player_two_name] == 3:
                return 'Deuce'
            else:
                if self.__scores_are_equal():
                    return '{0} all'.format(self.__parse_score(self.players[self.player_one_name]))
                else:
                    return '{0} - {1}'.format(
                        self.__parse_score(self.players[self.player_one_name]),
                        self.__parse_score(self.players[self.player_two_name]))
        except KeyError:
            return self.__special_score()

    def won_point(self, player_name):
        self.players[player_name] += 1

    def __parse_score(self, score):
        return self.score_names[score]

    def __scores_are_equal(self):
        return self.players[self.player_one_name] == self.players[self.player_two_name]

    def __special_score(self):
        if self.__scores_are_equal():
            return 'Deuce'

        if abs(self.players[self.player_one_name] - self.players[self.player_two_name]) >= 2:
            if self.players[self.player_one_name] > self.players[self.player_two_name]:
                return 'Win for Dave'
            else:
                return 'Win for Seb'

        if self.players[self.player_one_name] > self.players[self.player_two_name]:
            return 'Advantage Dave'
        else:
            return 'Advantage Seb'

