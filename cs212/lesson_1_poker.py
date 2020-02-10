"""
Write a Poker Program

poker(hands: List[hand]) -> hand
hand_rank(hand: Hand) -> rank

hand rank concepts: n-kind, straight, flush
"""

def poker(hands):
    """
    Return the best hand: poker([hand,...]) => hand
    TODO: define max function that returns best hand
    """
    return max(hands)