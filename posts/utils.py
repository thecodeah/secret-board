import random
import math

from django.utils import timezone

from .models import Post

USERNAME_ADJECTIVES = ("Blue", "Red", "Green", "Purple", "White", "Orange",
    "Black", "Gold", "Silver", "Yellow", "Brown", "Gray", "Pink", "Big",
    "Small", "Rich", "Super", "Crazy", "Square", "Strong", "Tall", "Short",
    "Skinny", "Chubby", "Bald", "Blonde", "Ginger", "Smart", "Young", "Old",
    "Shiny", "Spotty", "Tiny", "Large", "Huge", "Angry")
    
USERNAME_NOUNS = ("Alligator", "Alpaca", "Ant", "Ape", "Baboon", "Bat", "Bear",
    "Beaver", "Bee", "Bird", "Cow", "Coyote", "Crab", "Cricket", "Crocodile",
    "Crow", "Deer", "Dinosaur", "Dog", "Dolphin", "Donkey", "Dragonfly", "Duck",
    "Eagle", "Eel", "Elephant", "Falcon", "Ferret", "Fish", "Flamingo", "Fox",
    "Frog", "Goat", "Goose", "Gopher", "Gorilla", "Hamster", "Hawk", "Horse",
    "Husky", "Kangaroo", "Lion", "Lizard", "Llama", "Lobster", "Monkey",
    "Moose", "Mosquito", "Moth", "Octopus", "Orca", "Ostrich", "Otter", "Owl",
    "Panda", "Parrot", "Peacock", "Penguin", "Pig", "Pigeon", "Rabbit",
    "Raccoon", "Rat", "Raven", "Sheep", "Skunk", "Snail", "Snake", "Spider",
    "Tiger", "Walrus", "Whale", "Wolf", "Zebra")

# Returns a string consisting of an adjective, followed by a
# noun and 2 numbers ranging from 00 to 99. Ex : RedGoose24
def generate_username():
    return f"{random.choice(USERNAME_ADJECTIVES)}{random.choice(USERNAME_NOUNS)}{random.randint(1, 99):02}"

# Loops over each post on the website and updates it's popularity points.
def update_popularity():
    WEEK = (60 * 60 * 12 * 7) # The amount of seconds in a week.
    for post in Post.objects.all():
        post.popularity = 0

        post_age = (timezone.now() - post.pub_date)
        post_age = post_age.total_seconds()

        # The base for popularity points - Time in seconds up to a week.
        if(post_age < WEEK):
            post.popularity = WEEK - post_age

        # Bonus points - Interaction
        ## Get a set of UNIQUE commenters.
        commenters = set()
        for comment in post.comment_set.all():
            commenters.add(comment.author)

        post.popularity += len(commenters) * (60 * 60)
        post.popularity += post.likes.count() * (60 * 30)

        # Limit the popularity so that old posts can't get above new posts due
        # to bonuses.
        if post.popularity > WEEK:
            post.popularity = WEEK
        
        post.save()
