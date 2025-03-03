######################################################
# AB Testing (Independent Two-Sample T-Test)
######################################################

# Load the dataset
df = sns.load_dataset("tips")
df.head()

# Group the dataset by smoker status and calculate the mean of total bill for each group
df.groupby("smoker").agg({"total_bill": "mean"})

############################
# 1. Form the Hypotheses
############################

# H0: M1 = M2
# H1: M1 != M2

############################
# 2. Assumption Check
############################

# Normality Assumption
# Homogeneity of Variance

############################
# Normality Assumption
############################

# H0: The normality assumption is satisfied.
# H1: The normality assumption is not satisfied.

# Perform the Shapiro-Wilk test for normality for smokers
test_stat, pvalue = shapiro(df.loc[df["smoker"] == "Yes", "total_bill"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

# If p-value < 0.05, reject H0.
# If p-value >= 0.05, fail to reject H0.

# Perform the Shapiro-Wilk test for normality for non-smokers
test_stat, pvalue = shapiro(df.loc[df["smoker"] == "No", "total_bill"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

############################
# Homogeneity of Variance Assumption
############################

# H0: The variances are homogeneous.
# H1: The variances are not homogeneous.

# Perform the Levene's test for homogeneity of variance
test_stat, pvalue = levene(df.loc[df["smoker"] == "Yes", "total_bill"],
                           df.loc[df["smoker"] == "No", "total_bill"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

# If p-value < 0.05, reject H0.
# If p-value >= 0.05, fail to reject H0.


############################
# Application of Hypotheses 3 and 4
############################

# 1. If assumptions are met, perform the independent two-sample t-test (parametric test)
# 2. If assumptions are not met, perform the Mann-Whitney U test (non-parametric test)


############################
# 1.1 If Assumptions are Met, Perform the Independent Two-Sample T-Test (Parametric Test)
############################

# Perform the independent two-sample t-test assuming equal variances
test_stat, pvalue = ttest_ind(df.loc[df["smoker"] == "Yes", "total_bill"],
                              df.loc[df["smoker"] == "No", "total_bill"],
                              equal_var=True)

print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

# If p-value < 0.05, reject H0.
# If p-value >= 0.05, fail to reject H0.


############################
# 1.2 If Assumptions are Not Met, Perform the Mann-Whitney U Test (Non-Parametric Test)
############################

# Perform the Mann-Whitney U test
test_stat, pvalue = mannwhitneyu(df.loc[df["smoker"] == "Yes", "total_bill"],
                                 df.loc[df["smoker"] == "No", "total_bill"])

print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))





############################
# Application 2: Is There a Statistically Significant Difference Between the Average Ages of Female and Male Passengers on the Titanic?
############################

# Load the Titanic dataset
df = sns.load_dataset("titanic")
df.head()

# Group the dataset by sex and calculate the mean age for each group
df.groupby("sex").agg({"age": "mean"})


# 1. Form the Hypotheses:
# H0: M1 = M2 (There is no statistically significant difference between the average ages of female and male passengers)
# H1: M1 != M2 (There is a statistically significant difference between the average ages)


# 2. Check Assumptions

# Normality assumption
# H0: The normality assumption is satisfied.
# H1: The normality assumption is not satisfied.

# Perform the Shapiro-Wilk test for normality for female passengers
test_stat, pvalue = shapiro(df.loc[df["sex"] == "female", "age"].dropna())
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

# Perform the Shapiro-Wilk test for normality for male passengers
test_stat, pvalue = shapiro(df.loc[df["sex"] == "male", "age"].dropna())
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

# Homogeneity of variance assumption
# H0: The variances are homogeneous.
# H1: The variances are not homogeneous.

# Perform the Levene's test for homogeneity of variance between female and male passengers
test_stat, pvalue = levene(df.loc[df["sex"] == "female", "age"].dropna(),
                           df.loc[df["sex"] == "male", "age"].dropna())

print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

# Since assumptions are not met, perform the non-parametric test

# Perform the Mann-Whitney U test
test_stat, pvalue = mannwhitneyu(df.loc[df["sex"] == "female", "age"].dropna(),
                                 df.loc[df["sex"] == "male", "age"].dropna())

print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

# 90 280




############################
# Application 3: Is There a Statistically Significant Difference Between the Average Ages of Diabetic and Non-Diabetic Patients?
############################

# Load the diabetes dataset
df = pd.read_csv("datasets/diabetes.csv")
df.head()

# Group the dataset by outcome and calculate the mean age for each group
df.groupby("Outcome").agg({"Age": "mean"})

# 1. Form the Hypotheses:
# H0: M1 = M2
# There is no statistically significant difference between the average ages of diabetic and non-diabetic patients
# H1: M1 != M2
# There is a statistically significant difference between the average ages


# 2. Check Assumptions

# Normality assumption (H0: The normality assumption is satisfied)
# Perform the Shapiro-Wilk test for normality for diabetic patients (Outcome = 1)
test_stat, pvalue = shapiro(df.loc[df["Outcome"] == 1, "Age"].dropna())
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

# Perform the Shapiro-Wilk test for normality for non-diabetic patients (Outcome = 0)
test_stat, pvalue = shapiro(df.loc[df["Outcome"] == 0, "Age"].dropna())
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

# Since the normality assumption is not met, perform the non-parametric test.

# Hypothesis (H0: M1 = M2)
# Perform the Mann-Whitney U test
test_stat, pvalue = mannwhitneyu(df.loc[df["Outcome"] == 1, "Age"].dropna(),
                                 df.loc[df["Outcome"] == 0, "Age"].dropna())
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))



###################################################
# Business Problem: Is There a Difference in Scores Between Those Who Watched Most of the Course and Those Who Did Not?
###################################################

# H0: M1 = M2 (... there is no statistically significant difference between the means of the two groups)
# H1: M1 != M2 (... there is a statistically significant difference)

# Load the dataset
df = pd.read_csv("datasets/course_reviews.csv")
df.head()

# Calculate the mean rating for those who watched more than 75% of the course
df[(df["Progress"] > 75)]["Rating"].mean()

# Calculate the mean rating for those who watched less than 25% of the course
df[(df["Progress"] < 25)]["Rating"].mean()

# Perform the Shapiro-Wilk test for normality for the group who watched more than 75% of the course
test_stat, pvalue = shapiro(df[(df["Progress"] > 75)]["Rating"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

# Perform the Shapiro-Wilk test for normality for the group who watched less than 25% of the course
test_stat, pvalue = shapiro(df[(df["Progress"] < 25)]["Rating"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

# Since the normality assumption is not met, perform the Mann-Whitney U test
test_stat, pvalue = mannwhitneyu(df[(df["Progress"] > 75)]["Rating"],
                                 df[(df["Progress"] < 25)]["Rating"])

print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))


######################################################
# AB Testing (Two-Sample Proportion Test)
######################################################

# H0: p1 = p2
# There is no statistically significant difference between the conversion rate of the new design and the old design.
# H1: p1 != p2
# There is a statistically significant difference.

# Success counts for both designs
basari_sayisi = np.array([300, 250])
# Observation counts for both designs
gozlem_sayilari = np.array([1000, 1100])

# Perform the two-sample z-test for proportions
proportions_ztest(count=basari_sayisi, nobs=gozlem_sayilari)

# Calculate the conversion rates for both designs
basari_sayisi / gozlem_sayilari



############################
# Application: Is There a Statistically Significant Difference in Survival Rates Between Women and Men?
############################

# H0: p1 = p2
# There is no statistically significant difference between the survival rates of women and men.

# H1: p1 != p2
# There is a statistically significant difference.

# Load the Titanic dataset
df = sns.load_dataset("titanic")
df.head()

# Calculate the survival rate for female passengers
df.loc[df["sex"] == "female", "survived"].mean()

# Calculate the survival rate for male passengers
df.loc[df["sex"] == "male", "survived"].mean()

# Calculate the success counts for female and male passengers
female_succ_count = df.loc[df["sex"] == "female", "survived"].sum()
male_succ_count = df.loc[df["sex"] == "male", "survived"].sum()

# Perform the two-sample z-test for proportions
test_stat, pvalue = proportions_ztest(count=[female_succ_count, male_succ_count],
                                      nobs=[df.loc[df["sex"] == "female", "survived"].shape[0],
                                            df.loc[df["sex"] == "male", "survived"].shape[0]])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

