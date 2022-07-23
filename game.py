from cards import Card
import random


class Game:
    def __init__(self):
        self.size = 4
        self.card_options = ['Add', 'Sub', 'Mul', 'Dev', 'Cut', 'Gum', 'Egg', 'Gem']
        self.columns =  ['A', 'B', 'C', 'D']
        self.cards = []
        self.locations = []

        for column in self.columns:
            for num in range(1, self.size + 1):
                self.locations.append(f'{column}{num}')

    def set_cards(self):
        used_locations = []
        for word in self.card_options:
            for i in range(2):
                available_locations = set(self.locations) - set(used_locations)
                random_locations = random.choice(list(available_locations))
                used_locations.append(random_locations)
                card = Card(word, random_locations)
                self.cards.append(card)
    def create_row(self, num):
        row = []
        for column in self.columns:
            for card in self.cards:
                if card.locations == f'{column}{num}':
                    if card.matched:
                        row.append(str(card))
                    else:
                        row.append('   ')
        return row 
    def create_grid(self):
        # / A / B / C / D / 
        header = ' |  ' + '  |  '.join(self.columns) + '  |'
        print(header) 
        for row in range(1, self.size + 1 ):
            print_row = f'{row}| '
            get_row = self.create_row(row)  
            print_row += ' | '.join(get_row)  +  ' |'
            print(print_row)

    def check_match(self, loc1, loc2):
        cards = []
        for card in self.cards:
            if card.locations == loc1 or card.locations == loc2:
                cards.append(card)
        if cards[0] == cards[1]:
            cards[0].matched = True
            cards[1].matched = True
            return True
        else:
            for card in cards:
                print(f'{card.locations}: {card}')
            return False

    def check_win(self):
        for card in self.cards:
            if card.matched == False:
                return False
        return True

    def check_location(self, time):
        while True:
            guess = input(f"what's the location of your {time} card? ")
            if guess.upper() in self.locations:
                return guess.upper()
            else:
                print("That's not a valid location of Guess. It should look like this A1:(ranges between A1 to A4 or B1 TO B4 or C1 TO C4 or D1 to D4)")

    def start_game(self):
        game_running = True
        print("The Guess skills Game")
        self.set_cards()
        while game_running:
            self.create_grid()
            guess1 = self.check_location("first")
            guess2 = self.check_location("second")
            if self.check_match(guess1, guess2):
                if self.check_win():
                    print("Congrats!! You have guessed them all!")
                    self.create_grid()
                    game_running = False
            else:
                input("Those cards are not matched. Press Enter to continue")
        print("GAME OVER !!!!!!!!!!!")           

#dunder main
if __name__ == '__main__':
    game = Game()
    game.start_game()
    
    

    
