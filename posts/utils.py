import random

USERNAME_ADJECTIVES = ("Scared", "Lonely", "Alive", "Large", "Big",
    "Nice", "Technical", "Visible", "Unhappy", "Famous",
    "Similar", "Eastern", "Actual", "Existing", "Typical",
    "Odd", "Federal", "Dangerous", "Nervous", "Healthy",
    "Relevant", "Tiny", "Pure", "Boring", "Anxious", "Civil",
    "Cute", "Dramatic", "Tall", "Poor", "Northern", "Popular",
    "Afraid", "Expensive", "Pregnant", "Known", "Happy",
    "Blue", "Yellow", "Decent", "Exciting", "Helpful",
    "Accurate", "Pleasant", "Obvious", "Mental", "Massive",
    "Basic", "Strict", "Different", "Unusual", "Cool",
    "Lucky", "Guilty", "Crazy", "Serious")
    
USERNAME_NOUNS = ("Alligator", "Alpaca", "Ant", "Ape", "Baboon", "Bat",
    "Bear", "Beaver", "Bee", "Bird", "Cow", "Coyote",
    "Crab", "Cricket", "Crocodile", "Crow", "Deer",
    "Dinosaur", "Dog", "Dolphin", "Donkey", "Dragonfly",
    "Duck", "Eagle", "Eel", "Elephant", "Falcon", "Ferret",
    "Fish", "Flamingo", "Fox", "Frog", "Goat", "Goose",
    "Gopher", "Gorilla", "Hamster", "Hawk", "Horse",
    "Husky", "Kangaroo", "Lion", "Lizard", "Llama",
    "Lobster", "Monkey", "Moose", "Mosquito", "Moth",
    "Octopus", "Orca", "Ostrich", "Otter", "Owl", "Panda",
    "Parrot", "Peacock", "Penguin", "Pig", "Pigeon",
    "Rabbit", "Raccoon", "Rat", "Raven", "Sheep", "Skunk",
    "Snail", "Snake", "Spider", "Tiger", "Walrus", "Whale",
    "Wolf", "Zebra")

# Returns a string consisting of an adjective, followed by a
# noun and 3 numbers ranging from 000 to 999. Ex : LuckyCrab123
def generate_username():
    return f"{random.choice(USERNAME_ADJECTIVES)}{random.choice(USERNAME_NOUNS)}{random.randint(1, 999):03}"