class Football:
    def __init__(self, coach, ranking, team_name, player_name):
        self.coach = coach
        self.team_name = team_name
        self.rank = ranking
        self.player_name = player_name

    def get_player_name(self):
        print(self.player_name)

    def get_coach(self):
        if self.rank > 5:
            print(self.coach + "is about to get sacked if he does not improve his rank")
        elif self.rank == 3:
            coach_three = "{} is ranked {}-rd and is manager of {}."
            print(coach_three.format(self.coach, self.rank, self.team_name))
            print("He is on fire and need a bit more to be on the top.")
            print()
        elif self.rank == 2:
            coach_two = "{} is ranked {}-nd and is manager of {}."
            print(coach_two.format(self.coach, self.rank, self.team_name))
            print("He is the second of the top 3 coaches in the world.")
            print()
        elif self.rank == 1:
            coach_one = "{} is ranked {}-st and is manager of {}."
            print(coach_one.format(self.coach, self.rank, self.team_name))
            print("He is the best coach for 2020. We hope he keeps on like that.")
            print()
