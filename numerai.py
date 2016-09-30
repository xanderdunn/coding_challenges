#!/usr/bin/env python3

# You're given five buckets each with 10 balls, and each ball has a number 1-10, and each bucket has balls of a different color.  Choose a ball randomly from a bucket.  Then choose a second ball randomly from a bucket.  What is the probability that the second ball will be both a different color and a different number from the first ball?

# Third party
import numpy as np

# TODO: Optimize
# TODO: Progress bar
# TODO: Remove mutable state
# TODO: Parallelize

class Box(object):
    def __init__(self, color):
        self.color = color
        self.balls = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

def get_ball_from_single_box(box):
    random_index_choice = np.random.choice(len(box.balls), 1)[0]
    number = box.balls[random_index_choice]
    box.balls = np.delete(box.balls, random_index_choice)
    return number


def get_ball_from_all_boxes(boxes):
    num_boxes = len(boxes)
    random_box = boxes[np.random.choice(num_boxes, 1)[0]]
    color = random_box.color
    number = get_ball_from_single_box(random_box)
    return color, number

def main():
    np.random.seed(1234)
    total = 10000000
    num_satisfied = 0 # Number of times the second chosen ball had a different color and a different number
    for _ in range(total):
        boxes = [Box("red"), Box("blue"), Box("green"), Box("yellow"), Box("black")]
        color1, number1 = get_ball_from_all_boxes(boxes)
        color2, number2 = get_ball_from_all_boxes(boxes)
        if color1 != color2 and number1 != number2:
            num_satisfied += 1
    final_probability = num_satisfied / total
    print("Found probability of {}%".format(final_probability * 100))

if __name__ == "__main__":
    main()
