import random

# Open and read the contents of the text file
with open('wordlist.txt', 'r') as file:
    text_file_contents = file.read()

# Process wordlists
fours = []
fives = []
sixes = []
sevens = []

# Split the contents of the file into lines for processing
wordlist_lines = text_file_contents.split('\n')
for line in wordlist_lines:
    line = line.strip()
    if len(line) == 4:
        fours.append(line)
    elif len(line) == 5:
        fives.append(line)
    elif len(line) == 6:
        sixes.append(line)
    elif len(line) == 7:
        sevens.append(line)

# Create new lists and fill with a number of items in fours
fivesLess = []
sixesLess = []
sevensLess = []

# Open a file to write the seeds
with open('myseed.txt', 'w') as seeds_file:
    # Generate 1000 different seeds
    for _ in range(1000):
        fivesCounter = 0
        while fivesCounter < len(fours):
            randFive = random.choice(fives)
            if randFive not in fivesLess:
                fivesLess.append(randFive)
                fivesCounter += 1

        sixesCounter = 0
        while sixesCounter < len(fours):
            randSix = random.choice(sixes)
            if randSix not in sixesLess:
                sixesLess.append(randSix)
                sixesCounter += 1

        sevensCounter = 0
        while sevensCounter < len(fours):
            randSeven = random.choice(sevens)
            if randSeven not in sevensLess:
                sevensLess.append(randSeven)
                sevensCounter += 1

        choices = [fours, fivesLess, sixesLess, sevensLess]

        # Generate a single seed
        seed = []
        for _ in range(12):
            wordLengthChoice = random.choice(choices)
            wordChoice = random.choice(wordLengthChoice)
            seed.append(wordChoice)

        # Remove commas, brackets, and apostrophes from the seed
        seed_cleaned = [word.replace(',', '').replace('[', '').replace(']', '').replace("'", '') for word in seed]

        # Print the cleaned seed to the console
        print(seed_cleaned)

        # Write the cleaned seed to the file
        seeds_file.write(' '.join(seed_cleaned) + '\n')

        # Clear lists for the next iteration
        fivesLess.clear()
        sixesLess.clear()
        sevensLess.clear()
