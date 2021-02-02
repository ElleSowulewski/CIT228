dinosaurs = {
    "Spinosaurus": "Carnivore",
    "Parasaur": "Herbivore",
    "Microraptor": "Carnivore",
    "Quetzalcoatlus": "Carnivore",
    "Doedicurus": "Herbivore",
    "Iquanadon": "Herbivore"
}
mythical = {
    "Pegasus": "Herbivore",
    "Wyvern": "Carnivore",
    "Dragon": "Carnivore",
    "Unicorn": "Hervivore",
    "Manticore": "Carnivore",
    "Jackalope": "Herbivore"
}
animals = {
    "Fox": "Carnivore",
    "Giraffe": "Herbivore",
    "Lion": "Carnivore",
    "Hawk": "Carnivore",
    "Zebra": "Herbivore",
    "Chinchilla": "Herbivore"
}

creatures = [dinosaurs, mythical, animals]
for creature in creatures:
    print(creature)
