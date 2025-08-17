import random

class Promptgen:
    def __init__(self):
        self.last_attunement = []
    def pick_attunement(self):
        attunements = ["Flame", "Frost", "Thunder", "Gale", "Shadow", "Ironsing", "Blood"]
        if random.randint(1, 15) == 6:
            return "any attunement"
        if self.last_attunement:
            attunements.pop(attunements.index(self.last_attunement[-1]))
        att = random.choice(attunements)
        self.last_attunement.append(att)
        return att

    def pick_oath(self, bharper):
        oaths = ["Oathless","Fadetrimmer",
                 "Blindseer", "Chainwarden",
                 "Contractor", "Dawnwalker",
                 "Jetstriker", "Soulbreaker",
                 "Starkindred", "Visionshaper"]
        if random.randint(1, 24) == 6:
            return "any oath"
        if bharper:
            oaths.append("Blade Harper")
        return random.choice(oaths)

    def pick_use(self, depths=False):
        uses = ["chime", "team gank", "solo gank"]
        if depths:
            uses.append("depths gank")
        return random.choice(uses)

    def pick_weapon_type(self):
        weapon_class = ["Heavy", "Medium", "Light", "any"]
        match random.choice(weapon_class):
            case "Heavy":
                return random.choice(["Greataxe", "Greathammer", "Greatsword", "Any Heavy"])
            case "Medium":
                return random.choice(["Sword", "Spear", "Club", "Twinblade", "Any Medium"])
            case "Light":
                return random.choice(["Dagger", "Fist", "Rapier", "Any Light"])
            case "any":
                return "any weapon"

    def pick_legendary_wep(self, attunement, high_req):
        match attunement:
            case "Flame":
                return random.choice(["Pyre", "Pleeksty's", "Hellflame"])
            case "Frost":
                return random.choice(["Gran", "Kryswynter", "Hailbreaker"])
            case "Thunder":
                return random.choice(["Stormseye", "Boltcrusher"])
            case "Gale":
                return random.choice(["Curved", "Wraithclaw"])
            case "Shadow":
                if high_req:
                    return random.choice(["Crypt", "Spindle", "Weal and Woe"])
                return random.choice(["Crypt", "Spindle"])
            case "Ironsing":
                return random.choice(["Deepcrusher", "Requiem"])
            case "Blood":
                return random.choice(["BloodFouler"])
            case "any attunement":
                attunements = ["Flame", "Frost", "Thunder", "Gale", "Shadow", "Ironsing", "Blood"]
                attunements.pop(attunements.index(self.last_attunement[-1]))
                return self.pick_legendary_wep(random.choice(attunements), high_req)

    def generate_prompt(self, mono=True) -> str:
        if mono:
            return random.choice([
                f"Mono {self.pick_attunement()} {self.pick_oath(True)} {self.pick_weapon_type()} {self.pick_use()}",
                f"Mono {self.pick_legendary_wep(self.pick_attunement(), True)} {self.pick_oath(True)} {self.pick_use()}",
                f"{self.pick_legendary_wep(self.pick_attunement(), True)} {self.pick_oath(True)} {self.pick_use()}"
            ])
        return random.choice([
            f"Dual {self.pick_attunement()}/{self.pick_attunement()} {self.pick_oath(False)} {self.pick_weapon_type()} {self.pick_use()}",
            f"Dual {self.pick_attunement()}/{self.pick_legendary_wep(self.pick_attunement(), False)} {self.pick_oath(False)} {self.pick_use()}"
        ])
    
    def generate_ham_prompt(self, olevel) -> list[str]: # only for ham's server
        prompt = []
        match olevel:
            case "Library Liability":
                prompt.append(random.choice(
                    [
                        f"Mono {self.pick_attunement()} chime no heroblade",
                    ]
                ))
            case "Scribe":
                prompt.append(random.choice(
                    [
                        f"Mono {self.pick_attunement()} {self.pick_oath(True)} {self.pick_weapon_type()} {self.pick_use()}",
                        f"Mono {self.pick_legendary_wep(self.pick_attunement(), True)} {self.pick_oath(True)} {self.pick_use()}"
                    ]
                ))
            case "Scholar":
                prompt.append(random.choice(
                    [
                        f"Mono {self.pick_attunement()} {self.pick_oath(True)} {self.pick_weapon_type()} {self.pick_use()}",
                        f"Mono {self.pick_legendary_wep(self.pick_attunement(), True)} {self.pick_oath(True)} {self.pick_use()}",
                    ]
                ))
            case "Librarian":
                prompt.append(random.choice(
                    [
                        f"Dual {self.pick_attunement()}/{self.pick_attunement()} {self.pick_oath(False)} {self.pick_weapon_type()} {self.pick_use()}",
                        f"Dual {self.pick_attunement()}/{self.pick_legendary_wep(self.pick_attunement(), False)} {self.pick_oath(False)} {self.pick_use()}"
                    ]
                ))
            case "Lorekeeper":
                for i in range(2):
                    prompt.append(random.choice(
                        [
                            f"Dual {self.pick_attunement()}/{self.pick_attunement()} {self.pick_oath(False)} {self.pick_weapon_type()} {self.pick_use(True)}",
                            f"Dual {self.pick_attunement()}/{self.pick_legendary_wep(self.pick_attunement(), False)} {self.pick_oath(False)} {self.pick_use(True)}",
                        ]
                    ))
            case "Knowledge Seeker":
                for i in range(3):
                    prompt.append(random.choice(
                        [
                            f"Dual {self.pick_attunement()}/{self.pick_attunement()} {self.pick_oath(False)} {self.pick_weapon_type()} {self.pick_use(True)}",
                            f"Dual {self.pick_attunement()}/{self.pick_legendary_wep(self.pick_attunement(), False)} {self.pick_oath(False)} {self.pick_use(True)}",
                            f"{self.pick_legendary_wep(self.pick_attunement(), True)} {self.pick_oath(True)} {self.pick_use(True)}"
                        ]
                    ))
        return prompt

    #def pick_concept_prompt():

    #def pick_bans(self):
    #    return random.sample(["No Khan", "No Shrine of Mastery", "No Low invest (<50)", "No Legendaries", "No Heroblade"], random.randint(0, 5))



# Create an instance and call the method

