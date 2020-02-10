"""
Write a Poker Program

poker(hands: List[hand]) -> hand
hand_rank(hand: Hand) -> rank

hand rank concepts: n-kind, straight, flush
"""

def poker(hands):
    """
    Return the best hand: poker([hand,...]) => hand
    TODO: define max key to calculate value of hands
    """
    return max(hands, key=hand_rank)

def hand_rank(hand):
    """Returns rank for a hand"""
    return None

def test():
    """Test cases for the functions in a poker program"""
    sf = '6C 7C 8C 9C TC'.split()
    fk = '9D 9C 9H 9S 7D'.split()
    fh = 'TD TC TH 7H 7D'.split()
    assert(poker([sf, fk, fh])) == sf
    assert(poker([fk, fh])) == fk
    assert(poker([fh, fh])) == fh