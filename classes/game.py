
import random


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Person:
    def __init__(self, name, hp, mp, atk, df, magic, items, ):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 20
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.action = ["Attack", "Magic", "Items"]
        self.items = items
        self.name = name

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def take_dmg(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    def get_hp(self):
        return self.hp

    def get_maxhp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_maxmp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -= cost




    def generate_dmg(self):
            low = self.dmg - 35
            high = self.dmg + 60
            return random.randrange(low, high)

    def choose_action(self):
        i = 1
        print(bcolors.OKBLUE + bcolors.BOLD + "Actions" + bcolors.ENDC)

        for item in self.action:
            print("    " + str(i) + ":", item)
            i += 1

    def choose_magic(self):

        i = 1


        print("\n" + bcolors.OKBLUE + bcolors.BOLD + "          You open the Book of Omega granting you power over the elements!\n *Press 0 to go back*" + bcolors.ENDC)

        for spell in self.magic:
            print("             " + str(i) + ":", spell.name, "-costs:", str(spell.cost) + ")")
            i += 1

    def choose_item(self):
        i = 1
        print("\n" + bcolors.OKGREEN + bcolors.BOLD +"          Items:\n*Press 0 to go back*" + bcolors.ENDC)
        for item in self.items:
            print("             " + str(i) + ".", item["item"].name, ":\n", item["item"].description,"(x" + str(item["quantity"]) + ")")
            i += 1

    def choose_itemx(self):
        i = 1

    def choose_target(self, enemies):
         i = 1
         print("\n" + bcolors.FAIL + bcolors.BOLD + "     Target: " + bcolors.ENDC)
         for enemy in enemies:
             if enemy.get_hp() > 0:
                print("         " + str(i) + ".", enemy.name)
             i += 1
         choice = int(input("     Choose target: ")) - 1
         return choice



    def get_enemy_stats(self):
        hp_bar = ""
        bar_ticks = (self.hp / self.maxhp) * 100 / 2
        while bar_ticks > 0:
             hp_bar += "█"
             bar_ticks -= 1

        while len(hp_bar) < 50:
            hp_bar += " "

        hp_string = str(self.hp) + "/" + str(self.maxhp)
        current_hp = ""

        if len(hp_string) < 11:
            decreased = 11 - len(hp_string)

            while decreased > 0:
                current_hp += " "
                decreased -= 1
            current_hp += hp_string

        else:
            current_hp = hp_string

        print(bcolors.BOLD + self.name + "  " +
              current_hp   + bcolors.FAIL + "    |  " + hp_bar + "  | " + bcolors.ENDC)










    def get_stats(self):
        hp_bar=""
        bar_ticks = (self.hp / self.maxhp) * 100 / 7

        mp_bar = ""
        mp_ticks = (self.mp / self.maxmp) * 100 / 13

        while bar_ticks > 0:
            hp_bar += "█"
            bar_ticks-= 1

        while len(hp_bar) < 17:
           hp_bar += " "

        while mp_ticks > 0:
            mp_bar += "█"
            mp_ticks -= 1
        while len(mp_bar) < 10:
            mp_bar += " "

        hp_string = str(self.hp) + "/" + str(self.maxhp)
        current_hp = ""

        if len(hp_string) < 9:
            decreased = 9 - len(hp_string)

            while decreased > 0:
                current_hp += " "
                decreased -= 1
            current_hp  += hp_string

        else:
            current_hp = hp_string





        print(bcolors.BOLD + self.name + "  " +
             current_hp + bcolors.OKGREEN + "     |  " + hp_bar +"| " + bcolors.ENDC +
              str(self.mp) + "/" + str(self.maxmp) + bcolors.OKBLUE + "| ██████████ |" + bcolors.ENDC)
