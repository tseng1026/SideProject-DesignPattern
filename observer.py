from typing import List
from abc import ABC, abstractmethod


class ObserverInterface():
    @abstractmethod
    def update(self,
               temperature: float,
               humidity: float,
               pressure: float,
               ) -> None:
        """Reveive updates from subject."""
        pass


class SubjectInterface():
    @abstractmethod
    def register_observer(self, observer: ObserverInterface) -> None:
        """Attach an observer to the subject."""
        pass

    @abstractmethod
    def remove_observer(self, observer: ObserverInterface) -> None:
        """Detach an observer from the subject."""
        pass

    @abstractmethod
    def notify_observers(self) -> None:
        """Notify all observers about the events."""
        pass


class DisplayElementInterface(ABC):
    @abstractmethod
    def display(self) -> None:
        """Display data provide by the observable subject."""
        pass


class WeatherData(SubjectInterface):
    """WeatherData as an observable subject, containing the measurements temperature, humidity, pressure."""

    def __init__(self) -> None:
        self.__observers: List = []
        self.__temperature: float = 0.
        self.__humidity: float = 0.
        self.__pressure: float = 0.

    def register_observer(self, observer: ObserverInterface) -> None:
        """Attach an observer to the WeatherData (subject)."""
        if observer not in self.__observers:
            self.__observers.append(observer)
        else:
            raise("Failed to add observer")

    def remove_observer(self, observer: ObserverInterface) -> None:
        """Detach an observer from the WeatherData (subject)."""
        try:
            self.__observers.remove(observer)
        except ValueError:
            raise("Failed to remove observer")

    def notify_observers(self) -> None:
        """Notify all observers about the changes in measurements (event)."""
        for observer in self.__observers:
            observer.update(
                self.temperature, self.humidity, self.pressure)

    def set_measurements(self,
                         temperature: float,
                         humidity: float,
                         pressure: float,
                         ) -> None:
        """Set measurements manually."""
        self.__temperature = temperature
        self.__humidity = humidity
        self.__pressure = pressure
        self.notify_observers()

    @property
    def temperature(self) -> float:
        return self.__temperature

    @property
    def humidity(self) -> float:
        return self.__humidity

    @property
    def pressure(self) -> float:
        return self.__pressure


class CurrentConditionsDisplay(ObserverInterface, DisplayElementInterface):
    """CurrentConditionsDisplay as an observer of weatherData and display the measurements."""

    def __init__(self, weatherData: SubjectInterface) -> None:
        self.weatherData = weatherData
        self.weatherData.register_observer(self)

    def update(self,
               temperature: float,
               humidity: float,
               pressure: float,
               ) -> None:
        """Receive updates from WeatherData (subject)."""
        self.display(temperature, humidity, pressure)

    def display(self,
                temperature: float,
                humidity: float,
                pressure: float,
                ) -> None:
        """Display data provided by WeatherData (subject)."""
        print(
            f"Current Conditions: temperature {temperature}, humidity {humidity}%, and pressure {pressure} atm")


if __name__ == "__main__":
    weatherData = WeatherData()
    currentDisplay = CurrentConditionsDisplay(weatherData)

    weatherData.set_measurements(80, 65, 30.4)
    weatherData.set_measurements(82, 70, 29.2)
    weatherData.set_measurements(78, 90, 29.2)
