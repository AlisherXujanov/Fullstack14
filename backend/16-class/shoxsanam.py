class ElectronicItems:
    """Types of electronic items"""

    def __init__(self, name: str, battery_level: int = 100,  sound_type: str = 'Stereo') -> None:
        self.name = name
        self.battery_level = battery_level
        self.sound_type = sound_type

    def __str__(self):
        return f"{self.name} has {self.battery_level}% battery level and {self.sound_type} sound type"


e_item_1 = ElectronicItems("Headphones", 80, "Surround")
print(e_item_1)


class Phones(ElectronicItems):
    def __init__(self, model: str, name: str, battery_level: int = 100,  sound_type: str = 'Stereo'):
        super().__init__(name, battery_level, sound_type)
        self.model = model

    def __str__(self):
        return super().__str__() + "..."


class SoundSystems:
    ...
