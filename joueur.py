class Joueur:
    def __init__(self, name):

        self.hand=[]
        self.score=0
        self.name=name

    def calcul_hand(self, name="croupier"):
        self.score = 0
        for i in self.hand[0:]:
            
            if i[0] == 'valet' or i[0] == 'roi' or i[0] == 'dame':
                self.score += 10

            elif i[0] == 'as' and name != "croupier":
                choix = 0

                while choix != "1" and choix != "11" :
                    choix = input("choisir 1 ou 11: ")
                   # il faut fixer le choix de joueur a la premiere demande; demanderqu'une seul fois et save le choix

                self.score += int(choix)

            elif i[0] == 'as' and name == "croupier":

                if self.score <= 10:
                    self.score += 10
                else:
                    self.score += 1

            else :
                self.score += int(i[0])




