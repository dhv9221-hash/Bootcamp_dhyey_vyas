# Homework-1

# Currency Exchange Rate Forecasting


## Problem Statement

This project aims to predict the next-day exchange rate using historical data and engineered features like moving averages, volatility, and lag values.

## Users and Stakeholders

Stakeholders: Financial analysts, forex traders, import/export businesses

Users: Data scientists, risk managers, algorithmic traders

## Useful answers and Decesions

Predictive task: Forecast next-day exchange rate

Target: USD to EUR (can extend to other major pairs)

ML Output: Regression model predicting the exchange rate

Metric: MAE, RMSE, MAPE

Deliverables:

-> Clean dataset

-> Feature engineering script

-> Trained model & evaluation metrics

## Assumptions and Constraints

-> Historical exchange rate data is available via free APIs 

-> Daily frequency is acceptable; no high-frequency (minute-level) data required

-> API rate limits apply — we’ll cache or store results locally

-> Simple preprocessing is sufficient (fill missing days, calculate lags/rolling stats)

-> Model complexity is low 

-> No real-time execution or trading — this is a research/forecasting tool

## Known and Unknown Risks

-> Exchange rates are affected by unpredictable geopolitical/economic events

-> Models may overfit historical patterns not relevant in future

-> API data quality and completeness can vary 

## Lifecycle

Defining the problem --> Setting up the project architecture --> Data acquisition --> Data clenaing and pre processing --> Pattern recognition --> Application of model --> Visualization and analysis of the result --> conclusion