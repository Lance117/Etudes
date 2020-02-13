import random

"""
Write a Poker Program

poker(hands: List[hand]) -> hand
hand_rank(hand: Hand) -> rank

hand rank concepts: n-kind, straight, flush, two-pair
"""

mydeck = [r+s for r in '23456789TJQKA' for s in 'HSCD']

def deal(numhands, n=5, deck=mydeck):
    """Builds a deck of 52 cards"""
    random.shuffle(deck)
    return [deck[n*i:n*(i+1)] for i in range(numhands)]

def poker(hands):
    """
    Return the best hand: poker([hand,...]) => hand
    """
    return allmax(hands, key=hand_rank)

def allmax(iterable, key=None):
    """Return a list of all items equal to the max of the iterable."""
    res, maxval = [], None
    key = key or (lambda x: x)
    for x in iterable:
        cur_val = key(x)
        if not res or cur_val > maxval:
            res, maxval = [x], cur_val
        elif cur_val == maxval:
            res.append(x)
    return res

def hand_rank(hand):
    """
    Returns rank for a hand. Idea is to use tuple comparison to evaluate hand rank.
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

def card_ranks(cards):
    """Return a list of ranks, sorted with higher first"""
    ranks = ['__23456789TJQKA'.index(r) for r,s in cards]
    ranks.sort(reverse=True)
    return [5,4,3,2,1] if ranks == [14,5,4,3,2] else ranks

def straight(ranks):
    """Return True if the ordered ranks form a 5-card straight."""
    return max(ranks) - min(ranks) == 4 and len(set(ranks)) == 5

def flush(hand):
    """Return True if all the cards have the same suit"""
    return len(set([s for r,s in hand])) == 1

def kind(n, ranks):
    """
    Return the first rank that this hand has exactly n of.
    Return None if there is no n-of-a-kind in the hand.
    """
    for rank in ranks:
        if ranks.count(rank) == n:
            return rank
    return None

def two_pair(ranks):
    """
    If there are two pair, return the two ranks as a
    tuple: (highest, lowest); otherwise return None.
    """
    pair, lowpair = kind(2, ranks), kind(2, list(reversed(ranks)))
    return (pair, lowpair) if pair and pair != lowpair else None

def test():
    """Test cases for the functions in a poker program"""
    sf = '6C 7C 8C 9C TC'.split()
    sf2 = '6D 7D 8D 9D TD'.split()
    fk = '9D 9C 9H 9S 7D'.split()
    fh = 'TD TC TH 7H 7D'.split()
    tp = '5S 5D 9H 9C 6S'.split()
    s1 = 'AS 2S 3S 4S 5C'.split() # A-5 straight
    s2 = '2C 3C 4C 5S 6S'.split()
    ah = 'AS 2S 3S 4S 6C'.split() # ace high
    sh = '2S 3S 4S 6C 7D'.split()
    fkranks = card_ranks(fk)
    tpranks = card_ranks(tp)
    assert(card_ranks(sf)) == [10, 9, 8, 7, 6]
    assert(card_ranks(fk)) == [9, 9, 9, 9, 7]
    assert(card_ranks(fh)) == [10, 10, 10, 7, 7]
    assert(kind(4, fkranks)) == 9
    assert(kind(3, fkranks)) == None
    assert(kind(2, fkranks)) == None
    assert(kind(1, fkranks)) == 7
    assert(straight([9, 8, 7, 6, 5])) == True
    assert(straight([9, 8, 7, 6, 4])) == False
    assert(straight(card_ranks(s1))) == True
    assert(flush(sf)) == True
    assert(flush(fk)) == False
    assert(two_pair(fkranks)) == None
    assert(two_pair(tpranks)) == (9, 5)
    assert(hand_rank(sf)) == (8, 10)
    assert(hand_rank(fk)) == (7, 9, 7)
    assert(hand_rank(fh)) == (6, 10, 7)
    assert(poker([sf, fk, fh])) == [sf]
    assert(poker([fk, fh])) == [fk]
    assert(poker([sf, sf2])) == [sf, sf2]
    assert(poker([fh])) == [fh]
    assert(poker([sf] + [fh] * 99)) == [sf]
    return 'tests pass'

print(test())
