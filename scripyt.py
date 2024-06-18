import numpy as np
import pandas as pd
from scipy.stats import pearsonr, chi2_contingency
import matplotlib.pyplot as plt
import seaborn as sns

np.set_printoptions(suppress=True, precision=2)

# Load the NBA games dataset
nba = pd.read_csv('./nba_games.csv')

# Subset Data to 2010 Season, 2014 Season
nba_2010 = nba[nba.year_id == 2010]
nba_2014 = nba[nba.year_id == 2014]

# Print the first few rows of the 2010 and 2014 data
print(nba_2010.head())
print(nba_2014.head())

# Subset the points scored by Knicks and Nets in the 2010 season
knicks_pts_10 = nba_2010.pts[nba.fran_id == 'Knicks']
nets_pts_10 = nba_2010.pts[nba.fran_id == 'Nets']

# Print points scored by Knicks and Nets in 2010
print(knicks_pts_10)
print(nets_pts_10)

# Calculate the mean points scored by Knicks and Nets in 2010
knicks_mean_score = np.mean(knicks_pts_10)
nets_mean_score = np.mean(nets_pts_10)
diff_means = knicks_mean_score - nets_mean_score
print(diff_means)

# Plot overlapping histograms of points scored by Knicks and Nets in 2010
plt.hist(knicks_pts_10, alpha=0.8, density=True, label='knicks')
plt.hist(nets_pts_10, alpha=0.8, density=True, label='nets')
plt.legend()
plt.title("2010 Season")
plt.show()
plt.close()

# Subset the points scored by Knicks and Nets in the 2014 season
knicks_pts_14 = nba_2014.pts[nba.fran_id == 'Knicks']
nets_pts_14 = nba_2014.pts[nba.fran_id == 'Nets']

# Print points scored by Knicks and Nets in 2014
print(knicks_pts_14)
print(nets_pts_14)

# Calculate the mean points scored by Knicks and Nets in 2014
knicks_mean_score = np.mean(knicks_pts_14)
nets_mean_score = np.mean(nets_pts_14)
diff_means = knicks_mean_score - nets_mean_score
print(diff_means)

# Plot overlapping histograms of points scored by Knicks and Nets in 2014
plt.hist(knicks_pts_14, alpha=0.8, density=True, label='knicks')
plt.hist(nets_pts_14, alpha=0.8, density=True, label='nets')
plt.legend()
plt.title("2014 Season")
plt.show()
plt.close()

# Generate side-by-side boxplots for points scored per game by franchise in 2010
plt.clf()  # Clear the previous plot
sns.boxplot(data=nba_2010, x='fran_id', y='pts')
plt.title('Points Scored per Game by Franchise in 2010')
plt.show()

# Calculate a table of frequencies that shows the counts of game_result and game_location
location_result_freq = pd.crosstab(nba.game_result, nba.game_location)
print(location_result_freq)

# Convert the table of frequencies to a table of proportions
location_result_proportions = location_result_freq / len(nba)
print(location_result_proportions)

# Calculate the expected contingency table and the Chi-Square statistic
chi2, pval, dof, expected = chi2_contingency(location_result_freq)
print(expected)
print(chi2)

# Calculate the covariance between forecast and point_diff in 2010
point_diff_forecast_cov = np.cov(nba_2010.forecast, nba_2010.point_diff)
print(point_diff_forecast_cov)

# Calculate the correlation between forecast and point_diff in 2010
point_diff_forecast_corr = pearsonr(nba_2010.forecast, nba_2010.point_diff)
print(point_diff_forecast_corr)

# Generate a scatter plot of forecast and point_diff in 2010
plt.clf()  # Clear the previous plot
plt.scatter(nba_2010.forecast, nba_2010.point_diff)
plt.xlabel('Forecasted Win Prob.')
plt.ylabel('Point Differential')
plt.show()
