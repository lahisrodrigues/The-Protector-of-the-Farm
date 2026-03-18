from code.Enemy import Enemy
from code.Player import Player
from code.Prey import Prey


class EntityFactory:
    @staticmethod
    def get_entity(entity_name: str, position: tuple):
        match entity_name:
            case 'Chicken':
                return Prey(name='Chicken', position=position)
            case 'Bull':
                return Prey(name='Bull', position=position)
            case 'FoxPredator':
                return Enemy(name='FoxPredator', position=position)
            case 'DogPredator':
                return Enemy(name='DogPredator', position=position)
            case 'FarmerPlayer':
                return Player(name='FarmerPlayer', position=position)
        return None