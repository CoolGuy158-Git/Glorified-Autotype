"""
first-order Markov language model
---
say you have a dict(the model):
{
"cats" ["are", "amazing", "lazy"]
"dogs" ["are", "big", "strong"]
"are" ["cute", "big"]
}
and you have this user input:
"I like cats"

it takes the word last word it can recognize, in this case its "cats".
It then picks a random word from the list.
let's say it picked "are"
it then picks another word from the list of the key "are"
say it landed on "cute"
the LM then spits out the completed sentence
"are cute"
but since I remove the first word from the final response to make it less like an autotype it turns to
"cute"

input: "I like cats"
output: "cute"
"""

import ast
import random
import string
import time

with open("model.txt", "r") as model:
    model_list = ast.literal_eval(model.read())
while True:
    user_input = input("\n> ").strip(string.punctuation)
    user_input = " ".join(user_input.split()[::-1])
    if user_input == "exit":
        break
    last_word = None
    for words in user_input.split():
        if words.lower() in model_list:
            last_word = words.lower()
    if last_word is None:
        print("Unfortunately, I do not know how to respond to that.")
        break
    first = True
    print("*Analyzation*---------------------------------")
    print(f"Word that rings a bell: {last_word}")
    final_output = []
    for i in range(random.randint(6, 30)):
        while last_word not in model_list: # If it chooses a word that's not on the list
            last_word = random.choice(model_list[random.choice(list(model_list.keys()))]) # Try picking a new one

        next_words = model_list[last_word]
        print(f"Known next words: {next_words}, last word: {last_word}")
        current_word = random.choice(next_words)
        if not first: # Basically this is an attempt to make it less like its just completing what you're saying, but more like actually responding to your input
            final_output.append(current_word)
        last_word = current_word
        first = False
    print("----------------------------------------------")
    print("Generating response...")
    time.sleep(0.3)
    print("\n----------------------------------------------")
    print("AI Response:")
    print(f"    {' '.join(final_output)}.")
    print("\n----------------------------------------------")

