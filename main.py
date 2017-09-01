class Tennis:
    def __init__(self, player_one_name, player_two_name):
        self.player_one_name = player_one_name
        self.player_two_name = player_two_name
        self.player_one_score = 'love'
        self.player_two_score = 'love'

        self.players = {player_one_name: 'love', player_two_name: 'love'}

    def score(self):
        return self.players['Dave'] + ' - ' + self.players['Seb']

    def won_point(self, player_name):
        self.players[player_name] = 'fifteen'
