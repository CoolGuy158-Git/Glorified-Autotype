"""
train
---
This is where the training happens,
well not really "training" but close.

Basically, it gets EVERY pair of words in the training data,
and looks at what word follows each pair,
then every word that usually follows it gets listed.
here's a visualization.

say this is your training data:
"
cats are cute
cats are amazing
cats are lazy
dogs are big
dogs are strong
dogs are puppies
"
this algorithm basically turns that into a dict that looks like:
{
("cats", "are"): ["cute", "amazing", "lazy"],
("dogs", "are"): ["big", "strong", "puppies"]
}
"""

import time
import os

train_file = input("Enter training data file path: ")
if train_file == "":
    train_file = "training_data.txt"
start = time.time()
word_list = {}
for words in open(train_file, encoding="utf-8"):
    words = words.split()
    for i in range(len(words) - 2):
        current = words[i].lower()
        next_word = words[i + 1].lower()
        next_next_word = words[i + 2].lower()
        couple = (current, next_word) # Wow it's a couple.
        word_list.setdefault(couple, []).append(next_next_word)

file = open("model.txt", "w", encoding="utf-8")
file.write(str(word_list))
end = time.time()
elapsed = end - start
print("Training complete!")
print(f"{len(word_list)} pairs in total.")
print(f"Time: {elapsed} seconds.")
print(f"Size: {os.path.getsize("model.txt")/ 1024:.2f} KB")