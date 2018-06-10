from Duck import *
from Sparrow import *


class DepartmentManager:
    birds = []

    def find_by_run_type(self, isRunAway):
        founded_birds = []

        for bird in self.birds:
            if bird.isRunAway == isRunAway:
                founded_birds.append(bird)

        return founded_birds

    def sortByWeight(self):
        self.birds.sort(key=lambda bird: bird.weight)
        return self.birds

    @staticmethod
    def print_list(printed_list):
        for bird in printed_list:
            print(bird)

    print("\n")


if __name__ == '__main__':
    manager = DepartmentManager()
    duck = Birds(5, "don't run away", "Duck")
    sparrow = Birds(30, "run away", "Sparrow")
    stock = Birds(10, "run away", "Stock")
    manager.birds = [duck, sparrow, stock]
    manager.birds = manager.find_by_run_type("run away")
    manager.birds = manager.sortByWeight()
    manager.print_list(manager.birds)
