from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item
import random

print("\n\n")
#black magic
fire = Spell("Fire", 70, 180, "black")
thunder = Spell("Thunder", 15, 140, "black")
blizzard = Spell("Blizzard", 30, 250, "black")
dbeam = Spell("Dark Beam", 100, 3000, "black")
forceflash = Spell("Team Attack.", 170, 4500, "black")
#white magic
cure = Spell("Cure", 25, 1200, "white")
bandage = Spell("Bandage", 5, 100, "white")
sensubean = Spell("Take a Sensu Bean", 60, 700, "white")

#create some items
potion = Item("Potion", "potion", "Heals 100 HP", 100)
darke = Item("Dark Energy", "potion", "Heals 2000 HP", 2000)
superpotion = Item("Super Potion", "potion", "Heals 200 HP", 150)
elixer = Item("Elixer", "elixer", "Fully restores Hp of one party member", 99999)
bagofbeans = Item("Bag of Beans", "elixer","Heals the Entire Team", 99999 )
#items that doo damage
gerenade = Item("Gerenade", "attack", "Deals 500 HP damage.", 500)
teamattack = Item("Team Attack", "attack", "Focus the team into a single attack.", 4000)




player_magic = [fire, thunder, blizzard, dbeam, forceflash, bandage, cure, sensubean]
player_items = [ {"item": potion,"quantity": 3}, {"item": superpotion, "quantity":2}, {"item": elixer, "quantity": 1},
                {"item": bagofbeans, "quantity": 1}, {"item": gerenade, "quantity": 3}, {"item": teamattack, "quantity": 1}]


         # instntiate people
player1 = Person("Valos ", 4000, 150, 120, 35,[fire, thunder, blizzard, cure, sensubean] , [{"item": superpotion, "quantity":2},{"item": gerenade, "quantity": 5},])
player2 = Person("Akeron", 2900, 200, 190, 35, [fire, blizzard,cure,], [{"item": potion,"quantity": 3},{"item": elixer, "quantity": 1},{"item": gerenade, "quantity": 3}])
player3 = Person("Don   ", 3500, 400, 270, 250, [bandage,sensubean, thunder, dbeam, forceflash], [{"item": bagofbeans, "quantity": 1}, {"item": teamattack, "quantity": 1}])

players = [player1, player2, player3]

enemy1 = Person("Goony", 10200, 65, 850, 25, [], [{"item": darke, "quantity":1}])
enemy2 = Person("Randy", 3000, 65, 350, 50, [], [{"item": darke, "quantity":2}])
enemy3 = Person("Jimmy", 7200, 65, 650, 155, [], [{"item": darke, "quantity":0}])

enemies = [enemy1, enemy2, enemy3]

running = True
i = 0
# bcolors endc stop colors
print(bcolors.FAIL + bcolors.BOLD + "***A Gang Attacks!!!!" + bcolors.ENDC)

while running:
    print("===============================\n")
    for enemy in enemies:
        enemy.get_enemy_stats()
        print("\n" + bcolors.OKGREEN + bcolors.BOLD  + "" + bcolors.ENDC)

    for player in players:
        if player.get_hp() > 0:
            print("\n")

            player1.get_stats()
            player2.get_stats()
            player3.get_stats()
            print("\n")

            player.choose_action()
            choice = input("Choose action:")
            index = int(choice) - 1


            if index == 0:
                dmg = player.generate_damage()
                enemy = player.choose_target(enemies)
                enemies[enemy].take_dmg(dmg)
                print(player.name + " did ", dmg, " Damage.\n" + enemies[enemy].name + " has", enemies[enemy].get_hp(), " HP left!")

            elif index == 1:
                player.choose_magic()
                magic_choice = int(input("Choose a Spell:")) - 1

                if magic_choice == -1:
                    continue

                spell = player.magic[magic_choice]
                magic_dmg = spell.generate_damage()

                current_mp = player.get_mp()
                if spell.cost > current_mp:
                    print(bcolors.FAIL + "\n Not enough MP\n" + bcolors.ENDC)
                    continue
                player.reduce_mp(spell.cost)

                if spell.type == "white":
                    player.heal(magic_dmg)
                    print(bcolors.OKBLUE + "\n" + spell.name + " heals " + player.name + " for ", str(magic_dmg), " HP." + bcolors.ENDC)

                elif spell.type == "black":
                    enemy = player.choose_target(enemies)
                    enemies[enemy].take_dmg(magic_dmg)
                    print(bcolors.OKBLUE + player.name + " used " + spell.name + "\n  and did", magic_dmg, " Damage.\n" + enemies[enemy].name + " has",
                      str(enemies[enemy].get_hp()) + " hp left!", bcolors.ENDC)
            elif index == 2:
                player.choose_item()
                item_choice = int(input("Choose Item:")) - 1

                if item_choice == -1:
                    continue
                item = player.items[item_choice]["item"]
                if player.items[item_choice]["quantity"] == 0:
                    print(bcolors.FAIL + player.name + "\n doesnt have any " + item.name + bcolors.ENDC)
                    continue

                player.items[item_choice]["quantity"] -= 1




                if item.type == "potion":
                    player.heal(item.prop)
                    print(bcolors.OKGREEN + "\n" + item.name + " Heals " + player.name + " For ", str(item.prop), "HP" + bcolors.ENDC)

                elif item.type == "elixer":
                    if item == dathenny:
                        for i in players:
                            i.hp = i.maxhp
                            i.mp = i.maxmp

                        print(bcolors.OKGREEN + item.name + " Fully healed the entire team!" + bcolors.ENDC)

                    else:
                        player.hp = player.maxhp
                        player.mp = player.maxmp
                    print(bcolors.OKGREEN + item.name + " Fully healed " + player.name + "!" +bcolors.ENDC)


                elif item.type == "attack":
                    enemy = player.choose_target(enemies)
                    enemies[enemy].take_dmg(item.prop)
                    print(bcolors.OKGREEN + player.name + " used " + item.name + " and did ", str(item.prop), " damage to " + enemies[enemy].name + "!" + bcolors.ENDC)

    defeated_enemies = 0
    defeated_players = 0


    for enemy in enemies:


        if enemy.get_hp() == 0:
            print(bcolors.OKGREEN + bcolors.BOLD + str(enemy.name) + " is down!" + bcolors.ENDC)
            del enemy
            defeated_enemies += 1
    if  defeated_enemies == 3:

        print(bcolors.OKGREEN + bcolors.BOLD + "YOU WIN!" + bcolors.ENDC)
        running = False
    else:
        for enemy in enemies:
            enemy.choose_itemx()

            item_choice = 0
            if enemy.items[item_choice]["quantity"] < 1:
                if enemy.get_hp() > 0:
                    enemy_choice = 1
                    target = random.randrange(0, 3)
                    enemy_dmg = enemy.generate_damage()
                    players[target].take_dmg(enemy_dmg)
                    print(bcolors.FAIL + bcolors.BOLD + "      \n" + enemy.name + " attacks " + players[
                        target].name + " for ", enemy_dmg, " damage!!!!\n" + bcolors.ENDC)


            else:
                if enemy.items[item_choice]["quantity"] > 0:

                        if enemy.get_hp() < enemy.maxhp - 2000:
                            print(bcolors.FAIL + enemy.name + " has Dark Energy around him!\n" + " \nThe Dark Energy heals " + enemy.name + " for 2000hp!" )
                            enemy.heal(2000)
                            enemy.items[item_choice]["quantity"] -= 1

                        else:
                            if enemy.get_hp() > enemy.maxhp - 2000:
                                enemy_choice = 1
                                target = random.randrange(0, 3)
                                enemy_dmg = enemy.generate_damage()
                                players[target].take_dmg(enemy_dmg)
                                print(bcolors.FAIL + bcolors.BOLD + "      \n" + enemy.name + " attacks " +
                                      players[
                                          target].name + " for ", enemy_dmg, " damage!!!!\n" + bcolors.ENDC)








    for player in players:
        if player.get_hp() == 0:
            print(bcolors.FAIL + bcolors.BOLD + player.name + " is down!" + bcolors.ENDC)
            del player
            defeated_players += 1



    if defeated_players == 3:
        print(bcolors.FAIL + bcolors.BOLD + "Your team has been WIPED OUT!!\n *****GAME OVER*****" + bcolors.ENDC)
        running = False

