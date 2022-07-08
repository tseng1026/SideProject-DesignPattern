class SingletonMeta(type):
    def __init__(self, *args, **kwargs):
        self.__instance = None
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = super().__call__(*args, **kwargs)

        return self.__instance


class ChocolateBoiler(metaclass=SingletonMeta):
    def __init__(self) -> None:
        self.empty = True
        self.boiled = False

    def fill(self) -> None:
        if self.isEmpty():
            self.empty = False
            self.boiled = False

    def boil(self) -> None:
        if not self.isEmpty() and not self.isBoiled():
            self.boiled = True

    def drain(self) -> None:
        if not self.isEmpty() and not self.isBoiled():
            self.empty = True

    def isEmpty(self) -> bool:
        return self.empty

    def isBoiled(self) -> bool:
        return self.boiled

    def showStatus(self) -> None:
        print(f"isEmpty: {self.isEmpty()},\tisBoiled: {self.isBoiled()}")


if __name__ == "__main__":
    boiler1 = ChocolateBoiler()
    boiler2 = ChocolateBoiler()

    boiler2.showStatus()
    boiler1.fill()
    boiler2.showStatus()
    boiler1.boil()
    boiler2.showStatus()
    boiler1.drain()
    boiler2.showStatus()

    if id(boiler1) == id(boiler1):
        print("Singleton works, both variables contain the same instance.")
    else:
        print("Singleton failed, variables contain different instances.")
