
from class1 import Football
from class2 import Players
from class3 import Person

player_three = Players("Sergio Ramos", 3, "Zidane", 500, 10, "Real Madrid")
player_two = Players("Lionel Messi", 2, "Ronald Cooman", 650, 19, "Barcelona")
player_one = Players("Cristiano Ronaldo", 1, "Pirlo", 700, 20, "Juventus")

print("Here you can see the top 3 ranked players in the world:\n")
player_three.get_third_ranked_player_info()
player_two.get_second_ranked_player_info()
player_one.get_first_ranked_player_info()
print()
print("Here you can see the top three ranked coaches in the world for 2020:")
print()
coach_three = Football("Gian Piero Gasperini", 3, "Atalanta", None)
coach_two = Football("Jurgen Klopp", 2, "Liverpool", None)
coach_one = Football("Hans-Dieter Flick", 1, "Bayern Munich", None)

coach_three.get_coach()
coach_two.get_coach()
coach_one.get_coach()

person_one = Person("Cristiano Ronaldo", "05.02.1985", "Madeira, Portugal", "professional footballer", "Juventus", None)
person_two = Person("Hans-Dieter Flick", "24.02.1965", "Heidelberg,Germany", "professional football coach",
                    "Bayern Munich", None)

print("Here you can see more information about the best football player and the best manager:\n")
person_one.display_player_info()
person_two.display_coach_info()












