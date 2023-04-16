class Dragon:
    def __init__(self, height, flammability, color):
        self.height = height
        self.flammability = flammability
        self.color = color
    def str(self) -> str:
        return print(f'Dragon with height {self.height}, flammability {self.flammability} and {self.color} color')
    def change_color(self, new_color):
        self.color = new_color


dr = Dragon(175, 10, 'green')
dr1 = Dragon(83, 10, 'blue')

dr.str()
dr1.str()
dr.change_color('white')
dr.str()