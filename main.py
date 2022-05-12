# We want to use a normal distribution

import numpy

# Generic card classes

class Card:
  pass

class Pack:
  def __init__(self, cards=[]):
    self.cards = cards

  def __repr__(self):
    return str(self.cards)

  def is_empty(self):
    return self.cards == []

  @property
  def len(self):
    return len(self.cards)
  
  def deal_card(self):
    if self.cards:
      return self.cards.pop()
    else:
      raise ValueError('Pack is empty')
      
  def deal_pack(self, num=1):
    if num > len(self.cards):
      raise ValueError('Insufficient cards in pack')
    else:
      dealt = []
      for i in range(num):
        dealt.append(self.cards.pop())
    return Pack(dealt)

  def cut(self, loc=None, tol=None):
        
    if not loc:
      loc = len(self.cards) // 2

    if not tol:
      tol = len(self.cards) // 4

    place = numpy.random.normal(loc, tol)

    return Pack(self.cards[:place]), Pack(self.cards[place:])
      

# This is specific to playing cards

# A class to describe a suit

class Suit:
  def __init__(self, name, order):
    self.name = name
    self.order = order

  def __repr__(self):
    return self.name

  def __lt__(self, other):
    return self.order < other.order

# A class to describe a rank

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

class PlayingCardPack(Pack):
  def __init__(self):
    super().__init__()
    
    for s in PlayingCard.suits:
      for r in PlayingCard.ranks:
        self.cards.append(PlayingCard(r, s))


if __name__ == '__main__':
  pack = PlayingCardPack()
  c = pack.deal_card()
  print(c)
  p = pack.deal_pack(10)
  print(p)
  
  