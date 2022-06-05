class Player:
    def __init__(self, pos, name):
        self.pos = pos
        self.name = name
    
    def update_pos(self, new_pos):
        self.pos = new_pos
    
    def get_name(self):
        return self.name

    def get_pos(self):
        return self.pos