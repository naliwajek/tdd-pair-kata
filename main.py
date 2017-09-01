class Tennis:
    def __init__(self, player_one_name, player_two_name):
        self.player_one_name = player_one_name
        self.player_two_name = player_two_name
        self.players = {player_one_name: 0, player_two_name: 0}
        self.score_names = {0: 'love', 1: 'fifteen', 2: 'thirty', 3: 'forty'}

    def score(self):
        try:
            if self.__is_first_deuce():
                return 'Deuce'

            if self.__scores_are_equal():
                return '{0} all'.format(self.__parse_score_for(self.player_one_name))

            return '{0} - {1}'.format(
                self.__parse_score_for(self.player_one_name),
                self.__parse_score_for(self.player_two_name))
        except KeyError:
            return self.__special_score()

    def won_point(self, player_name):
        self.players[player_name] += 1

    def __parse_score_for(self, player_name):
        return self.__parse_score(self.players[player_name])

    def __parse_score(self, score):
        return self.score_names[score]

    def __point_difference(self):
        return self.players[self.player_one_name] - self.players[self.player_two_name]

    def __scores_are_equal(self):
        return self.players[self.player_one_name] == self.players[self.player_two_name]

    def __is_first_deuce(self):
        return self.players[self.player_one_name] == 3 and self.players[self.player_two_name] == 3

    def __game_state_on(self, state, condition):
        return '{0} {1}'.format(state, self.player_one_name if condition else self.player_two_name)

    def __player_one_leads(self):
        return self.__point_difference() > 0

    def __special_score(self):
        if self.__scores_are_equal():
            return 'Deuce'

        if abs(self.__point_difference()) >= 2:
            return self.__game_state_on('Win for', self.__player_one_leads())

        return self.__game_state_on('Advantage', self.__player_one_leads())

