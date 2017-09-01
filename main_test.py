import pytest
import main


def test_tennis_game_class():
    assert main.TennisGame('Alice', 'Bob')


def test_player_has_score():
    t = main.TennisGame('Alice', 'Bob')
    assert t.score() == 'Love-Love'


def test_player_wins_point():
    t = main.TennisGame('Alice', 'Bob')
    t.won_point('Alice')
    assert t.score() == 'Fifteen-Zero'


def test_player_leads_by_two_points():
    t = main.TennisGame('Alice', 'Bob')
    t.won_point('Alice')
    t.won_point('Alice')
    assert t.score() == 'Thirty-Zero'


def test_player_one_wins():
    t = main.TennisGame('Alice', 'Bob')
    t.won_point('Alice')
    t.won_point('Alice')
    t.won_point('Alice')
    t.won_point('Alice')
    assert t.score() == 'Won for Alice'


def test_player_two_wins():
    t = main.TennisGame('Alice', 'Bob')
    t.won_point('Bob')
    t.won_point('Bob')
    t.won_point('Bob')
    t.won_point('Bob')
    assert t.score() == 'Won for Bob'

def the_game_ends():
    t = main.TennisGame('Alice', 'Bob')
    t.won_point('Bob')
    t.won_point('Bob')
    t.won_point('Bob')
    t.won_point('Bob')
    with pytest.raises(main.GameOverException):
        t.won_point('Bob')

def test_unknown_cannot_win_point():
    t = main.TennisGame('Alice', 'Bob')
    with pytest.raises(main.UnknownPlayerException):
        t.won_point('Sally')


def test_translator():
    translator = main.PointTranslator()
    assert translator.translate(0, 0) == 'Love-Love'
    assert translator.translate(1, 1) == 'Fifteen-All'
    assert translator.translate(0, 1) == 'Zero-Fifteen'
    assert translator.translate(0, 2) == 'Zero-Thirty'
    assert translator.translate(2, 2) == 'Thirty-All'
    assert translator.translate(3, 2) == 'Fourty-Thirty'
    assert translator.translate(3, 3) == 'Deuce'
    assert translator.translate(4, 4) == 'Deuce'
    assert translator.translate(14, 14) == 'Deuce'

def test_advantage():
    t = main.TennisGame('Alice', 'Bob')
    t.won_point('Bob')
    t.won_point('Alice')
    t.won_point('Bob')
    t.won_point('Alice')
    t.won_point('Bob')
    t.won_point('Alice')
    t.won_point('Bob')
    t.won_point('Alice')
    t.won_point('Bob')
    t.won_point('Alice')
    t.won_point('Bob')
    t.won_point('Alice')
    t.won_point('Alice')

    assert t.score() == 'Advantage for Alice'

def won_after_advantage():
    t = main.TennisGame('Alice', 'Bob')
    t.won_point('Bob')
    t.won_point('Alice')
    t.won_point('Bob')
    t.won_point('Alice')
    t.won_point('Bob')
    t.won_point('Alice')
    t.won_point('Bob')
    t.won_point('Alice')
    t.won_point('Bob')
    t.won_point('Alice')
    t.won_point('Bob')
    t.won_point('Alice')
    t.won_point('Alice')
    t.won_point('Alice')
    t.won_point('Alice')

    assert t.score() == 'Won for Alice'

def won_after_advantage_for_second_player():
    t = main.TennisGame('Alice', 'Bob')
    t.won_point('Bob')
    t.won_point('Alice')
    t.won_point('Bob')
    t.won_point('Alice')
    t.won_point('Bob')
    t.won_point('Alice')
    t.won_point('Bob')
    t.won_point('Alice')
    t.won_point('Bob')
    t.won_point('Alice')
    t.won_point('Bob')
    t.won_point('Bob')

    assert t.score() == 'Won for Bob'
