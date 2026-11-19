# Week 02 Lab

Instrument a provided training script (`train.py`) with MLflow experiment tracking; log params, metrics, and artifacts across a few runs, then compare them in the MLflow UI.

Starter files for this week's lab are pulled into your repo via `git fetch upstream && git merge upstream/main`, as introduced in the Week 1 lab.

## Part 6 - Reflection 
1. Which run performed best, and by roughly how much better than your baseline? 
The third run (`n_estimators=200`, `max_depth=None`) performed the best, achieving an accuracy of ~0.9694 (~96.9%). This is roughly a ~13.9% absolute improvement over the baseline run (`n_estimators=10`, `max_depth=3`), which scored ~0.8306 (~83.1%).

2. Why do you think that hyperparameter combination won? 
Increasing `n_estimators` to 200 allowed the ensemble to average predictions across significantly more decision trees, reducing model variance. Setting `max_depth=None` allowed individual trees to grow fully until all leaves were pure, capturing complex non-linear patterns within the handwritten digits dataset that shallower trees (`max_depth=3`) missed.

3. From the lecture's "four legs of reproducibility" (code, data, environment, config): which leg does today's MLflow setup now cover that Part2's bare script didn't? 
Today's MLflow setup covers the "config" leg of reproducibility. Rather than printing hyperparameters and metrics to an ephemeral terminal session where they are lost upon execution, MLflow systematically tracks, versions, and logs the specific model configuration parameters (`n_estimators`, `max_depth`, `random_state`) alongside their corresponding performance metrics and output artifacts.