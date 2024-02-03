class Game:
    def __init__(self):
        self.three_people = []
        self.marry = ""
        self.love = ""
        self.date = ""

    def get_people(self):
        while len(self.three_people) < 3:
            name = input(f"Enter a Name {len(self.three_people) + 1}: ").strip()
            self.three_people.append(name)

    def get_choice(self, action, used_names):
        choice = input(f"Who would you {action}? ").strip()
        while choice not in self.three_people or choice in used_names:
            print(f"The name must be one of the three people you first chose and hasn't been chosen already.")
            choice = input(f"Who would you {action}? ").strip()
        return choice

    def get_choices(self):
        print("Now you have to choose who you would marry, love, date")
        used_names = []
        self.marry = self.get_choice("marry", used_names)
        used_names.append(self.marry)

        self.love = self.get_choice("love", used_names)
        used_names.append(self.love)

        self.date = self.get_choice("date", used_names)

    def display_choices(self):
        expression = (f"I want to marry {self.marry}, I want to love {self.love}, I want to date {self.date}")
        print(expression)

game = Game()
game.get_people()
game.get_choices()
game.display_choices()

