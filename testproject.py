class Defender:
    def __init__(self, name, level, health, spec):
        self.name = name
        self.level = level
        self.health = health
        self.spec = spec
        pass

    def take_damage(self, damage):
        try:
            self.health -= damage
            print(f"{self.name} takes {damage} damage.")
            print(f"{self.name} has {self.health} health remaining.")
            if self.health <= 0:
                raise Exception(f"{self.name} has died.")
        except Exception as e:
            print(e)

class Attacker:
    def __init__(self, name, level, health, spec):
        self.name = name
        self.level = level
        self.health = health
        self.spec = spec
        pass

    def death_bolt(self, target, damage):
        print(f"{self.name} casts death bolt at {target.name} and deals {damage} damage.")
        target.take_damage(damage)
        pass

character_Laienne = Defender("Laienne", 80, 6000000, "Elemental")
character_Sargeras = Attacker("Sargeras", 500, 700000000, "Demon")

print(f"{character_Laienne.name} has {character_Laienne.health} health.")

character_Sargeras.death_bolt(character_Laienne, 1000000)