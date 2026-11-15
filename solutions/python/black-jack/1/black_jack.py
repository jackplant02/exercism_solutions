"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    """Determine the scoring value of a card.

    Parameters:
        card (str): The given card.

    Returns:
        int: The value of a given card.  See below for values.

        1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
        2.  'A' (ace card) = 1
        3.  '2' - '10' = numerical value.
    """

    value_dictionary = {
        "K": 10,
        "J": 10,
        "Q": 10,
        "A": 1,
    }

    if card.isdigit():
        return int(card)
    return value_dictionary[card]


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    Parameters:
        card_one (str): First card dealt in the hand.  See below for values.
        card_two (str): Second card dealt in the hand. See below for values.

        1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
        2.  'A' (ace card) = 1
        3.  '2' - '10' = numerical value.

    Returns:
        str or tuple: The resulting tuple contains both cards if they are of equal value.
    """

    value_1 = value_of_card(card_one)
    value_2 = value_of_card(card_two)

    if value_2 > value_1:
        return card_two

    if value_1 > value_2:
        return card_one

    return card_one, card_two


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for an upcoming ace card.

    Parameters:
        card_one (str): First card dealt in the hand.  See below for values.
        card_two (str): Second card dealt in the hand. See below for values.

        1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
        2.  'A' (ace card) = 11 (if already in hand)
        3.  '2' - '10' = numerical value.

    Returns:
        int: Either 1 or 11, which is the value of the upcoming ace card.
    """

    if any(x == "A" for x in [card_one, card_two]):
        return 1

    current_sum = value_of_card(card_one) + value_of_card(card_two)

    if current_sum > 10:
        return 1

    return 11


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    Parameters:
        card_one (str): First card dealt in the hand.  See below for values.
        card_two (str): Second card dealt in the hand. See below for values.

        1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
        2.  'A' (ace card) = 11 (if already in hand)
        3.  '2' - '10' = numerical value.

    Returns:
        bool: Is the hand is a blackjack (two cards worth 21).
    """

    # Source - https://stackoverflow.com/a/16138094
    # Posted by David Alber, modified by community. See post 'Timeline' for change history
    # Retrieved 2026-11-15, License - CC BY-SA 3.0

    card_list = [card_one, card_two]

    any_ten = len({"10", "J", "Q", "K"}.intersection(card_list)) > 0
    any_ace = any(x == "A" for x in card_list)

    return bool(any_ten and any_ace)


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

     Parameters:
         card_one (str): First card in the hand.
         card_two (str): Second card in the hand.

    Returns:
         bool: Can the hand be split into two pairs? (i.e. cards are of the same value).
    """

    return bool(value_of_card(card_one) == value_of_card(card_two))


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    Parameters:
        card_one (str): First card in the hand.
        card_two (str): Second card in the hand.

    Returns:
        bool: Can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """
    value_1 = value_of_card(card_one)
    value_2 = value_of_card(card_two)

    return 9 <= value_1 + value_2 <= 11
