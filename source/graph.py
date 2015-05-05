# Take parsed data and visualize using popular Python math libraries
from collections import Counter

import csv
import matplotlib.pyplot as plt
import numpy as np

import parse as prs 

parsed_data = prs.parse(prs.MY_FILE, ",")

def visualize_days(parsed_data):
    """Visualize data by day of week"""
    
    # Count how many incidents occur per day, store result in counter variable
    
    # Separate days of the week (x-axis) from number of incidents per day (y-axis)
    
    # Assign number of incidents per day to a matplotlib plot instance
    
    # Create x-axis ticks, assign the labels
    
    # Save the plot
    
    # Close the plot file
    
def main():
    visualize_days(data_file)
    
if __name__ == "__main__":
    main()