# Glorified Autotype

---

## What?

It is a simple first-order Markov language model.

say you have a dict(the model):
```txt
{
"cats" ["are", "amazing", "lazy"]
"dogs" ["are", "big", "strong"]
"are" ["cute", "big"]
}
```
and you have this user input:
```txt
"I like cats"
```

it takes the word last word it can recognize, in this case its "cats".
It then picks a random word from the list.
let's say it picked "are"
it then picks another word from the list of the key "are"
say it landed on "cute"
the LM then spits out the completed sentence
"are cute"
but since I remove the first word from the final response to make it less like an autotype it turns to
"cute"

```txt
input: "I like cats"
output: "cute"
```

"In probability theory, a Markov model is a stochastic model used to model pseudo-randomly changing systems. It is assumed that future states depend only on the current state, not on the events that occurred before it (that is, it assumes the Markov property). Generally, this assumption enables reasoning and computation with the model that would otherwise be intractable. For this reason, in the fields of predictive modelling and probabilistic forecasting, it is desirable for a given model to exhibit the Markov property."
[source](https://en.wikipedia.org/wiki/Markov_model)

---

## Why?

Basically I saw this [video](https://www.youtube.com/watch?v=xUh5t4Ib6UU), and while what I did was not as cool as what the guy did,
I basically heard him talking bout how his og model only took what possible next word will appear and build a response out of that.
I went searching a little and found that it was something called 'Markov LM', and I got interested and abandoned my homework to work on this!

---

## Notes

The training_data.txt is just a sample training data, I recommend at least a 600 line, conversational, or essay like training data for this to work well.
Before trying to run main.py, run train.py first to generate the model, only then can main.py work.
