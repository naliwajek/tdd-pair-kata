from main import Tennis
import pytest

def test_unknown_player():
    game = Tennis('Dave', 'Seb')

    with pytest.raises(ValueError):
        game.won_point('Chris')

def test_player_one_wins_point():
    game = Tennis('Dave', 'Seb')
    game.won_point('Dave')

    assert game.score() == 'fifteen - love'

def test_players_score_equal():
    game = Tennis('Dave', 'Seb')
    game.won_point('Dave')
    game.won_point('Seb')

    assert game.score() == 'fifteen all'

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

def test_player_one_gets_advantage():
    game = Tennis('Dave', 'Seb')
    game.won_point('Seb')
    game.won_point('Seb')
    game.won_point('Seb')
    game.won_point('Dave')
    game.won_point('Dave')
    game.won_point('Dave')
    game.won_point('Dave')

    assert game.score() == 'Advantage Dave'

def test_game():
    game = Tennis('Dave', 'Seb')
    game.won_point('Seb')
    game.won_point('Seb')
    game.won_point('Seb')
    game.won_point('Dave')
    game.won_point('Dave')
    game.won_point('Dave')
    assert game.score() == 'Deuce'
    game.won_point('Seb')
    assert game.score() == 'Advantage Seb'
    game.won_point('Dave')
    assert game.score() == 'Deuce'
    game.won_point('Dave')
    assert game.score() == 'Advantage Dave'
    game.won_point('Dave')
    assert game.score() == 'Win for Dave'


