import random

#TODO: Find a shark fact API and use it. 

facts = []

facts.append("Dorsal side (their backs) of the shark's body is dark in color (black, grey, brownish) and their bellies are completely white. Specific body coloration is excellent camouflage that prevents prey from seeing the shark.")
facts.append("Great White Sharks can eat entire sea lion in a single meal.")
facts.append("Great White sharks are solitary animals. They gather only during mating season.")
facts.append("Great White Sharks have excellent sense of smell: they can smell one drop of blood in a million drops of water!")
facts.append("Most sharks become motionless when they are flipped over. This phenomenon is called tonic immobility and Great Whites may experience it also. Orcas use this technique to defeat Great White Shark - they keep the shark flipped over until it stops breathing.")
facts.append("Basking sharks swim slowly and spend most of their time close to the surface of the water. This shark is named basking shark because it looks like it is basking in the sun while it swims and collects food.")
facts.append("Bull sharks are active both during the night and day.")
facts.append("Bull shark is carnivore with great appetite. Fish, turtles, crustaceans, dolphins, birds and other sharks, are normal part of the bull shark's menu.")
facts.append("Nurse shark is docile by nature, but it will bite when it is provoked.")
facts.append("Nurse shark is a carnivore. Its diet is based on the small fish, lobsters, crabs, sea urchins, squids, snails and bivalve.")
facts.append("Speartooth shark relies on the electro-receptors (called ampullae of Lorenzini) to detect movement of the prey (fish) in the water.")


# Returns a random shark fact from the facts array.
def get_fact():
    return random.choice(facts)