import random

suits = ('Hearts','Diamonds','Spades','clubs')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine',
        'Ten','Jack','Queen','King','Ace')
values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,
        'Ten':10,'Jack':10,'Queen':10,'King':10,'Ace':11}

playing = True

class Card():
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck():
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return 'the deck has : ' + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card

class Hand():
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]

        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

class Chips():
    def __init__(self,total=100):
        self.total = total
        self.bet = 0
    def win_bet(self):
        self.total+=self.win_bet
    def lose_bet(self):
        self.total -= self.bet

def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('How many chip to bet?'))
        except:
            print('Sorry, integer please.')
        else:
            if chips.bet > chips.total:
                print 'Sorry not enough. You have {}'.format(chips.total)
            else:
                break

    def hit(deck,hand):
        hand.add_card(deck.deal())
        hand.adjust_for_ace()

    def hit_or_stand(deck,hand):
        global playing
        while True:
            x = input('Hit or Stand? Enter h or s')
            if x[0].lower() == 'h':
                hit(deck,hand)
            elif x[0].lower() == 's'
                print('Player stands Dealer\'s Turn')
                playing = False
            else:
                print 'Sorry, not understand'
                continue
            break

def player_busts(player,dealer,chips):
    print('Bust player')
    chips.lose_bet()

def player_wins():
    print 'player wins'
    chips.win_bet()

def dealer_busts():
    print 'dealer busts'
    chips.win_bet()

def dealer_wins():
    print 'dealer wins'
    chips.lose_bet()

def push(player,dealer,chips):
    print 'Tie! Push.'

'''
test_deck = Deck()
test_deck.shuffle()
#print(test_deck)

test_player = Hand()
pulled_card = test_deck.deal()
print pulled_card
test_player.add_card(pulled_card)
print test_player.value
'''

while True:
    deck = Deck()
    deck.shuffle()
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    player_chips = Chips()

    take_bet(player_chips)

    show_some(player_hand,dealer_hand)

    while playing:
        hit_or_stand（deck,player_hand)
        show_some(player_hand,dealer_hand)

        
