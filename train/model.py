# Literally just a barebones copy of main.py
import string
from nltk.tag import RegexpTagger
import random
import ast

tagger = RegexpTagger([ # Imma try this lib, it's basically a bunch of defined rules on what a verb/noun might be
    (r".*(ing)$", "VBG"),
    (r".*ed$", "VBD"),
    (r".*ly$", "RB"),
    (r".*(tion|ment|ness)$", "NN"),
    (r"^(want|like|love|need|learn|play|make|get|have|know|think|see|watch|use|build|write|do|does|did)$", "VB"), # Other extra verbs, just in case the rules won't catch these
    (r".*", "NN")
])

def gen_response(input):
    with open("../model.txt", "r", encoding="utf-8") as model:
        model_list = ast.literal_eval(model.read())
    user_input = " ".join(input.strip(string.punctuation).split()[::-1])
    last_word = None

    original_words = input.split()
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
        return "NULL: No pair found", None
    starting_pair = last_word

    first = True
    final_output = []
    previous_pairs = []
    for i in range(50):
        while last_word not in model_list:
            last_word = random.choice(list(model_list.keys()))

        next_words = model_list[last_word].copy()
        scores = {word: next_words.count(word) for word in set(next_words)}

        for distance, pair in enumerate(reversed(previous_pairs[:-1]), 1):
            if pair in model_list:
                amount = 1 / (2 ** distance)

                for word in scores:
                    scores[word] += model_list[pair].count(word) * amount
        previous_pairs.append(last_word)
        current_word = random.choices(list(scores.keys()),weights=list(scores.values()))[0]
        if current_word.endswith((".", "!", "?")):
            final_output.append(current_word)
            break

        if not first:
            final_output.append(current_word)
            if len(final_output) % 10 == 0:
                final_output.append("\n")
        last_word = (last_word[1], current_word)
        first = False

    return " ".join(final_output), starting_pair