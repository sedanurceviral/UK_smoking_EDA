# Exploratory Data Analysis on Smoking Dataset

## Overview

This repository contains a script for performing an Exploratory Data Analysis (EDA) on a smoking dataset. The dataset provides information about various attributes related to smoking habits, income, education, and demographics. The script helps in understanding the dataset, cleaning it, and visualizing key insights.

## Libraries Used

- matplotlib: Used for creating static, animated, and interactive visualizations.
- pandas: Data manipulation and analysis library.
- seaborn: A Python visualization library based on matplotlib that provides a high-level interface for drawing attractive and informative statistical graphics.
- numpy: Library for numerical operations in Python.

## Steps in the Analysis

1. *Loading Data*  
   The dataset is loaded from a CSV file into a pandas DataFrame. Various data attributes are examined and cleaned for further analysis.

2. *Data Overview*  
   The function check_df() provides an initial overview of the dataset, displaying:
   - Number of unique values in each column.
   - The shape (dimensions) of the dataset.
   - Data types of the columns.
   - The first and last few rows of the dataset.
   - Missing values and duplicates.
   - Descriptive statistics and quantiles.

3. *Handling Categorical and Numerical Columns*  
   - *Categorical Columns*: These columns are identified and summarized using the cat_summary() function. The function prints the count of each category and their relative percentages, along with visualizations (count plots) if requested.
   - *Numerical Columns*: These columns are summarized using the num_summary() function. The function calculates descriptive statistics (e.g., mean, quantiles) and displays histograms for each numerical column if requested.

4. *Target Variable Analysis*  
   - The script analyzes the relationship between the target variable (e.g., smoking behavior) and other features. The function target_summary_with_cat() calculates the mean target value grouped by categorical columns, while target_summary_with_num() calculates the mean target value grouped by numerical columns.

## Features of the Analysis

- *Exploratory Data Analysis*: Provides a comprehensive analysis of the dataset, including summary statistics, distributions, and visualizations.
- *Categorical and Numerical Insights*: Identifies the categorical and numerical features in the dataset and provides summary statistics and visualizations.
- *Target Variable Analysis*: Investigates how the target variable correlates with other features in the dataset.

## Getting Started

To use the script, ensure that the necessary libraries are installed. You can install them using the following commands:

```bash
pip install matplotlib pandas seaborn numpy
