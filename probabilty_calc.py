import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for color, count in kwargs.items():
            self.contents.extend([color] * count)

    def draw(self, num_balls):
        if num_balls >= len(self.contents):
            return self.contents
        drawn_balls = random.sample(self.contents, num_balls)
        for ball in drawn_balls:
            self.contents.remove(ball)
        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successful_draws = 0

    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)
        drawn_counts = {color: drawn_balls.count(color) for color in set(drawn_balls)}

        success = True
        for color, count in expected_balls.items():
            if color not in drawn_counts or drawn_counts[color] < count:
                success = False
                break

        if success:
            successful_draws += 1

    probability = successful_draws / num_experiments
    return probability
