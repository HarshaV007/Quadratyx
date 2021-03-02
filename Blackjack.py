# Game of Blackjack
import random


# Classes

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{self.rank} of {self.suit}'


class Deck:

    def __init__(self, type_of_deck='empty'):
        self.cards = []
        if type_of_deck == 'full':
            for suit in suits:
                for num in ranks:
                    self.cards.append(Card(suit, num))

    def __str__(self):
        temp_string = ''
        for card in self.cards:
            temp_string += str(card)
            temp_string += ', '
        return temp_string

    def __len__(self):
        return len(self.cards)

    def draw_card(self, position=0):
        if self.cards:
            if position == 'top':
                position = 0
            elif position == 'bottom':
                position = -1
            elif position == 'random':
                position = random.randrange(len(self))
            return self.cards.pop(position)
        else:
            return False

    def insert_card(self, card, position=0):
        if not isinstance(card, Card):
            raise TypeError("Given object is not a Card")
        if position == 'top':
            position = 0
        elif position == 'bottom':
            position = -1
        elif position == 'random':
            position = random.randrange(len(self))
        self.cards.insert(position, card)

    def view_card(self, position=0):
        if self.cards:
            if position == 'top':
                position = 0
            elif position == 'bottom':
                position = -1
            elif position == 'random':
                return random.choice(self.cards)
            return str(self.cards[position])
        else:
            return 'None'

    def shuffle(self):
        random.shuffle(self.cards)

    def clear(self):
        self.cards = []


class Hand(Deck):
    def __init__(self):
        Deck.__init__(self)
        self.points = 0

    def calculate_points(self):
        aces = 0
        self.points = 0
        for card in self.cards:
            if isinstance(card.rank, int):
                self.points += card.rank
            elif card.rank == 'Ace':
                self.points += 1  # aces at minimum has a value of 1
                aces += 1
            elif isinstance(card.rank, str):
                self.points += 10
        while self.points <= 11 and aces > 0: # Tallying up aces as that is all that's left
            self.points += 10
            aces -= 1

    def insert_card(self, card, position=0):  # Extending the method in order to account for revised points after each
        # card is added
        Deck.insert_card(self, card, position)
        self.calculate_points()


class Player:
    def __init__(self, name, starting_cash=0):
        self.hand = Hand()  # initialise an empty hand object
        self.in_game = True
        self.account = starting_cash
        self.victory_state = False
        self.name = name

    def __str__(self):
        return self.name

    def bet(self, amount):
        if amount > self.account or amount < 0:
            raise ValueError('Balance_Exceeded or invalid value')
        else:
            self.account -= amount
            return amount

    def payout(self, amount):
        self.account += amount
        return True


# Functions

def display_state(deck, dealer, player, type_of_display='partial'):
    print('---------------------------------------------------------------------')
    print('Deck                    Dealer                  Player')
    print(f'{len(deck)} cards left           {len(dealer.hand)} cards on hand         {len(player.hand)} cards on hand')
    if type_of_display == 'full':
        print(f'                        points : {dealer.hand.points}             points : {player.hand.points}')
    else:
        print(
            f'                        Top card : {dealer.hand.view_card("bottom"):{15}}     points : {player.hand.points}')
    print(f'Cards in hand : {player.hand}')
    if type_of_display == 'full':
        print(f"Cards in dealer's hand : {dealer.hand}")
    print(f"Account Balance : {player.account}      Pool : {pool}      Dealer's Balance : {dealer.account}")
    print('--------------------------------------------------------------------')


# Function to payout depending on victor which is read from a boolean state (player.victory_state) in their objects

def victory_result(dealer, player, prize_pool):
    if dealer.victory_state and not player.victory_state:
        dealer.payout(prize_pool)
        print('The house has won, Better luck next time')
    elif player.victory_state and not dealer.victory_state:
        player.payout(prize_pool)
        print('Congratulations on your victory, care for another try on your luck?')
    return 0


def ask_for_new_game():
    while True:
        if input('Another run? Enter y to continue, enter any other key to exit ').upper() == 'Y':
            return True
        else:
            return False


def check_for_bust(player_1, player_2):
    if player_1.hand.points > 21:
        player_1.in_game = False
        player_2.in_game = False
        player_2.victory_state = True
        print(f'{player_1} has BUST!')


def no_bust_victory_check(player, dealer):
    if not player.victory_state and not dealer1.victory_state:
        if dealer.hand.points >= player1.hand.points:
            dealer.victory_state = True
        else:
            player.victory_state = True


def make_bet(player, dealer):
    game_state1 = True
    prize_pool = 0
    while True:
        if player.account == 0:  # End the game when player is out of cash
            print('Your account is empty, Game over!')
            game_state1 = False
            break
        if game_state1:
            try:
                prize_pool = player.bet(int(input('Enter the amount to bet ')))
                if dealer1.account < prize_pool:  # End the game when dealer is out of cash
                    print('Dealer cannot bet that amount anymore, Game Over!')
                    game_state1 = False
                    break
                prize_pool += dealer.bet(prize_pool)
                break
            except ValueError:
                print('Enter a proper value')
    return prize_pool, game_state1


def player_action(player, dealer, deck_in_play):
    while player.in_game or dealer.in_game:
        if player.in_game:
            while True:  # while loop to force proper input
                try:
                    control_value = input("Enter your choice - (H)it or (S)tand ").upper()
                    if control_value == 'H':
                        player.hand.insert_card(deck_in_play.draw_card())
                        break
                    elif control_value == 'S':
                        player.in_game = False
                        break
                    else:
                        print('Invalid value try again!')

                except TypeError:
                    print('Invalid value try again!')
        display_state(deck_in_play, dealer, player)

        check_for_bust(player, dealer)

        if dealer.in_game and dealer.hand.points <= break_point:  # Break off point is 16 right?
            dealer.hand.insert_card(deck_in_play.draw_card())
            display_state(deck_in_play, dealer, player)
        else:
            dealer.in_game = False

        check_for_bust(dealer, player)


if __name__ == "__main__":

    # Suits and Cards for creating a full deck

    suits = ('Spades', 'Hearts', 'Clubs', 'Diamonds')
    ranks = ('Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King')

    # Constants
    break_point = 16
    player_starting_cash = 1000
    dealer_starting_cash = 2000

    # Initialisation of game variables
    pool = 0
    playing_deck = Deck('full')
    playing_deck.shuffle()
    player1 = Player('Player', player_starting_cash)
    dealer1 = Player('House', dealer_starting_cash)
    game_state = True

    # Main loop

    while game_state and len(playing_deck) > 10:

        player1.in_game = True
        player1.victory_state = False
        dealer1.in_game = True
        dealer1.victory_state = False
        player1.hand.clear()
        dealer1.hand.clear()

        display_state(playing_deck, dealer1, player1)
        # Let the player bet an amount and force a proper input
        pool, game_state = make_bet(player1, dealer1)  # Tuple unpacking for multiple values...

        if not game_state:  # break out of main game session since either the Player or the House has lost
            break

        # Initially draw 2 cards each for dealer and player
        for i in range(0, 2):
            dealer1.hand.insert_card(playing_deck.draw_card())
            player1.hand.insert_card(playing_deck.draw_card())
            display_state(playing_deck, dealer1, player1)

        # Let the player and dealer hit until they stand
        player_action(player1, dealer1, playing_deck)

        no_bust_victory_check(player1, dealer1)
        pool = victory_result(dealer1, player1, pool)
        display_state(playing_deck, dealer1, player1, 'full')
        game_state = ask_for_new_game()