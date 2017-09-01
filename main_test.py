from main import Tennis

def test_new_game():
    game = Tennis('Dave', 'Seb')

    assert game.score() == 'love - love'
