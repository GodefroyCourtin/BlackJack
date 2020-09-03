class Joueur:
    def __init__(self, name):
        self.hand=[]
        self.score=0
        self.name=name

    def calcul_hand(self, cards, name="croupier"):
        for card in cards:
            
            if card[0] == 'valet' or card[0] == 'roi' or  card[0] == 'dame':
                self.score += 10

            elif card[0] == 'as' and name != "croupier":
                choix = 0
                
                while choix != "1" and choix != "11" :
                    choix = input("choisir 1 ou 11: ")
                    
                self.score += int(choix)
            elif  card[0] == 'as' and name == "croupier":
                if self.score <= 10:
                    self.score += 11
                else:
                    self.score += 1
            else :
                self.score += int(card[0])

     



