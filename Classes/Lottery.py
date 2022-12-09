from random import choice

class Lottery():
    """Initialize a lottery ticket"""
    def __init__(self,lotterych):
        self.lotterych = lotterych
    
    def get_winning_ticket(self, lotterych):
        """This module replicates lottery."""
        winnerlist = []
        if isinstance(lotterych, list) and lotterych is not None:
            while len(winnerlist) < 4:
                item_won = choice(lotterych)
                if item_won not in winnerlist:
                    winnerlist.append(item_won)
            return winnerlist
            
lotterych = ['a','b','c','d','e',1,2,3,4,5,6,7,8,9,10]
my_picks = Lottery(lotterych)
print(f"winning lottery: {my_picks.get_winning_ticket(lotterych)}")
