# Week 04 Lab

Build a reusable preprocessing pipeline (sklearn Pipeline/ColumnTransformer); PCA as a worked stateful-transform example.

Starter files for this week's lab will be added here before the lab session
(pulled into your repo via `git fetch upstream && git merge upstream/main`,
as introduced in the Week 1 lab).

Q.1 Why a similar accuracy doesn't mean the leak was harmles? 
A.1 Similar accuracy is a coincidence; leakage artificially contaminates training with test data, leading to over-optimistic validation and poor generalization on real unseen data.

Q.2 The exact cause of the leak and how it was proven.
A.2 Fitting the imputer and StandardScaler on the entire dataset before train_test_split. We proved it by showing numerical differences between leaky_scaler.mean_ and correct_scaler.mean_.

Q.3 Production recomputing and train-serving skew.
A.3 This describes train-serving skew. Leakage contaminates training data with test data, whereas dynamic production re-fitting uses a shifting baseline distribution that mismatches training.

Q.4 PCA state and the danger of fresh fiting in production.
A.4 PCA's "state" is its learned principal components. Running a fresh fit_transform() in production changes the feature projection space on every request, destroying model reliability.
