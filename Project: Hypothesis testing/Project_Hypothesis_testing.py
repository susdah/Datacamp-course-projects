# Import all the libraries:
import pandas as pd
import matplotlib.pyplot as plt
import pingouin as pingu
import numpy as np

# 1. Import the files into two databases and parse it on dates:
women_df = pd.read_csv("women_results.csv", parse_dates =['date'])
men_df = pd.read_csv("men_results.csv", parse_dates =['date'])

# 2. Exclude everything that is dated before 2002-01-01 and the wrong tournament:
women_df = women_df.loc[ (women_df['date'] >= '2002-01-01') &
                        (women_df['tournament'] == "FIFA World Cup")]
men_df = men_df.loc[ (men_df['date'] >= '2002-01-01') &
                        (men_df['tournament'] == "FIFA World Cup")]

# 3. Check that both are normally distributed: They are not. They are both left skewed.
women_df['total_score'] = women_df['home_score'] + women_df['away_score']
men_df['total_score'] = men_df['home_score'] + men_df['away_score']
plt.hist(women_df['total_score'], bins=25)
plt.hist(men_df['total_score'], bins=25)
plt.show()

# 4. Use a Wilcoxon-Mann-Whitney test as neither distribution is normal (both left-skewed).
alpha = 0.1
MWU = pingu.mwu(x = women_df['total_score'],
         y = men_df['total_score'],
         alternative = 'greater')
p_val = MWU['p-val'].values[0]

# 5. Interpret the results
result = "reject" if p_val < 0.1 else "fail to reject"
result_dict = {"p_val": p_val, "result": result}
print(result_dict)
