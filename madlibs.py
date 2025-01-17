# Import random module
import random

# Ask for user input function
def user_prompts():
    """ Prompts user for inputs for Madlbs game. """
    # Prompt user for inputs to store as a dictionary
    dict_of_words = {
        'animal': input('Please enter a type of animal: ').lower(),
        'noun': input('Please enter a noun (person, place or thing): ').lower(),
        'adjective': input('Please enter an adjective (word describing a noun): ').lower(),
        'place': input('Please enter a place name: ').lower(),
        'verb': input('Please enter a verb (doing action, without -ing): ').lower()
    } 
    # Store user inputs as a dictionary
    return dict_of_words

# Function that generates the madlibs
def generate_madlibs(dict_of_words):
    """ Initiate sample stories and select one """
    # A list of stories to choose from
    sample_stories = [
    "The {adjective} {animal} discovered a {noun} hiding behind the {place}.",
    "Deep in the {place}, a {adjective} {noun} learned how to {verb} from a wise {animal}.",
    "Nobody knew why the {noun} would {verb} every time it visited the {place}.",
    "The {adjective} {animal} built a secret {place} where {noun}s could {verb} freely.",
    "There was a legend about a {adjective} {noun} that would {verb} near the {place}.",
    "Every {animal} in the {place} wanted to {verb} with the {adjective} {noun}.",
    "The most {adjective} {place} was home to a {noun} that loved to {verb}.",
    "A {adjective} {animal} taught the {noun} how to {verb} in the middle of the {place}.",
    "The {noun} had never seen such a {adjective} {animal} {verb} before.",
    "At the edge of the {place}, the {adjective} {noun} met a mysterious {animal}.",
    "The {animal} couldn't believe that the {noun} could {verb} so {adjective}.",
    "Inside the {place}, the {adjective} {animal} found a {noun} trying to {verb}.",
    "The {noun} traveled to every {place} to {verb} with each {adjective} {animal}.",
    "Sometimes the {adjective} {noun} would {verb} while the {animal} watched.",
    "The {place} became famous when a {adjective} {animal} and {noun} decided to {verb} there."
]
    # Select a story from above sample stories
    story = random.choice(sample_stories)
    # Unpack dictionary and pass in user inputs to format the story
    return story.format(**dict_of_words)


def main():
    """ Main program that generates a complete Madlibs game. """
    print("Welcome to Madlibs, let's make a fun story! \n")
     # Store user inputs by calling user_inputs()
    words = user_prompts()
    # Store the story and add the prompts to the story
    madlib = generate_madlibs(words)
    print("Enjoy your story: ")
    print(madlib)

# Execute the game
if __name__ == "__main__":
    main()
