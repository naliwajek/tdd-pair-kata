class Tennis:
    def __init__(self, player_one_name, player_two_name):
        self.player_one_name = player_one_name
        self.player_two_name = player_two_name
        self.player_one_score = 'love'
        self.player_two_score = 'love'

    def score(self):
        return self.player_one_score + ' - ' + self.player_two_score

    def won_point(self, player_name):
        self.player_one_score = 'fifteen'
