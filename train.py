"""
train
---
This is where the training happens,
well not really "training" but close.

Basically, it gets EVERY word in the training data, and looks at what words follow it,
then every word that usually follow it lists.
here's a visualization.

say this is your training data:
"
cats are cute
cats amazing
cats lazy
dogs are big
dogs strong
dogs puppies
"
this algorithm basically turns that into a dict that looks like:
{
"cats" ["are", "amazing", "lazy"]
"dogs" ["are", "big", "strong"]
"are" ["cute", "big"]
}
"""

import string

train_file = input("Enter training data file path: ")
if train_file == "":
    train_file = "training_data.txt"
word_list = {}
for words in open(train_file):
    words = words.split()
    for i in range(len(words) - 1):
        current = words[i].lower().strip(string.punctuation)
        next_word = words[i + 1].lower().strip(string.punctuation)
        word_list.setdefault(current, []).append(next_word)
print(f"Final training data: \n{word_list}")
file = open("model.txt", "w")
file.write(str(word_list))