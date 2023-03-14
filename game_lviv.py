import game_lviv_classes as gm


hall = gm.Room("Коридор")
hall.set_description("Коридор 3 поверху БФК. Є настільний футбол.")

a308 = gm.Room("Аудиторія 308")
a308.set_description("Аудиторія з проектором.")

a307 = gm.Room("Аудиторія 307")
a307.set_description("Аудиторія де проводиться пара в бізнес-школи УКУ.")

a303 = gm.Room("Аудиторія 303")
a303.set_description("Аудиторія де проводиться пара в культорологів.")

hall.link_room(a308, "north")
hall.link_room(a303, "east")
hall.link_room(a307, "west")
a308.link_room(a307, "south")
a308.link_room(hall, "east")
a307.link_room(a308, "north")
a307.link_room(hall, "east")
a303.link_room(hall, "west")


bsstudent_boss = gm.Enemy("Андрій", "Випускник бізнес школи УКУ", 3)
hall.set_character(bsstudent_boss)

bsstudent = gm.Enemy("Юра", "Студент бізнес школи УКУ", 2)
a307.set_character(bsstudent)

kulto = gm.Enemy("Іра", "Студентка культорології", 100)
a303.set_character(kulto)
kulto.set_weakness("Одноразова електронна сигарета")

odnrz = gm.Item("Одноразова електронна сигарета")
odnrz.set_description("Можна використати, щоб перемогти студентку культорології")
a308.set_item(odnrz)

player = gm.Player('player', 1)

current_room = hall
backpack = []

dead = False
kills = 0

while dead == False:

    print("\n")
    current_room.get_details()

    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    item = current_room.get_item()
    if item is not None:
        item.describe()

    command = input("> ")

    if command in ["north", "south", "east", "west"]:
        # Move in the given direction
        current_room = current_room.move(command)
    elif command == "fight":
        if inhabitant is not None:
            if inhabitant == kulto:
                # Fight with the inhabitant, if there is one
                # Do I have this item?
                if odnrz in backpack:

                    if inhabitant.fight(odnrz.get_name()) == True:
                        # What happens if you win?
                        print("Hooray, you won the fight!\nYou have levelled up.")
                        current_room.character = None
                        player.level_up()
                        kills += 1

                    else:
                        # What happens if you lose?
                        print("Oh dear, you lost the fight.")
                        player.lives -= 1
                        
                else:
                    print("You don't have a " + odnrz.get_name())
            else:
                if player.get_level() < inhabitant.get_level():
                    print("Oh dear, you lost the fight.\nLevel up before figthing.")
                    player.lives -= 1
                else:
                    print("Hooray, you won the fight!\nYou have levelled up.")
                    current_room.character = None
                    kills += 1

                    player.level_up()
                    if kills == 3:
                        print("Вітаю, ви перемогли випускника бізнес школи УКУ і він пішов пити каву.")
                        dead = True
        else:
            print("There is no one here to fight with")
    elif command == "take":
        if item is not None:
            print("You put the " + item.get_name() + " in your backpack")
            backpack.append(item)
            current_room.set_item(None)
        else:
            print("There's nothing here to take!")
    else:
        print("I don't know how to " + command)

    if player.lives == 0:
        print("That's the end of the game")
        dead = True
    
    