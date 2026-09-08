"""
model_gen
---

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
total_transitions = 0
for words in open(train_file, encoding="utf-8"):
    words = words.split()
    for i in range(len(words) - 2):
        current = words[i].lower()
        next_word = words[i + 1].lower()
        next_next_word = words[i + 2].lower()
        couple = (current, next_word) # Wow it's a couple.
        word_list.setdefault(couple, []).append(next_next_word)
        total_transitions += 1

file = open("model.txt", "w", encoding="utf-8")
file.write(str(word_list))
end = time.time()
elapsed = end - start
print("Training complete!")
print("--*Training info*--")
print(f"{len(word_list)} pairs in total.")
print(f"{total_transitions} transitions.")
print(f"{total_transitions / len(word_list)} avg transitions per pair.")
print("-------------------")
print("\n--*Time info*--")
print(f"{elapsed / total_transitions:.6f} seconds per transition.")
print(f"{elapsed} seconds to train.")
print("---------------")
print("\n--*File info*--")
print(f"Size: {os.path.getsize("model.txt")/ 1024:.2f} KB")
print("---------------")