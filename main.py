class Tennis:
    def __init__(self, player_one_name, player_two_name):
        self.player_one_name = player_one_name
        self.player_two_name = player_two_name
        self.players = {player_one_name: 0, player_two_name: 0}
        self.score_names = {0: 'love', 1: 'fifteen', 2: 'thirty', 3: 'fourty'}

    def score(self):
        return '{0} - {1}'.format(self.__parse_score(self.players[self.player_one_name]),
            self.__parse_score(self.players[self.player_two_name]))

    def won_point(self, player_name):
        self.players[player_name] += 1

    def __parse_score(self, score):
        return self.score_names[score]
