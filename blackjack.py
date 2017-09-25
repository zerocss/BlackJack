import random
    
class Player(object):
    
    wins = 0
    losses = 0
    busts = 0
    
    hand = []
    
    total = 0
    
    def __init__(self, money = 100):
        self.money = money
        
    def bet(self, amount):
        self.amount = amount
        while True: #loop uintil you get an integer
            try:
                amount = int(amount)
            except:
                # print("Enter a number. It has to be less than $%s" %(self.money))
                amount = input("Enter a number less than $%s: " %(self.money))
                continue
            else:
                if amount > self.money:
                    amount = input("Try Again - Enter a number less than $%s: " %(self.money))
                elif self.money == 0:
                    print("You don't have any money left. Can't bet anything")
                    break
                else:
                    print("Betting: $%s" %(amount))
                    self.money -= amount
                    print("You now have $%s left" %(self.money))
                    break
                
    def add_money(self, amount):
        self.amount = amount
        self.money += amount
        
    def get_stats(self):
        print("Wins: %s, Losses: %s, Busts: %s" %(self.wins, self.losses, self.busts))
        
    def add_to_hand(self, card, card_value):
        self.card = card
        self.card_value = card_value
        #Add the card to the player's hand
        self.hand.append(card)
        #Add card's value to the player's total
        #Try to handle the ace
        if card[1] == "A":
            #If 11 would put the total over 21, then change the ace amount to 1
            if (self.total + 11) > 21:
                self.total += 1
            else:
                self.total += 11
        else:
            self.total += card_value
            
    def see_hand(self):
        print(self.hand)
        
#------------------------------------------------------------------------------
class Deck(object):
    
    card_face = ("Hearts", "Spades", "Clubs", "Diamonds")
    card_value = {"A": 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10,
                    "J": 10, "Q": 10, "K": 10}
    cards_used = []
    card_drawn = 0

#[0] Hearts
#[1] Spades
#[2] Clubs
#[3] Diamonds
    
    def __init__(self):
        pass
    
    def random_card(self):
        face = random.randint(0,3)
        value = random.randint(1, 13)
        #if the value lands on 1,11,12 or 13, need to change value to
        #A, J, Q, or K
        if value == 1:
            value = "A"
        elif value == 11:
            value = "J"
        elif value == 12:
            value = "Q"
        elif value == 13:
            value = "K"
            
        card = [value, face]
        
        return card
    

    def deal_card(self):
        
        self.card_drawn = self.random_card()
        
        #check to see if the card has been used already
        i = 0
        while i < len(self.cards_used):
            if self.cards_used[i] == self.card_drawn:
                #draw a new random card and restart the loop
                self.card_drawn = self.random_card()
                i = 0
            else:
                i += 1
        
        
        print("You receive: %s of %s" %(self.card_drawn[0], self.card_face[self.card_drawn[1]]))
        self.cards_used.append(self.card_drawn)
        
    #Return the card drawn to add it to hand
    def add_card_drawn(self):
        return self.card_drawn
    
    #Get the card value associated with the dictionary's key
    def get_card_value(self):
        card = self.card_drawn
        return self.card_value[card[0]]
#-------------------------------------------------------------------------------

p1 = Player()
deck = Deck()

def player_input():
    decision = input("Hit or Stay?: ")
    
    while decision.lower() != "hit" and decision.lower() != "stay":
        decision = input("Try Again - Choose either Hit or Stay: ")
    else:
        return decision

#First dealing of cards
deck.deal_card()
add_card = deck.add_card_drawn()
card_value = deck.get_card_value()

p1.add_to_hand(add_card, card_value)

deck.deal_card()
add_card = deck.add_card_drawn()
card_value = deck.get_card_value()

p1.add_to_hand(add_card, card_value)
        

while p1.total != 21 and p1.total < 21:
    
    bet_amount = input("How much would you like to bet?")
    p1.bet(bet_amount)
    decision = player_input()

    deck.deal_card()
    add_card = deck.add_card_drawn()
    card_value = deck.get_card_value()

    p1.add_to_hand(add_card, card_value)
    p1.see_hand()
    print(p1.total)
    
    if p1.total == 21:
        print("You hit BlackJack!")
    elif p1.total > 21:
        print("Sorry you busted")