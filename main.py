"""
second-order Markov language model
---
say you have a dict(the model):
{
("cats", "are"): ["cute", "amazing", "lazy"]
("dogs", "are"): ["big", "strong", "puppies"]
}
and you have this user input:
"I like cats"

it takes the pair of words it can recognize, in this case
("like", "cats").
It then picks a random word from the list.
let's say it picked "are"
it then takes the second word from the pair and the new word
and makes a new pair:
("cats", "are")

it then picks another word from the list of the new pair.
say it landed on "cute"
the LM then spits out the completed sentence
"are cute"
but since I remove the first word from the final response
to make it less like an autotype it turns to
"cute"

input: "I like cats"
output: "cute"

also it prioritizes VERB+NOUN/PRONOUN pairs.
"""

import ast
import random
import string
import time

# I'll give a little warning cuz when I tested it, it kinda said something racist HELP
print("""
************************************************************************************************
| WARNING!                                                                                     |
| This Ai doesn't have any filters!                                                            |
| What it says depends entirely on the training data you decide to feed it, AND RANDOMNESS!    |
| IT HAS NO MIND.                                                                              |
************************************************************************************************
""")
from nltk.tag import RegexpTagger # It takes time to import so ill just add it under the print warning, this acts like the time.sleep()
mode = "image"
with open("model.txt", "r", encoding="utf-8") as model:
    model_list = ast.literal_eval(model.read())
print("Glorified Auto-Type LM")
tagger = RegexpTagger([ # Imma try this lib, it's basically a bunch of defined rules on what a verb/noun might be
    (r".*(ing)$", "VBG"),
    (r".*ed$", "VBD"),
    (r".*ly$", "RB"),
    (r".*(tion|ment|ness)$", "NN"),
    (r"^(want|like|love|need|learn|play|make|get|have|know|think|see|watch|use|build|write|do|does|did)$", "VB"), # Other extra verbs, just in case the rules won't catch these
    (r".*", "NN")
])
while True:
    og_user_input = input("\n> ").strip(string.punctuation)
    user_input = " ".join(og_user_input.split()[::-1])
    if user_input == "exit":
        break
    last_word = None
    words = user_input.split()

    original_words = og_user_input.split()
    tags = tagger.tag([word.lower().strip(string.punctuation) for word in original_words])
    # Get VERB + NOUN pairs
    for i in range(len(tags) - 1):
        first_word, first_tag = tags[i]
        second_word, second_tag = tags[i + 1]

        if first_tag in ("VB", "VBG", "VBD", "VBN", "VBP", "VBZ"):
            if second_tag in ("NN", "NNP", "NNS", "NNPS"):
                pair = (first_word, second_word)
                if pair in model_list:
                    last_word = pair
                    break

    # Fallback just get the other stuff
    if last_word is None:
        words = user_input.split()

        for i in range(len(words) - 1):
            pair = (words[i + 1].lower(), words[i].lower())

            if pair in model_list:
                last_word = pair
                break
    if last_word is None:
        print("Unfortunately, I do not know how to respond to that.")
        print("Try saying something like 'Hello there my dear friend, how are you today?'")
        continue
    first = True
    print("*Analyzation*---------------------------------")
    print(f"Pair that rings a bell: {last_word}")
    final_output = []
    for i in range(50): # Max response is 50 chars
        while last_word not in model_list: # If it chooses a word that's not on the list
            last_word = random.choice(list(model_list.keys())) # Try picking a new one

        next_words = model_list[last_word]
        # print(f"Known next words: {next_words}, last word: {last_word}")
        current_word = random.choice(next_words)
        print(f"Picked word: {current_word}")
        if current_word.endswith((".", "!", "?")): # If sentence ends then just end response
            final_output.append(current_word)
            print("-END-")
            break

        if not first: # Basically this is an attempt to make it less like its just completing what you're saying, but more like actually responding to your input
            final_output.append(current_word)
            if len(final_output) % 10 == 0:
                final_output.append("\n")
        last_word = (last_word[1], current_word)
        first = False

    print("----------------------------------------------")
    print("Generating response...")
    time.sleep(0.3)
    print("\n----------------------------------------------")
    print(f"Prompt: {og_user_input}")
    print("AI Response:")
    print(f"    {' '.join(final_output)}.")
    print("\n----------------------------------------------")


