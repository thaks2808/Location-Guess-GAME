#class card
#holds a card
#matched or not?
#location
#__eq__ method to compare matches
#__str__ to print thr grid

class Card:
    def __init__(self, card, locations) -> None:
        self.card = card
        self.locations = locations
        self.matched = False

    def __eq__(self, other) -> bool:
        return self.card == other.card
    
    def __str__(self):
        return self.card

if __name__ == '__main__':
    card1 = Card('egg', 'A1')
    card2 = Card('egg', 'B1')
    card3 = Card('hut', 'D4')

    print(card1 == card2)
    print(card1 == card3)

