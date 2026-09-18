import numpy_experiment
import probability
import matplotlib.pyplot as plt
from fractions import Fraction

while True:
    try:
        target = int(input(f"What number are you looking for?:"))
        if target < 1 or target > 100:
            print("You need to enter a number between 1 and 100")
            continue
        how_many_trials = int(input(f"How many trials shall be conducted?"))
        if how_many_trials > 20 or how_many_trials < 1:
            print("Number of trials must be between 1 and 20.")
        else:
            break
    except ValueError:
        print("You need to enter a number.")

for trials in range(how_many_trials):
    while True:
        try: 
            maximum = int(input(f"What do you want the maximum amount of attempts to be?"))
            if maximum > 20000 or maximum < 1:
                print("The maximum must be between 1 and 20000")
            else:
                break
        except ValueError:
            print("You need to enter a number.")
    successful_attempts = numpy_experiment.generate_attempts(maximum, target)
    odds_plot_points, maximum_plot_points = probability.collect_graphing_data(maximum, successful_attempts)

for counter, numbers in enumerate(probability.trial, start=1):
    fraction = Fraction(numbers).limit_denominator()
    print(f"The experimental probability for trial {counter} is {fraction}.")


plt.xlabel("Maximum amount of Attempts")
plt.ylabel("Experimental Probability")
plt.title("Probability vs Number of Attempts")
plt.plot(probability.maximum_values, odds_plot_points, marker="o")
plt.show()
