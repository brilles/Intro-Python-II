# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []

    def __repr__(self):
        return f"Player{self.name, self.current_room}"

    def details(self):
        print(f"{self.name}, you are at the {self.current_room.name}, {self.current_room.description}")
    
    def check_items(self):
        try: 
            self.current_room.items[0]
            print('Items here: ')
            for i in self.current_room.items:
                print(f"{i.name} - '{i.description}'")
        except:
            print("No items here, look elsewhere")
    
    def show_inventory(self):
        if len(self.items) == 0:
            print("You don't have any items!")
        else:
            print('Your items: ')
            for i in self.items:
                print(f"{i.name} - '{i.description}'")

