# Класс ферма - фабрика животных
from animal_class import Animal
from bird_class import Bird
from dog_class import Dog
from fish_class import Fish

_DOG_NAMES = {"Рэкс", "Лорд", "Джек", "Лайма", "Лора", "Шарик", "Буян", "Бек"}
_FISH_NAMES = {"Карп", "Лещ", "Щука", "Сазан", "Осетр", "Форель", "Сельдь"}
_BIRD_NAMES = {"Сова", "", "", "", "", "", ""}


class Ferma():
    def __init__(self):
        # Количество сгенерированных классов
        self._count_dog = 0
        self._count_fish = 0
        self._count_bird = 0
        # Список сгенерированных животных
        self.list_animals = []

    def generate(self, animal_type: str) -> Animal:
        """Генерация животного

        :animal_type: Вид генерируемого животного
        :return: класс сгенерированного животного
        """
        result = None
        match animal_type:
            case "Dog":
                pass
            case "Bird":
                pass
            case "Fish":
                pass

        return result

    def _gen_dog(self):
        return Dog()
