"""
Game module.
"""

class Room:
    """
    Room class.
    """
    def __init__(self, name) -> None:
        """
        Inits a room with a name.
        """
        self.name = name
        self.character = None
        self.item = None
        self.rooms = {'north': self, 'east': self, 'south': self, 'west': self}

    def set_description(self, description) -> None:
        """
        Sets room description.
        """
        self.description = description

    def set_item(self, item) -> None:
        """
        Sets room item.
        """
        self.item = item

    def set_character(self, character) -> None:
        """
        Sets room character.
        """
        self.character = character

    def get_item(self) -> object:
        """
        Gets room item.
        """
        return self.item

    def get_character(self) -> object:
        """
        Gets room character.
        """
        return self.character

    def link_room(self, room, direction) -> None:
        """
        Links a room.
        """
        if direction in self.rooms:
            self.rooms[direction] = room

    def move(self, direction) -> object:
        """
        Moves to another room.
        """
        if self.rooms[direction] != self:
            return self.rooms[direction]
    
    def get_details(self) -> None:
        """
        Describe a room.
        """
        print(self.name)
        print('--------------------')
        print(self.description)
        for key, val in self.rooms.items():
            if val != self:
                print(f'{val.name} is {key}')


class Item:
    """
    Item class.
    """
    def __init__(self, name) -> None:
        """
        Inits an enemy with a name.
        """
        self.name = name

    def get_name(self) -> str:
        """
        Get the name of the item.
        """
        return self.name

    def set_description(self, description) -> None:
        """
        Sets item description.
        """
        self.description = description

    def describe(self) -> None:
        """
        Describe an item.
        """
        print(f'The [{self.name}] is here - {self.description}')

class Character:
    """
    Character class.
    """
    def __init__(self, name, level) -> None:
        """
        Inits a character.
        """
        self.name = name
        self.level = level
    def level_up(self) -> None:
        """
        Level up.
        """
        self.level += 1
    def get_level(self) -> int:
        """
        Get level.
        """
        return int(self.level)

class Player(Character):
    """
    Player class.
    """
    def __init__(self, name, level) -> None:
        """
        Inits a player.
        """
        super().__init__(name, level)
        self.inventory = []
        self.lives = 2

    def add_inventory(self, item) -> None:
        """
        Adds item to the inventory.
        """
        self.inventory.append(item)
    
    

class Enemy(Character):
    """
    Enemy class.
    """
    defeated = 0
    def __init__(self, name, description, level) -> None:
        """
        Inits an enemy with a name and a description.
        """
        super().__init__(name, level)
        self.description = description
    
    def set_conversation(self, conversation) -> None:
        """
        Sets enemy conversation.
        """
        self.conversation = conversation
    
    def set_weakness(self, weakness) -> None:
        """
        Sets enemy weakness.
        """
        self.weakness = weakness

    def describe(self) -> None:
        """
        Describe an enemy.
        """
        print(f'{self.name} is here!')
        print(self.description)

    def talk(self) -> None:
        """
        Talk with an enemy.
        """
        print(self.conversation)
    def fight(self, item):
        """
        Fight with an enemy.
        """
        if item == self.weakness:
            Enemy.defeated += 1
            return True
        return False
    def get_defeated(self):
        """
        Return how many times was the enemy defeated.
        """
        return Enemy.defeated

