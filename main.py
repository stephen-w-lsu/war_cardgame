import random

# Define card attributes
suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
ranks = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]
values = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10,
          "Jack": 11, "Queen": 12, "King": 13, "Ace": 14}


# Create Card class
class Card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"


# Create Deck class from Card class
class Deck():
    def __init__(self):
        self.whole_deck = []
        for suit in suits:
            for rank in ranks:
                self.whole_deck.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.whole_deck)

    def deal_one(self):
        return self.whole_deck.pop()


# Create Player class for each player holds half the deck
class Player():
    def __init__(self, name):
        self.name = name
        self.whole_deck = []

    def remove_card(self):
        return self.whole_deck.pop(0)

    def add_card(self, new_cards):
        if type(new_cards) == type([]):
            return self.whole_deck.extend(new_cards)
        else:
            return self.whole_deck.append(new_cards)

    def __str__(self):
        return f"Player {self.name} has {len(self.whole_deck)} cards."


# Game Setup
player_one = Player("One")
player_two = Player("Two")

new_deck = Deck()
new_deck.shuffle()

for x in range(26):
    player_one.add_card(new_deck.deal_one())
    player_two.add_card(new_deck.deal_one())


# Game Logic
game_on = True

round_num = 0

while game_on:
    round_num += 1
    print(f"Round {round_num}")

    if len(player_one.whole_deck) == 0:
        print("Player1 is out of cards! Player2 has won!")
        game_on = False
        break
    if len(player_two.whole_deck) == 0:
        print("Player2 is out of cards! Player1 has won!")
        game_on = False
        break

    player_one_cards = []
    player_one_cards.append(player_one.remove_card())

    player_two_cards = []
    player_two_cards.append(player_two.remove_card())

    at_war = True

    while at_war:

        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_card(player_one_cards)
            player_one.add_card(player_two_cards)
            at_war = False

        elif player_one_cards[-1].value < player_two_cards[-1].value:
            player_two.add_card(player_one_cards)
            player_two.add_card(player_two_cards)
            at_war = False

        else:
            print("WAR is on!")

            if len(player_one.whole_deck) < 5:
                print("Player1 has insufficient cards! Player2 has won!")
                game_on == False
                break

            elif len(player_two.whole_deck) < 5:
                print("Player2 has insufficient cards! Player1 has won!")
                game_on == False
                break

            else:
                for x in range(5):
                    player_one_cards.append(player_one.remove_card())
                    player_two_cards.append(player_two.remove_card())

