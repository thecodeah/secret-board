import random

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
    for post in Post.objects.all():
        post_age = (timezone.now() - post.pub_date)

        # Get a set of UNIQUE commenters.
        commenters = set()
        for comment in post.comment_set.all():
            commenters.add(comment.author)

        # The base for popularity points.
        # Likes + Unique comments - age in days.
        post.popularity = (post.likes.count() + len(commenters)) - post_age.days

        # Bonus points for new posts
        if post_age.seconds <= 10:
            post.popularity += 100
        if post_age.seconds <= (5 * 60):
            post.popularity += 1
        if post_age.seconds <= (30 * 60):
            post.popularity += 1
        if post_age.days < 1:
            post.popularity += 3
        if post_age.days <= 7:
            # Posts that are older than a week will have a hard time competing
            # with the new posts.
            post.popularity += 50
        
        post.save()
