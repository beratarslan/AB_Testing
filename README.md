# AB Testing and Hypothesis Testing Examples

This repository contains examples of hypothesis testing and A/B testing in Python using various datasets. The main objective is to demonstrate different statistical tests for analyzing data and understanding whether there are statistically significant differences between groups.

## 1. **Independent Two-Sample T-Test (AB Testing)**

### Problem:
The goal is to check if there is a statistically significant difference between the total bill amounts for smokers and non-smokers in a restaurant dataset (`tips`).

- **Hypotheses**:
  - **H0**: There is no significant difference between the total bills of smokers and non-smokers.
  - **H1**: There is a statistically significant difference between the total bills of smokers and non-smokers.

### Steps:
1. **Form the Hypotheses**:
   - H0: M1 = M2
   - H1: M1 != M2
2. **Assumption Check**:
   - Normality Assumption: Shapiro-Wilk test
   - Homogeneity of Variance: Levene's test
3. **Test**:
   - If assumptions are met, perform an independent two-sample t-test.
   - If assumptions are not met, perform the Mann-Whitney U test.

## 2. **Survival Rates Analysis (Titanic Dataset)**

### Problem:
This analysis investigates if there is a significant difference in the survival rates between female and male passengers on the Titanic.

- **Hypotheses**:
  - **H0**: There is no significant difference between the survival rates of female and male passengers.
  - **H1**: There is a statistically significant difference between the survival rates of female and male passengers.

### Steps:
1. **Form the Hypotheses**:
   - H0: p1 = p2
   - H1: p1 != p2
2. **Assumption Check**:
   - Normality Assumption: Shapiro-Wilk test
   - Homogeneity of Variance: Levene's test
3. **Test**:
   - If assumptions are met, perform a two-sample z-test for proportions.
   - If assumptions are not met, use the Mann-Whitney U test.

## 3. **Diabetic vs Non-Diabetic Patients Age Analysis**

### Problem:
This analysis investigates if there is a significant difference between the average ages of diabetic and non-diabetic patients.

- **Hypotheses**:
  - **H0**: There is no statistically significant difference between the average ages of diabetic and non-diabetic patients.
  - **H1**: There is a statistically significant difference between the average ages of diabetic and non-diabetic patients.

### Steps:
1. **Form the Hypotheses**:
   - H0: M1 = M2
   - H1: M1 != M2
2. **Assumption Check**:
   - Normality Assumption: Shapiro-Wilk test
3. **Test**:
   - If normality assumptions are not met, use the Mann-Whitney U test.

## 4. **Course Ratings Analysis (Business Problem)**

### Problem:
This analysis investigates if there is a significant difference between the ratings of those who watched the majority of a course and those who watched very little.

- **Hypotheses**:
  - **H0**: There is no statistically significant difference in ratings between those who watched more than 75% of the course and those who watched less than 25%.
  - **H1**: There is a statistically significant difference.

### Steps:
1. **Form the Hypotheses**:
   - H0: M1 = M2
   - H1: M1 != M2
2. **Assumption Check**:
   - Normality Assumption: Shapiro-Wilk test
3. **Test**:
   - Since normality assumptions are not met, perform the Mann-Whitney U test.

## 5. **AB Testing (Proportion Test)**

### Problem:
In this example, we compare the conversion rates of two designs to check if there is a statistically significant difference in their success rates.

- **Hypotheses**:
  - **H0**: There is no statistically significant difference between the conversion rates of the two designs.
  - **H1**: There is a statistically significant difference between the conversion rates of the two designs.

### Steps:
1. **Form the Hypotheses**:
   - H0: p1 = p2
   - H1: p1 != p2
2. **Test**:
   - Use a two-sample z-test for proportions.

## Datasets:

1. **Titanic Dataset**: `sns.load_dataset("titanic")` (Used for analyzing survival rates between female and male passengers).
2. **Diabetes Dataset**: `pd.read_csv("datasets/diabetes.csv")` (Used for analyzing the age difference between diabetic and non-diabetic patients).
3. **Course Reviews Dataset**: `pd.read_csv("datasets/course_reviews.csv")` (Used for analyzing course ratings based on progress).
4. **Tips Dataset**: `sns.load_dataset("tips")` (Used for analyzing total bills between smokers and non-smokers).

---

### Requirements:
- Python 3.x
- Pandas
- NumPy
- SciPy
- Seaborn (for datasets)

