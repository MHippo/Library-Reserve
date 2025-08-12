import random

class Promptgen:
    def __init__(self):
        self.last_attunement = ["poop"] #needs to be added or else index error
    
    def pick_attunement(self):
        attunements = ["Flame", "Frost", "Thunder", "Gale", "Shadow", "Ironsing", "Blood"]
        if random.randint(1, 15) == 6:
            return "any"
        att = random.choice(attunements)
        if att == self.last_attunement[-1]:
            attunements.pop(attunements.index(att))
        att = random.choice(attunements)
        self.last_attunement.append(att)
        return att

    def pick_oath(self, bharper):
        oaths = ["Oathless", "Arcwarder",
                 "Blindseer", "Chainwarden",
                 "Contractor", "Dawnwalker", "Fadetrimmer",
                 "Jetstriker", "Soulbreaker",
                 "Starkindred", "Visionshaper"]
        if random.randint(1, 24) == 6:
            return "any"
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
                return random.choice(["Greataxe", "Greathammer", "Greatsword", "Any"])
            case "Medium":
                return random.choice(["Sword", "Spear", "Club", "Rifle", "Twinblade", "Any"])
            case "Light":
                return random.choice(["Dagger", "Fist", "Rapier", "Pistol", "Any"])
            case "any":
                return "any"

    def pick_legendary_wep(self, attunement):
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
                return random.choice(["Crypt", "Spindle", "Weal and Woe"])
            case "Ironsing":
                return random.choice(["Deepcrusher", "Requiem"])
            case "Blood":
                return random.choice(["BloodFouler"])
            case "any":
                attunements = ["Flame", "Frost", "Thunder", "Gale", "Shadow", "Ironsing", "Blood"]
                attunements.pop(attunements.index(self.last_attunement[-1]))
                return self.pick_legendary_wep(random.choice(attunements))

    def generate_prompt(self, mono=True) -> str:
        if mono:
            return random.choice([
                f"Mono {self.pick_attunement()} {self.pick_oath(True)} {self.pick_weapon_type()} {self.pick_use()}",
                f"Mono {self.pick_legendary_wep(self.pick_attunement())} {self.pick_oath(True)} {self.pick_use()}",
                f"{self.pick_legendary_wep(self.pick_attunement())} {self.pick_oath(True)} {self.pick_use()}"
            ])
        return random.choice([
            f"Dual {self.pick_attunement()}/{self.pick_attunement()} {self.pick_oath(False)} {self.pick_weapon_type()} {self.pick_use()}",
            f"Dual {self.pick_attunement()}/any {self.pick_oath(False)} {self.pick_weapon_type()} {self.pick_use()}",
            f"Dual {self.pick_attunement()}/{self.pick_legendary_wep(self.pick_attunement())} {self.pick_oath(False)} {self.pick_use()}",
            f"Dual {self.pick_legendary_wep(self.pick_attunement())}/any {self.pick_oath(False)} {self.pick_use()}",
        ])
    
    def generate_ham_prompt(self, olevel) -> list[str]: # only for ham's server
        prompt = []
        match olevel:
            case "Library Liability" | "scribe":
                prompt.append(random.choice(
                    [
                        f"Mono {self.pick_attunement()} {self.pick_oath(True)} {self.pick_weapon_type()} chime",
                        f"Mono {self.pick_legendary_wep(self.pick_attunement())} {self.pick_oath(True)} chime",
                    ]
                ))
            case "scholar":
                prompt.append(random.choice(
                    [
                        f"Mono {self.pick_attunement()} {self.pick_oath(True)} {self.pick_weapon_type()} {self.pick_use()}",
                        f"Mono {self.pick_legendary_wep(self.pick_attunement())} {self.pick_oath(True)} {self.pick_use()}",
                    ]
                ))
            case "Book Keeper":
                prompt.append(random.choice(
                    [
                        f"Dual {self.pick_attunement()}/{self.pick_attunement()} {self.pick_oath(False)} {self.pick_weapon_type()} {self.pick_use()}",
                        f"Dual {self.pick_attunement()}/{self.pick_legendary_wep(self.pick_attunement())} {self.pick_oath(False)} {self.pick_use()}"
                    ]
                ))
            case "Librarian":
                for i in range(2):
                    prompt.append(random.choice(
                        [
                            f"Dual {self.pick_attunement()}/{self.pick_attunement()} {self.pick_oath(False)} {self.pick_weapon_type()} {self.pick_use(True)}",
                            f"Dual {self.pick_attunement()}/{self.pick_legendary_wep(self.pick_attunement())} {self.pick_oath(False)} {self.pick_use(True)}",
                        ]
                    ))
            case "Lorekeeper":
                for i in range(3):
                    prompt.append(random.choice(
                        [
                            f"Dual {self.pick_attunement()}/{self.pick_attunement()} {self.pick_oath(False)} {self.pick_weapon_type()} {self.pick_use(True)}",
                            f"Dual {self.pick_attunement()}/{self.pick_legendary_wep(self.pick_attunement())} {self.pick_oath(False)} {self.pick_use(True)}",
                            f"{self.pick_legendary_wep(self.pick_attunement())} {self.pick_oath(True)} {self.pick_use(True)}"
                        ]
                    ))
        return prompt


    #def pick_concept_prompt():

    #def pick_bans(self):
    #    return random.sample(["No Khan", "No Shrine of Mastery", "No Low invest (<50)", "No Legendaries", "No Heroblade"], random.randint(0, 5))



# Create an instance and call the method

