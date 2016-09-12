"""
Problem:

A Markov Chain (MC) can be thought of as a graph.  I.e., it's a data structure with vertices and edges between the vertices.  The edges are directed.  There may be an edge from vertex A to vertex B, but not back.  A MC has probabilities associated with each edge.  For a given vertex, the probabilities on all its outgoing edges sum to 1.
An application of a MC is a probabilistic state machine.  Each vertex represents a state.  The transition from one state to another is based on the roll of a dice (metaphorically), and the probabilities on the outgoing edges.  I.e., one edge is randomly chosen, such that edges with higher probabilities are proportionally more likely.
We're going to implement a toy application based on Markov Chains.  The idea of the application is to read in English sentences, and then output probabilistically English-like sentences.  The way this works will be to build a Markov Chain from the input.  Each unique word in the input will be represented by a vertex.  There will be an edge from word A to word B, if word A directly precedes word B somewhere in the input.  The probability associated with that edge will be the count of times word A directly precedes word B divided by the total number of occurrences of word A.  In order to simplify the problem, don't worry about punctuation, case, or multiple sentences.  I.e., treat the input simply as a stream of words.
Here's an example of input, and what the Markov Chain would look like:

Input:
    "it was the best of times it was the worst of times"
Markov chain (edge probabilities in parenthesis):
    it -> was (1)
    was -> the (1)
    the -> best (.5)
        -> worst (.5)
    best -> of (1)
    worst -> of (1)
    of -> times (1)

Assume the input is already parsed into words, and you are given one word at a time in the order each appears in the input.  Use this to build up the internal Markov Chain with the add_word method.  Once this is done, the next_word method can be used to query the chain.  The vertex for the word given is looked up, a dice is thrown, and an edge is chosen at random, but based on the probability distribution.  The word that the chosen edge leads to is returned.
    
"""

from random import randint

class Markov:
    # Tree is a map from words to a list of words  
    def __init__(self):
        self.tree = dict()
        self.previous_word = ""
    
    def add_word(self, word):
        """Add a word to the tree representation."""
        if self.previous_word == "":
            self.previous_word = word
        else:
            existing_words = []
            if self.previous_word in self.tree:
                existing_words = self.tree[self.previous_word]
            self.tree[self.previous_word] = existing_words + [word]
            self.previous_word = word
            
    def next_word(self, word):
        """Print out the next word in the tree."""
        i = len(self.tree[word])
        j = randint(0, i - 1)
        return self.tree[word][j]

mc = Markov()

# Gather input, build internal data structure
mc.add_word("it")
mc.add_word("was")
mc.add_word("the")
mc.add_word("best")
mc.add_word("of")
mc.add_word("times")
mc.add_word("it")
mc.add_word("was")
mc.add_word("the")
mc.add_word("worst")
mc.add_word("of")
mc.add_word("times")

# Query

# Should print "was"
print mc.next_word("it")  

# Should print "best" half the time and "worst" the other half
print mc.next_word("the") 
