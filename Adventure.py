ROOMS = {
    'Fair Grounds': {'South': 'Bloody Bumper Cars', 'North': 'Corn Mase of Lost Souls', 'East': 'Ferris Wheel of Hell', 'West': 'Creaking Carousel'},
    'Creaking Carousel': {'South': 'Haunted House', 'North': 'Gift Shop of Horror', 'East': 'Fair Grounds', 'item': 'Flash Light'},
    'Haunted House': {'North': 'Creaking Carousel', 'item': 'Book of Spells'},
    'Bloody Bumper Cars': {'North': 'Fair Grounds', 'item': 'Knife'},
    'Gift Shop of Horror': {'South': 'Creaking Carousel', 'East': 'Corn Mase of Lost Souls', 'item': 'Costume'},
    'Corn Mase of Lost Souls': {'South': 'Fair Grounds', 'West': 'Gift Shop of Horror', 'item': 'Rosary'},
    'Ferris Wheel of Hell': {'South': 'Circus Tent', 'West': 'Fair Grounds', 'item': 'Holy Water'},
    'Circus Tent': {'North': 'Ferris Wheel of Hell', 'item': 'Evil Feast Master'}  # villain Evil Feast Master
}



class Player:
    def __init__(self):
        self.position = 'Fair Grounds'
        self.next_moves = self.position
        self.inventory = []

    def make_move(self):
        try:
            stat = f"""You are in the {self.position} \nInventory : {self.inventory} 
            \nYou see a {ROOMS[self.position]['item']} \n--------------------------- \nEnter your move: """
        except Exception:
            stat = f"""You are in the {self.position} \nInventory: {self.inventory} \n \n--------------------------- 
            \nEnter your move: """

        move = input(stat)
        if move.startswith('get'):
            next_item = move.split(' ')[1:]
            next_item=' '.join(next_item)
            if next_item == ROOMS[self.position]['item']:
                print(f"{ROOMS[self.position]['item']} retrieved")
                self.inventory.append(ROOMS[self.position]['item'])
                del ROOMS[self.position]['item']
                self.make_move()
            else:
                print(f"Can’t get {next_item}!")
                self.make_move()
        elif move.startswith('go'):
            next_position = move.split(' ')[1]
            if next_position in ROOMS[self.position].keys():
                self.position = ROOMS[self.position][next_position]
                self.win_lose()
            else:
                print('You can’t go that way!')
                self.make_move()

    def win_lose(self):
        while len(set(self.inventory)) < 6 and self.position != 'Circus Tent':
            self.make_move()
        else:
            if len(set(self.inventory)) < 6 and self.position == 'Circus Tent':
                print(f"""You are in the {self.position} \nInventory : {self.inventory} 
            \nYou see a {ROOMS[self.position]['item']} \n """)
                print(self.lose())
                exit()
            else:
                print(f"""You are in the {self.position} \nInventory : {self.inventory} 
            \nYou see a {ROOMS[self.position]['item']} \n  """)
                print(self.win())
                exit()

    def win(self):
        return """Congratulations! You have collected all items and defeated the Evil Feast Master! \n
    Thanks for playing the game. Hope you enjoyed it."""

    def lose(self):
        return """ NOM NOM...GAME OVER! \n
        Thanks for playing the game. Hope you enjoyed it."""


def show_instructions():
    # print a main menu and the commands
    print("Dragon Text Adventure Game \n \n")
    print("Collect 6 items to win the game, or be defeated by the Evil Feast Master.")
    print("Move commands: go South, go North, go East, go West ")
    print("Add to Inventory: get 'item name'  \n")


if __name__ == '__main__':
    player = Player()
    show_instructions()
    player.make_move()
