# We want to use a normal distribution

import numpy


# Generic card classes

class Card:
    pass


class Deck:
    def __init__(self, cards=[]):
        self.cards = cards

    def __repr__(self):
        return str(self.cards)

    def __bool__(self):
        return bool(self.cards)

    def is_empty(self):
        return self.cards == []

    def push(self, card):
        self.cards.append(card)

    @property
    def len(self):
        return len(self.cards)

    def merge_below(self, other):
        self.cards = self.cards + other.cards

    def merge_above(self, other):
        self.cards = other.cards + self.cards

    def deal_card(self):
        if self.cards:
            return self.cards.pop()
        else:
            raise ValueError('Deck is empty')

    def deal(self, num=1):
        deal_deck = []
        for i in range(num):
            if self.cards:
                deal_deck.append(self.cards.pop())
        return Deck(deal_deck)

    def cut(self, loc=None, tol=None):

        if not loc:
            loc = len(self.cards) // 2

        if not tol:
            tol = len(self.cards) // 4

        place = int(numpy.random.normal(loc, tol))

        self.cards, right = self.cards[:place], self.cards[place:]

        return Deck(right)

    def cut_shuffle(self, num=7):
        for i in range(num):
            right = self.cut()

            self.merge_above(right)

    def insert(self, pos, other):
        self.cards = self.cards[:pos] + other.cards + self.cards[pos:]

    def riffle_merge(self, other, lam=4):
        riffle_pos = 0

        while other:
            left_num = int(numpy.random.poisson(lam))
            right_num = int(numpy.random.poisson(lam))

            self.insert(riffle_pos, other.deal(right_num))

            riffle_pos += left_num + right_num

    def riffle_shuffle(self, num=10):
        for i in range(num):
            right = self.cut()
            self.riffle_merge(right)


# This is specific to playing cards

# A class to describe a suit

class Suit:
    def __init__(self, name, order):
        self.name = name
        self.order = order

    def __repr__(self):
        return self.name

    def __lt__(self, other):
        return self.order < other.order


# A class to describe a rank

class Rank:
    def __init__(self, name, order, picture=False):
        self.name = name
        self.order = order
        self.picture = picture

    def __repr__(self):
        return self.name

    def __lt__(self, other):
        return self.order < other.order


# Now the playing cards themselves

class PlayingCard(Card):
    hearts = Suit('Hearts', 1)
    clubs = Suit('Clubs', 2)
    diamonds = Suit('Diamonds', 3)
    spades = Suit('Spades', 4)

    suits = [hearts, clubs, diamonds, spades]

    ace = Rank('Ace', 14, picture=True)
    two = Rank('Two', 2)
    three = Rank('Three', 3)
    four = Rank('Four', 4)
    five = Rank('Five', 5)
    six = Rank('Six', 6)
    seven = Rank('Seven', 7)
    eight = Rank('Eight', 8)
    nine = Rank('Nine', 9)
    ten = Rank('Ten', 10)
    jack = Rank('Jack', 11, picture=True)
    queen = Rank('Queen', 12, picture=True)
    king = Rank('King', 13, picture=True)

    ranks = [ace,
             two,
             three,
             four,
             five,
             six,
             seven,
             eight,
             nine,
             ten,
             jack,
             queen,
             king
             ]

    @classmethod
    def full_deck(cls):
        build_deck = Deck()
        for s in cls.suits:
            for r in cls.ranks:
                build_deck.push(PlayingCard(r, s))
        return build_deck

    def __init__(self, rank=ace, suit=spades):
        if rank in self.ranks:
            self.rank = rank
        else:
            raise ValueError('Needs to be a valid card rank')
        if suit in self.suits:
            self.suit = suit
        else:
            raise ValueError('Needs to be a valid card suit')

    def __repr__(self):
        return f'{self.rank} of {self.suit}'


if __name__ == '__main__':
    deck = PlayingCard.full_deck()

    print(deck)

    deck.riffle_shuffle(1)

    print(deck)

    a = deck.deal(7)

    print(a)

    b = deck.deal(7)

    print(b)
