# P-hacking is a topic that needs to be addressed

import random

def run_experiment():
    """flip a fair coin 1000 times, True = heads, False = tails"""
    return [random.random() < 0.5 for _ in range(1000)]

def reject_fairness(experiment):
    """using the 5%% significance levels"""
    num_heads = len([flip for flip in experiment if flip])
    return num_heads < 469 or num_heads > 531

random.seed(0)
experiments = [run_experiment() for _ in range(1000)]
num_rejections = len([experiment
                      for experiment in experiments
                      if reject_fairness(experiment)])

# print num_rejections  # 46

print '-' * 100
print """
A procedure that erroneously rejects the null hyothesis only 5%% of
the time will by definition - 5%% of the time erroneously reject the null hypothesis.

What this means is that if you're setting out to find \"significant\" results,
you usually can test enough hypothesis against your data ser, and one of them
will almost certainly appear significant. Remove the right outlier, and you could
probably get your p value below 0.05.

This is something called p-hacking and is in some ways a consequemce of the
\"inference from p-values framework\". We can show this with an experiment that
tests our hypothesis 1000 times and counts up the number of instances we would
reject the null hypothesis.

    def run_experiment():
        \"\"\"flip a fair coin 1000, times, True = heads, False = tails\"\"\"
        return [random.random() < 0.5 for _ in range(1000)]

    def reject_fairness(experiment):
        \"\"\"using the 5%% significance levels\"\"\"
        num_heads = len([flip for flip in experiment if flip])
        return num_heads < 469 or num_heads > 531

    random.seed(0)  # so we can get reproducable resutls
    experiments = [run_experiment() for _ in range(1000)]
    num_rejections = len([experiments
                          for experiment in experiments
                          if reject_fairness(experiment)])

    print num_rejections  # %s

Our results show that if we had run tested our two-sided hypothesis that the coin
was in fact not fair, we would have discovered %s instances when we could have
rejected the null hypothesis of a fair coin.

*** If you want to do good science, you should determine your hypothesis before
looking at your data, you should clean your data without the hypothesis in mind,
and you should keep in mind the p-values are not substitutes for common sense.

*** An alternative approach is Bayesian Inference
""" %(num_rejections, num_rejections)
print '-' * 100
