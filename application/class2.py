from class1 import Football


class Players(Football):
    def __init__(self, player_name, ranking, coach, appearances, score, team_name):
        super().__init__(coach, ranking, team_name, player_name)
        self.appearances = appearances
        self.score = score
        self.team = team_name

    def get_score(self):
        print(self.score)

    def get_third_ranked_player_info(self):

        third_player = "{} is the {}-rd ranked player with {} appearances and plays for {}."
        print(third_player.format(self.player_name, self.rank, self.appearances, self.team))

    def get_second_ranked_player_info(self):
        second_player = "{} is the {}-nd ranked player with {} appearances and plays for {}."
        print(second_player.format(self.player_name, self.rank, self.appearances, self.team))

    def get_first_ranked_player_info(self):
        first_player = "{} is the {}-st ranked player with {} appearances and plays for {}."
        print(first_player.format(self.player_name, self.rank, self.appearances, self.team))








