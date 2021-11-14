ROOMS = {
    'Great Hall': {'South': 'Library', 'North': 'Kitchen', 'East': 'Gallery', 'West': 'Bedroom'},
    'Bedroom': {'South': 'Cellar', 'North': 'Dining Room', 'East': 'Great Hall', 'item': 'Armor'},
    'Cellar': {'North': 'Bedroom', 'item': 'Arrows'},
    'Library': {'North': 'Great Hall', 'item': 'Book'},
    'Dining Room': {'South': 'Bedroom', 'East': 'Kitchen', 'item': 'Bow'},
    'Gallery': {'South': 'Dungeon', 'West': 'Great Hall', 'item': 'Helmet'},
    'Kitchen': {'South': 'Great Hall', 'West': 'Dining Room', 'item': 'Shield'},
    'Dungeon': {'North': 'Gallery', 'item': 'Dragon'}  # villain Dragon
}


class Player:
    def __init__(self):
        self.position = 'Great Hall'
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
            next_item = move.split(' ')[1]
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
        pass

    def win(self):
        return 

    def lose(self):
        return 


def show_instructions():
    # print a main menu and the commands
    print("Dragon Text Adventure Game")
    print("Collect 6 items to win the game, or be eaten by the dragon.")
    print("Move commands: go South, go North, go East, go West")
    print("Add to Inventory: get 'item name'")


if __name__ == '__main__':
    player = Player()

