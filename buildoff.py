import hikari
from promptgenv3 import Promptgen

olevel = {
    "1400661228925485216": 0, #Liability
    "1400638589410480139": 1, #Scribe
    "1400642408848294129": 2, #Scholar
    "1398123028856049885": 3, #Librarian
    "1368273744459468890": 4, #Lorekeeper
    "1398122704833478729": 5, #Knowledge Seeker
}

class Wager:
    def __init__(self, user_1: hikari.Member.id , user_2: hikari.Member.id):
        self.user_1 = user_1
        self.user_2 = user_2

        
        

        match olevel:
            case 0 | 1 | 2:
                self.build_prompt = Promptgen.generate_prompt(True)
            case 3 :
                self.build_prompt = random.choice([Promptgen.generate_prompt(True), Promptgen.generate_prompt(False)])
            case 4 | 5:
                self.build_prompt = Promptgen.generate_prompt(False)
            
        self.log = f"{self.user_1.username} vs {self.user_2.username}\n{self.build_prompt}"

    def check_user_olevel(self, user: hikari.Member.id) -> int:
        #