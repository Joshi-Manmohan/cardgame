import random

# Define the card deck
SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
DECK = [(rank, suit) for suit in SUITS for rank in RANKS]

# Function to get the value of a card
def card_value(card):
    return RANKS.index(card[0])  # Returns the index of the rank

# Function to draw a card
def draw_card(deck):
    return random.choice(deck)

def play_game():
    deck = DECK.copy()
    score = 0
    current_card = draw_card(deck)
    
    print("Welcome to Higher or Lower!")
    print(f"Your starting card is: {current_card[0]} of {current_card[1]}")

    while True:
        next_card = draw_card(deck)
        print("\nNext card is drawn.")
        guess = input("Will the next card be higher or lower? (h/l): ").lower()

        if guess not in ['h', 'l']:
            print("Invalid input! Please enter 'h' for higher or 'l' for lower.")
            continue

        print(f"The next card is: {next_card[0]} of {next_card[1]}")

        if (card_value(next_card) > card_value(current_card) and guess == 'h') or \
           (card_value(next_card) < card_value(current_card) and guess == 'l'):
            score += 1
            print(f"You guessed right! Your score is now: {score}")
        else:
            print(f"You guessed wrong. Your final score is: {score}")
            break
        
        current_card = next_card
        
        # Remove drawn card from the deck
        deck.remove(next_card)

        if len(deck) == 0:
            print("No more cards left in the deck. Thanks for playing!")
            break

if __name__ == "__main__":
    play_game()
