from typing import List
from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass

    @abstractmethod
    def undo(self) -> None:
        pass


class NoCommand(Command):
    def execute(self) -> None:
        print("No command!")

    def undo(self) -> None:
        print("No command!")


class LightOnCommand(Command):
    def execute(self) -> None:
        print("Light on!")

    def undo(self) -> None:
        LightOffCommand().execute()


class LightOffCommand(Command):
    def execute(self) -> None:
        print("Light off!")

    def undo(self) -> None:
        LightOnCommand().execute()


class StereoOnCommand(Command):
    def execute(self) -> None:
        print("Stereo on!")

    def undo(self) -> None:
        StereoOffCommand().execute()


class StereoOffCommand(Command):
    def execute(self) -> None:
        print("Stereo off!")

    def undo(self) -> None:
        StereoOnCommand().execute()


class MacroCommand(Command):
    def __init__(self, commands: List[Command]) -> None:
        self.commands = commands

    def execute(self) -> None:
        for command in self.commands:
            command.execute()

    def undo(self) -> None:
        for command in self.commands:
            command.undo()


class RemoteControl():
    def __init__(self) -> None:
        self.on_commands: List[Command] = [NoCommand()] * 3
        self.off_commands: List[Command] = [NoCommand()] * 3
        self.undo_command: Command = NoCommand()

    def set_command(
        self,
        slot: int,
        on_command: Command,
        off_command: Command,
    ) -> None:
        self.on_commands[slot] = on_command
        self.off_commands[slot] = off_command

    def press_button_on(self, slot: int) -> None:
        self.on_commands[slot].execute()
        self.undo_command = self.on_commands[slot]

    def press_button_off(self, slot: int) -> None:
        self.off_commands[slot].execute()
        self.undo_command = self.off_commands[slot]

    def press_button_undo(self) -> None:
        self.undo_command.undo()


if __name__ == "__main__":
    remote_control = RemoteControl()

    remote_control.press_button_on(0)
    remote_control.press_button_off(0)

    remote_control.set_command(
        1,
        LightOnCommand(),
        LightOffCommand(),
    )
    remote_control.press_button_on(1)
    remote_control.press_button_off(1)

    remote_control.set_command(
        2,
        MacroCommand([LightOnCommand(), StereoOnCommand()]),
        MacroCommand([LightOffCommand(), StereoOffCommand()]),
    )
    remote_control.press_button_on(2)
    remote_control.press_button_off(2)
    remote_control.press_button_undo()
