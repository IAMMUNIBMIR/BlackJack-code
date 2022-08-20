import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True

class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        return self.suit+ ' of '+self.rank

class Deck:
    
    def __init__(self):
        self.decklist = []
        for suit in suits:
            for rank in ranks:
                self.decklist.append(Card(suit,rank))
                
    def __str__(self):
        deckcomp = ''
        for card in self.decklist:
            deckcomp += '\n'+ card.__str__()
        return 'The deck has: '+deckcomp

    def shuffle(self):
        random.shuffle(self.decklist)

    def Dealcard(self):
        return self.decklist.pop()

class Hand:
    def __init__(self):
        self.cards = []
        self.aces = 0
        self.value = 0

    def add_card(self,card):
        self.cards.append(card)
        self.value = values[card.rank] + self.value
        
        if card.rank == 'Ace':
            self.aces = self.aces + 1

    def Acevalue(self):
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1

class Chips:
    def __init__(self):
       self.totalchips = 100
       self.bet = 0

    def win_bet(self):
        self.totalchips += self.bet

    def lose_bet(self):
        self.totalchips -= self.bet

def Take_bet(chips):
    
    while True:
        
        try:
            chips.bet = int(input('Please enter your bet'))

        except:
            print('Please enter a valid arguement')

        else:
            if chips.bet > chips.totalchips:
                print('You dont have sufficient chips,You only have:{}'.format(chips.total))
            else:
                break

def Hit(Deck,Hand):

    Hand.add_card(Deck.Dealcard())
    Hand.Acevalue()

def hit_or_stand(Deck,Hand):
    global playing
    while playing == True:
        choice = input('Would you like to hit or stand? Enter H or S')
        Move = choice[0].upper()
        if Move == "H":
            Hit(Deck,Hand)
        else:
            if Move == "S":
                print("Player stand, Dealers's turn ")
                playing = False

            else:
                print('Please enter a valid input')
            continue
        break

def revealpartialcards(player,dealer):
    print("\n Dealer's Hand: ")
    print("First card is hidden")
    print(dealer.cards[1])
    
    print("\n Player's Hand")
    for card in player.cards:
        print(card)

def revealallcards(player,dealer):
    print("\n Dealer's Hand")
    for card in dealer.cards:
        print(card)

    print("Value of the Dealer's hand is: {}".format(dealer.value))
    
    print("\n Player's Hand")
    for card in player.cards:
        print(card)

    print("Value of the Player's hand is: {}".format(player.value))

def player_busts(player,dealer,Chips):
    print('Player has BUST')
    Chips.lose_bet()

def player_wins(player,dealer,Chips):
    print("Player wins!")
    Chips.win_bet()

def dealer_busts(player,dealer,Chips):
    print('Dealer has BUSTED, Player wins')
    Chips.win_bet()
    
def dealer_wins(player,dealer,Chips):
    print("Player lost! Dealer wins")
    Chips.lose_bet()
   
def push(player,dealer):
    print('Dealer and player have tied! PUSH')



while True:
    print('Welcome to BlackJack')

    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.Dealcard())
    player_hand.add_card(deck.Dealcard())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.Dealcard())
    dealer_hand.add_card(deck.Dealcard())

    player_chips = Chips()

    Take_bet(player_chips)

    revealpartialcards(player_hand,dealer_hand)

    while playing:

        hit_or_stand(deck,player_hand)

        revealpartialcards(player_hand,dealer_hand)

        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,Chips)
            break

        if player_hand.value <= 21:

            while dealer_hand.value < 17:
                Hit(deck,dealer_hand)
                
                revealallcards(player_hand,dealer_hand)

            if dealer_hand.value > 21:
                dealer_busts(player_hand,dealer_hand,player_chips)

            elif player_hand.value < dealer_hand.value:
                dealer_wins(player_hand,dealer_hand,player_chips)

            elif player_hand.value > dealer_hand.value:
                player_wins(player_hand,dealer_hand,player_chips)

            else:
                push(player_hand,dealer_hand)

        print("Player's remaining chips {}".format(player_chips.totalchips))

        Restartgame = input('Would you like to play again')

        if Restartgame[0].upper() == "Y":
            playing = True
            continue
        else:
            print('Thanks for playing')

            break

            

            

                
                
                

                


        


































#Task link : https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/blob/master/08-Milestone%20Project%20-%202/02-Milestone%20Project%202%20-%20Walkthrough%20Steps%20Workbook.ipynb
#Solution link: https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/blob/master/08-Milestone%20Project%20-%202/03-Milestone%20Project%202%20-%20Complete%20Walkthrough%20Solution.ipynb
