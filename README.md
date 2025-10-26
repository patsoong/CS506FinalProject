# NBA Champions Prediction Project

##  Description
This project explores **predicting NBA champions** using historical team and player statistics. The primary goal is to build models that leverage past performance to predict outcomes such as:
- The **NBA Champion** for a given season.
- The **Eastern and Western Conference winners**.

Additionally, we aim to perform **feature engineering** to create new variables (e.g., roster depth, player efficiency distributions, strength of schedule, injury impact) and evaluate whether they improve prediction accuracy.

---

##  Goals
1. Predict the **NBA Champion** based on team and player data from previous seasons.
2. Predict **conference champions** (Eastern and Western).
3. Explore **engineered features** to identify hidden relationships that improve predictive power.
4. Analyze model performance and provide insights into which features best explain championship outcomes.

---

## Data Collection
- **Sources**:
  - [Basketball Reference](https://www.basketball-reference.com/) for season-level team and player stats.
  - [NBA Stats API](https://github.com/swar/nba_api) for more granular game-by-game data.
  - [NBA Dataset - Box Scores and Stats](https://www.kaggle.com/datasets/eoinamoore/historical-nba-data-and-player-box-scores?select=TeamStatistics.csv) holds the current dataset in use.
  - Kaggle datasets (e.g., “NBA Games Since 2004” and “NBA Team Stats”).

- **Data Needed**:
  - Team statistics (Offensive/Defensive rating, Net rating, pace, win percentage).
  - Player statistics (PER, Win Shares, Box Plus/Minus, VORP).
  - Playoff results (conference finals, finals).
  - Possible engineered features: average bench scoring, star player load, injury-adjusted win percentage.

---

##  Modeling Plan
We will experiment with multiple methods:
- **Logistic Regression / Linear Models** – for interpretability (predicting binary outcomes like champion vs. non-champion).
- **Random Forest / XGBoost** – for handling non-linear relationships and feature importance.
- **Clustering (k-means, PCA)** – to group similar championship-caliber teams across history.
- **Neural Networks** (optional if time permits) – to capture more complex patterns.

---

##  Visualization Plan
- **Feature Importance Charts** – highlight which metrics best predict champions.
- **Heatmaps** – correlation between engineered features and playoff success.
- **Conference Prediction Graphs** – probability of winning East/West by team.
- **Interactive Dashboards** (optional with Plotly/Altair) – exploring variables like star usage vs. team depth.

---

##  Test Plan
- **Train/Test Split**: Train on seasons before 2015, test on seasons from 2015–2023. OR Train on randomly selected 80% of the dataset and test on the remaining 20%. 
- **Cross-Validation**: Use k-fold cross-validation to ensure robustness.
- **Evaluation Metrics**: Accuracy for binary predictions, precision/recall for champion classification, log-loss for probability calibration.

---

##  Scope & Timeline
This project is designed for **two months of work**:
1. **Weeks 1–2**: Data collection & cleaning.
2. **Weeks 3–4**: Baseline models & exploratory data analysis.
3. **Weeks 5–6**: Feature engineering & advanced models (XGBoost, clustering).
4. **Weeks 7–8**: Visualization, testing, and final write-up.

---

##  Expected Outcomes
- A predictive model for NBA Champions & conference winners.
- Insights into which team and player characteristics most strongly drive championship success.
- A reproducible workflow (data pipeline, modeling, and visualization).
