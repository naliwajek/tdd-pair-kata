from main import Tennis

def test_new_game():
    game = Tennis('Dave', 'Seb')

    assert game.score() == 'love - love'

def test_player_one_wins_point():
    game = Tennis('Dave', 'Seb')
    game.won_point('Dave')

    assert game.score() == 'fifteen - love'

def test_player_two_wins_point():
    game = Tennis('Dave', 'Seb')
    game.won_point('Seb')

    assert game.score() == 'love - fifteen'

def test_player_one_wins_another_point():
    game = Tennis('Dave', 'Seb')
    game.won_point('Dave')
    game.won_point('Seb')
    game.won_point('Dave')

    assert game.score() == 'thirty - fifteen'

def test_player_one_wins_game():
    game = Tennis('Dave', 'Seb')
    game.won_point('Dave')
    game.won_point('Dave')
    game.won_point('Dave')
    game.won_point('Dave')

    assert game.score() == 'Win for Dave'

def test_player_two_wins_game():
    game = Tennis('Dave', 'Seb')
    game.won_point('Seb')
    game.won_point('Seb')
    game.won_point('Seb')
    game.won_point('Seb')

    assert game.score() == 'Win for Seb'

def test_players_reach_deuce():
    game = Tennis('Dave', 'Seb')
    game.won_point('Seb')
    game.won_point('Seb')
    game.won_point('Seb')
    game.won_point('Dave')
    game.won_point('Dave')
    game.won_point('Dave')

    assert game.score() == 'Deuce'

