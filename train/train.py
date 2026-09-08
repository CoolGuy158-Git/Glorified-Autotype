"""
Train
---
Thought about adding reinforcement learning.
Asked myself, 'How could you possibly implement reinforcement learning to a markov?'
This is the best I could think of.
Uncomment the print's if you want logs.
I commented them before commiting cuz they made the program WAYYY slower.
Future improvements (Perhaps contribute?):
    More training rules.
    OPTIMIZE THIS IS SO SLOW.
    Perhaps a better rule_gen.py
"""

from rule_gen import gen_input
from model import gen_response
import ast

epoch = input("How many epoch: ")
iterations_num = 0
epoch_num = 0
score = 0
with open("../model.txt", "r", encoding="utf-8") as model:
    model_list = ast.literal_eval(model.read())
reasons = []

"""
Reward and punish system
---
In the reward and punish system, I add or remove the first words.
Those basically acts as weights.
You see the model itself looks like
('you', 'get'): ['back', 'it', 'it', 'here']

Meaning the chances of 'it' being the next word is 50, the other two words are 25/25.
So say you dont want the markov to generate 'it' and to generate more 'here'
So you just remove on 'it' and add a 'here' so now theres a 50% chance 'here is gonna get generated.
So why the first words? Because the first words determine the next word which determine the next next word, and thus the entire response.
"""
def reward(amount):
    first_word = response.split()[0]
    if first_word in model_list[pair]:
        for i in range(amount):
            model_list[pair].append(first_word)
def punish(amount):
    first_word = response.split()[0]
    for i in range(amount):
        if first_word in model_list[pair]:
            model_list[pair].remove(first_word)
        else: # If no more of the first word is found don't remove all keep at least 1 instance of it.
            model_list[pair].append(first_word)
            break


for i in range(int(epoch) * 10):
    # your existing critic/reward/punishment code
    # print("\n*-----------------------------------------------------*\n")
    data = gen_input()
    result = gen_response(" ".join(data["input"]))
    iterations_num += 1
    # print(f"Iteration: {iterations_num}")
    # print(f"Input: {' '.join(data['input'])}")
    # print(f"Expected: {data['expected']}")

    response = result[0]
    pair = result[1]
    # print(f"Response: {response}")
    """
    This is the actual training part.
    It starts by seeing if expected word is in the response,
    if so that means it is somewhat context aware so plus 5 else minus 5.
    Then if word len is less than 3 punish by removing the end word (keeping atleast 1 copy of it though).
    If word len is over 10 reward 3.
    """
    if response == "NULL: No pair found":
        pass # I thought about adding a response so that yk the model's list can be expanded and thus say more things but yea it's too hard tbh.
    else:
        if data["expected"] in response.split():
            score += 5
            model_list[pair].append(data["expected"])
            reward(5)
            reasons.append("+5: Expected word is found")
            # print("Plus 5: Expected word is found")
        else:
            score -= 5
            punish(5)
            for f in range(3): # Give the thing a weight of 3
                model_list[pair].append(data["expected"])
            # print("Minus 5: Expected word is not found")
            reasons.append("-5: Expected word is not found")

        if len(response.split()) < 3:
            score -= 2
            end_word = response.split()[-1]
            if end_word in model_list[pair]:
                for f in range(2):
                    if end_word in model_list[pair]:
                        model_list[pair].remove(end_word)
                    else:
                        model_list[pair].remove(end_word)
            model_list[pair].append(data["expected"])
            # print("Minus 2: Word len is less than 3")
            reasons.append("-2: Word len is less than 3")
        if len(response.split()) > 10:
            score += 3
            model_list[pair].append(data["expected"])
            reward(3)
            # print("Plus 3: Word len is more than 10")
            reasons.append("+3: Word len is more than 10")
    if iterations_num == 10:
        with open("../model.txt", "w", encoding="utf-8") as model:
            model.write(repr(model_list)) # Update model list every run to show changes and yk save every changes
        iterations_num = 0
        epoch_num += 1
        print("\n_______________________________")
        print(f"Epoch {epoch_num}/{epoch}")
        print("\n".join(reasons))
        print(f"Total score: {score}")
        print("_______________________________")
        score = 0
        reasons = []
    # print("\n*-----------------------------------------------------*\n")
