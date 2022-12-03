class human:
    def __init__(self, name):
        self.name = name


class Bus:
    def __init__(self, model, color):
        self.color = color
        self.model = model
        self.passengers = []
    def add_passengers(self, people):
        self.passengers.append(people)


    def print_passengers(self):
        if self.passengers != []:
            print(f"У автобусі {self.model} є такі пасажири ")
            for passenger in self.passengers:
                print(passenger.name)

        else:
            print(f"У автобусі{self.model} немає пасажирів.")


tomato = Bus("tomato","black")
tomato.add_passengers(human("Nazar"))
tomato.add_passengers(human("Oleg"))
tomato.add_passengers(human("Marek"))
tomato.add_passengers(human("Dmytro"))
tomato.add_passengers(human("Taras"))
tomato.print_passengers()
