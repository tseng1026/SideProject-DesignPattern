from typing import List
from abc import ABC, abstractmethod


class Ingredient():
    __name = ""

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name) -> None:
        self.__name = name


class PizzaIngredientFactory(ABC):
    @abstractmethod
    def create_dough(self) -> Ingredient:
        pass

    @abstractmethod
    def create_sauce(self) -> Ingredient:
        pass

    @abstractmethod
    def create_cheese(self) -> Ingredient:
        pass

    @abstractmethod
    def create_clam(self) -> Ingredient:
        pass


class ChicagoPizzaIngredientFactory(PizzaIngredientFactory):
    def create_dough(self) -> Ingredient:
        dough = Ingredient()
        dough.name = "very thin crust dough"
        print(f"Tossing {dough.name}...")
        return dough

    def create_sauce(self) -> Ingredient:
        sauce = Ingredient()
        sauce.name = "brushetta sauce"
        print(f"Adding {sauce.name}...")
        return sauce

    def create_cheese(self) -> Ingredient:
        cheese = Ingredient()
        cheese.name = "goat cheese"
        print(f"Adding {cheese.name}...")
        return cheese

    def create_clam(self) -> Ingredient:
        clam = Ingredient()
        clam.name = "clamari"
        print(f"Adding {clam.name}...")
        return clam


class NewYorkPizzaIngredientFactory(PizzaIngredientFactory):
    def create_dough(self) -> Ingredient:
        dough = Ingredient()
        dough.name = "thin crust dough"
        print(f"Tossing {dough.name}...")
        return dough

    def create_sauce(self) -> Ingredient:
        sauce = Ingredient()
        sauce.name = "marinara sauce"
        print(f"Adding {sauce.name}...")
        return sauce

    def create_cheese(self) -> Ingredient:
        cheese = Ingredient()
        cheese.name = "reggiano cheese"
        print(f"Adding {cheese.name}...")
        return cheese

    def create_clam(self) -> Ingredient:
        clam = Ingredient()
        clam.name = "fresh clam"
        print(f"Adding {clam.name}...")
        return clam


class Pizza(ABC):
    def __init__(self) -> None:
        self.name: str = ""
        self.dough: Ingredient = None
        self.sauce: Ingredient = None
        self.cheese: Ingredient = None
        self.clam: Ingredient = None

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

    @abstractmethod
    def prepare(self) -> None:
        pass

    def bake(self) -> None:
        print("Baking for 25 minutes at 350 degrees...")

    def cut(self) -> None:
        print("Cutting the pizza into diagonal slices...")

    def box(self) -> None:
        print("Placing the pizza in official PizzaStore box...")


class CheesePizza(Pizza):
    def __init__(self, ingredient_factory) -> None:
        self.ingredient_factory = ingredient_factory

    def prepare(self) -> None:
        print("Preparing...")
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()


class ClamPizza(Pizza):
    def __init__(self, ingredient_factory) -> None:
        self.ingredient_factory = ingredient_factory

    def prepare(self) -> None:
        print("Preparing...")
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()
        self.clam = self.ingredient_factory.create_clam()


class PizzaStore(ABC):
    @abstractmethod
    def create_pizza(self, pizza_type: str) -> Pizza:
        pass

    def order_pizza(self, pizza_type: str) -> Pizza:
        self.pizza = self.create_pizza(pizza_type)

        self.pizza.prepare()
        self.pizza.bake()
        self.pizza.cut()
        self.pizza.box()
        return self.pizza


class ChicagoPizzaStore(PizzaStore):
    def create_pizza(self, pizza_type: str) -> Pizza:
        ingredient_factory = ChicagoPizzaIngredientFactory()

        if pizza_type == "cheese":
            pizza = CheesePizza(ingredient_factory)
            pizza.name = "Chicago Style Cheese Pizza"
        elif pizza_type == "clam":
            pizza = ClamPizza(ingredient_factory)
            pizza.name = "Chicago Style Clam Pizza"
        else:
            raise "Unsupported pizza type."
        return pizza


class NewYorkPizzaStore(PizzaStore):
    def create_pizza(self, pizza_type: str) -> Pizza:
        ingredient_factory = NewYorkPizzaIngredientFactory()

        if pizza_type == "cheese":
            pizza = CheesePizza(ingredient_factory)
            pizza.name = "New York Style Cheese Pizza"
        elif pizza_type == "clam":
            pizza = ClamPizza(ingredient_factory)
            pizza.name = "New York Style Clam Pizza"
        else:
            raise "Unsupported pizza type."
        return pizza


if __name__ == "__main__":
    chicagoStore = ChicagoPizzaStore()
    newYorkStore = NewYorkPizzaStore()

    pizza = chicagoStore.order_pizza("cheese")
    print(f"Here's your {pizza.name}!\n")

    pizza = newYorkStore.order_pizza("clam")
    print(f"Here's your {pizza.name}!\n")
