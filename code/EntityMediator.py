class EntityMediator:
    @staticmethod
    def verify_collision(entity_list):
        for index_1 in range(len(entity_list)):
            ent1 = entity_list[index_1]
            if ent1 is None: continue

            for index_2 in range(index_1 + 1, len(entity_list)):
                ent2 = entity_list[index_2]
                if ent2 is None: continue

                event_type = EntityMediator.__verify_collision_entity(ent1, ent2)
                if event_type:
                    return ent1, ent2, event_type

        return None, None, None

    @staticmethod
    def __verify_collision_entity(ent1, ent2):
        if ent1.rect.colliderect(ent2.rect):
            shot_names = ["StoneShoot"]
            enemy_names = ["FoxPredator", "DogPredator"]
            prey_names = ["Chicken", "Bull"]

            if (ent1.name in shot_names and ent2.name in enemy_names) or \
                    (ent2.name in shot_names and ent1.name in enemy_names):
                return "STRIKE"

            if (ent1.name in enemy_names and ent2.name in prey_names) or \
                    (ent2.name in enemy_names and ent1.name in prey_names):
                return "CAUGHT"

        return None