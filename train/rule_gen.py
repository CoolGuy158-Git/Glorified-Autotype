"""
Rule-Based generator.
---
This generates the text which will be inputted to train the model.
It makes a sentence with a:
Participant + Verb + Noun + Adjective
format.
"""

import random

def gen_input():
    participant = "I", "you", "he", "she", "they", "we", "it"
    verb = "like", "am", "are", "is", "eat", "see", "have", "want", "love", "hate", "play", "go", "make", "know", "need"
    noun = "cat", "dog", "human", "food", "pizza", "game", "book", "car", "house", "school", "friend", "computer", "bird", "fish", "tree"
    adjective = "good", "bad", "big", "small", "nice", "cute", "funny", "happy", "sad", "fast", "slow", "red", "blue", "green", "cool"

    participant_chosen = random.choice(participant)
    verb_chosen = random.choice(verb)
    noun_chosen = random.choice(noun)
    adjective_chosen = random.choice(adjective)

    if participant_chosen in ["he", "she", "it"] and verb_chosen == "have":
        verb_chosen = "has"
    elif participant_chosen in ["he", "she", "it"] and verb_chosen == "go":
        verb_chosen = "goes"
    elif participant_chosen in ["he", "she", "it"] and verb_chosen not in ["are", "is"]:
        verb_chosen = verb_chosen + "s"

    if participant_chosen in ["they", "we"] and verb_chosen in ["is"]:
        verb_chosen = "are"
    if verb_chosen in ["are"] and verb_chosen in ["are"]:
        verb_chosen = random.choice(("like", "am", "is", "eat", "see", "have", "want", "love", "hate", "play", "go", "make", "know", "need"))
    if verb_chosen in ["is", "are"]:
        verb_chosen = verb_chosen + " a"
    return {"input": (participant_chosen, verb_chosen, adjective_chosen, noun_chosen),"expected": noun_chosen}


