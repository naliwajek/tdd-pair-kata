from main import Tennis

def test_new_game():
    game = Tennis('Dave', 'Seb')

    assert game.score() == 'love - love'

def test_player_one_wins_point():
    game = Tennis('Dave', 'Seb')

    game.won_point('Dave')

    assert game.score() == 'fifteen - love'
