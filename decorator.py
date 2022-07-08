from abc import ABC, abstractmethod


class ComponentInterface():
    __description = "Unknown Beverage"

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str) -> None:
        self.__description = description

    @abstractmethod
    def compute_price(self) -> float:
        pass


class DecoratorInterface(ComponentInterface):
    __component: ComponentInterface = None

    def __init__(self, component: ComponentInterface) -> None:
        self.__component = component

    @property
    def component(self) -> ComponentInterface:
        return self.__component


class Espresso(ComponentInterface):
    description = "Espresso"

    def compute_price(self) -> float:
        return 1.99


class HouseBlend(ComponentInterface):
    description = "House Blend Coffee"

    def compute_price(self) -> float:
        return 0.89


class Mocha(DecoratorInterface):
    def __init__(self, beverage: ComponentInterface):
        self.beverage = beverage
        self.description = beverage.description + ", Mocha"

    def compute_price(self):
        return self.beverage.compute_price() + 0.20


if __name__ == "__main__":
    beverage1 = Espresso()
    print(f"{beverage1.description} ${beverage1.compute_price()}")

    beverage2 = HouseBlend()
    beverage2 = Mocha(beverage2)
    print(f"{beverage2.description} ${beverage2.compute_price()}")
