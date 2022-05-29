"""It's a warrior mini-game. Takes no arguments, class instance gets first level and 100 exp at start, \
to gain exp and increase warrior level/rank use 'self.training' to train your warrior or use 'self.battle' to fight. \
Has taken from https://www.codewars.com/kata/5941c545f5c394fef900000c."""

class Warrior:

    def __init__(self):
        self.experience = 100
        self.level = 1
        self.rank = 'Pushover'
        self.achievements = []

    def _update_attrs(self):
        if self.experience < 10000:
            dict_of_ranks = {0: "Pushover", 1: "Novice", 2: "Fighter",
                             3: "Warrior", 4: "Veteran", 5: "Sage", 6: "Elite", 7: "Conqueror",
                             8: "Champion", 9: "Master", 10: "Greatest"}
            self.level = self.experience // 100
            self.rank = dict_of_ranks[self.level // 10]
        else:
            self.level = 100
            self.rank = "Greatest"
            self.experience = 10000

    def training(self, lst):
        description, earn_exp, min_lvl = lst
        if min_lvl <= self.level:
            self.experience += earn_exp
            self.achievements.append(description)
            self._update_attrs()
            return description
        return "Not strong enough"

    def battle(self, enemy_lvl):
        if 1 <= enemy_lvl <= 100:
            diff = self.level - enemy_lvl
            if 0 <= diff <= 1:
                if diff:
                    self.experience += 5
                else:
                    self.experience += 10
                s = 'A good fight'
            elif diff >= 2:
                s = "Easy fight"
            elif self.level // 10 == enemy_lvl // 10 or diff >= -4:
                self.experience += 20 * diff ** 2
                s = "An intense fight"
            else:
                s = "You've been defeated"
            self._update_attrs()
            return s
        return "Invalid level"


if __name__ == '__main__':
    print(Warrior().__doc__)
