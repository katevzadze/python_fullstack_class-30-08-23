from typing import Literal


class Animal:
    def __init__(
            self,
            animal_type: str,
            animal_talk: str,
            animal_eat: Literal["мясо", "рыбу", "траву"]):
        self.animal_type = animal_type
        self.animal_talk = animal_talk
        self.animal_eat = animal_eat

    def __str__(self) -> str:
        return f"Это {self.animal_type}."

    def action(self) -> str:
        return f"{self.animal_type} издает звук {self.animal_talk} и ест {self.animal_eat}."


tiger = Animal("Тигр", "ррр", "мясо")
cat = Animal("Кот", "мяу", "рыбу")
caw = Animal("Корова", "му", "траву")
print(tiger, tiger.action())
print(cat, cat.action())
print(caw, caw.action())
