from typing import List
from abc import ABC, abstractmethod


class Pizza(ABC):
    def __init__(self) -> None:
        self.__name: str = ""
        self.__toppings: List = []

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

    @property
    def toppings(self) -> List:
        return self.__toppings

    @toppings.setter
    def toppings(self, toppings: List) -> None:
        self.__toppings = toppings

    def prepare(self) -> None:
        print(f"Preparing {self.name}...")
        print("Tossing dough...")
        print("Adding sauce...")
        print("Adding toppings: ")
        for topping in self.toppings:
            print(f"   {topping}")

    def bake(self) -> None:
        print("Baking for 25 minutes at 350 degrees...")

    def cut(self) -> None:
        print("Cutting the pizza into diagonal slices...")

    def box(self) -> None:
        print("Placing the pizza in official PizzaStore box...")


class ChicagoStyleCheesePizza(Pizza):
    def __init__(self) -> None:
        self.name = "Chicago Style Cheese Pizza"
        self.toppings = ["Shredded Mozzarella Cheese"]

    def cut(self) -> None:
        print("Cutting the pizza into square slices")


class ChicagoStyleVeggiePizza(Pizza):
    def __init__(self) -> None:
        self.name = "Chicago Style Veggie Pizza"
        self.toppings = ["Mushroom", "Pepper"]


class NewYorkStyleCheesePizza(Pizza):
    def __init__(self) -> None:
        self.name = "NewYork Style Cheese Pizza"
        self.toppings = ["Shredded Mozzarella Cheese"]


class NewYorkStylePepperoniPizza(Pizza):
    def __init__(self) -> None:
        self.name = "NewYork Style Pepperoni Pizza"
        self.toppings = ["Susage"]


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
        if pizza_type == "cheese":
            return ChicagoStyleCheesePizza()
        elif pizza_type == "veggie":
            return ChicagoStyleVeggiePizza()
        else:
            raise "Unsupported pizza type."


class NewYorkPizzaStore(PizzaStore):
    def create_pizza(self, pizza_type: str) -> Pizza:
        if pizza_type == "cheese":
            return NewYorkStyleCheesePizza()
        elif pizza_type == "pepperoni":
            return NewYorkStylePepperoniPizza()
        else:
            raise "Unsupported pizza type."


if __name__ == "__main__":
    chicagoStore = ChicagoPizzaStore()
    newYorkStore = NewYorkPizzaStore()

    pizza = chicagoStore.order_pizza("cheese")
    print(f"Here's your {pizza.name}!\n")

    pizza = newYorkStore.order_pizza("pepperoni")
    print(f"Here's your {pizza.name}!\n")
