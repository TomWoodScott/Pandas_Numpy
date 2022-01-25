"""
#### Tasks

Create a chart similar to `examples/Figure_1.png`, where we show the counts of good and bad outcomes for the
    `cholesterol`, `gluc`, `alco`, `active`, and `smoke` variables for patients with cardio=1 and cardio=0 in different
    panels.

Use the data to complete the following tasks in `medical_data_visualizer.py`:
* Add an `overweight` column to the data. To determine if a person is overweight, first calculate their BMI by dividing
    their weight in kilograms by the square of their height in meters. If that value is > 25 then the person is
    overweight. Use the value 0 for NOT overweight and the value 1 for overweight.
* Normalize the data by making 0 always good and 1 always bad. If the value of `cholesterol` or `gluc` is 1, make the
    value 0. If the value is more than 1, make the value 1.
* Convert the data into long format and create a chart that shows the value counts of the categorical features using
    seaborn's `catplot()`. The dataset should be split by 'Cardio' so there is one chart for each `cardio` value.
    The chart should look like `examples/Figure_1.png`.
* Clean the data. Filter out the following patient segments that represent incorrect data:
  - diastolic pressure is higher than systolic (Keep the correct data with `(df['ap_lo'] <= df['ap_hi'])`)
  - height is less than the 2.5th percentile (Keep the correct data with `(df['height'] >= df['height'].quantile(0.025))`)
  - height is more than the 97.5th percentile
  - weight is less than the 2.5th percentile
  - weight is more than the 97.5th percentile
* Create a correlation matrix using the dataset. Plot the correlation matrix using seaborn's `heatmap()`.
    Mask the upper triangle. The chart should look like `examples/Figure_2.png`.
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('../data1/medical_examination.csv')

# Add 'overweight' column, 0 = not overweight, 1 = overweight. if BMI > 25 then overweight
df['BMI'] = df['weight'] / (df['height']/100)**2
df['overweight'] = [1 if i > 25 else 0 for i in df.BMI]
df = df.drop(columns=['BMI'])
# In the above code it is maybe cleaner to just call the 'BMI' column 'overweight' and then write over it in the next
# step, however i want this to have more readable steps and more methods for practise


# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1,
# make the value 0. If the value is more than 1, make the value 1.


df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)
df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)


# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename
    df_cat = pd.melt(df, var_name = 'variable', value_vars = ['active','alco','cholesterol', 'gluc','overweight','smoke'], id_vars = 'cardio')


    # Draw the catplot with 'sns.catplot()' hue -> changes colour dependent on "value"
    fig = sns.catplot(data = df_cat, x="variable", col="cardio", kind="count", hue="value").set_axis_labels("variable", "total").fig


    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(corr)

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(16,9))

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, mask=mask, square=True, center=0, vmax=0.3, fmt="0.1f", linewidths=0.5, annot=True, cbar_kws = {'shrink':0.5})

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig


draw_cat_plot()
draw_heat_map()