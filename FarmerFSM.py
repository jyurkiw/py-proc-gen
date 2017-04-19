from AI import FSM, Position
import random


class Farmer(FSM.FiniteStateMachine, Position.Location):
    """
    The farmer will...
        Relax at home until his stamina goes above 90.
        If well-rested and at home, he'll go to the fields.
        When at the fields he'll work until his stamina drops below 10.
        When going home from the fields, he'll walk until his stamina drops below 10.
            If below 10 while walking home he'll rest until his stamina is above 20.
    """
    def __init__(self):
        self.stamina = 90
        self.distance_from_house = 0
        self.name = "Frank"
        self.message = ""

        FSM.FiniteStateMachine.__init__(self, self.relaxing_state)
        Position.Location.__init__(self, Position.HOUSE)

    def relaxing_state(self):
        self.stamina += random.randint(1, 7)
        self.message = "Relaxing!"

        if self.stamina > 90 and self.location is Position.HOUSE:
            self.message = "Done relaxing. Back to work!"
            self.set_state(self.go_to_fields)
        elif self.location is Position.FIELD and self.stamina > 20:
            self.message = "Caught my breath! Heading home."
            self.set_state(self.go_home_state)

    def go_to_fields(self):
        self.distance_from_house += random.randint(4, 13)
        self.stamina -= random.randint(1, 3)

        if self.distance_from_house >= 100:
            self.set_state(self.work_field_state)
            self.location = Position.FIELD
            self.message = "Time to start working!"
        else:
            self.message = "Walking to the fields"

    def go_home_state(self):
        self.distance_from_house -= random.randint(3, 10)
        self.stamina -= random.randint(1, 3)

        if self.distance_from_house <= 0:
            self.set_state(self.relaxing_state)
            self.location = Position.HOUSE
            self.message = "Going to take a load off."
        elif self.stamina < 10 and self.location is Position.FIELD:
            self.set_state(self.relaxing_state)
            self.message = "Been workin' hard. Need to catch my breath!"
        else:
            self.message = "Walking home!"

    def work_field_state(self):
        self.stamina -= random.randint(2, 6)

        if self.stamina <= 20:
            self.set_state(self.go_home_state)
            self.message = "Done working the fields! Time to go home."
        else:
            self.message = "Hard work pays off!"


class Mira(FSM.FiniteStateMachine, Position.Location):
    """
    Mira will...
        Relax at home until her stamina is above 60.
        If well-rested and at home and dinner is not ready, she'll cook dinner.
            If she doesn't have any vegetables, she'll get them from the pantry.
            If she has vegetables, she'll cook them into a stew.
        If well-rested and at home and dinner is ready, she'll go to the forest to pick flowers.
        If in the Forest, she'll look for flowers.
            If she finds any she'll pick them.
            If she doesn't, she'll also look for mushrooms.
            If she finds mushrooms, she'll pick them.
        If in the Forest and her stamina drops below 20, she'll go home.
        If heading home from the Forest and her stamina drops below 10, she'll relax and catch her breath.
    """
    def __init__(self):
        self.stamina = 60
        self.distance_from_house = 0
        self.has_vegetables = False
        self.dinner_is_cooked = False
        self.dinner_completion = 0
        self.name = "Mira"
        self.message = ""

        FSM.FiniteStateMachine.__init__(self, self.relaxing_state)
        Position.Location.__init__(self, Position.HOUSE)

    def relaxing_state(self):
        self.stamina += random.randint(1, 7)
        self.message = "Relaxing!"

        if self.stamina > 60 and self.location is Position.HOUSE and not self.dinner_is_cooked:
            self.message = "Going to cook up a tasty stew!"
            self.set_state(self.cook_dinner_state)
        elif self.stamina > 60 and self.location is Position.HOUSE and self.distance_from_house <= 0 and self.dinner_is_cooked:
            self.message = "This place could use some flowers!"
            self.set_state(self.go_to_forest_state)
        elif self.stamina > 60 and self.location is Position.HOUSE and self.distance_from_house > 0 and self.dinner_is_cooked:
            self.message = "My feed don't hurt as much! Time to go to the forest."
            self.set_state(self.go_to_forest_state)
        elif self.stamina > 30 and self.location is Position.FOREST:
            self.message = "My feet don't hurt as much! Time to get back home."
            self.set_state(self.go_home_state)

    def cook_dinner_state(self):
        self.stamina -= random.randint(1, 11)
        self.message = "Cooking up a tasty stew!"

        if not self.has_vegetables:
            self.message = "Need some tasty vegetables before I start cooking!"
            self.set_state(self.fetch_vegetables_state)
        elif self.dinner_completion < 100 and self.stamina < 25:
            self.message = "Cooking up a tasty stew is a lot of hard work!"
            self.set_state(self.relaxing_state)
        elif self.dinner_completion < 100:
            self.dinner_completion += random.randint(5, 25)
        elif self.dinner_completion >= 100:
            self.dinner_is_cooked = True
            self.message = "This stew looks tasty!"
            self.set_state(self.relaxing_state)

    def fetch_vegetables_state(self):
        self.stamina -= random.randint(5, 11)
        self.message = "I've got some lovely vegetables in the pantry!"
        self.has_vegetables = True
        self.set_state(self.cook_dinner_state)

    def go_to_forest_state(self):
        self.stamina -= random.randint(1, 3)
        self.distance_from_house += random.randint(3, 10)
        self.message = "Heading to the forest!"

        if self.distance_from_house >= 75 and self.location is Position.HOUSE:
            self.message = "In the forest. Time to look for some flowers!"
            self.location = Position.FOREST
            self.set_state(self.look_for_flowers_state)
        elif self.location is Position.HOUSE and self.stamina < 40:
            self.message = "Ow! My feet hurt from all this walking!"
            self.set_state(self.relaxing_state)

    def go_home_state(self):
        self.stamina -= random.randint(1, 4)
        self.distance_from_house -= random.randint(3, 9)
        self.message = "Heading home!"

        if self.location is Position.FOREST and self.stamina < 10:
            self.message = "Ow! My feet hurt from all this walking!"
            self.set_state(self.relaxing_state)
        elif self.location is Position.FOREST and self.distance_from_house <= 0:
            self.message = "Finally home!"
            self.location = Position.HOUSE
            self.set_state(self.relaxing_state)

    def look_for_flowers_state(self):
        self.stamina -= random.randint(1, 6)
        self.distance_from_house += random.randint(1, 6)
        self.message = "Looking for flowers!"

        find_score = random.randint(1, 101)
        if self.stamina < 10:
            self.message = "Couldn't find any flowers, and now I'm tired."
            self.set_state(self.go_home_state)
        elif 60 <= find_score <= 90:
            self.message = "Found some pretty flowers!"
            self.set_state(self.pick_flowers_state)
        elif find_score > 90:
            self.message = "Found some yummy mushrooms!"
            self.set_state(self.pick_mushrooms_state)

    def pick_flowers_state(self):
        self.stamina -= random.randint(1, 4)
        self.distance_from_house += random.randint(0, 3)
        self.message = "Picking pretty flowers!"

        if self.stamina < 20:
            self.message = "Look at all the pretty flowers I picked! It's time to go home."
            self.set_state(self.go_home_state)

    def pick_mushrooms_state(self):
        self.stamina -= random.randint(2, 5)
        self.distance_from_house += random.randint(0, 3)
        self.message = "Picking some yummy mushrooms!"

        if self.stamina < 20:
            self.message = "Look at all the yummy mushrooms I picked! It's time to go home."
            self.set_state(self.go_home_state)


def print_message(agent):
    print(agent.name + ": " + agent.message)


def main_loop(agent_list):
    for turn in range(0, 200):
        for agent in agent_list:
            agent.run_state()
            print_message(agent)
        print("---------------")


if __name__ == "__main__":
    farmer = Farmer()
    mira = Mira()
    main_loop([farmer, mira])


