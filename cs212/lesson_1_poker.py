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
    """
    Returns rank for a hand
    TODO: functions to determine hand type

    straight(ranks): True if hand is straight
    flush(hand): True if hand is flush
    kind(n, ranks): returns first rank that hand has n of
    two_pair(ranks): if two pair, returns a tuple
    card_ranks(hand): returns ORDERED tuple of ranks in a hand (highest to lowest)
    """
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):
        return (8, max(ranks))
    elif kind(4, ranks):
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):
        return (6, kind(3, ranks), kind(2, ranks))
    elif flush(hand):
        return (5, ranks)
    elif straight(hand):
        return (4, max(ranks))
    elif kind(3, ranks):
        return (3, kind(3, ranks), ranks)
    elif two_pair(ranks):
        return (2, two_pair(ranks), ranks)
    elif kind(2, ranks):
        return (1, kind(2, ranks), ranks)
    else:
        return (0, ranks)

def test():
    """Test cases for the functions in a poker program"""
    sf = '6C 7C 8C 9C TC'.split()
    fk = '9D 9C 9H 9S 7D'.split()
    fh = 'TD TC TH 7H 7D'.split()
    assert(card_ranks(sf)) == [10, 9, 8, 7, 6]
    assert(card_ranks(fk)) == [9, 9, 9, 9, 7]
    assert(card_ranks(fh)) == [10, 10, 10, 7, 7]
    assert(poker([sf, fk, fh])) == sf
    assert(poker([fk, fh])) == fk
    assert(poker([fh, fh])) == fh
    assert(poker([fh])) == fh
    assert(poker([sf] + [fh] * 99)) == sf
    assert(hand_rank(sf)) == (8, 10)
    assert(hand_rank(fk)) == (7, 9, 7)
    assert(hand_rank(fh)) == (6, 10, 7)
    return 'tests pass'

print(test())