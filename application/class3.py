from class2 import Players
import datetime


class Person(Players):
    def __init__(self, player_name, birthdate, city, profession, team_name, coach):
        super(Person, self).__init__(player_name, coach,
                                     NotImplemented, NotImplemented,NotImplemented, team_name)
        self.birthdate = birthdate
        self.profession = profession
        self.city = city

    def age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate
        return age

    def display_player_info(self):
        player_info = "His name is {} and is born on {} in {}. He is {} and plays for {}."
        print(player_info.format(self.player_name, self.birthdate, self.city, self.profession, self.team_name))

    def display_coach_info(self):
        coach_info = "His name is Hans-Dieter Flick and is born on {} in {}. He is {} and manages {}."
        print(coach_info.format(self.birthdate, self.city, self.profession, self.team_name))
