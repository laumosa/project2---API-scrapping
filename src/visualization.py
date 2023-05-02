import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt




def visualizing_csv_temperature (df_csv_temp):
    # Set plot style
    sns.set_style('whitegrid')

    # Create the plot with hue for each year
    ax = sns.barplot(data=df_csv_temp, x='Month', y='AvgTemperature', hue='Year', palette='coolwarm', linewidth=2.5, ci=None)

    # Add plot title and axis labels
    ax.set_title('Average Monthly Temperature in Madrid', fontsize=16)
    ax.set_xlabel('Month', fontsize=14)
    ax.set_ylabel('Average Temperature (C)', fontsize=14)

    # Add legend and adjust legend location
    ax.legend(title='Year', title_fontsize=10, fontsize=9, loc='upper left')

    # Set tick label font size and rotation
    ax.tick_params(labelsize=12, rotation=45)

    # Set the color for the March label
    ax.get_xticklabels()[2].set_color('red')

    plt.savefig("figures/graph_temperature.png")
    plt.show()

    # Open file
    os.system("start figures/graph_temperature.png")




def visualizing_csv_covid (df_csv_covid):
    # Set plot style
    sns.set_style('whitegrid')

    # Create the plot with hue for each year
    ax = sns.barplot(data=df_csv_covid, x='mes_nombre', y='num_casos', linewidth=2.5, ci=None, color=sns.color_palette('coolwarm')[1])

    # Add plot title and axis labels
    ax.set_title('Average Covid Cases in Madrid (2020)', fontsize=16)
    ax.set_xlabel('Month', fontsize=14)
    ax.set_ylabel('Average Covid Cases', fontsize=14)

    # Set tick label font size and rotation
    ax.tick_params(labelsize=10, rotation=45)

    # Set the color for the March label
    ax.get_xticklabels()[2].set_color('red')

    # Display the plot
    plt.show()
    plt.savefig("figures/graph_covid.png")

    # Open file
    os.system("start figures/graph_covid.png")




def visualizing_api_barplot (df_api):
    # Set plot style
    sns.set_style('whitegrid')

    # Create the plot with hue for each year
    ax = sns.barplot(data=df_api, x='month_name', y='value', linewidth=2.5, ci=None, color=sns.color_palette('coolwarm')[1])

    # Add plot title and axis labels
    ax.set_title('Average levels of pm25 in Madrid (Jan-May 2020)', fontsize=16)
    ax.set_xlabel('Month', fontsize=14)
    ax.set_ylabel('Average levels of pm25', fontsize=14)

    # Set tick label font size and rotation
    ax.tick_params(labelsize=10, rotation=45)

    # Invert x-tick labels
    ax.set_xticklabels(ax.get_xticklabels()[::-1])

    # Set the color for the March label
    ax.get_xticklabels()[2].set_color('red')

    # Display the plot
    plt.show()
    plt.savefig("figures/graph_barplot.png")

    # Open file
    os.system("start figures/graph_barplot.png")




    
def visualizing_api_boxplot (df_api):
    # Create the plot with hue for each year
    ax = sns.boxplot(data=df_api, x='month_name', y='value', hue='month_name', color=sns.color_palette('coolwarm')[1], dodge=False, width=0.5)

    # Add plot title and axis labels
    ax.set_title('Average levels of pm25 in Madrid (Jan-May 2020)', fontsize=16)
    ax.set_xlabel('Month', fontsize=14)
    ax.set_ylabel('Average levels of pm25', fontsize=14)

    # Remove legend
    plt.gca().get_legend().remove()

    # Invert x-tick labels
    ax.set_xticklabels(ax.get_xticklabels()[::-1])

    # Display the plot
    plt.show()
    plt.savefig("figures/graph_boxplot.png")

    # Open file
    os.system("start figures/graph_boxplot.png")