# NBA Trends Analysis

In this project, you’ll analyze data from the NBA (National Basketball Association) and explore possible associations. This analysis focuses on understanding team performance, win probabilities, and the relationship between game location and game outcomes.

## Project Overview

This project utilizes data originally sourced from 538’s Analysis of the Complete History Of The NBA. The data includes the original, unmodified data from Basketball Reference as well as several additional variables added by 538 for their own analysis. For this project, the data has been limited to just 5 teams and 10 columns (plus one constructed column, `point_diff`, which is the difference between `pts` and `opp_pts`).

## Data Description

The dataset contains the following columns:
- `game_id`: Unique identifier for each game
- `fran_id`: Franchise name
- `pts`: Points scored by the team
- `opp_pts`: Points scored by the opponent team
- `forecast`: 538’s projected win probability for the team
- `game_location`: Location of the game ('H' for home, 'A' for away)
- `game_result`: Result of the game ('W' for win, 'L' for loss)
- `year_id`: Year of the game
- `month_id`: Month of the game
- `day_id`: Day of the game
- `point_diff`: Difference between `pts` and `opp_pts`

## Analysis Steps

1. **Subset Data by Season**: Filter the dataset to focus on the 2010 and 2014 seasons.
2. **Compare Team Performance**: Compare the performance of the Knicks and Nets in both the 2010 and 2014 seasons by analyzing their points scored per game.
3. **Visualize Data Distributions**: Create histograms and boxplots to visualize the distribution of points scored by different teams.
4. **Analyze Game Location and Outcome**: Investigate the relationship between game location and game result using contingency tables and Chi-Square tests.
5. **Correlation Analysis**: Explore the correlation between forecasted win probabilities and actual point differentials.

