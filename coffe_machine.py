class Coffee:
    def grindCoffee(self):

        pass


    def makeCoffee(self):

        pass

    def pourIntoCup(self):

        pass

class Espresso(Coffee):
    def grindCoffee(self):
        print("Grinding coffee beans for Espresso!")

    def makeCoffee(self):
        print("Mixing Espresso!")

    def pourIntoCup(self):
        print("Pouring Espresso in the cup!")

class Capuccino(Coffee):
    def grindCoffee(self):
        print("Grinding coffee beans for Capuccino!")

    def makeCoffee(self):
        print("Mixing Capuccino!")

    def pourIntoCup(self):
        print("Pouring Capuccino in the cup!")

class Americano(Coffee):
    def grindCoffee(self):
        print("Grinding coffe beans for Americano!")

    def makeCoffee(self):
        print("Mixing Americano!")

    def pourIntoCup(self):
        print("Pouring Americano in the cup!")

class CoffeeFactory:
    def checkCoffe(type:str)-> Coffee:
        match type:
            case "Espresso":
                return Espresso()
            case "Capuccino":
                return Capuccino()
            case "Americano":
                return Americano()


coffee=CoffeeFactory.checkCoffe("Espresso")

coffee.grindCoffee()
coffee.makeCoffee()
coffee.pourIntoCup()











