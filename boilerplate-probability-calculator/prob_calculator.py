import copy
import random


# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for k, v in kwargs.items():
            for _ in range(v):
                self.contents.append(k)

    def draw(self, balls):
        if balls > len(self.contents):
            return self.contents

        draw_action = random.sample(self.contents, k=balls)
        for draw_ball in draw_action:
            self.contents.remove(draw_ball)

        return draw_action


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    nr_exp_balls = []
    for k in expected_balls:
        nr_exp_balls.append(expected_balls[k])

    successes = 0
    for i in range(num_experiments):
        n_hat = copy.deepcopy(hat)
        balls = n_hat.draw(num_balls_drawn)
        nr_balls = []

        for k in expected_balls:
            nr_balls.append(balls.count(k))

        if nr_balls >= nr_exp_balls:
            successes += 1

    return successes / num_experiments
