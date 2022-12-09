from random import choice
from Lottery import Lottery as Lottery

class LotteryAnalysis():
    """Initialize an analysis of lottery"""
    def __init__(self,lotterych):
        self.lottery_pick = Lottery(lotterych)

    def lotterypick(self, lotterych):
        """This module is used to replicate the lottery module."""
        ticket = []
        if isinstance(lotterych, list) and lotterych is not None:
            while len(ticket) < 4:
                item_won = choice(lotterych)
                if item_won not in ticket:
                    ticket.append(item_won)
            return ticket

    def check_ticket(self, played_ticket, lotterych):
        """Compare the original lottery and the duplicate lottery."""
        if isinstance(lotterych, list) and isinstance(played_ticket, list) and lotterych is not None and played_ticket is not None:
            for element in played_ticket:
                if element not in lotterych:
                    return False
            return True
            """if lotterych==played_ticket:
                return True
            else:
                return False"""

    def analyze(self, lotterych): 
        """analyze two tickets and find the number of tries it takes to get the lottery."""
        plays = 0
        won = False

        # Let's set a max number of tries, in case this takes forever!
        max_tries = 1_000_000 

        winning_ticket = self.lottery_pick.get_winning_ticket(lotterych)
        while not won:
            new_ticket = LotteryAnalysis.lotterypick(self, lotterych)
            won = LotteryAnalysis.check_ticket(self, new_ticket, winning_ticket)
            plays += 1
            if plays >= max_tries:
                break
            if won:
                print("We have a winning ticket!")
                print(f"Your ticket: {new_ticket}")
                print(f"Winning ticket: {winning_ticket}")
                print(f"It only took {plays} tries to win!")
            else:
                print(f"Tried {plays} times, without pulling a winner. :(")
                print(f"Your ticket: {new_ticket}")
                print(f"Winning ticket: {winning_ticket}")    

lotterych = ['a','b','c','d','e',1,2,3,4,5,6,7,8,9,10]

my_picks = LotteryAnalysis(lotterych)
my_picks.analyze(lotterych)