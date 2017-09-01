class Tennis:
    def __init__(self, player_one_name, player_two_name):
        self.player_one_name = player_one_name
        self.player_two_name = player_two_name

    def score(self):
        return 'love - love'

    def won_point(self, player_name):
        return self.score()